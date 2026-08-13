# ECharts 图表组件模板

适用于所有 ECharts 可视化图表组件开发，包含柱状图、饼图、折线图、雷达图等。

## 支持图表类型

| 图表类型 | 文件名 | 说明 |
|----------|--------|------|
| 柱状图 | `bar.md` | 支持垂直/水平柱状图，渐变色柱体，圆角配置 |
| 饼图 | `pie.md` | 支持饼图、环形图、玫瑰图，标签/图例配置 |
| 折线图 | `line.md` | 支持多折线、面积图、平滑曲线，数据点配置 |
| 雷达图 | `radar.md` | 支持多边形/圆形雷达图，多系列对比 |

## 通用 Props 定义规范

所有 ECharts 图表组件遵循相同的 Props 定义规范：

- `chartData` (Object/Array) - 图表数据，标记 `useDynamic: true`
- 样式配置按分组名组织，`groupName` 对应配置面板分组名称
- 数值属性设置 `min`/`max` 范围限制
- 需要可视化配置的属性引用 `configurationTemplate`

## 通用生命周期

```javascript
onMounted(() => {
  initChart();
  window.addEventListener('resize', handleResize);
  const resizeObserver = new ResizeObserver(() => handleResize());
  if (chartRef.value) resizeObserver.observe(chartRef.value);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  chart.value?.dispose();
});
```

## 模板使用

1. 打开对应图表类型的模板文件（如 `bar.md`）
2. 复制完整 Vue 组件代码
3. 根据实际需求修改默认数据和 Props 配置
4. 按需添加配置面板组件和国际化文件

## 关键依赖

- `echarts` 5.x
- `vue-i18n`
- `element-plus` (配置面板)