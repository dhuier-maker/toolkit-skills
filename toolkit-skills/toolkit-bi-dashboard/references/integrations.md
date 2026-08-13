# 集成与使用示例

## 与 toolkit-visual-asset-generator 配合

当用户需要自定义背景图时，可调用 toolkit-visual-asset-generator 生成。

### 触发条件

用户需求中包含以下关键词时，自动调用 toolkit-visual-asset-generator：
- "需要背景图"、"自定义背景"、"科技感背景"
- "生成背景图"、"大屏背景"

### 集成流程

```
用户: 创建一个湄洲岛旅游 BI 大屏，需要一个科技感背景图
    ↓
toolkit-bi-dashboard 启动
    ↓
检测到需要背景图 → 调用 toolkit-visual-asset-generator（bi-background 场景，tech-blue 风格）
    ↓
生成 bg.png → 放入 src/assets/bg.png
    ↓
继续生成 Vue 项目结构
```

### 背景图规格

| 参数 | 值 | 说明 |
|------|-----|------|
| 场景 | bi-background | BI大屏背景 |
| 风格 | tech-blue | 科技蓝（默认） |
| 分辨率 | 1920x1080 | 标准大屏 |
| 输出 | PNG + HTML | 可复用源码 |

### 背景风格选项

| 风格 | 说明 |
|------|------|
| tech-blue | 科技蓝渐变 + 光点（默认） |
| dark-cyber | 赛博暗黑 + 霓虹 |
| gradient-wave | 渐变波浪 |
| grid-matrix | 网格矩阵 |
| particle-field | 粒子场 |

> **注**：toolkit-visual-asset-generator 支持双模式生成。AI API 模式适合创意背景，SVG+CSS 模式 100% 成功且可编辑。需求模糊时可通过 `toolkit-image-prompt-writer → toolkit-visual-asset-generator` 联动增强 prompt 质量。

---

## 使用示例

### 示例 1：旅游景区 BI 大屏

**用户输入**：
```
创建一个湄洲岛旅游大数据 BI 大屏
- 左侧：实时客流、酒店入住、门票销售、停车场数据
- 中间：GIS 地图展示景区分布
- 右侧：运营指标、入离岛趋势、出行方式
```

**输出**：
- 完整的 Vue 项目结构
- Dashboard.vue 主页面
- Header、DataCard、ChartBar 等组件
- api/index.js API 封装
- common.css 样式变量

### 示例 2：企业运营驾驶舱

**用户输入**：
```
做一个企业运营 BI 大屏，三栏布局
- 左侧：销售额、订单量、用户数、转化率
- 中间：折线图展示趋势
- 右侧：各品类销售占比、库存预警
```

**输出**：
- 同示例 1，中间区域使用 ChartLine 组件
