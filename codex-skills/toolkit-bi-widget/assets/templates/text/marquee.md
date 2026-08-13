# 跑马灯组件模板 (MarqueeText)

完整参考：`references/component-templates.md` 第八章 8.3 节

## Props 定义

### 数据配置

```javascript
text: {
  type: String,
  default: '这是一条跑马灯滚动文本，用于展示公告或重要信息。',
  desc: '滚动文本',
  name: '滚动文本',
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| speed | Number | 50 | 滚动速度（像素/秒）10-200 |
| fontSize | Number | 16 | 字体大小 12-48 |
| fontColor | String | '#ffffff' | 字体颜色 |
| direction | String | 'left' | 滚动方向：left/right |
| pauseOnHover | Boolean | true | 悬停暂停 |

## 核心逻辑

```javascript
const checkScroll = () => {
  const containerWidth = containerRef.value.offsetWidth;
  const textWidth = contentRef.value.querySelector('.text')?.offsetWidth || 0;
  needScroll.value = textWidth > containerWidth;
};

const startAnimation = () => {
  if (!needScroll.value || !contentRef.value) return;
  const textWidth = contentRef.value.querySelector('.text').offsetWidth;
  const duration = (textWidth * 2) / props.speed;
  contentRef.value.style.animation = `marquee-${props.direction} ${duration}s linear infinite`;
};
```

## CSS 动画

```css
@keyframes marquee-left {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

@keyframes marquee-right {
  0% { transform: translateX(-50%); }
  100% { transform: translateX(0); }
}
```

完整跑马灯组件代码请参考 `references/component-templates.md` 第八章 8.3 节。
