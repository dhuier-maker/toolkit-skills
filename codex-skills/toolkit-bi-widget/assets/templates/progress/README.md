# 进度/排名组件模板

适用于排名进度条、数据卡片、统计数字等无需 ECharts 的纯 CSS/动画组件。

## 支持的模板

| 模板文件 | 说明 |
|----------|------|
| `ranking-list.md` | 带横向进度条的城市排名列表 |
| `progress-bar.md` | 方块式进度条排名组件 |

## 通用特点

- 纯 CSS/动画实现，不依赖 ECharts
- 支持动画配置（时长、循环等）
- 使用 CSS 变量实现动态样式

## 动画配置示例

```javascript
const getAnimationDuration = computed(() => {
  const duration = props.animateDuration / 1000;
  const count = props.openAnimate ? 'infinite' : 0;
  return {
    animationDuration: duration + 's',
    animationIterationCount: count,
  };
});
```

## 完整参考

- **排名进度条** → `references/component-templates.md` 第三节
- **城市排名列表** → `references/component-templates.md` CityRankingList 章节