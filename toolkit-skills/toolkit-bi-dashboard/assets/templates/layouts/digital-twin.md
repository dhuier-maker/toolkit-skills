# 3D数字孪生布局模板

> 适用于3D数字孪生场景，中间区域承载大型 Three.js 3D 场景，左右面板较窄（280px），3D场景上方可叠加浮动数据面板。

---

## 一、布局结构

```
┌─────────────────────────────────────────────────────────────┐
│                      顶部标题栏                              │
├──────────┬─────────────────────────────────┬────────────────┤
│          │                                 │                │
│ 左面板    │     3D数字孪生场景               │   右面板       │
│ (280px)  │   (Three.js + 数据叠加层)        │  (280px)      │
│          │   [数据面板1] [数据面板2]         │                │
└──────────┴─────────────────────────────────┴────────────────┘
```

---

## 二、Dashboard.vue 核心模板

```vue
<template>
  <div class="digital-twin-dashboard" :class="`theme-${currentTheme}`">
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

      <!-- 中间3D场景区域 -->
      <section class="center-area">
        <!-- Three.js 渲染容器 -->
        <div class="three-container" ref="threeContainer"></div>

        <!-- 3D场景叠加数据面板 -->
        <div class="overlay-panels">
          <div
            class="overlay-panel"
            v-for="overlay in overlayPanels"
            :key="overlay.id"
            :style="{ top: overlay.top, left: overlay.left, right: overlay.right, bottom: overlay.bottom }"
          >
            <div class="overlay-header">{{ overlay.title }}</div>
            <div class="overlay-body">
              <div class="overlay-metric" v-for="metric in overlay.metrics" :key="metric.label">
                <span class="metric-value">{{ metric.value }}</span>
                <span class="metric-label">{{ metric.label }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 3D场景底部工具栏 -->
        <div class="scene-toolbar">
          <button
            class="tool-btn"
            v-for="tool in sceneTools"
            :key="tool.id"
            :class="{ active: activeTool === tool.id }"
            @click="switchTool(tool.id)"
          >
            <span class="tool-icon" v-html="tool.icon"></span>
            <span class="tool-label">{{ tool.label }}</span>
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
  name: 'DigitalTwinDashboard',
  components: { DateTimeDisplay },
  props: {
    title: { type: String, default: '3D数字孪生平台' },
    theme: { type: String, default: 'techBlue' },
    sceneUrl: { type: String, default: '' },
    autoRotate: { type: Boolean, default: true },
  },
  setup(props) {
    const threeContainer = ref(null)
    const activeTool = ref('overview')
    const currentTheme = computed(() => props.theme)

    // Three.js 实例
    let scene, camera, renderer, controls, animationId

    // 左侧面板配置
    const leftPanels = reactive([
      { id: 'device-stats', title: '设备统计', component: 'DeviceStatsPanel', data: {} },
      { id: 'alarm-list', title: '告警列表', component: 'AlarmListPanel', data: {} },
    ])

    // 右侧面板配置
    const rightPanels = reactive([
      { id: 'env-monitor', title: '环境监测', component: 'EnvMonitorPanel', data: {} },
      { id: 'energy-stats', title: '能耗统计', component: 'EnergyStatsPanel', data: {} },
    ])

    // 叠加数据面板
    const overlayPanels = reactive([
      {
        id: 'overlay-1',
        title: '运行状态',
        top: '20px',
        left: '20px',
        right: 'auto',
        bottom: 'auto',
        metrics: [
          { label: '在线设备', value: '1,286' },
          { label: '离线设备', value: '23' },
        ],
      },
      {
        id: 'overlay-2',
        title: '今日告警',
        top: '20px',
        left: 'auto',
        right: '20px',
        bottom: 'auto',
        metrics: [
          { label: '紧急', value: '3' },
          { label: '一般', value: '17' },
        ],
      },
    ])

    // 场景工具栏
    const sceneTools = reactive([
      { id: 'overview', label: '总览', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg>' },
      { id: 'device', label: '设备', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M22 9V7h-2V5c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-2h2v-2h-2v-2h2v-2h-2V9h2zm-4 10H4V5h14v14zM6 13h5v4H6v-4zm6-6h4v3h-4V7zM6 7h5v5H6V7zm6 4h4v6h-4v-6z"/></svg>' },
      { id: 'alarm', label: '告警', icon: '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>' },
    ])

    // 初始化 Three.js 场景
    const initThreeScene = () => {
      if (!threeContainer.value) return

      const container = threeContainer.value
      const width = container.clientWidth
      const height = container.clientHeight

      // 场景
      scene = new THREE.Scene()
      scene.background = new THREE.Color(0x0a1628)

      // 相机
      camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 10000)
      camera.position.set(0, 100, 300)

      // 渲染器
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
      renderer.setSize(width, height)
      renderer.setPixelRatio(window.devicePixelRatio)
      container.appendChild(renderer.domElement)

      // 控制器
      controls = new OrbitControls(camera, renderer.domElement)
      controls.enableDamping = true
      controls.dampingFactor = 0.05
      controls.autoRotate = props.autoRotate
      controls.autoRotateSpeed = 0.5

      // 灯光
      const ambientLight = new THREE.AmbientLight(0x404040, 2)
      scene.add(ambientLight)
      const directionalLight = new THREE.DirectionalLight(0x00d4ff, 1)
      directionalLight.position.set(100, 200, 100)
      scene.add(directionalLight)

      // 地面网格
      const gridHelper = new THREE.GridHelper(500, 50, 0x00d4ff, 0x0a2a4a)
      scene.add(gridHelper)

      animate()
    }

    const animate = () => {
      animationId = requestAnimationFrame(animate)
      controls && controls.update()
      renderer && renderer.render(scene, camera)
    }

    const handleResize = () => {
      if (!threeContainer.value || !camera || !renderer) return
      const width = threeContainer.value.clientWidth
      const height = threeContainer.value.clientHeight
      camera.aspect = width / height
      camera.updateProjectionMatrix()
      renderer.setSize(width, height)
    }

    const switchTool = (toolId) => {
      activeTool.value = toolId
    }

    const goBack = () => {}

    onMounted(() => {
      initThreeScene()
      window.addEventListener('resize', handleResize)
    })

    onBeforeUnmount(() => {
      window.removeEventListener('resize', handleResize)
      if (animationId) cancelAnimationFrame(animationId)
      if (renderer) {
        renderer.dispose()
        threeContainer.value && threeContainer.value.removeChild(renderer.domElement)
      }
      scene = null
      camera = null
      renderer = null
      controls = null
    })

    return {
      threeContainer, activeTool, currentTheme,
      leftPanels, rightPanels, overlayPanels, sceneTools,
      switchTool, goBack,
    }
  },
}
</script>
```

---

## 三、核心样式（含主题变量）

```scss
/* ========== 主题变量 ========== */
.digital-twin-dashboard {
  /* -- techBlue 深蓝科技风 -- */
  --bg-primary: #0a1628;
  --bg-panel: rgba(13, 27, 42, 0.85);
  --border-glow: rgba(0, 212, 255, 0.18);
  --accent: #00d4ff;
  --accent-glow: rgba(0, 212, 255, 0.5);
  --text-primary: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.6);
  --text-dim: rgba(255, 255, 255, 0.4);
  --overlay-bg: rgba(10, 22, 40, 0.75);
  --toolbar-bg: rgba(10, 22, 40, 0.9);
  --scene-bg: #0a1628;

  &.theme-partyRed {
    --bg-primary: #1a0a0a;
    --bg-panel: rgba(42, 13, 13, 0.85);
    --border-glow: rgba(255, 60, 60, 0.18);
    --accent: #ff3c3c;
    --accent-glow: rgba(255, 60, 60, 0.5);
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.6);
    --text-dim: rgba(255, 255, 255, 0.4);
    --overlay-bg: rgba(26, 10, 10, 0.75);
    --toolbar-bg: rgba(26, 10, 10, 0.9);
    --scene-bg: #1a0a0a;
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
    --overlay-bg: rgba(240, 244, 248, 0.85);
    --toolbar-bg: rgba(255, 255, 255, 0.95);
    --scene-bg: #e8edf2;
  }
}

/* ========== 布局样式 ========== */
.digital-twin-dashboard {
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

.header-left, .header-right { width: 180px; }

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
  width: 280px;
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

/* ========== 中间3D区域 ========== */
.center-area {
  flex: 1;
  position: relative;
  overflow: hidden;
  background: var(--scene-bg);
}

.three-container {
  width: 100%;
  height: 100%;
}

/* ========== 叠加数据面板 ========== */
.overlay-panels {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.overlay-panel {
  position: absolute;
  min-width: 160px;
  background: var(--overlay-bg);
  border: 1px solid var(--border-glow);
  border-radius: 6px;
  backdrop-filter: blur(8px);
  pointer-events: auto;
}

.overlay-header {
  padding: 8px 12px;
  font-size: 12px;
  color: var(--accent);
  border-bottom: 1px solid var(--border-glow);
}

.overlay-body {
  padding: 8px 12px;
  display: flex;
  gap: 16px;
}

.overlay-metric {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.metric-value {
  font-size: 20px;
  font-weight: bold;
  color: var(--text-primary);
}

.metric-label {
  font-size: 11px;
  color: var(--text-secondary);
}

/* ========== 场景工具栏 ========== */
.scene-toolbar {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 4px;
  padding: 6px;
  background: var(--toolbar-bg);
  border: 1px solid var(--border-glow);
  border-radius: 8px;
  backdrop-filter: blur(8px);
}

.tool-btn {
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

  .tool-icon { display: flex; align-items: center; }
  .tool-label { font-size: 12px; }

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
| `title` | String | `'3D数字孪生平台'` | 大屏标题 |
| `theme` | String | `'techBlue'` | 主题：`techBlue` / `partyRed` / `lightBusiness` |
| `sceneUrl` | String | `''` | 3D模型加载地址（GLTF/GLB） |
| `autoRotate` | Boolean | `true` | 3D场景是否自动旋转 |

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
| `--overlay-bg` | `rgba(10,22,40,0.75)` | `rgba(26,10,10,0.75)` | `rgba(240,244,248,0.85)` |
| `--toolbar-bg` | `rgba(10,22,40,0.9)` | `rgba(26,10,10,0.9)` | `rgba(255,255,255,0.95)` |
| `--scene-bg` | `#0a1628` | `#1a0a0a` | `#e8edf2` |

---

## 七、使用指南

1. **3D场景加载**：通过 `sceneUrl` 传入 GLTF/GLB 模型地址，在 `initThreeScene` 中使用 GLTFLoader 加载
2. **叠加数据面板**：通过 `overlayPanels` 配置浮动面板的位置和内容，面板使用 `position: absolute` 叠加在3D场景上
3. **场景工具栏**：底部工具栏用于切换3D场景的视角模式（总览/设备/告警等）
4. **主题切换**：通过 `theme` prop 切换主题，所有颜色通过 CSS 变量自动适配
5. **注意事项**：
   - Three.js 渲染器需要在 `onMounted` 中初始化，`onBeforeUnmount` 中销毁
   - 窗口 resize 时需更新相机宽高比和渲染器尺寸
   - 叠加面板设置 `pointer-events: none` 以避免阻挡3D交互，面板本身设为 `auto`
   - 侧面板宽度较窄（280px），内容应精简，避免信息过载
