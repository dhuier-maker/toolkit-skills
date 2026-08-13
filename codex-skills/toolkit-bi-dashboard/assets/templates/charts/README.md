# 图表组件模板

> 基于 ECharts 5.x 的可复用图表组件，适用于 BI 大屏数据展示。

| 文件 | 组件名 | 功能 |
|------|--------|------|
| [chart-bar.md](chart-bar.md) | ChartBar | 柱状图 — 支持横向/纵向，渐变配色 |
| [chart-pie.md](chart-pie.md) | ChartPie | 饼图/环形图 — 支持环形半径配置，内嵌标签 |
| [chart-line.md](chart-line.md) | ChartLine | 折线图 — 支持平滑曲线、面积填充、symbol 控制 |
| [data-card.md](data-card.md) | DataCard | 数据卡片 — 带图标、数值、变化率、点击交互 |
| [chart-gauge.md](chart-gauge.md) | ChartGauge | 仪表盘 — 半圆/整圆，指针/弧形进度，中心数字 |
| [chart-rank.md](chart-rank.md) | ChartRank | 排名列表 — 序号+进度条+自动滚动+金银铜高亮 |
| [chart-scatter.md](chart-scatter.md) | ChartScatter | 2D散点图 — 气泡大小映射、坐标轴规范、多系列 |
| [chart-badge.md](chart-badge.md) | ChartBadge | 状态标记 — 6状态色×4尺寸+地图脉冲动画 |
| [chart-timeline.md](chart-timeline.md) | ChartTimeline | 时间轴 — 节点状态色+内容卡片 |
| [chart-org.md](chart-org.md) | ChartOrg | 组织架构图 — ECharts树形/组织架构 |

## 通用特性

- 使用 ECharts 5.x API
- 自动响应窗口 resize
- 组件销毁时自动 dispose 释放资源
- 支持 watch 数据变化自动更新
- 配合主题系统的 CSS 变量实现配色切换

## 使用方式

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title"><span class="title-bar"></span><span>数据概览</span></div>
    <div class="panel-content">
      <ChartBar :data="barData" />
    </div>
  </div>
</template>

<script>
import ChartBar from '@/components/ChartBar.vue'

export default {
  components: { ChartBar },
  data() {
    return {
      barData: [
        { name: '分类A', value: 120 },
        { name: '分类B', value: 80 }
      ]
    }
  }
}
</script>
```

## 依赖

```bash
npm install echarts@5.2.2 --save
```
