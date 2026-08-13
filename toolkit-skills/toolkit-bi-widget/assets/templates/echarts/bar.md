# 柱状图模板 (Bar Chart)

完整参考：`references/component-templates.md` 第一节

## 功能介绍

支持垂直/水平柱状图，支持渐变色柱体、圆角、标签显示、提示框、X/Y轴配置等。

## 目录结构

```
ComponentName/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   ├── ChartOrientation.vue    # 图表方向
    │   ├── BarWidth.vue            # 柱体宽度
    │   ├── BarColor.vue            # 柱体颜色
    │   ├── BarBorderRadius.vue     # 柱体圆角
    │   ├── XAxisLineColor.vue      # X轴线颜色
    │   ├── YAxisLineColor.vue      # Y轴线颜色
    │   ├── LabelColor.vue          # 标签颜色
    │   ├── TooltipBackgroundColor.vue # 提示框背景
    │   └── style/
    ├── locale/
    │   ├── index.js
    │   └── lang/
    │       ├── zh-cn.json
    │       └── en.json
    └── static/
        └── img/
```

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
chartData: {
  type: Object,
  default: () => ({
    categories: ['类别1', '类别2', '类别3', '类别4', '类别5', '类别6'],
    values: [84, 70, 61, 79, 50, 58],
  }),
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},
```

### 样式配置 - 柱体 (groupKey: 'style', groupName: '样式配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| chartOrientation | String | 'vertical' | 图表方向：vertical/horizontal |
| barWidth | Number | 30 | 柱体宽度 10-100 |
| barBorderRadius | Array/Number | [10,10,0,0] | 柱体圆角 |
| barColors | Array | 渐变配置 | 柱体颜色（支持渐变） |

### X轴配置 (groupName: 'X轴配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| xAxisShow | Boolean | true | 是否显示X轴 |
| xAxisLineColor | String | 'rgba(255,255,255,0.2)' | X轴线颜色 |
| xAxisLabelColor | String | '#ffffff' | X轴标签颜色 |
| xAxisLabelFontSize | Number | 14 | X轴标签字号 |

### Y轴配置 (groupName: 'Y轴配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| yAxisShow | Boolean | true | 是否显示Y轴 |
| yAxisSplitLineShow | Boolean | true | 显示分割线 |
| yAxisSplitLineColor | String | 'rgba(255,255,255,0.1)' | 分割线颜色 |

### 标签配置 (groupName: '标签配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showLabel | Boolean | true | 显示柱顶标签 |
| labelColor | String | '#ffffff' | 标签颜色 |
| labelFontSize | Number | 14 | 标签字号 |

### 提示框配置 (groupName: '提示框配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showTooltip | Boolean | true | 显示提示框 |
| tooltipBackgroundColor | String | 'rgba(0,0,0,0.8)' | 提示框背景色 |

### 网格配置 (groupName: '网格配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| gridTop/GridBottom/GridLeft/GridRight | Number | 60 | 网格边距 |

## ECharts Option 核心结构

```javascript
const option = {
  backgroundColor: 'transparent',
  tooltip: {
    trigger: 'axis',
    backgroundColor: props.tooltipBackgroundColor,
    textStyle: { color: '#fff' },
  },
  grid: {
    top: props.gridTop,
    bottom: props.gridBottom,
    left: props.gridLeft,
    right: props.gridRight,
    containLabel: true,
  },
  xAxis: {
    type: isHorizontal ? 'value' : 'category',
    data: categories,
    axisLine: { lineStyle: { color: props.xAxisLineColor } },
    axisLabel: { color: props.xAxisLabelColor, fontSize: props.xAxisLabelFontSize },
  },
  yAxis: {
    type: isHorizontal ? 'category' : 'value',
    splitLine: { lineStyle: { color: props.yAxisSplitLineColor } },
  },
  series: [{
    type: 'bar',
    data: values,
    barWidth: props.barWidth,
    itemStyle: {
      color: convertColor(props.barColors[0]),
      borderRadius: props.barBorderRadius,
    },
    label: {
      show: props.showLabel,
      color: props.labelColor,
      fontSize: props.labelFontSize,
    },
  }],
};
```

## 完整代码

完整柱状图组件代码请参考 `references/component-templates.md` 第一节中的 index.vue。