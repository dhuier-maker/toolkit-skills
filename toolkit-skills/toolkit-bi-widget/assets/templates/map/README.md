# 地图组件模板

适用于高德地图 API 的地图可视化组件，包括点位地图、热力图、飞线图、边界地图等。

## 支持的模板

| 模板文件 | 说明 |
|----------|------|
| `china-map.md` | 中国地图组件，支持点位标记、热力图、区域高亮 |

## 关键依赖

```javascript
import AMapLoader from '@amap/amap-jsapi-loader';
```

## 初始化模式

```javascript
const initMap = () => {
  AMapLoader.reset();
  AMapLoader.load({
    key: 'YOUR_AMAP_KEY',
    version: '2.0',
    Loca: { version: '2.0.0' },
    plugins: ['AMap.DistrictSearch', 'AMap.Polyline', 'AMap.convertFrom'],
  }).then((AMap) => {
    chart.value = new AMap.Map('map-container', {
      layers: [new AMap.TileLayer.Satellite()],
      mapStyle: 'amap://styles/whitesmoke',
      center: props.mapCenter,
      zoom: props.mapZoom,
    });
    // 添加标记点
  });
};
```

## 安全配置

```javascript
window._AMapSecurityConfig = {
  securityJsCode: 'YOUR_SECURITY_CODE',
};
```

## 核心 Props

- `dynamicData` (Object) - 地图点位数据，标记 `useDynamic: true`
- `mapCenter` (Array) - 地图中心点坐标
- `mapZoom` (Number) - 地图缩放级别

## 生命周期

```javascript
onMounted(() => {
  window._AMapSecurityConfig = { securityJsCode: 'YOUR_SECURITY_CODE' };
});

onUnmounted(() => {
  chart.value?.destroy();
});
```
