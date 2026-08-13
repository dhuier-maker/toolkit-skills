# BI Dashboard 模板库目录

> 按分类整理的完整 BI 大屏模板文件，每个文件包含可直接复制的完整代码。

---

## 分类结构

| 目录 | 说明 | 文件数 |
|------|------|--------|
| `themes/` | 主题系统（深蓝科技、青绿生态、党建红金、暖橙数据、紫蓝深邃、浅色商务） | 5 |
| `layouts/` | 布局模板（三栏布局、多TAB切换、数字孪生、网络关系、3D投影、顶部卡片+网格、左右对称、上中下三段） | 8 |
| `charts/` | 图表组件（柱状图、饼图、折线图、数据卡片、仪表盘、排名列表、散点图、状态标记、时间轴、组织架构） | 11 |
| `maps/` | GIS 地图组件（中国地图、飞线地图、高德地图） | 4 |
| `3d/` | 3D 可视化组件（地球、柱状图、散点图、粒子特效） | 5 |
| `interaction/` | 交互组件（搜索框/下拉/开关/视频监控/面板操作按钮组） | 2 |

---

## 文件映射

### themes/ — 主题系统

| 文件 | 内容 | 触发词 |
|------|------|--------|
| [themes/README.md](themes/README.md) | 主题系统说明，6套主题触发词、向后兼容映射、选型速查 | — |
| [themes/dark-tech.md](themes/dark-tech.md) | 6套主题完整配置：JS配置、CSS变量、SCSS样式、ThemeProvider、ThemeSelector | 深蓝科技、青绿生态、党建红金、暖橙数据、紫蓝深邃、浅色商务 |
| [themes/party-red.md](themes/party-red.md) | 党建红金主题补充样式：祥云装饰、五角星、飘带 | 党建大屏、红色主题、党政大屏 |
| [themes/light-bright.md](themes/light-bright.md) | 浅色商务主题补充样式：卡片阴影、Tab组件 | 浅色大屏、商务大屏、报表大屏 |
| [themes/tourism.md](themes/tourism.md) | 青绿生态主题补充样式：水波纹、波浪装饰 | 生态大屏、水利大屏、农业大屏 |

### layouts/ — 布局模板

| 文件 | 内容 |
|------|------|
| [layouts/README.md](layouts/README.md) | 布局模板说明（8种布局模式） |
| [layouts/three-column.md](layouts/three-column.md) | 三栏布局模板：Dashboard.vue 核心结构 |
| [layouts/multi-tab.md](layouts/multi-tab.md) | 多TAB切换布局模板：底部导航胶囊按钮 + 图标模式 |
| [layouts/digital-twin.md](layouts/digital-twin.md) | 3D数字孪生布局模板：Three.js 3D城市场景 + 数据叠加层 |
| [layouts/network-relation.md](layouts/network-relation.md) | 网络关系布局模板：径向网络图 + 节点交互 |
| [layouts/hologram-center.md](layouts/hologram-center.md) | 3D投影中心布局模板：全息投影 + 卡片网格 |
| [layouts/top-cards-grid.md](layouts/top-cards-grid.md) | 顶部卡片+网格布局模板：KPI卡片行 + 2×2图表网格 |
| [layouts/symmetric-split.md](layouts/symmetric-split.md) | 左右对称布局模板：50% 对比分析 |
| [layouts/top-middle-bottom.md](layouts/top-middle-bottom.md) | 上中下三段布局模板：KPI + 主图表 + 辅助图表 |

### charts/ — 图表组件

| 文件 | 内容 | 组件 |
|------|------|------|
| [charts/README.md](charts/README.md) | 图表组件说明（4种ECharts组件） | — |
| [charts/chart-bar.md](charts/chart-bar.md) | 柱状图组件（支持横向/纵向） | ChartBar.vue |
| [charts/chart-pie.md](charts/chart-pie.md) | 饼图/环形图组件 | ChartPie.vue |
| [charts/chart-line.md](charts/chart-line.md) | 折线图组件（支持面积图/平滑曲线） | ChartLine.vue |
| [charts/data-card.md](charts/data-card.md) | 数据卡片组件（带变化率/点击交互） | DataCard.vue |
| [charts/chart-gauge.md](charts/chart-gauge.md) | 仪表盘组件（半圆/整圆、指针/弧形进度） | ChartGauge.vue |
| [charts/chart-rank.md](charts/chart-rank.md) | 排名列表组件（序号+条形+自动滚动+金银铜） | ChartRank.vue |
| [charts/chart-scatter.md](charts/chart-scatter.md) | 2D散点图组件（气泡大小映射） | ChartScatter.vue |
| [charts/chart-badge.md](charts/chart-badge.md) | 状态标记组件（6状态色×4尺寸+脉冲动画） | ChartBadge.vue |
| [charts/chart-timeline.md](charts/chart-timeline.md) | 时间轴组件（节点状态色+内容卡片） | ChartTimeline.vue |
| [charts/chart-org.md](charts/chart-org.md) | 组织架构图组件（ECharts树形） | ChartOrg.vue |

### maps/ — GIS 地图组件

| 文件 | 内容 | 组件 |
|------|------|------|
| [maps/README.md](maps/README.md) | GIS 地图组件说明 | — |
| [maps/china-map.md](maps/china-map.md) | ECharts 中国地图 + 飞线 + 散点 | ChinaMap.vue |
| [maps/fly-lines-map.md](maps/fly-lines-map.md) | 飞线地图（OD流向可视化） | FlyLinesMap.vue |
| [maps/amap-container.md](maps/amap-container.md) | 高德地图容器（标记点/控制面板） | AMapContainer.vue |

### 3d/ — 3D 可视化组件

| 文件 | 内容 | 组件 |
|------|------|------|
| [3d/README.md](3d/README.md) | 3D 可视化组件说明 | — |
| [3d/globe-3d.md](3d/globe-3d.md) | 3D 地球（Three.js，数据点/光柱/大气层光晕） | Globe3D.vue |
| [3d/bar-3d.md](3d/bar-3d.md) | 3D 柱状图（ECharts-GL，多维度） | Bar3D.vue |
| [3d/scatter-3d.md](3d/scatter-3d.md) | 3D 散点图（ECharts-GL，三维分布） | Scatter3D.vue |
| [3d/particle-effect.md](3d/particle-effect.md) | 粒子特效（Canvas，鼠标交互/连线） | ParticleEffect.vue |

### interaction/ — 交互组件

| 文件 | 内容 | 组件 |
|------|------|------|
| [interaction/ui-elements.md](interaction/ui-elements.md) | 交互元素（搜索框发光/下拉/开关/日期/面板操作按钮组） | SearchBox/SelectBox/SwitchToggle/PanelActions |
| [interaction/video-monitor.md](interaction/video-monitor.md) | 视频监控面板（状态指示+REC闪烁+4宫格） | VideoMonitor.vue |

---

## 使用方式

1. 根据用户需求确定大屏类型（主题、布局、中间区域）
2. 从对应分类目录选取需要的模板文件
3. 组合模板文件生成完整的大屏项目
4. 参考 [references/core-templates.md](../references/core-templates.md) 补充项目配置文件（package.json, vite.config.js 等）

**注意**：
- `references/` 目录下的文件是项目骨架文件（package.json、main.js、路由配置等），直接取用
- `templates/` 目录下的文件是功能组件，按需组合
- 所有 `.md` 文件内容均为可直接复制的完整代码
