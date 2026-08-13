# 3D 粒子系统模板 (Particle3D)

完整参考：`references/threejs-templates.md` 第四节

## 功能介绍

炫酷粒子特效组件，支持多种分布形状（球形/立方体/锥形/螺旋）、多种动画类型（流动/爆炸/波动/环绕），适用于科技感背景、数据粒子展示。

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
particleCount: {
  type: Number,
  default: 10000,
  desc: '粒子数量',
  name: '粒子数量',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 1,
  min: 1000,
  max: 100000,
},

dataSource: {
  type: Array,
  default: () => null,
  desc: '数据源（可选，用于数据驱动粒子）',
  name: '数据源',
  groupKey: 'data',
  groupName: '数据配置',
  useDynamic: true,
  sort: 2,
},
```

### 样式配置 (groupKey: 'style')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| particleColor | String | '#00a8e8' | 粒子主色 |
| particleColor2 | String | '#00d4aa' | 粒子渐变色 |
| particleSize | Number | 2 | 粒子大小 0.5-10 |
| particleShape | String | 'sphere' | 分布形状：sphere/cube/cone/spiral |
| spreadRadius | Number | 200 | 扩散半径 50-500 |

### 动画配置 (groupKey: 'animation')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| animationType | String | 'flow' | 动画：flow/explode/wave/orbit |
| animationSpeed | Number | 1 | 动画速度 0.1-5 |
| enableGlow | Boolean | true | 发光效果 |

### 显示配置 (groupKey: 'display')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| showStats | Boolean | false | 统计面板（粒子数/FPS） |
| autoRotate | Boolean | true | 自动旋转 |

## 粒子创建

```javascript
particleGeometry = new THREE.BufferGeometry();
positions = new Float32Array(props.particleCount * 3);
colors = new Float32Array(props.particleCount * 3);

// 根据形状生成位置
for (let i = 0; i < props.particleCount; i++) {
  let x, y, z;
  switch (props.particleShape) {
    case 'sphere':
      // 球体内均匀分布
      break;
    case 'cube':
      // 立方体内均匀分布
      break;
    case 'cone':
      // 锥形分布
      break;
    case 'spiral':
      // 螺旋分布
      break;
  }
  positions[i3] = x;
  positions[i3 + 1] = y;
  positions[i3 + 2] = z;
}

particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
particleGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

particleMaterial = new THREE.PointsMaterial({
  size: props.particleSize,
  vertexColors: true,
  blending: props.enableGlow ? THREE.AdditiveBlending : THREE.NormalBlending,
});

particles = new THREE.Points(particleGeometry, particleMaterial);
scene.add(particles);
```

## 完整代码

完整粒子系统代码请参考 `references/threejs-templates.md` 第四节中的 index.vue。
