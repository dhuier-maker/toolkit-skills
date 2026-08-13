# 饼图模板 (Pie Chart)

完整参考：`references/component-templates.md` 第五节

## 功能介绍

支持饼图、环形图、玫瑰图三种类型，支持标签配置、图例配置、颜色自定义。

## 目录结构

```
ComponentName/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   ├── PieType.vue            # 饼图类型（饼图/环形/玫瑰）
    │   ├── InnerRadius.vue        # 内半径
    │   ├── Colors.vue             # 颜色序列
    │   ├── LabelPosition.vue      # 标签位置
    │   ├── LegendPosition.vue     # 图例位置
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
  type: Array,
  default: () => [
    { name: '类别A', value: 1048 },
    { name: '类别B', value: 735 },
    { name: '类别C', value: 580 },
    { name: '类别D', value: 484 },
    { name: '类别E', value: 300 },
  ],
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
| pieType | String | 'ring' | 类型：ring/rose/solid |
| innerRadius | Number | 50 | 内半径%（环形） 0-80 |
| outerRadius | Number | 70 | 外半径% 30-100 |
| colors | Array | 预设 | 颜色序列 |

### 标签配置 (groupName: '标签配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showLabel | Boolean | true | 显示标签 |
| labelPosition | String | 'outside' | 标签位置：outside/inside/center |
| labelFontSize | Number | 14 | 标签字号 10-30 |

### 图例配置 (groupName: '图例配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showLegend | Boolean | true | 显示图例 |
| legendPosition | String | 'bottom' | 图例位置：top/bottom/left/right |

## ECharts Option 核心结构

```javascript
const option = {
  backgroundColor: 'transparent',
  tooltip: { trigger: 'item' },
  legend: {
    show: props.showLegend,
    textStyle: { color: '#fff' },
  },
  color: props.colors,
  series: [{
    type: 'pie',
    radius: isRing ? [`${props.innerRadius}%`, `${props.outerRadius}%`] : [0, `${props.outerRadius}%`],
    roseType: isRose ? 'area' : false,
    label: {
      show: props.showLabel,
      position: props.labelPosition,
      formatter: '{b}: {d}%',
    },
    data: props.chartData,
  }],
};
```

## 完整代码

完整饼图组件代码请参考 `references/component-templates.md` 第五节中的 index.vue。