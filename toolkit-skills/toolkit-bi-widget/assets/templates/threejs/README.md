# 3D/WebGL 组件模板

基于 Three.js 的高级 3D 可视化组件模板，适用于智慧城市、数字孪生、3D 地球、建筑可视化等场景。

## 支持的模板

| 模板文件 | 说明 | 复杂度 |
|----------|------|--------|
| `city-3d.md` | 3D城市组件，建筑群、道路、区域边界 | 中 |
| `earth-3d.md` | 3D地球组件，国家标记、飞线动画、热力点 | 中 |
| `map-3d.md` | 3D地图组件，区域高亮、地形展示 | 中 |
| `particle-3d.md` | 3D粒子系统，粒子特效、数据驱动动画 | 低 |
| `fly-line-3d.md` | 3D飞线组件，数据流向、迁徙图 | 中 |
| `bar-3d.md` | 3D柱状图，立体柱状图、三维图表 | 低 |

## 技术栈

```
- Three.js r150+
- @types/three
- OrbitControls
- GLTFLoader / FBXLoader / OBJLoader
- DRACOLoader
```

## 通用 Three.js 组件骨架

完整基础骨架参考 `references/threejs-templates.md` 第一节。

### 关键点

1. **使用 `markRaw`** 避免 Three.js 对象被响应式代理
2. **生命周期管理**：onMounted 初始化，onUnmounted 清理
3. **动画循环**：使用 requestAnimationFrame
4. **资源清理**：dispose 几何体、材质、纹理、渲染器

### 通用 Props

```javascript
// 场景配置
backgroundColor: { type: String, default: '#0a1628' },
ambientLightIntensity: { type: Number, default: 0.6 },
directionalLightIntensity: { type: Number, default: 0.8 },

// 相机配置
cameraPosition: { type: Object, default: () => ({ x: 0, y: 100, z: 200 }) },
cameraFov: { type: Number, default: 60 },
enableAutoRotate: { type: Boolean, default: true },
autoRotateSpeed: { type: Number, default: 0.5 },

// 交互配置
enableZoom: { type: Boolean, default: true },
enablePan: { type: Boolean, default: true },
minDistance: { type: Number, default: 50 },
maxDistance: { type: Number, default: 1000 },
```

## 完整参考

- 基础骨架：`references/threejs-templates.md` 第一节
- 最佳实践：`references/threejs-best-practices.md`