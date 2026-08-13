# 3D 可视化组件模板

> 为 BI 大屏提供炫酷的 3D 可视化能力，包括 3D 地球、3D 柱状图、3D 散点图、粒子特效。

## 技术选型

| 技术 | 特点 | 适用场景 |
|------|------|----------|
| Three.js | 最强大的 Web3D 库 | 3D 地球、复杂 3D 场景 |
| ECharts-GL | 与 ECharts 无缝集成 | 3D 柱状图、3D 散点图 |
| Canvas 2D | 轻量高性能 | 粒子特效 |

## 组件列表

| 文件 | 组件名 | 技术栈 | 功能 |
|------|--------|--------|------|
| [globe-3d.md](globe-3d.md) | Globe3D | Three.js | 3D 地球，含数据点、光柱、大气层光晕、自动旋转 |
| [bar-3d.md](bar-3d.md) | Bar3D | ECharts-GL | 3D 柱状图，多维度数据，自动旋转 |
| [scatter-3d.md](scatter-3d.md) | Scatter3D | ECharts-GL | 3D 散点图，三维数据分布 |
| [particle-effect.md](particle-effect.md) | ParticleEffect | Canvas 2D | 粒子特效，鼠标交互，粒子连线 |

## 依赖

```bash
npm install three echarts echarts-gl --save
```

## 通用注意事项

1. 容器必须有明确高度
2. Three.js 组件销毁时需正确清理：取消动画帧、释放几何体/材质、销毁渲染器
3. ECharts-GL 组件销毁时调用 dispose()
4. 检查浏览器 WebGL 支持
5. 大屏分辨率高时控制粒子数量 200-500

## 使用示例

```vue
<template>
  <div class="bi-dashboard">
    <ParticleEffect :count="100" color="#00d4ff" />
    <div class="center-area">
      <Globe3D :data="globeData" :auto-rotate="true" :radius="80" />
    </div>
    <div class="side-panel">
      <div class="panel-frame">
        <div class="panel-title">季度销售分析</div>
        <Bar3D :data="bar3DData" :x-data="['Q1','Q2','Q3','Q4']" :y-data="['产品A','产品B','产品C']" />
      </div>
    </div>
  </div>
</template>
```
