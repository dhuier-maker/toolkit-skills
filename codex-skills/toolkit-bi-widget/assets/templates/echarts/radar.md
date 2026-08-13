# 雷达图模板 (Radar Chart)

完整参考：`references/component-templates.md` 第七节

## 功能介绍

支持多边形/圆形雷达图，多系列数据对比，自定义指示器、分割层数、颜色配置。

## 目录结构

```
ComponentName/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   ├── RadarShape.vue         # 雷达图形状（多边形/圆形）
    │   ├── AreaColors.vue         # 区域颜色
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
    indicators: [
      { name: '销售', max: 100 },
      { name: '管理', max: 100 },
      { name: '信息技术', max: 100 },
      { name: '客服', max: 100 },
      { name: '研发', max: 100 },
      { name: '市场', max: 100 },
    ],
    series: [
      { name: '预算分配', value: [60, 73, 85, 40, 90, 88] },
      { name: '实际开销', value: [80, 50, 95, 60, 85, 70] },
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
| shape | String | 'polygon' | 形状：polygon/circle |
| areaColors | Array | 预设 | 区域颜色（fill+stroke） |
| splitNumber | Number | 5 | 分割层数 3-10 |

### 轴配置 (groupName: '轴配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| axisLineColor | String | 'rgba(255,255,255,0.3)' | 轴线颜色 |
| splitLineColor | String | 'rgba(255,255,255,0.1)' | 分割线颜色 |
| splitAreaColors | Array | 预设 | 分割区域颜色 |

### 标签配置 (groupName: '标签配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| labelColor | String | '#ffffff' | 标签颜色 |
| labelFontSize | Number | 12 | 标签字号 10-24 |

## ECharts Option 核心结构

```javascript
const option = {
  backgroundColor: 'transparent',
  tooltip: { trigger: 'item' },
  legend: { textStyle: { color: '#fff' }, bottom: 10 },
  radar: {
    indicator: indicators,
    shape: props.shape,
    splitNumber: props.splitNumber,
    axisName: { color: props.labelColor, fontSize: props.labelFontSize },
    axisLine: { lineStyle: { color: props.axisLineColor } },
    splitLine: { lineStyle: { color: props.splitLineColor } },
    splitArea: { areaStyle: { color: props.splitAreaColors } },
  },
  series: [{
    type: 'radar',
    data: seriesData.map((item, index) => {
      const colorConfig = props.areaColors[index % props.areaColors.length];
      return {
        name: item.name,
        value: item.value,
        areaStyle: { color: colorConfig.fill },
        lineStyle: { color: colorConfig.stroke, width: 2 },
      };
    }),
  }],
};
```

## 完整代码

完整雷达图组件代码请参考 `references/component-templates.md` 第七节中的 index.vue。