# 中国地图模板 (China Map)

完整参考：`references/component-templates.md` 第二节

## 功能介绍

基于高德地图 API 的点位地图组件，支持多点标记、地图中心点设置、缩放控制。

## 目录结构

```
ComponentName/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   ├── MapCenter.vue          # 地图中心点配置
    │   ├── MapZoom.vue            # 缩放等级配置
    │   └── style/
    ├── locale/
    │   ├── index.js
    │   └── lang/
    │       ├── zh-cn.json
    │       └── en.json
    └── static/
        └── map/
```

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
dynamicData: {
  type: Object,
  default: () => ({
    points: [
      { name: '点位1', value: [119.418678, 26.812159], introduction: '描述信息' },
    ],
  }),
  desc: i18n.global.t('dataSpecification'),
  name: i18n.global.t('displayContent'),
  groupKey: 'data',
  groupName: i18n.global.t('dataConfiguration'),
  useDynamic: true,
  sort: 1,
},

mapCenter: {
  type: Array,
  default: () => [119.55451, 26.672242],
  groupKey: 'data',
  groupName: '数据配置',
  sort: 2,
  configurationTemplate: () => import('./components/MapCenter.vue'),
},

mapZoom: {
  type: Number,
  default: 9,
  groupKey: 'data',
  groupName: '数据配置',
  sort: 3,
  configurationTemplate: () => import('./components/MapZoom.vue'),
},
```

## 核心逻辑

```javascript
const initMap = (points) => {
  AMapLoader.reset();
  AMapLoader.load({
    key: 'YOUR_AMAP_KEY',
    version: '2.0',
    Loca: { version: '2.0.0' },
    plugins: ['AMap.DistrictSearch', 'AMap.Polyline'],
  }).then((AMap) => {
    chart.value = new AMap.Map('map', {
      layers: [new AMap.TileLayer.Satellite()],
      mapStyle: 'amap://styles/whitesmoke',
      center: props.mapCenter,
      zoom: props.mapZoom,
    });

    // 添加标记点
    points.forEach((item) => {
      const marker = new AMap.Marker({
        position: item.value,
        label: { content: item.name, direction: 'bottom' },
      });
      chart.value.add(marker);
    });
  });
};
```

## provide/inject 中心点和缩放

```javascript
provide('mapCenter', {
  mapCenter: currentMapCenter,
  setMapCenter: (center) => { currentMapCenter.value = center; },
});

provide('mapZoom', {
  mapZoom: currentMapZoom,
  setMapZoom: (zoom) => { currentMapZoom.value = zoom; },
});
```

## 完整代码

完整地图组件代码请参考 `references/component-templates.md` 第二节中的 index.vue。