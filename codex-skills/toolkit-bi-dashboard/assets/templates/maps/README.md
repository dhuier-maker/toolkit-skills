# GIS 地图组件模板

> 为 BI 大屏提供 GIS 地图可视化能力，支持 ECharts 地图和高德地图。

## 地图引擎对比

| 类型 | 组件 | 依赖 | 适用场景 |
|------|------|------|----------|
| ECharts 中国地图 | ChinaMap | echarts | 国内城市数据展示，散点+飞线 |
| 飞线地图 | FlyLinesMap | echarts | OD 流向可视化 |
| 高德地图 | AMapContainer | 高德 SDK | 国内景区、城市，需要底图 |

## 组件列表

| 文件 | 组件名 | 功能 |
|------|--------|------|
| [china-map.md](china-map.md) | ChinaMap | ECharts 中国地图 + 散点 + 飞线，多 CDN 兜底加载 |
| [fly-lines-map.md](fly-lines-map.md) | FlyLinesMap | 飞线地图（OD流向），端点脉冲动画 |
| [amap-container.md](amap-container.md) | AMapContainer | 高德地图容器，标记点、控制面板、错误重试 |

## 依赖

```bash
npm install echarts@5.2.2 --save
```

高德地图需要额外申请 Key。

## 通用注意事项

1. 容器必须有明确高度（`height: 100%` 需要父容器有明确高度）
2. 中国地图使用 CDN 加载 GeoJSON，需要网络通畅
3. 组件销毁时调用 dispose() 释放 ECharts 实例
4. 添加 loading 和 error 状态提升用户体验

## 使用示例

```vue
<template>
  <div class="center-area">
    <ChinaMap
      :scatter-data="scatterData"
      :lines-data="linesData"
      :show-lines="true"
      :show-scatter="true"
    />
  </div>
</template>

<script>
import ChinaMap from '@/components/ChinaMap.vue'

export default {
  components: { ChinaMap },
  data() {
    return {
      scatterData: [
        { name: '北京', lng: 116.405, lat: 39.905, value: 100 },
        { name: '上海', lng: 121.474, lat: 31.230, value: 90 }
      ],
      linesData: [
        { fromName: '北京', toName: '上海', fromCoords: [116.405, 39.905], toCoords: [121.474, 31.230], value: 95 }
      ]
    }
  }
}
</script>
```
