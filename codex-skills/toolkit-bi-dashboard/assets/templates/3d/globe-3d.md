# 3D 地球组件 (Globe3D.vue)

> 基于 Three.js 的 3D 地球可视化组件，含数据点、光柱、大气层光晕、自动旋转。

---

```vue
<template>
  <div class="globe-3d" ref="wrapperRef">
    <div v-if="loading" class="globe-loading">
      <i class="el-icon-loading"></i>
      <span>3D 地球加载中...</span>
    </div>
    <div v-if="error" class="globe-error">
      <i class="el-icon-warning"></i>
      <span>{{ error }}</span>
    </div>
    <div ref="containerRef" class="globe-container"></div>
    <div class="globe-overlay" v-if="topData.length > 0">
      <div class="data-panel">
        <div class="panel-title">全球数据分布</div>
        <div class="data-item" v-for="item in topData" :key="item.name">
          <span class="data-name">{{ item.name }}</span>
          <span class="data-value">{{ formatNumber(item.value) }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'

export default {
  name: 'Globe3D',
  props: {
    data: {
      type: Array,
      default: () => [
        { name: '北京', lat: 39.9, lng: 116.4, value: 85 },
        { name: '上海', lat: 31.2, lng: 121.5, value: 92 },
        { name: '广州', lat: 23.1, lng: 113.3, value: 78 },
        { name: '深圳', lat: 22.5, lng: 114.1, value: 88 },
        { name: '成都', lat: 30.6, lng: 104.1, value: 65 },
        { name: '杭州', lat: 30.3, lng: 120.2, value: 72 },
        { name: '武汉', lat: 30.6, lng: 114.3, value: 60 },
        { name: '西安', lat: 34.3, lng: 108.9, value: 55 }
      ]
    },
    radius: { type: Number, default: 80 },
    autoRotate: { type: Boolean, default: true },
    rotateSpeed: { type: Number, default: 0.002 }
  },
  data() {
    return {
      scene: null, camera: null, renderer: null, controls: null,
      globe: null, points: [], bars: [], animationId: null,
      topData: [], loading: true, error: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      setTimeout(() => { this.initThree() }, 100)
    })
  },
  beforeDestroy() { this.cleanup() },
  methods: {
    formatNumber(value) {
      return value ? value.toLocaleString() : '0'
    },

    cleanup() {
      if (this.animationId) { cancelAnimationFrame(this.animationId); this.animationId = null }
      if (this.renderer) { this.renderer.dispose(); this.renderer = null }
      if (this.scene) {
        this.scene.traverse((object) => {
          if (object.geometry) object.geometry.dispose()
          if (object.material) {
            if (Array.isArray(object.material)) { object.material.forEach(m => m.dispose()) }
            else { object.material.dispose() }
          }
        })
        this.scene = null
      }
      this.camera = null; this.controls = null; this.globe = null
      window.removeEventListener('resize', this.handleResize)
    },

    initThree() {
      try {
        const container = this.$refs.containerRef
        const wrapper = this.$refs.wrapperRef
        const width = wrapper.clientWidth || 400
        const height = wrapper.clientHeight || 400
        if (width === 0 || height === 0) {
          this.error = '容器尺寸为 0，请检查 CSS'
          this.loading = false
          return
        }

        this.scene = new THREE.Scene()
        this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000)
        this.camera.position.z = 250

        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
        this.renderer.setSize(width, height)
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
        container.appendChild(this.renderer.domElement)

        this.controls = new OrbitControls(this.camera, this.renderer.domElement)
        this.controls.enableDamping = true
        this.controls.dampingFactor = 0.05
        this.controls.minDistance = 120
        this.controls.maxDistance = 400
        this.controls.enablePan = false

        const ambientLight = new THREE.AmbientLight(0x404040, 1.5)
        this.scene.add(ambientLight)
        const directionalLight = new THREE.DirectionalLight(0xffffff, 1)
        directionalLight.position.set(1, 1, 1)
        this.scene.add(directionalLight)

        this.createGlobe()
        this.addDataPoints()
        this.animate()
        window.addEventListener('resize', this.handleResize)
        this.loading = false
      } catch (e) {
        console.error('Three.js 初始化失败:', e)
        this.error = '3D 渲染初始化失败: ' + e.message
        this.loading = false
      }
    },

    createGlobe() {
      const geometry = new THREE.SphereGeometry(this.radius, 64, 64)
      const material = new THREE.MeshPhongMaterial({
        color: 0x0d1b2a, transparent: true, opacity: 0.9, shininess: 30
      })
      this.globe = new THREE.Mesh(geometry, material)
      this.scene.add(this.globe)

      const wireframeGeometry = new THREE.SphereGeometry(this.radius + 0.5, 32, 32)
      const wireframeMaterial = new THREE.MeshBasicMaterial({
        color: 0x00d4ff, wireframe: true, transparent: true, opacity: 0.15
      })
      this.scene.add(new THREE.Mesh(wireframeGeometry, wireframeMaterial))

      const atmosphereGeometry = new THREE.SphereGeometry(this.radius * 1.15, 64, 64)
      const atmosphereMaterial = new THREE.MeshBasicMaterial({
        color: 0x00d4ff, transparent: true, opacity: 0.1, side: THREE.BackSide
      })
      this.scene.add(new THREE.Mesh(atmosphereGeometry, atmosphereMaterial))
    },

    addDataPoints() {
      if (!this.data || this.data.length === 0) return

      const latLngToVector3 = (lat, lng, radius) => {
        const phi = (90 - lat) * (Math.PI / 180)
        const theta = (lng + 180) * (Math.PI / 180)
        return new THREE.Vector3(
          -(radius * Math.sin(phi) * Math.cos(theta)),
          radius * Math.cos(phi),
          radius * Math.sin(phi) * Math.sin(theta)
        )
      }

      const sorted = [...this.data].sort((a, b) => b.value - a.value).slice(0, 5)
      this.topData = sorted

      this.data.forEach(item => {
        const position = latLngToVector3(item.lat, item.lng, this.radius)

        const pointGeometry = new THREE.SphereGeometry(1.5, 16, 16)
        const pointMaterial = new THREE.MeshBasicMaterial({ color: 0x00d4ff, transparent: true, opacity: 0.9 })
        const point = new THREE.Mesh(pointGeometry, pointMaterial)
        point.position.copy(position)
        this.scene.add(point)
        this.points.push(point)

        const barHeight = Math.min(item.value / 5, 25)
        const barGeometry = new THREE.CylinderGeometry(0.8, 0.8, barHeight, 8)
        const barMaterial = new THREE.MeshBasicMaterial({ color: 0x00d4ff, transparent: true, opacity: 0.7 })
        const bar = new THREE.Mesh(barGeometry, barMaterial)
        const direction = position.clone().normalize()
        bar.position.copy(position.clone().add(direction.clone().multiplyScalar(barHeight / 2)))
        bar.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), direction)
        this.scene.add(bar)
        this.bars.push(bar)
      })
    },

    animate() {
      this.animationId = requestAnimationFrame(this.animate)
      if (this.autoRotate && this.globe) { this.globe.rotation.y += this.rotateSpeed }
      if (this.controls) { this.controls.update() }
      if (this.renderer && this.scene && this.camera) {
        this.renderer.render(this.scene, this.camera)
      }
    },

    handleResize() {
      const wrapper = this.$refs.wrapperRef
      if (!wrapper || !this.camera || !this.renderer) return
      const width = wrapper.clientWidth
      const height = wrapper.clientHeight
      if (width === 0 || height === 0) return
      this.camera.aspect = width / height
      this.camera.updateProjectionMatrix()
      this.renderer.setSize(width, height)
    }
  },
  watch: {
    data: {
      handler() {
        this.points.forEach(p => this.scene?.remove(p))
        this.bars.forEach(b => this.scene?.remove(b))
        this.points = []; this.bars = []
        if (this.scene) { this.addDataPoints() }
      },
      deep: true
    }
  }
}
</script>

<style lang="scss" scoped>
.globe-3d {
  width: 100%;
  height: 100%;
  min-height: 300px;
  position: relative;
}

.globe-container { width: 100%; height: 100%; }

.globe-loading, .globe-error {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background: rgba(13, 27, 42, 0.9);
  color: #87ceeb;
  font-size: 14px;
  z-index: 10;
  i { font-size: 32px; }
}

.globe-error { color: #ff6b6b; }

.globe-overlay {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 10;
  pointer-events: none;
}

.data-panel {
  padding: 16px;
  background: rgba(13, 27, 42, 0.9);
  border: 1px solid rgba(0, 212, 255, 0.3);
  border-radius: 8px;
}

.panel-title {
  font-size: 14px;
  color: #00d4ff;
  margin-bottom: 12px;
}

.data-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6px 0;
  border-bottom: 1px solid rgba(0, 212, 255, 0.1);
  &:last-child { border-bottom: none; }
}

.data-name { font-size: 12px; color: #87ceeb; }
.data-value { font-size: 14px; color: #fff; font-weight: bold; }
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| data | Array | (预设示例) | 数据点 [{name, lat, lng, value}] |
| radius | Number | 80 | 地球半径 |
| autoRotate | Boolean | true | 是否自动旋转 |
| rotateSpeed | Number | 0.002 | 旋转速度 |

---

## 数据格式

```javascript
globeData: [
  { name: '北京', lat: 39.9, lng: 116.4, value: 85 },
  { name: '上海', lat: 31.2, lng: 121.5, value: 92 }
]
```

---

## 依赖

```bash
npm install three --save
```
