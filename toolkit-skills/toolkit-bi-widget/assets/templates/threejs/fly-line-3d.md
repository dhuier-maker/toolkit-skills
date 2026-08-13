# 3D 飞线模板 (FlyLine3D)

完整参考：`references/threejs-templates.md` 第三节（飞线部分）

## 功能介绍

数据飞线可视化组件，支持贝塞尔曲线飞线、流动点动画、起点/终点标记。适用于数据流向、迁徙图、物流路线等场景。

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
flyLineData: {
  type: Array,
  default: () => [
    { from: { lat: 35.86, lng: 104.19 }, to: { lat: 37.09, lng: -95.71 }, value: 5000, color: '#00d4aa' },
    { from: { lat: 35.86, lng: 104.19 }, to: { lat: 36.20, lng: 138.25 }, value: 3000, color: '#00a8e8' },
  ],
  desc: '飞线数据',
  name: '飞线数据',
  groupKey: 'data',
  groupName: '数据配置',
  useDynamic: true,
  sort: 1,
},

startPoints: {
  type: Array,
  default: () => [
    { name: '北京', lat: 39.90, lng: 116.40 },
  ],
  desc: '起点标记',
  name: '起点',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 2,
},

endPoints: {
  type: Array,
  default: () => [
    { name: '上海', lat: 31.23, lng: 121.47 },
  ],
  desc: '终点标记',
  name: '终点',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 3,
},
```

### 样式/动画配置 (groupKey: 'style')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| lineColor | String | '#00d4aa' | 飞线颜色 |
| lineOpacity | Number | 0.8 | 飞线透明度 0-1 |
| lineWidth | Number | 2 | 飞线宽度 |
| dotSize | Number | 3 | 流动点大小 |
| flySpeed | Number | 1 | 飞线速度 0.1-5 |
| arcHeight | Number | 0.3 | 弧线高度系数 |

## 核心逻辑

### 飞线创建

```javascript
const createFlyLine = (data) => {
  const startPoint = latLngToVector3(data.from.lat, data.from.lng, earthRadius);
  const endPoint = latLngToVector3(data.to.lat, data.to.lng, earthRadius);

  // 贝塞尔曲线控制点（向外抬高）
  const midPoint = new THREE.Vector3()
    .addVectors(startPoint, endPoint)
    .multiplyScalar(0.5);
  const distance = startPoint.distanceTo(endPoint);
  midPoint.normalize().multiplyScalar(earthRadius + distance * props.arcHeight);

  // 创建曲线
  const curve = new THREE.QuadraticBezierCurve3(startPoint, midPoint, endPoint);
  const points = curve.getPoints(100);

  // 飞线几何体
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({
    color: data.color || props.lineColor,
    transparent: true,
    opacity: props.lineOpacity,
  });

  const line = new THREE.Line(geometry, material);
  line.userData.curve = curve;
  line.userData.progress = Math.random();
  scene.add(line);

  // 流动点
  const dotGeometry = new THREE.SphereGeometry(props.dotSize, 8, 8);
  const dotMaterial = new THREE.MeshBasicMaterial({
    color: data.color || props.lineColor,
  });
  const dot = new THREE.Mesh(dotGeometry, dotMaterial);
  dot.userData.curve = curve;
  dot.userData.progress = Math.random();
  scene.add(dot);
};
```

### 动画更新

```javascript
const animate = () => {
  requestAnimationFrame(animate);

  flyLines.forEach((obj) => {
    if (obj.userData.curve) {
      obj.userData.progress += 0.005 * props.flySpeed;
      if (obj.userData.progress > 1) obj.userData.progress = 0;

      if (obj.type === 'Mesh') {
        const point = obj.userData.curve.getPoint(obj.userData.progress);
        obj.position.copy(point);
      }
    }
  });

  renderer.render(scene, camera);
};
```

## 完整代码

完整飞线代码可参考 `references/threejs-templates.md` 第三节 Earth3D 中的飞线相关部分。
