# 3D 地球模板 (Earth3D)

完整参考：`references/threejs-templates.md` 第三节

## 功能介绍

全球数据可视化组件，支持国家标记点、飞线动画、波纹效果、星空背景、大气层光晕。

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
countryData: {
  type: Array,
  default: () => [
    { name: '中国', code: 'CN', lat: 35.86, lng: 104.19, value: 125000 },
    { name: '美国', code: 'US', lat: 37.09, lng: -95.71, value: 85000 },
  ],
  desc: '国家数据',
  name: '国家数据',
  groupKey: 'data',
  groupName: '数据配置',
  useDynamic: true,
  sort: 1,
},

flyLineData: {
  type: Array,
  default: () => [
    { from: { lat: 35.86, lng: 104.19 }, to: { lat: 37.09, lng: -95.71 }, value: 5000 },
  ],
  desc: '飞线数据',
  name: '飞线数据',
  groupKey: 'data',
  groupName: '数据配置',
  useDynamic: true,
  sort: 2,
},
```

### 样式/动画配置

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| earthColor | String | '#0a1628' | 地球底色 |
| landColor | String | '#1a3a5c' | 陆地颜色 |
| markerColor | String | '#00a8e8' | 标记点颜色 |
| flyLineColor | String | '#00d4aa' | 飞线颜色 |
| earthRadius | Number | 100 | 地球半径 50-200 |
| autoRotate | Boolean | true | 自动旋转 |
| rotateSpeed | Number | 0.2 | 旋转速度 |
| flyLineSpeed | Number | 1 | 飞线速度 |

## 坐标转换工具

```javascript
const latLngToVector3 = (lat, lng, radius) => {
  const phi = (90 - lat) * (Math.PI / 180);
  const theta = (lng + 180) * (Math.PI / 180);
  const x = -radius * Math.sin(phi) * Math.cos(theta);
  const y = radius * Math.cos(phi);
  const z = radius * Math.sin(phi) * Math.sin(theta);
  return new THREE.Vector3(x, y, z);
};
```

## 核心要素

1. **地球主体** - SphereGeometry + MeshStandardMaterial
2. **大气层光晕** - ShaderMaterial 实现外层发光
3. **经纬网格** - 24条经线 + 12条纬线
4. **标记点** - 球体 + 光柱 + 波纹环
5. **飞线** - QuadraticBezierCurve3 贝塞尔曲线
6. **星空背景** - Points 粒子系统

## 完整代码

完整 3D 地球组件代码请参考 `references/threejs-templates.md` 第三节中的 index.vue。
