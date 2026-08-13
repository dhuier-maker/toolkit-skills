# 标题组件模板 (TitleText)

完整参考：`references/component-templates.md` 第八章 8.1 节

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
text: {
  type: String,
  default: '大屏标题',
  desc: '标题文本',
  name: '标题文本',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| fontSize | Number | 32 | 字体大小 12-72 |
| fontColor | String | '#ffffff' | 字体颜色 |
| fontWeight | String | 'bold' | 字体粗细 |
| textAlign | String | 'center' | 文本对齐 |
| textShadow | Boolean | true | 文字阴影 |
| shadowColor | String | 'rgba(0,217,255,0.8)' | 阴影颜色 |
| background | String | 'gradient...' | 背景样式 |

## 模板结构

```html
<div class="title-container" :style="containerStyle">
  <div class="title-text" :style="textStyle">{{ text }}</div>
</div>
```

## 完整代码

```javascript
const containerStyle = computed(() => ({
  background: props.background,
  textAlign: props.textAlign,
}));

const textStyle = computed(() => ({
  fontSize: props.fontSize + 'px',
  color: props.fontColor,
  fontWeight: props.fontWeight,
  textShadow: props.textShadow
    ? `0 0 10px ${props.shadowColor}, 0 0 20px ${props.shadowColor}`
    : 'none',
}));
```

完整标题组件代码请参考 `references/component-templates.md` 第八章 8.1 节。
