# 01：Ray 分布式批处理

> 你在第一阶段的转换脚本是单进程的——一个 episode 处理完再处理下一个。当 episode 数量到几十个时，单进程就太慢了。Ray 是 Python 生态最成熟的分布式计算框架，特别适合这种"每个 episode 独立处理"的并行任务。

## 1. 为什么用 Ray

你的转换任务有以下特征——这些特征正好是 Ray 的最佳场景：

```text
特征 1：每个 episode 独立处理，没有跨 episode 依赖
         → 天然可并行

特征 2：单个 episode 处理重（图像解码 + 同步 + MP4 编码）
         → 计算密集，需要多核

特征 3：数据量可能超过单机内存
         → 需要流式处理

特征 4：中间可能失败（磁盘满、坏帧、OOM）
         → 需要任务级容错和恢复
```

### Ray vs 其他方案

| 方案 | 适合场景 | 优势 | 劣势 |
|------|---------|------|------|
| **multiprocessing** | 单机、简单任务 | 无需额外依赖 | 不支持多机、容错差 |
| **Celery** | 异步任务队列 | 成熟、可靠 | 偏 Web 场景，数据科学生态弱 |
| **Ray** | ML/数据工程 | Python 原生、ML 生态好、支持分布式 | 学习曲线 |
| **Spark** | 大数据 ETL | 超大规模、SQL 友好 | JVM 生态、对 Python 不够原生 |
| **Dask** | 科学计算 | 与 NumPy/Pandas 兼容 | ML 生态不如 Ray |

**推荐**：如果你的团队已有 Spark 基础设施，用 Spark 也可以。否则 Ray 是 ML 数据工程的首选。

## 2. Ray 核心概念（Web 工程师视角）

| Ray 概念 | Web 类比 | 说明 |
|---------|---------|------|
| Task（任务） | 一次函数调用 | `@ray.remote` 装饰的函数，异步执行 |
| Actor（角色） | 微服务实例 | 有状态的长生命周期对象 |
| Object Store | Redis 缓存 | 跨进程共享的数据存储 |
| Driver | API Gateway | 主进程，提交任务并收集结果 |
| Cluster | K8s 集群 | 多台机器组成的工作节点群 |

## 3. 单机到分布式的最小迁移

### 原始单进程版本（你第一阶段的代码）

```python
from pathlib import Path

def convert_episode(bag_path: Path, output_dir: Path) -> dict:
    """转换单个 episode：bag → LeRobot 格式。"""
    # 你第一阶段的代码
    frames = extract_and_align(bag_path, fps=30)
    frames_to_lerobot(frames, output_dir, dataset_name=bag_path.stem)
    return {"episode": bag_path.stem, "status": "ok", "frames": len(frames)}


# 单进程串行处理
results = []
for bag_path in sorted(Path("data/raw").glob("*.bag")):
    result = convert_episode(bag_path, Path("data/derived"))
    results.append(result)
```

### Ray 并行版本

```python
import ray
from pathlib import Path

# 初始化 Ray（单机模式自动检测 CPU 核数）
ray.init()


@ray.remote
def convert_episode_remote(
    bag_path: str,
    output_dir: str,
) -> dict:
    """Ray Task：在独立进程中转换单个 episode。

    返回值通过 Object Store 传回 Driver。
    """
    bag_path_obj = Path(bag_path)
    output_dir_obj = Path(output_dir)

    try:
        frames = extract_and_align(bag_path_obj, fps=30)
        frames_to_lerobot(frames, output_dir_obj, dataset_name=bag_path_obj.stem)
        return {
            "episode": bag_path_obj.stem,
            "status": "ok",
            "frames": len(frames),
        }
    except Exception as e:
        return {
            "episode": bag_path_obj.stem,
            "status": "error",
            "error": str(e),
        }


# 提交所有 episode 的转换任务
bag_paths = sorted(Path("data/raw").glob("*.bag"))
futures = [
    convert_episode_remote.remote(str(p), "data/derived")
    for p in bag_paths
]

# 等待所有任务完成并收集结果
results = ray.get(futures)

for r in results:
    print(f"  {r['episode']}: {r['status']}")

ray.shutdown()
```

核心变化只有三步：
1. `ray.init()` 初始化运行时。
2. `@ray.remote` 装饰函数。
3. `.remote()` 提交任务，`ray.get()` 收集结果。

## 4. 资源管理

### CPU 和内存分配

```python
@ray.remote(
    num_cpus=2,        # 每个 task 占用 2 个 CPU 核
    num_gpus=0,        # 不需要 GPU（纯数据处理）
    memory=4 * 1024**3,  # 4 GB 内存上限
)
def convert_episode_remote(bag_path: str, output_dir: str) -> dict:
    ...
```

Ray 会根据可用资源自动决定并发度。如果机器有 16 核 CPU，每个 task 需要 2 核，那么最多 8 个 task 同时运行。

### 处理大内存的 episode

某些 episode 可能包含大量高分辨率图像，单次处理需要很多内存。用 Actor 模式做有状态的分批处理：

```python
@ray.remote
class EpisodeProcessor:
    """有状态的 episode 处理器，支持分批处理避免 OOM。"""

    def __init__(self, bag_path: str, batch_size: int = 100):
        self.bag_path = Path(bag_path)
        self.batch_size = batch_size
        self._reader = None
        self._total_frames = 0
        self._processed_frames = 0

    def open(self) -> int:
        """打开 bag，返回总帧数。"""
        self._reader = AnyReader([self.bag_path])
        self._reader.open()
        self._total_frames = self._reader.message_count
        return self._total_frames

    def process_batch(self, batch_index: int) -> dict:
        """处理第 batch_index 批帧。"""
        start = batch_index * self.batch_size
        end = min(start + self.batch_size, self._total_frames)
        frames = extract_batch(self._reader, start, end)
        # 写出这一批的结果
        write_batch(frames, self.output_dir, batch_index)
        self._processed_frames += len(frames)
        return {"batch": batch_index, "frames": len(frames)}

    def close(self) -> None:
        if self._reader:
            self._reader.close()
```

## 5. 容错与恢复

### 自动重试

```python
@ray.remote(
    max_restarts=3,        # 失败后最多重启 3 次
    max_task_retries=2,    # 每个 task 最多重试 2 次
)
def convert_episode_remote(bag_path: str, output_dir: str) -> dict:
    ...
```

### 幂等检查（结合前置计划第四周）

```python
def should_skip(bag_path: Path, output_dir: Path) -> bool:
    """检查是否已经处理过且结果完整。

    利用前置计划学过的校验和机制：
    如果输出目录存在、校验和匹配、且标记为 committed，则跳过。
    """
    manifest_path = output_dir / bag_path.stem / "manifest.json"
    if not manifest_path.exists():
        return False

    manifest = json.loads(manifest_path.read_text())
    if manifest.get("status") != "committed":
        return False

    # 验证源文件校验和
    expected_sha = manifest["source"]["sha256"]
    actual_sha = compute_sha256(bag_path)
    return expected_sha == actual_sha


# 提交任务前过滤已完成的
bag_paths = sorted(Path("data/raw").glob("*.bag"))
pending = [
    p for p in bag_paths
    if not should_skip(p, Path("data/derived"))
]

print(f"总计 {len(bag_paths)} 个 episode，跳过 {len(bag_paths) - len(pending)} 个已完成的")

futures = [
    convert_episode_remote.remote(str(p), "data/derived")
    for p in pending
]
```

### 失败处理策略

```python
# 不等所有任务，逐个收集结果
pending_futures = list(futures)
results: list[dict] = []

while pending_futures:
    finished, pending_futures = ray.wait(pending_futures)
    for future in finished:
        result = ray.get(future)
        results.append(result)
        if result["status"] == "error":
            print(f"  ⚠️ {result['episode']} 失败: {result['error']}")
            # 失败的 episode 记录到失败队列，不阻塞其他任务
```

## 6. 分布式集群（多机）

单机不够时，可以组建 Ray 集群：

```bash
# 头节点（调度器）
ray start --head --port=6379

# 工作节点（数据处理）
ray start --address='192.168.1.100:6379' --num-cpus=16 --memory='64GB'
```

```python
# 连接到远程集群
ray.init(address="ray://192.168.1.100:10001")
```

> 对比你的 Web 经验：Ray 集群类似于 K8s，但更轻量。如果你已有 K8s，可以用 KubeRay 在 K8s 上运行 Ray。

## 7. 完整的分布式转换流水线

```python
"""从多个 bag 批量生成 LeRobot 数据集的分布式流水线。"""
import json
from pathlib import Path

import ray


@ray.remote(num_cpus=2, memory=4 * 1024**3)
def process_single_episode(
    bag_path: str,
    config: dict,
) -> dict:
    """处理单个 episode 并返回结果摘要。"""
    from pathlib import Path
    bag = Path(bag_path)

    try:
        # 1. 校验输入
        if not bag.exists():
            return {"episode": bag.stem, "status": "error", "error": "not_found"}

        # 2. 提取和对齐
        frames = extract_and_align(bag, fps=config["fps"])

        # 3. 质量检查
        if len(frames) < config["min_frames"]:
            return {
                "episode": bag.stem,
                "status": "rejected",
                "reason": f"too few frames: {len(frames)}",
            }

        # 4. 转换格式
        frames_to_lerobot(
            frames,
            output_dir=Path(config["output_dir"]),
            dataset_name=bag.stem,
            fps=config["fps"],
        )

        # 5. 生成 manifest
        manifest = {
            "episode_id": bag.stem,
            "source": {"path": str(bag), "sha256": compute_sha256(bag)},
            "frames": len(frames),
            "fps": config["fps"],
            "config_version": config["version"],
            "status": "committed",
        }
        manifest_path = Path(config["output_dir"]) / bag.stem / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2))

        return {"episode": bag.stem, "status": "committed", "frames": len(frames)}

    except Exception as e:
        return {"episode": bag.stem, "status": "error", "error": str(e)}


def run_batch_pipeline(
    input_dir: Path,
    output_dir: Path,
    fps: int = 30,
    min_frames: int = 100,
) -> None:
    """批量转换流水线。"""
    ray.init()

    config = {
        "fps": fps,
        "min_frames": min_frames,
        "output_dir": str(output_dir),
        "version": "dataset-1",
    }

    # 发现所有输入
    bag_paths = sorted(input_dir.glob("*.bag"))
    print(f"发现 {len(bag_paths)} 个 episode")

    # 过滤已完成的（幂等）
    pending = [p for p in bag_paths if not should_skip(p, output_dir)]
    print(f"待处理: {len(pending)} 个")

    # 提交任务
    futures = [
        process_single_episode.remote(str(p), config)
        for p in pending
    ]

    # 逐个收集结果
    results: list[dict] = []
    while futures:
        finished, futures = ray.wait(futures)
        for future in finished:
            result = ray.get(future)
            results.append(result)
            emoji = {"committed": "✅", "rejected": "⚠️", "error": "❌"}
            print(f"  {emoji.get(result['status'], '?')} {result['episode']}: {result['status']}")

    # 汇总
    summary = {
        "total": len(results),
        "committed": sum(1 for r in results if r["status"] == "committed"),
        "rejected": sum(1 for r in results if r["status"] == "rejected"),
        "error": sum(1 for r in results if r["status"] == "error"),
    }
    print(f"\n汇总: {summary}")

    ray.shutdown()


if __name__ == "__main__":
    run_batch_pipeline(
        input_dir=Path("data/raw"),
        output_dir=Path("data/derived"),
    )
```

## 8. 本篇练习

1. 安装 Ray（`pip install ray`），把第一阶段的 `convert_episode` 函数用 `@ray.remote` 包装，处理 3 个以上的模拟 bag。
2. 对比单进程和 Ray 并行的处理时间，验证加速比。
3. 故意在一个 episode 中制造错误（如损坏的 bag），观察其他 episode 是否正常完成。
4. 思考：如果 episode 之间有依赖（如需要全局统计量），你会怎么修改并行策略？

下一篇进入云存储与流式读取——当数据存在 S3/OSS 时，怎么不落地直接处理。
