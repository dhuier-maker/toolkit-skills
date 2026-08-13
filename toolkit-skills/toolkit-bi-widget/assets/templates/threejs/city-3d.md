# 3D 城市模板 (City3D)

完整参考：`references/threejs-templates.md` 第二节

## 功能介绍

智慧城市可视化组件，支持建筑群、道路、区域边界等 3D 展示。建筑按类型着色（商业/住宅/公共/工业），支持点击高亮和信息面板显示。

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
buildingData: {
  type: Array,
  default: () => [
    { id: 1, name: '商业中心A', type: 'commercial', x: 0, z: 0, width: 30, depth: 30, height: 80, area: 72000, floors: 20 },
    { id: 2, name: '住宅小区B', type: 'residential', x: 50, z: 30, width: 40, depth: 25, height: 50, area: 50000, floors: 15 },
    { id: 3, name: '医院', type: 'public', x: -40, z: -20, width: 50, depth: 40, height: 35, area: 70000, floors: 10 },
  ],
  desc: '建筑数据数组',
  name: '建筑数据',
  groupKey: 'data',
  groupName: '数据配置',
  useDynamic: true,
  sort: 1,
},

regionBoundary: {
  type: Array,
  default: () => [
    { x: -100, z: -100 },
    { x: 150, z: -100 },
    { x: 150, z: 100 },
    { x: -100, z: 100 },
  ],
  desc: '区域边界坐标',
  name: '区域边界',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 2,
},
```

### 样式配置 (groupKey: 'style')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| groundColor | String | '#0d1b2a' | 地面颜色 |
| buildingColors | Object | 预设 | 各类型建筑颜色 |
| enableGlow | Boolean | true | 发光效果 |
| glowIntensity | Number | 0.5 | 发光强度 0-1 |

## 核心对象

```javascript
let scene, camera, renderer, controls;
let buildings = [];
let raycaster, mouse;
```

## 建筑创建

```javascript
props.buildingData.forEach((data) => {
  const geometry = new THREE.BoxGeometry(data.width, data.height, data.depth);
  const color = new THREE.Color(getBuildingColor(data.type));
  const material = new THREE.MeshStandardMaterial({
    color,
    roughness: 0.7,
    metalness: 0.3,
    emissive: props.enableGlow ? color : 0x000000,
    emissiveIntensity: props.enableGlow ? props.glowIntensity : 0,
  });
  const building = new THREE.Mesh(geometry, material);
  building.position.set(data.x, data.height / 2, data.z);
  building.userData = { ...data };
  scene.add(building);
  buildings.push(building);
});
```

## 事件处理

```javascript
// 点击建筑
const handleClick = (event) => {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(buildings);
  if (intersects.length > 0) {
    const building = intersects[0].object;
    selectedBuilding.value = building.userData;
    emit('building-click', building.userData);
  }
};
```

## 完整代码

完整 3D 城市组件代码请参考 `references/threejs-templates.md` 第二节中的 index.vue。
