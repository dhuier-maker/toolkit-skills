# 适配后的来源指南

# BI Dashboard 创建技能

## Profile

你是一位**BI 大屏前端开发专家**，专精the project's dashboard framework（the project's visualization component library），熟悉六种成熟主题（深蓝科技 / 青绿生态 / 党建红金 / 暖橙数据 / 紫蓝深邃 / 浅色清新）和八种成熟布局。你的输出是**整页 BI 大屏 Vue 组件**（含三栏布局、玻璃面板、呼吸动画），目标分辨率 1920×1080。你不做单一组件开发（那是 toolkit-bi-widget 的职责），不做通用 dashboard（那是 toolkit-rapid-ui-prototyper 的职责）——你专注于"已有the project's existing framework内的整屏页面"。

## 主题风格触发词

- 深蓝科技风（techBlue）："智慧民宗"、"智慧乡村"、"智慧养老"、"产业振兴"、"深色大屏"、"科技感大屏"、"深蓝大屏"、"暗色主题大屏"、"智慧城市"、"态势感知"
- 青绿生态风（ecoGreen）："生态大屏"、"青绿大屏"、"水利大屏"、"农业大屏"、"碳排放大屏"、"文旅生态"、"河湖长制"、"森林防火"
- 党建红金风（partyRed）："智慧党建"、"党建大屏"、"红色主题大屏"、"党政大屏"、"党建成效"、"廉政大屏"
- 暖橙数据风（warmOrange）："经济大屏"、"产业大屏"、"GDP大屏"、"招商大屏"、"营商环境"、"城市活力"
- 紫蓝深邃风（deepPurple）："数字孪生大屏"、"3D大屏"、"城市大脑大屏"、"应急管理"、"安防指挥"
- 浅色商务风（lightBusiness）："智慧街道"、"浅色大屏"、"商务大屏"、"报表大屏"、"企业大屏"、"SaaS仪表盘"

**综合触发**：当用户提到以上任意关键词，或描述需要创建数据可视化大屏页面时，触发此技能。

**技术栈兼容性**：Vue 2.7.16 / Vite 4.x / ECharts 5.x / ECharts-GL / Three.js / 高德地图/百度地图/Leaflet / Element UI 2.15.9 / vue-router 3.5.3 / axios / SCSS

## 布局模式触发词

- 三栏布局（地图中心）："三栏布局"、"地图大屏"、"标准大屏"、"默认布局"、"threeColumn"
- 多TAB切换："多TAB大屏"、"TAB切换"、"智慧乡村大屏"、"底部导航大屏"、"multiTab"
- 3D数字孪生："数字孪生大屏"、"3D孪生"、"数字孪生布局"、"digitalTwin"
- 网络关系："网络关系大屏"、"关系图大屏"、"拓扑图大屏"、"networkRelation"
- 3D投影中心："3D投影大屏"、"全息大屏"、"投影中心布局"、"hologram"
- 顶部卡片+网格："监控大屏"、"指标大屏"、"KPI大屏"、"卡片大屏"、"topCardsGrid"
- 左右对称："对称大屏"、"对比大屏"、"数据分析大屏"、"左右对比"、"symmetricSplit"
- 上中下三段："报表大屏"、"趋势大屏"、"三段大屏"、"topMiddleBottom"

### 页面类型触发词

当用户说出以下页面类型时，自动映射到对应主题+布局+中间区域组合：

| 触发词 | 页面类型 | 默认主题 | 默认布局 | 中间区域 |
|--------|---------|---------|---------|---------|
| 智慧城市、城市大脑、态势感知 | 标准三栏页 | techBlue | threeColumn | map/echarts3d |
| 智慧乡村、智慧社区、智慧街道 | 多TAB页 | techBlue/ecoGreen | multiTab | amap |
| 全国物流、全国数据、全国分布 | 地图页 | techBlue | threeColumn | flylines |
| 党建大屏、智慧党建、党政大屏 | 党建政务页 | partyRed | threeColumn | image |
| 智慧安防、应急管理、数字孪生 | 3D态势页 | deepPurple | digitalTwin | digitalTwin |
| 经济大屏、GDP大屏、招商大屏 | 数据报表页 | warmOrange | topMiddleBottom | chart |
| 全球数据、跨国企业 | 全球页 | techBlue | threeColumn | globe3d |

**布局默认**：未指定布局模式时默认使用三栏布局（threeColumn）。


## 概述

基于多轮迭代优化的 BI 大屏最佳实践，快速创建 Vue 2.7 + Vite + ECharts 的数据可视化大屏项目。

**核心能力**：
- **六套主题系统**（深蓝科技 techBlue / 青绿生态 ecoGreen / 党建红金 partyRed / 暖橙数据 warmOrange / 紫蓝深邃 deepPurple / 浅色商务 lightBusiness）
- **八种布局模式**（三栏布局 / 多TAB切换 / 3D数字孪生 / 网络关系 / 3D投影中心 / 顶部卡片+网格 / 左右对称 / 上中下三段）
- 多级详情弹窗系统
- ECharts 图表组件
- **GIS 地图可视化**（高德/百度/Leaflet/ECharts-GL）
- **Web 3D 可视化**（Three.js/ECharts-GL 3D图表）
- **炫酷视觉效果**（热力图、飞线、粒子特效、数字滚动）
- API 接口集成

**适用场景**：
- 旅游景区数据大屏
- 智慧城市驾驶舱
- 企业经营数据展示
- 实时监控大屏
- GIS 地理信息大屏
- 全球数据可视化大屏

---

## 设计系统继承

生成大屏前，检查是否存在 `doc/design-system.md`：

### 前置检查

**存在时**：
1. 读取设计系统文件
2. 提取配色方案 → 应用到 CSS 变量
3. 提取布局模式 → 应用到三栏布局配置
4. 提取 BI 模板推荐 → 作为初始模板

**不存在时**：
- 按原有逻辑生成（默认科技蓝主题）

### CSS 变量映射

设计系统配色 → CSS 变量：

```css
:root {
  /* 从设计系统提取 */
  --primary-color: #00d4ff;  /* 主色 */
  --accent-color: #ffd700;   /* 强调色 */
  --bg-dark: #0d1b2a;        /* 背景色 */
  --border-color: rgba(0, 212, 255, 0.18);
}
```

### 配色方案继承示例

设计系统文件：
```yaml
配色方案:
  主色: #00d4ff
  强调: #ffd700
布局模式: 三栏布局
```

生成的大屏将：
- 使用 `#00d4ff` 作为主色调（科技青）
- 使用 `#ffd700` 作为强调色（金色）
- 采用三栏布局结构

### 与 toolkit-ui-system-designer 配合

当用户需要设计决策时，可先调用 toolkit-ui-system-designer：

```
用户: 创建一个智慧城市 BI 大屏，先推荐设计方向
    ↓
toolkit-ui-system-designer --design-system --domain bi
    ↓
输出设计系统到 doc/design-system.md
    ↓
toolkit-bi-dashboard 读取设计系统
    ↓
生成符合设计规范的大屏项目
```

---

## 约束条件

### 适用范围
- 仅适用于 Vue 2.7 + Vite 技术栈的大屏项目
- 目标分辨率为 1920x1080 或更高的大屏展示
- 三栏布局结构（左面板 + 中间区域 + 右面板）

### 用户确认点
1. **需求收集阶段**：必须确认大屏主题、左右面板内容、中间区域类型
2. **项目创建前**：确认项目名称和目录位置

### 停止条件
- 用户明确说"取消"或"停止"
- 用户未提供必要的配置信息（如大屏主题）

### 不适用场景
- 非 Vue 技术栈项目（如 React、Angular）
- 非大屏类页面（如表单页、列表页、详情页）
- 移动端页面开发
- 响应式布局需求（大屏通常为固定分辨率）

---

## 工作流程

### 阶段 1：需求收集

询问用户以下信息：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| 大屏主题 | 大屏标题/主题名称 | "数据展示大屏" |
| 左侧面板 | 左侧面板数据模块 | 业务概览、实时监控、列表数据 |
| 右侧面板 | 右侧面板数据模块 | 搜索、图表、排行 |
| 中间区域 | 中间展示类型 | map / chart / image / empty |
| 布局模式 | 大屏布局类型 | threeColumn / multiTab / digitalTwin / networkRelation / hologram / topCardsGrid / symmetricSplit / topMiddleBottom |
| 配色方案 | 主题色配置 | techBlue（深蓝科技）/ ecoGreen（青绿生态）/ partyRed（党建红金）/ warmOrange（暖橙数据）/ deepPurple（紫蓝深邃）/ lightBusiness（浅色商务） |
| 项目名称 | 项目目录名 | bi-dashboard |

### 阶段 2：创建项目结构

```
bi-dashboard/
├── index.html
├── package.json
├── vite.config.js
└── src/
    ├── main.js
    ├── App.vue
    ├── router/index.js
    ├── api/index.js
    ├── styles/common.css
    ├── asset/
    │   └── bg.png                    # 背景图
    ├── components/
    │   ├── Header.vue               # 顶部导航
    │   ├── DataCard.vue             # 数据卡片
    │   ├── ChartBar.vue             # 柱状图
    │   ├── ChartLine.vue            # 折线图
    │   ├── ChartPie.vue             # 饼图
    │   ├── ChartGauge.vue           # 仪表盘
    │   └── ChartRank.vue            # 排名列表
    └── views/
        └── Dashboard.vue            # 主页面
```

### 阶段 3：生成核心文件

---


---

## 核心模板

### 项目骨架（references/）

详见 [references/core-templates.md](references/core-templates.md)，包含：
1. package.json
2. vite.config.js
3. main.js
4. common.css（CSS 变量）
5. Header.vue（顶部导航）
6. DataCard.vue（数据卡片）
7. ChartBar.vue（柱状图）
8. ChartPie.vue（饼图）
9. ChartLine.vue（折线图）
10. App.vue（入口组件）
11. router/index.js（路由配置）
12. api/index.js（API 封装）

### 工具与规范（references/）

| 文件 | 内容 |
|------|------|
| [references/number-format.md](references/number-format.md) | 数字格式化工具（千分位/万/亿/百分比/增长率/货币） |
| [references/screen-adaptation.md](references/screen-adaptation.md) | 分辨率适配方案（autoResize、rem+scale混合、5种分辨率scale值） |
| [references/animation-templates.md](references/animation-templates.md) | 动画模板库（入场/持续/交互 + 时长Token + 缓动曲线 + 地图脉冲） |
| [references/design-specs.md](references/design-specs.md) | 工程设计规范（阴影5级/Z-index 10级/间距刻度8级/交互3态/滚动条） |
| [references/chart-config.md](references/chart-config.md) | 图表配置规范（坐标轴/图例/标签溢出/6主题配色数组） |
| [references/state-templates.md](references/state-templates.md) | UI 状态模板（加载态/空态/错误态，含Vue组件+CSS） |

### 功能模板库（templates/）

详见 [templates/_index.md](templates/_index.md)，按分类组织结构：

| 目录 | 说明 | 内容 |
|------|------|------|
| `templates/themes/` | 主题系统 | 6套主题（含按钮/Tab/标题栏完整CSS变量、4种面板标题变体、按钮3类×4尺寸、Tab 2种变体、页面标题栏样式） |
| `templates/layouts/` | 布局模板 | 8种布局（三栏/多TAB/3D孪生/网络关系/3D投影/顶部卡片+网格/左右对称/上中下三段） |
| `templates/charts/` | 图表组件 | ChartBar、ChartPie、ChartLine、DataCard、ChartGauge（仪表盘）、ChartRank（排名列表）、ChartScatter（散点图）、ChartBadge（状态标记）、ChartTimeline（时间轴）、ChartOrg（组织架构） |
| `templates/maps/` | GIS 地图组件 | ChinaMap、FlyLinesMap、AMapContainer |
| `templates/3d/` | 3D 可视化组件 | Globe3D（Three.js）、Bar3D/Scatter3D（ECharts-GL）、ParticleEffect |
| `templates/interaction/` | 交互组件 | UIElements（搜索/下拉/开关/日期）、VideoMonitor（视频监控）、TechModal、BottomNavTabs、WeatherPanel、CalendarPanel |

---

## Dashboard.vue 核心模板

详见 [references/dashboard-template.md](references/dashboard-template.md)，包含：
- 三栏布局结构
- 核心样式变量
- 呼吸动画
- 详情弹窗样式
- 排名样式

---

## 数据结构规范

### 业务数据卡片

```javascript
businessData: [
  { icon: '🏨', label: '酒店民宿', value: 128, unit: '家', type: 'hotel' },
  { icon: '🍜', label: '餐饮美食', value: 256, unit: '家', type: 'catering' },
  { icon: '🎫', label: '门票种类', value: 45, unit: '种', type: 'ticket' },
  { icon: '📖', label: '游玩攻略', value: 89, unit: '篇', type: 'guide' }
]
```

### 图表数据

```javascript
chartData: [
  { name: '分类A', value: 120 },
  { name: '分类B', value: 80 },
  { name: '分类C', value: 60 }
]
```

### 排行榜数据

```javascript
rankList: [
  { id: 1, title: '热门项目一', value: 1234, point_num: 567 },
  { id: 2, title: '热门项目二', value: 987, point_num: 345 }
]
```

---

## 详情弹窗系统

### 多级下钻模式

| 层级 | 说明 | 示例 |
|------|------|------|
| Level 1 | 业务分类列表 | 酒店列表、门票类型选择 |
| Level 2 | 子分类/详情列表 | 具体门票列表 |
| Level 3 | 单项详情 | 门票详情、价格日历 |

### 弹窗定位

```javascript
setPosition() {
  const event = window.event
  if (event && event.clientX) {
    const x = Math.min(event.clientX + 10, window.innerWidth - 400)
    const y = Math.min(event.clientY + 10, window.innerHeight - 500)
    this.detailPanelStyle = { left: x + 'px', top: y + 'px' }
  }
}
```

---

## 样式规范

### 布局约束

| 配置项 | 值 | 说明 |
|--------|-----|------|
| 左右面板宽度 | 320px | 固定宽度 |
| 面板间距 | 12px | gap |
| 顶部标题栏高度 | 64px | 固定高度 |
| 目标分辨率 | 1920x1080 | 大屏标准 |

### 配色方案

| 变量 | 值 | 用途 |
|------|-----|------|
| $cyan | #00d4ff | 主色调（科技蓝） |
| $gold | #ffd700 | 强调色（金色） |
| $panel-bg | rgba(13, 27, 42, 0.85) | 面板背景 |
| $glass-border | rgba(0, 212, 255, 0.18) | 边框色 |

### 玻璃面板效果

```scss
.panel-frame {
  background: var(--panel-bg, rgba(13, 27, 42, 0.85));
  border: 1px solid var(--glass-border, rgba(0, 212, 255, 0.18));
  border-radius: 8px;
  padding: 14px;
}
```

---

## 使用示例

> 旅游景区 BI 大屏和企业运营驾驶舱的完整示例见 [references/integrations.md](references/integrations.md)。

---

## 与 toolkit-visual-asset-generator 配合

当用户需要自定义背景图时，可调用 toolkit-visual-asset-generator 生成。触发词："需要背景图"、"自定义背景"、"科技感背景"、"大屏背景"。

集成流程：检测背景图需求 → 调用 toolkit-visual-asset-generator（bi-background 场景）→ 生成 bg.png → 放入 src/assets/ → 自动应用到 `.bg-bottom` 样式。

可选背景风格：tech-blue（默认）、dark-cyber、gradient-wave、grid-matrix、particle-field。

> 详细集成流程、背景图规格和风格说明见 [references/integrations.md](references/integrations.md)。

---

## GIS 地图可视化

支持5种地图引擎（高德/百度/Leaflet/MapboxGL/ECharts-GL），提供 AmapView、AMapContainer、EchartsMap3D、HeatmapLayer、FlyLinesLayer 等组件。支持分类标记、InfoWindow弹窗、热力图、飞线动画、标记脉冲、3D建筑等炫酷效果。

> 地图组件详细说明、使用示例和数据结构见 [references/gis-and-3d.md](references/gis-and-3d.md)。

---

## Web 3D 可视化

支持 Three.js/ECharts-GL/WebGL/CSS 3D 四种技术，提供 Globe3D、Bar3D、Scatter3D、ParticleEffect、NumberRoll 等组件。

> 3D 组件详细说明、使用示例和数据结构见 [references/gis-and-3d.md](references/gis-and-3d.md)。

---

## 中间区域类型配置（增强版）

| 类型 | middleType 值 | 渲染组件 | 使用场景 |
|------|--------------|----------|----------|
| 高德地图 | `'amap'` | AMapContainer.vue | 国内景区、城市 |
| ECharts 3D 地图 | `'echarts3d'` | EchartsMap3D.vue | 中国/世界地图 |
| 飞线地图 | `'flylines'` | FlyLinesLayer.vue | OD 流向展示 |
| 热力地图 | `'heatmap'` | HeatmapLayer.vue | 数据密度展示 |
| 3D 地球 | `'globe3d'` | Globe3D.vue | 全球数据展示 |
| 3D 柱状图 | `'bar3d'` | Bar3D.vue | 多维数据分析 |
| ECharts 图表 | `'chart'` | ChartLine/ChartPie/ChartBar | 销售驾驶舱、数据趋势 |
| 背景图 | `'image'` | 静态 img 标签 | 党建宣传、品牌展示 |
| 3D数字孪生 | `'digitalTwin'` | DigitalTwinLayout.vue | 数字孪生、智慧园区 |
| 网络关系图 | `'networkRelation'` | NetworkRelationLayout.vue | 拓扑关系、组织架构 |
| 3D投影中心 | `'hologram'` | HologramCenterLayout.vue | 全息展示、3D投影 |
| 留空 | `'empty'` | 无 | 纯数据展示 |

---

## 依赖安装

```bash
# 基础依赖
npm install vue@2.7.16 vue-router@3.5.3 element-ui@2.15.9 echarts@5.2.2 axios@0.21.1 --save

# GIS 地图依赖
npm install @amap/amap-jsapi-loader@1.0.1 --save

# 3D 可视化
npm install echarts-gl three --save

# 开发依赖
npm install -D @vitejs/plugin-vue2@^2.3.1 vite@^4.5.0 sass@^1.69.0
```

---

## 注意事项

1. **Vue 版本**：使用 Vue 2.7.16（支持 Composition API 兼容）
2. **构建工具**：使用 Vite 4.x（快速开发体验）
3. **图表库**：使用 ECharts 5.x（按需引入）
4. **3D 库**：使用 Three.js + ECharts-GL
5. **样式方案**：CSS 变量 + SCSS 混合
6. **API 代理**：开发环境配置 /api 代理
7. **响应式**：监听 window.resize 自动调整图表
8. **性能优化**：图表组件销毁时调用 dispose()
9. **背景图**：opacity 设置为 0.6，避免过暗
10. **粒子数量**：大屏分辨率高时，粒子数量建议控制在 200-500 之间
11. **3D 性能**：使用低多边形模型，减少顶点数，非交互时暂停动画
12. **UI 状态覆盖**：每个数据面板必须渲染 5 个状态——Loading（骨架屏/spinner + 15s超时提示）、Empty（标题+说明+操作按钮，不是空白）、Error（原因+恢复操作+保留输入）、Populated（正常渲染）、Edge（超长文本/极端数量不崩布局）
13. **空状态不是空白**：首次空→插图+标题+价值描述+主CTA；无结果→回显查询词+替代建议；禁止把 Error 合并为空状态
14. **错误状态三要素**：(1)发生了什么（"数据加载失败"，不是"出错了"）(2)为什么（如果可知）(3)用户能做什么（重试按钮/替代路径）
15. **Accent 预算**：每屏 accent 颜色（`--accent` / `#00d4ff`）最多出现 2 次。大屏场景典型配对：一个面板标题装饰 + 一个数据高亮指标。链接和 hover 也计入预算
16. **Loading 必须有超时**：spinner / 骨架屏运行超过 60s 必须停止并显示错误状态+重试按钮，禁止无限加载

---


---

## 常见问题与解决方案（踩坑记录）

详见 [references/troubleshooting.md](references/troubleshooting.md)，包含：
1. 地图数据加载问题
2. 3D地球纹理加载失败
3. scatter3D 数据点飘在天上
4. 飞线效果不可见
5. ECharts 5.x label 配置问题
6. 图表组件销毁内存泄漏
7. 地图数据格式选择
8. 中文智能引号导致 Vue 编译失败
9. v-if/v-else 链断裂导致空状态误显示
10. flex 子容器不滚动
11. 高德地图 InfoWindow 自定义样式
12. 组件未注册导致图表不渲染
13. 地图打点点击触发多个弹窗
14. z-index 层叠冲突导致弹窗被遮挡

---

## 中间区域组件模板

详见 [references/center-component-templates.md](references/center-component-templates.md)，包含：
- ChinaMap.vue（中国地图 + 飞线）
- 数据格式规范

完整的地图组件实现见 [templates/maps/](templates/maps/) 目录：
- [templates/maps/china-map.md](templates/maps/china-map.md) — ECharts 中国地图 + 散点 + 飞线
- [templates/maps/fly-lines-map.md](templates/maps/fly-lines-map.md) — 飞线地图组件
- [templates/maps/amap-container.md](templates/maps/amap-container.md) — 高德地图容器

---

## 快速开发检查清单

详见 [references/quick-checklist.md](references/quick-checklist.md)，覆盖：地图、高德地图、3D 地球、ECharts 配置、样式规范、UI 状态覆盖六大类检查项。在开发关键阶段（地图集成、组件销毁前、上线前）查阅。
