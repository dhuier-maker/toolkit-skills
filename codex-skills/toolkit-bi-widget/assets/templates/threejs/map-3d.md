# 3D 地图模板 (Map3D)

## 功能介绍

基于 Three.js 的 3D 地图可视化组件，支持区域高亮、地形展示、数据柱状图叠加。适用于区域数据可视化、地理信息展示等场景。

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
regionData: {
  type: Array,
  default: () => [
    { name: '区域A', value: 100, color: '#00a8e8', path: [] },
    { name: '区域B', value: 200, color: '#00d4aa', path: [] },
  ],
  desc: '区域数据数组',
  name: '区域数据',
  groupKey: 'data',
  groupName: '数据配置',
  useDynamic: true,
  sort: 1,
},

mapCenter: {
  type: Object,
  default: () => ({ x: 0, z: 0 }),
  desc: '地图中心坐标',
  name: '地图中心',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 2,
},
```

### 样式配置 (groupKey: 'style')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| terrainColor | String | '#0d1b2a' | 地形颜色 |
| regionColor | String | '#1a3a5c' | 区域颜色 |
| borderColor | String | '#00a8e8' | 边界颜色 |
| extrusionHeight | Number | 10 | 区域拉伸高度 |
| enableGrid | Boolean | true | 显示网格 |

## 核心逻辑

```javascript
// 创建区域（使用 ShapeGeometry 拉伸）
const createRegion = (region) => {
  const shape = new THREE.Shape();
  region.path.forEach((point, i) => {
    if (i === 0) shape.moveTo(point.x, point.z);
    else shape.lineTo(point.x, point.z);
  });

  const extrudeSettings = {
    depth: props.extrusionHeight,
    bevelEnabled: true,
    bevelThickness: 0.5,
    bevelSize: 0.3,
  };

  const geometry = new THREE.ExtrudeGeometry(shape, extrudeSettings);
  const material = new THREE.MeshStandardMaterial({
    color: region.color || props.regionColor,
    roughness: 0.7,
    metalness: 0.2,
  });

  const mesh = new THREE.Mesh(geometry, material);
  return mesh;
};
```

## 完整代码

本模板基于 Three.js 通用骨架开发，完整代码可参考 `references/threejs-templates.md` 第一节的通用骨架进行扩展。
