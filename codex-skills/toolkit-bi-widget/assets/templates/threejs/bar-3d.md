# 3D 柱状图模板 (Bar3D)

## 功能介绍

基于 Three.js 的立体柱状图组件，支持三维空间中的柱状图展示，每根柱子可独立设置颜色、高度，支持旋转和缩放交互。适用于需要立体效果的数据可视化场景。

## Props 定义

### 数据配置 (groupKey: 'data')

```javascript
chartData: {
  type: Array,
  default: () => [
    { name: '类别A', value: 85, color: '#00a8e8' },
    { name: '类别B', value: 70, color: '#00d4aa' },
    { name: '类别C', value: 95, color: '#4a90e2' },
    { name: '类别D', value: 60, color: '#faad14' },
    { name: '类别E', value: 80, color: '#ff4d4f' },
  ],
  desc: '柱状图数据',
  name: '数据',
  groupKey: 'data',
  groupName: '数据配置',
  useDynamic: true,
  sort: 1,
},
```

### 样式配置 (groupKey: 'style')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| barWidth | Number | 10 | 柱体宽度 |
| barDepth | Number | 10 | 柱体深度 |
| barGap | Number | 15 | 柱体间距 |
| defaultColor | String | '#00a8e8' | 默认颜色 |
| enableGlow | Boolean | true | 柱顶发光 |
| showLabels | Boolean | true | 显示标签 |

### 相机配置 (groupKey: 'camera')

| 属性名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| cameraPosition | Object | {x:80,y:60,z:80} | 相机位置 |
| enableAutoRotate | Boolean | true | 自动旋转 |

## 核心逻辑

```javascript
const createBars = () => {
  const maxValue = Math.max(...props.chartData.map(d => d.value));
  const scale = 50 / maxValue;

  props.chartData.forEach((data, index) => {
    const height = data.value * scale;
    const geometry = new THREE.BoxGeometry(props.barWidth, height, props.barDepth);
    const color = new THREE.Color(data.color || props.defaultColor);
    const material = new THREE.MeshStandardMaterial({
      color,
      roughness: 0.6,
      metalness: 0.3,
      emissive: props.enableGlow ? color : 0x000000,
      emissiveIntensity: props.enableGlow ? 0.2 : 0,
    });

    const bar = new THREE.Mesh(geometry, material);
    const xPos = (index - props.chartData.length / 2) * (props.barWidth + props.barGap);
    bar.position.set(xPos, height / 2, 0);
    bar.userData = data;
    scene.add(bar);
    bars.push(bar);
  });
};
```

## 完整代码

本模板基于 Three.js 通用骨架开发，参考 `references/threejs-templates.md` 第一节的通用骨架进行扩展。