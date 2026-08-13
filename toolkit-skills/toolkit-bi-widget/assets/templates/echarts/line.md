# 折线图模板 (Line Chart)

完整参考：`references/component-templates.md` 第六节

## 功能介绍

支持多折线、面积图、平滑曲线、数据点显示、X/Y轴配置、图例配置。

## 目录结构

```
ComponentName/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   ├── ShowArea.vue           # 面积图开关
    │   ├── Smooth.vue             # 平滑曲线开关
    │   ├── LineColors.vue         # 线条颜色
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
    categories: ['1月', '2月', '3月', '4月', '5月', '6月'],
    series: [
      { name: '系列A', data: [120, 132, 101, 134, 90, 230] },
      { name: '系列B', data: [220, 182, 191, 234, 290, 330] },
    ],
  }),
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showArea | Boolean | false | 显示面积 |
| smooth | Boolean | true | 平滑曲线 |
| lineColors | Array | 预设 | 线条颜色序列 |
| lineWidth | Number | 2 | 线条宽度 1-10 |

### 数据点配置 (groupName: '数据点配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showSymbol | Boolean | true | 显示数据点 |
| symbolSize | Number | 6 | 数据点大小 2-20 |

### X/Y轴配置

参考柱状图的 X/Y 轴配置模式。

## ECharts Option 核心结构

```javascript
const series = seriesData.map((item, index) => {
  const color = props.lineColors[index % props.lineColors.length];
  return {
    name: item.name,
    type: 'line',
    data: item.data,
    smooth: props.smooth,
    showSymbol: props.showSymbol,
    symbolSize: props.symbolSize,
    lineStyle: { width: props.lineWidth, color },
    areaStyle: props.showArea ? {
      color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
        { offset: 0, color: color + '80' },
        { offset: 1, color: color + '10' },
      ]),
    } : undefined,
  };
});

const option = {
  backgroundColor: 'transparent',
  tooltip: { trigger: 'axis' },
  legend: { textStyle: { color: '#fff' } },
  grid: { top: 60, bottom: 60, left: 60, right: 60, containLabel: true },
  xAxis: {
    type: 'category',
    data: categories,
    boundaryGap: false,
    axisLine: { lineStyle: { color: props.xAxisLineColor } },
  },
  yAxis: {
    type: 'value',
    splitLine: { lineStyle: { color: props.yAxisSplitLineColor } },
  },
  series,
};
```

## 完整代码

完整折线图组件代码请参考 `references/component-templates.md` 第六节中的 index.vue。