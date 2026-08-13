# Props 定义规范

每个 prop 必须包含完整的元数据，用于可视化平台的配置面板生成。

## 元数据字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | Type | 是 | 数据类型（String/Number/Boolean/Array/Object） |
| default | Value | 是 | 默认值 |
| desc | String | 是 | 属性描述（支持i18n） |
| name | String | 是 | 显示名称（支持i18n） |
| groupKey | String | 是 | 分组键：'data' \| 'style' \| 'style-composing' |
| groupName | String | 是 | 分组名称（支持i18n） |
| sort | Number | 是 | 排序权重，控制配置面板显示顺序 |
| useDynamic | Boolean | 否 | 是否启用动态数据配置（数据类prop必填） |
| configurationTemplate | Function | 否 | 配置面板组件（动态导入） |
| hidden | Boolean | 否 | 是否在配置面板隐藏 |
| min | Number | 否 | 数值最小值 |
| max | Number | 否 | 数值最大值 |
| jsonExample | String | 否 | JSON示例格式 |

## 分组键规范

- `data`: 数据配置组 - 数据源、数据格式相关
- `style`: 样式配置组 - 颜色、尺寸、边框等
- `style-composing`: 排版配置组 - 对齐方式、布局等

## Props 定义示例

```javascript
const props = defineProps({
  // ========== 数据配置 ==========
  chartData: {
    type: Object,
    default: () => ({
      categories: ['类别1', '类别2', '类别3'],
      values: [100, 200, 150],
    }),
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  // ========== 样式配置 ==========
  barWidth: {
    type: Number,
    default: 30,
    desc: '柱体宽度',
    name: '柱体宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    min: 10,
    max: 100,
    configurationTemplate: () => import('./components/BarWidth.vue'),
  },

  barColor: {
    type: String,
    default: '#00D9FF',
    desc: '柱体颜色',
    name: '柱体颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    configurationTemplate: () => import('./components/BarColor.vue'),
  },

  // ========== 排版配置 ==========
  justifyContent: {
    type: String,
    default: 'start',
    desc: i18n.global.t('horizontalAlignment'),
    name: i18n.global.t('horizontalAlignment'),
    hidden: true,
    groupKey: 'style-composing',
    groupName: i18n.global.t('layout'),
    sort: 5,
    configurationTemplate: () => import('./components/JustifyContent.vue'),
  },
});
```

---

## 基础属性模板

```javascript
panelTitle: {
  type: String,
  default: '默认标题',
  desc: i18n.global.t('panelTitle'),
  name: i18n.global.t('panelTitle'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  sort: 1,
},
```

## 动态数据属性模板

```javascript
dynamicData: {
  type: Array,
  default: () => [{ id: 1, name: '示例' }],
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 2,
  jsonExample: '[{"id":1,"name":"示例"}]',
},
```

## 样式属性模板

```javascript
valueColor: {
  type: String,
  default: '#ffffff',
  desc: i18n.global.t('valueColor'),
  name: i18n.global.t('valueColor'),
  groupKey: 'style',
  groupName: i18n.global.t('styleConfiguration'),
  sort: 3,
  // hidden: true,  // 可选：隐藏高级配置
},
```
