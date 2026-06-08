> 原文地址：https://docs.ros.org/en/jazzy/Releases.html

# 发行版

## 什么是发行版？

ROS 发行版是一组版本化的 ROS 包集合。这类似于 Linux 发行版（如 Ubuntu）。ROS 发行版的目的是让开发者在准备好全面升级之前，能够基于相对稳定的代码库工作。因此，一旦发行版发布，我们尽量将更改限制在核心包的错误修复和非破坏性改进上（ros-desktop-full 下的所有包）。这通常适用于整个社区，但对于"更高层次"的包，规则较为宽松，由包的维护者自行决定以避免破坏性变更。

## 发行版列表

下表中标记为蓝色的行是当前受支持的发行版。

| 发行版 | 发布日期 | EOL 日期 | ROS Boss |
|---|---|---|---|
| **Lyrical Luth** | 2026年5月22日 | 2031年5月 | Shane Loretz |
| **Kilted Kaiju** | 2025年5月23日 | 2026年12月 | Scott K Logan |
| **Jazzy Jalisco** | 2024年5月23日 | 2029年5月 | Marco A. Gutiérrez |
| Iron Irwini | 2023年5月23日 | 2024年12月4日 | Yadunund Vijay |
| **Humble Hawksbill** | 2022年5月23日 | 2027年5月 | Christophe Bédard / Audrow Nash |
| Galactic Geochelone | 2021年5月23日 | 2022年12月9日 | Scott Logan |
| Foxy Fitzroy | 2020年6月5日 | 2023年6月20日 | Jacob Perron / Dharini Dutia |
| Eloquent Elusor | 2019年11月22日 | 2020年11月 | Michael Carroll |
| Dashing Diademata | 2019年5月31日 | 2021年5月 | Steven! Ragnarök |
| Crystal Clemmys | 2018年12月14日 | 2019年12月 | Steven! Ragnarök |
| Bouncy Bolson | 2018年7月2日 | 2019年7月 | Mikael Arguedas / Steven! Ragnarök |
| Ardent Apalone | 2017年12月8日 | 2018年12月 | Steven! Ragnarök |
| beta3 | 2017年9月13日 | 2017年12月 | |
| beta2 | 2017年7月5日 | 2017年9月 | |
| beta1 | 2016年12月19日 | 2017年7月 | |
| alpha1 - alpha8 | 2015年8月31日 | 2016年12月 | |

## 未来发行版

每年 **5 月 23 日**（[世界海龟日](https://www.worldturtleday.org/)）都会发布一个新的 ROS 2 发行版。

| 发行版 | 发布日期 | EOL 日期 |
|---|---|---|
| Makoa Mata-mata | 2027年5月 | 2028年12月 |

## Rolling 发行版

**ROS 2 Rolling Ridley** 是 ROS 2 的滚动开发发行版。它在 [REP 2002](https://reps.openrobotics.org/rep-2002/) 中描述，于 2020 年 6 月首次引入。

Rolling 发行版有两个目的：

1. 作为未来稳定 ROS 2 发行版的**暂存区域**
2. 作为最近开发版本的**集合**

顾名思义，Rolling 会持续更新，**可能包含破坏性更改的就地更新**。我们建议大多数人使用最新的稳定发行版。

发布到 Rolling 发行版的包将自动发布到未来的 ROS 2 稳定发行版中。

## 跨发行版通信

节点**不能保证跨发行版通信**。例如，基于 Humble 构建并运行的节点不能保证与基于 Iron 构建并运行的节点正确通信。它可能会工作，但不受支持，不应依赖此行为。

请注意，跨供应商（单发行版内）通信同样不受保证。

---

[返回主页](../index.md)
