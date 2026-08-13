# 3D投影中心布局模板

> 适用于3D全息投影/数字人场景，中间区域承载旋转3D模型与光环效果，左右面板标准宽度（320px），适合展示核心3D主体与周边数据。

---

## 一、布局结构

```
┌─────────────────────────────────────────────────────────────┐
│                      顶部标题栏                              │
├──────────┬─────────────────────────────────┬────────────────┤
│          │                                 │                │
│ 左面板    │     3D投影中心                   │   右面板       │
│ (320px)  │  (旋转3D模型 + 光环效果)         │  (320px)      │
│          │                                 │                │
└──────────┴─────────────────────────────────┴────────────────┘
```

---

## 二、Dashboard.vue 核心模板

```vue
<template>
  <div class="hologram-center-dashboard" :class="`theme-${currentTheme}`">
    <!-- 顶部标题栏 -->
    <header class="dashboard-header">
      <div class="header-left">
        <button class="back-btn" @click="goBack">返回</button>
      </div>
      <div class="header-center">
        <h1 class="main-title">{{ title }}</h1>
      </div>
      <div class="header-right">
        <DateTimeDisplay />
      </div>
    </header>

    <!-- 主体内容 -->
    <main class="dashboard-main">
      <!-- 左侧面板 -->
      <aside class="side-panel left-panel">
        <div class="panel-frame" v-for="panel in leftPanels" :key="panel.id">
          <div class="panel-title">
            <span class="title-bar"></span>
            <span>{{ panel.title }}</span>
          </div>
          <div class="panel-content">
            <component :is="panel.component" :data="panel.data" />
          </div>
        </div>
      </aside>

      <!-- 中间3D投影区域 -->
      <section class="center-area">
        <!-- Three.js 渲染容器 -->
        <div class="hologram-container" ref="hologramContainer"></div>

        <!-- 光环效果层 -->
        <div class="halo-layer">
          <div class="halo-ring halo-ring-outer"></div>
          <div class="halo-ring halo-ring-middle"></div>
          <div class="halo-ring halo-ring-inner"></div>
        </div>

        <!-- 3D模型底部信息 -->
        <div class="hologram-info">
          <div class="info-item" v-for="info in hologramInfo" :key="info.label">
            <span class="info-value">{{ info.value }}</span>
            <span class="info-label">{{ info.label }}</span>
          </div>
        </div>

        <!-- 投影模式切换 -->
        <div class="projection-modes">
          <button
            class="mode-btn"
            v-for="mode in projectionModes"
            :key="mode.id"
            :class="{ active: activeMode === mode.id }"
            @click="switchMode(mode.id)"
          >
            <span class="mode-icon" v-html="mode.icon"></span>
            <span class="mode-label">{{ mode.label }}</span>
          </button>
        </div>
      </section>

      <!-- 右侧面板 -->
      <aside class="side-panel right-panel">
        <div class="panel-frame" v-for="panel in rightPanels" :key="panel.id">
          <div class="panel-title">
            <span class="title-bar"></span>
            <span>{{ panel.title }}</span>
          </div>
          <div class="panel-content">
            <component :is="panel.component" :data="panel.data" />
          </div>
        </div>
      </aside>
    </main>
  </div>
</template>

<script>
import { ref, reactive, onMounted, onBeforeUnmount, computed } from 'vue'
import DateTimeDisplay from './components/DateTimeDisplay.vue'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'

export default {
  name: 'HologramCenterDashboard',
  components: { DateTimeDisplay },
  props: {
    title: { type: String, default: '3D全息投影平台' },
    theme: { type: String, default: 'techBlue' },
    modelUrl: { type: String, default: '' },
    rotateSpeed: { type: Number, default: 0.01 },
    haloColor: { type: String, default: '' },
  },
  setup(props) {
    const hologramContainer = ref(null)
    const activeMode = ref('solid')
    const currentTheme = computed(() => props.theme)

    // Three.js 实例
    let scene, camera, renderer, controls, model, animationId

    // 左侧面板配置
    const leftPanels = reactive([
      { id: 'model-params', title: '模型参数', component: 'ModelParamsPanel', data: {} },
      { id: 'data-overview', title: '数据总览', component: 'DataOverviewPanel', data: {} },
      { id: 'timeline', title: '时间轴', component: 'TimelinePanel', data: {} },
    ])

    // 右侧面板配置
    const rightPanels = reactive([
      { id: 'detail-info', title: '详细信息', component: 'DetailInfoPanel', data: {} },
      { id: 'analysis', title: '分析报告', component: 'AnalysisPanel', data: {} },
    ])

    // 3D模型底部信息
    const hologramInfo = reactive([
      { label: '模型精度', value: '99.2%' },
      { label: '数据节点', value: '2,486' },
      { label: '实时帧率', value: '60 FPS' },
      { label: '渲染质量', value: 'Ultra' },
    ])

    // 投影模式
    const projectionModes = reactive([
      { id: 'solid', label: '实体', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/></svg>' },
      { id: 'wireframe', label: '线框', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M3 3h18v18H3V3zm2 2v14h14V5H5zm2 2h10v10H7V7z"/></svg>' },
      { id: 'xray', label: '透视', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>' },
      { id: 'particle', label: '粒子', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><circle cx="5" cy="5" r="2"/><circle cx="19" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><circle cx="8" cy="8" r="1.5"/><circle cx="16" cy="16" r="1.5"/></svg>' },
    ])

    // 初始化 Three.js 场景
    const initHologramScene = () => {
      if (!hologramContainer.value) return

      const container = hologramContainer.value
      const width = container.clientWidth
      const height = container.clientHeight

      // 场景
      scene = new THREE.Scene()
      scene.background = new THREE.Color(0x0a1628)

      // 相机
      camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 10000)
      camera.position.set(0, 50, 200)

      // 渲染器
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
      renderer.setSize(width, height)
      renderer.setPixelRatio(window.devicePixelRatio)
      container.appendChild(renderer.domElement)

      // 控制器
      controls = new OrbitControls(camera, renderer.domElement)
      controls.enableDamping = true
      controls.dampingFactor = 0.05
      controls.enablePan = false
      controls.minDistance = 80
      controls.maxDistance = 400

      // 灯光
      const ambientLight = new THREE.AmbientLight(0x404040, 1.5)
      scene.add(ambientLight)

      const pointLight1 = new THREE.PointLight(0x00d4ff, 2, 500)
      pointLight1.position.set(0, 100, 0)
      scene.add(pointLight1)

      const pointLight2 = new THREE.PointLight(0x00d4ff, 1, 300)
      pointLight2.position.set(0, -50, 100)
      scene.add(pointLight2)

      // 创建3D模型（示例：多面体）
      const geometry = new THREE.IcosahedronGeometry(40, 1)
      const material = new THREE.MeshPhongMaterial({
        color: 0x00d4ff,
        emissive: 0x003344,
        specular: 0x00d4ff,
        shininess: 100,
        transparent: true,
        opacity: 0.85,
        wireframe: false,
      })
      model = new THREE.Mesh(geometry, material)
      model.position.set(0, 20, 0)
      scene.add(model)

      // 外层光环（3D环面）
      const ringGeometry = new THREE.TorusGeometry(60, 0.5, 16, 100)
      const ringMaterial = new THREE.MeshBasicMaterial({
        color: 0x00d4ff,
        transparent: true,
        opacity: 0.6,
      })
      const ring1 = new THREE.Mesh(ringGeometry, ringMaterial)
      ring1.rotation.x = Math.PI / 2
      ring1.position.set(0, 20, 0)
      scene.add(ring1)

      const ring2 = new THREE.Mesh(ringGeometry.clone(), ringMaterial.clone())
      ring2.rotation.x = Math.PI / 3
      ring2.rotation.z = Math.PI / 4
      ring2.position.set(0, 20, 0)
      scene.add(ring2)

      // 底部圆形平台
      const platformGeometry = new THREE.CircleGeometry(80, 64)
      const platformMaterial = new THREE.MeshBasicMaterial({
        color: 0x00d4ff,
        transparent: true,
        opacity: 0.08,
        side: THREE.DoubleSide,
      })
      const platform = new THREE.Mesh(platformGeometry, platformMaterial)
      platform.rotation.x = -Math.PI / 2
      platform.position.set(0, -20, 0)
      scene.add(platform)

      // 底部网格
      const gridHelper = new THREE.GridHelper(200, 30, 0x00d4ff, 0x0a2a4a)
      gridHelper.position.set(0, -20, 0)
      scene.add(gridHelper)

      animate()
    }

    const animate = () => {
      animationId = requestAnimationFrame(animate)

      // 模型自旋转
      if (model) {
        model.rotation.y += props.rotateSpeed
      }

      controls && controls.update()
      renderer && renderer.render(scene, camera)
    }

    const switchMode = (modeId) => {
      activeMode.value = modeId
      if (!model) return

      switch (modeId) {
        case 'solid':
          model.material.wireframe = false
          model.material.opacity = 0.85
          model.material.transparent = true
          break
        case 'wireframe':
          model.material.wireframe = true
          model.material.opacity = 1.0
          model.material.transparent = false
          break
        case 'xray':
          model.material.wireframe = false
          model.material.opacity = 0.3
          model.material.transparent = true
          break
        case 'particle':
          // 粒子模式需要替换为 Points 对象，此处仅作模式标识
          model.material.wireframe = false
          model.material.opacity = 0.15
          model.material.transparent = true
          break
      }

      model.material.needsUpdate = true
    }

    const handleResize = () => {
      if (!hologramContainer.value || !camera || !renderer) return
      const width = hologramContainer.value.clientWidth
      const height = hologramContainer.value.clientHeight
      camera.aspect = width / height
      camera.updateProjectionMatrix()
      renderer.setSize(width, height)
    }

    const goBack = () => {}

    onMounted(() => {
      initHologramScene()
      window.addEventListener('resize', handleResize)
    })

    onBeforeUnmount(() => {
      window.removeEventListener('resize', handleResize)
      if (animationId) cancelAnimationFrame(animationId)
      if (renderer) {
        renderer.dispose()
        hologramContainer.value && hologramContainer.value.removeChild(renderer.domElement)
      }
      scene = null
      camera = null
      renderer = null
      controls = null
      model = null
    })

    return {
      hologramContainer, activeMode, currentTheme,
      leftPanels, rightPanels, hologramInfo, projectionModes,
      switchMode, goBack,
    }
  },
}
</script>
```

---

## 三、核心样式（含主题变量）

```scss
/* ========== 主题变量 ========== */
.hologram-center-dashboard {
  /* -- techBlue 深蓝科技风 -- */
  --bg-primary: #0a1628;
  --bg-panel: rgba(13, 27, 42, 0.85);
  --border-glow: rgba(0, 212, 255, 0.18);
  --accent: #00d4ff;
  --accent-glow: rgba(0, 212, 255, 0.5);
  --text-primary: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.6);
  --text-dim: rgba(255, 255, 255, 0.4);
  --halo-color: rgba(0, 212, 255, 0.25);
  --halo-border: rgba(0, 212, 255, 0.4);
  --scene-bg: #0a1628;
  --info-bg: rgba(10, 22, 40, 0.8);
  --mode-bg: rgba(10, 22, 40, 0.9);

  &.theme-partyRed {
    --bg-primary: #1a0a0a;
    --bg-panel: rgba(42, 13, 13, 0.85);
    --border-glow: rgba(255, 60, 60, 0.18);
    --accent: #ff3c3c;
    --accent-glow: rgba(255, 60, 60, 0.5);
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.6);
    --text-dim: rgba(255, 255, 255, 0.4);
    --halo-color: rgba(255, 60, 60, 0.25);
    --halo-border: rgba(255, 60, 60, 0.4);
    --scene-bg: #1a0a0a;
    --info-bg: rgba(26, 10, 10, 0.8);
    --mode-bg: rgba(26, 10, 10, 0.9);
  }

  &.theme-lightBusiness {
    --bg-primary: #f0f4f8;
    --bg-panel: rgba(255, 255, 255, 0.92);
    --border-glow: rgba(0, 120, 212, 0.18);
    --accent: #0078d4;
    --accent-glow: rgba(0, 120, 212, 0.5);
    --text-primary: #1a1a1a;
    --text-secondary: rgba(26, 26, 26, 0.6);
    --text-dim: rgba(26, 26, 26, 0.4);
    --halo-color: rgba(0, 120, 212, 0.2);
    --halo-border: rgba(0, 120, 212, 0.35);
    --scene-bg: #e8edf2;
    --info-bg: rgba(240, 244, 248, 0.9);
    --mode-bg: rgba(255, 255, 255, 0.95);
  }
}

/* ========== 布局样式 ========== */
.hologram-center-dashboard {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary);
  overflow: hidden;
}

.dashboard-header {
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  background: linear-gradient(180deg, var(--accent-glow), transparent);
  border-bottom: 1px solid var(--border-glow);
  flex-shrink: 0;
}

.header-left, .header-right { width: 200px; }

.back-btn {
  padding: 6px 16px;
  background: rgba(0, 212, 255, 0.15);
  border: 1px solid var(--accent);
  border-radius: 4px;
  color: var(--accent);
  cursor: pointer;
  &:hover { background: rgba(0, 212, 255, 0.25); }
}

.main-title {
  font-size: 28px;
  font-weight: bold;
  color: var(--text-primary);
  text-shadow: 0 0 20px var(--accent-glow);
  text-align: center;
}

.dashboard-main {
  flex: 1;
  display: flex;
  gap: 0;
  overflow: hidden;
}

/* ========== 侧面板 ========== */
.side-panel {
  width: 320px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 12px;
  overflow-y: auto;
  flex-shrink: 0;
  background: var(--bg-panel);
  border-right: 1px solid var(--border-glow);

  &.right-panel {
    border-right: none;
    border-left: 1px solid var(--border-glow);
  }

  &::-webkit-scrollbar { width: 3px; }
  &::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 2px; }
}

.panel-frame {
  border: 1px solid var(--border-glow);
  border-radius: 6px;
  background: var(--bg-panel);
  animation: breathe 3s ease-in-out infinite;
}

.panel-title {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  font-size: 14px;
  color: var(--accent);
  border-bottom: 1px solid var(--border-glow);
}

.title-bar {
  width: 3px;
  height: 14px;
  background: var(--accent);
  border-radius: 2px;
}

.panel-content {
  padding: 12px;
}

/* ========== 中间3D投影区域 ========== */
.center-area {
  flex: 1;
  position: relative;
  overflow: hidden;
  background: var(--scene-bg);
}

.hologram-container {
  width: 100%;
  height: 100%;
}

/* ========== 光环效果 ========== */
.halo-layer {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -55%);
  pointer-events: none;
}

.halo-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid var(--halo-border);
  background: transparent;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.halo-ring-outer {
  width: 360px;
  height: 360px;
  animation: halo-rotate 12s linear infinite, halo-pulse 4s ease-in-out infinite;
  border-style: dashed;
}

.halo-ring-middle {
  width: 280px;
  height: 280px;
  animation: halo-rotate 8s linear infinite reverse, halo-pulse 3s ease-in-out infinite 0.5s;
  border-width: 1.5px;
}

.halo-ring-inner {
  width: 200px;
  height: 200px;
  animation: halo-rotate 5s linear infinite, halo-pulse 2.5s ease-in-out infinite 1s;
  border-style: dotted;
}

@keyframes halo-rotate {
  from { transform: translate(-50%, -50%) rotate(0deg); }
  to { transform: translate(-50%, -50%) rotate(360deg); }
}

@keyframes halo-pulse {
  0%, 100% {
    opacity: 0.4;
    box-shadow: 0 0 10px var(--halo-color);
  }
  50% {
    opacity: 0.8;
    box-shadow: 0 0 30px var(--halo-color), 0 0 60px var(--halo-color);
  }
}

/* ========== 底部信息 ========== */
.hologram-info {
  position: absolute;
  bottom: 70px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 32px;
  padding: 10px 24px;
  background: var(--info-bg);
  border: 1px solid var(--border-glow);
  border-radius: 8px;
  backdrop-filter: blur(8px);
}

.info-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.info-value {
  font-size: 18px;
  font-weight: bold;
  color: var(--accent);
}

.info-label {
  font-size: 11px;
  color: var(--text-dim);
}

/* ========== 投影模式切换 ========== */
.projection-modes {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 4px;
  padding: 6px;
  background: var(--mode-bg);
  border: 1px solid var(--border-glow);
  border-radius: 8px;
  backdrop-filter: blur(8px);
}

.mode-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 8px 14px;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 4px;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s;

  .mode-icon { display: flex; align-items: center; }
  .mode-label { font-size: 12px; }

  &:hover {
    color: var(--text-primary);
    background: rgba(0, 212, 255, 0.08);
  }

  &.active {
    color: var(--accent);
    background: rgba(0, 212, 255, 0.12);
    border-color: var(--accent);
  }
}
```

---

## 四、呼吸动画

```scss
@keyframes breathe {
  0%, 100% {
    box-shadow: 0 0 8px rgba(0, 212, 255, 0.15);
    border-color: var(--border-glow);
  }
  50% {
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.35);
    border-color: var(--accent);
  }
}

.panel-frame {
  animation: breathe 3s ease-in-out infinite;
}
```

---

## 五、Props / 配置项

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `title` | String | `'3D全息投影平台'` | 大屏标题 |
| `theme` | String | `'techBlue'` | 主题：`techBlue` / `partyRed` / `lightBusiness` |
| `modelUrl` | String | `''` | 3D模型加载地址（GLTF/GLB） |
| `rotateSpeed` | Number | `0.01` | 模型自旋转速度（弧度/帧） |
| `haloColor` | String | `''` | 光环颜色（为空时跟随主题 accent 色） |

---

## 六、主题变量映射

| CSS变量 | techBlue（深蓝科技风） | partyRed（党建红金） | lightBusiness（浅色商务） |
|---------|----------------------|-------------------|----------------------|
| `--bg-primary` | `#0a1628` | `#1a0a0a` | `#f0f4f8` |
| `--bg-panel` | `rgba(13,27,42,0.85)` | `rgba(42,13,13,0.85)` | `rgba(255,255,255,0.92)` |
| `--border-glow` | `rgba(0,212,255,0.18)` | `rgba(255,60,60,0.18)` | `rgba(0,120,212,0.18)` |
| `--accent` | `#00d4ff` | `#ff3c3c` | `#0078d4` |
| `--accent-glow` | `rgba(0,212,255,0.5)` | `rgba(255,60,60,0.5)` | `rgba(0,120,212,0.5)` |
| `--text-primary` | `#ffffff` | `#ffffff` | `#1a1a1a` |
| `--text-secondary` | `rgba(255,255,255,0.6)` | `rgba(255,255,255,0.6)` | `rgba(26,26,26,0.6)` |
| `--text-dim` | `rgba(255,255,255,0.4)` | `rgba(255,255,255,0.4)` | `rgba(26,26,26,0.4)` |
| `--halo-color` | `rgba(0,212,255,0.25)` | `rgba(255,60,60,0.25)` | `rgba(0,120,212,0.2)` |
| `--halo-border` | `rgba(0,212,255,0.4)` | `rgba(255,60,60,0.4)` | `rgba(0,120,212,0.35)` |
| `--scene-bg` | `#0a1628` | `#1a0a0a` | `#e8edf2` |
| `--info-bg` | `rgba(10,22,40,0.8)` | `rgba(26,10,10,0.8)` | `rgba(240,244,248,0.9)` |
| `--mode-bg` | `rgba(10,22,40,0.9)` | `rgba(26,10,10,0.9)` | `rgba(255,255,255,0.95)` |

---

## 七、使用指南

1. **3D模型加载**：通过 `modelUrl` 传入 GLTF/GLB 模型地址，在 `initHologramScene` 中使用 GLTFLoader 加载替换默认多面体
2. **光环效果**：CSS 实现的三层光环（外/中/内），各自独立旋转和脉冲动画，通过 `--halo-color` 和 `--halo-border` 控制颜色
3. **投影模式**：底部工具栏支持四种模式切换 - 实体/线框/透视/粒子，通过修改材质属性实现
4. **底部信息栏**：展示模型关键指标，数据通过 `hologramInfo` 配置
5. **主题切换**：通过 `theme` prop 切换主题，所有颜色通过 CSS 变量自动适配
6. **注意事项**：
   - Three.js 渲染器需要在 `onMounted` 中初始化，`onBeforeUnmount` 中销毁
   - 窗口 resize 时需更新相机宽高比和渲染器尺寸
   - 光环效果使用 CSS `pointer-events: none` 不影响3D交互
   - 侧面板宽度为 320px，比数字孪生布局稍宽，可容纳更多信息
   - `rotateSpeed` 控制模型自旋转速度，设为 0 可关闭自旋转
   - `haloColor` 为空时跟随主题 accent 色，自定义时传入合法颜色值
