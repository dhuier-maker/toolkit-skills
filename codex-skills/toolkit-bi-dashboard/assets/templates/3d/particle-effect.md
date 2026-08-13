# 粒子特效组件 (ParticleEffect.vue)

> 基于 Canvas 2D 的粒子特效，支持鼠标交互、粒子连线，适合作为大屏背景。

---

```vue
<template>
  <div class="particle-effect" ref="containerRef">
    <canvas ref="canvasRef" class="particle-canvas"></canvas>
  </div>
</template>

<script>
export default {
  name: 'ParticleEffect',
  props: {
    count: { type: Number, default: 150 },
    color: { type: String, default: '#00d4ff' },
    size: { type: Number, default: 2 },
    linkDistance: { type: Number, default: 120 },
    speed: { type: Number, default: 0.3 }
  },
  data() {
    return {
      canvas: null, ctx: null, particles: [], animationId: null,
      mouse: { x: null, y: null }, width: 0, height: 0
    }
  },
  mounted() {
    this.$nextTick(() => { this.initCanvas() })
  },
  beforeDestroy() {
    if (this.animationId) { cancelAnimationFrame(this.animationId) }
    window.removeEventListener('resize', this.handleResize)
    if (this.canvas) {
      this.canvas.removeEventListener('mousemove', this.handleMouseMove)
      this.canvas.removeEventListener('mouseleave', this.handleMouseLeave)
    }
  },
  methods: {
    initCanvas() {
      this.canvas = this.$refs.canvasRef
      if (!this.canvas) return
      this.ctx = this.canvas.getContext('2d')
      this.resize()
      if (this.width > 0 && this.height > 0) {
        this.createParticles()
        this.animate()
        this.canvas.addEventListener('mousemove', this.handleMouseMove)
        this.canvas.addEventListener('mouseleave', this.handleMouseLeave)
        window.addEventListener('resize', this.handleResize)
      }
    },

    resize() {
      const container = this.$refs.containerRef
      if (!container) return
      this.width = container.clientWidth || 400
      this.height = container.clientHeight || 400
      this.canvas.width = this.width
      this.canvas.height = this.height
    },

    handleResize() {
      this.resize()
      this.createParticles()
    },

    createParticles() {
      this.particles = []
      for (let i = 0; i < this.count; i++) {
        this.particles.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          vx: (Math.random() - 0.5) * this.speed,
          vy: (Math.random() - 0.5) * this.speed,
          size: Math.random() * this.size + 1
        })
      }
    },

    animate() {
      if (!this.ctx || this.width === 0 || this.height === 0) return
      this.animationId = requestAnimationFrame(this.animate)

      this.ctx.clearRect(0, 0, this.width, this.height)

      this.particles.forEach((p, i) => {
        // 更新位置
        p.x += p.vx
        p.y += p.vy

        // 边界检测
        if (p.x < 0 || p.x > this.width) p.vx *= -1
        if (p.y < 0 || p.y > this.height) p.vy *= -1

        // 鼠标交互
        if (this.mouse.x !== null && this.mouse.y !== null) {
          const dx = this.mouse.x - p.x
          const dy = this.mouse.y - p.y
          const dist = Math.sqrt(dx * dx + dy * dy)
          if (dist < 100) {
            p.x -= dx * 0.02
            p.y -= dy * 0.02
          }
        }

        // 绘制粒子
        this.ctx.beginPath()
        this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2)
        this.ctx.fillStyle = this.color
        this.ctx.fill()

        // 绘制连线
        for (let j = i + 1; j < this.particles.length; j++) {
          const p2 = this.particles[j]
          const dx = p.x - p2.x
          const dy = p.y - p2.y
          const dist = Math.sqrt(dx * dx + dy * dy)
          if (dist < this.linkDistance) {
            this.ctx.beginPath()
            this.ctx.moveTo(p.x, p.y)
            this.ctx.lineTo(p2.x, p2.y)
            this.ctx.strokeStyle = `rgba(0, 212, 255, ${0.5 * (1 - dist / this.linkDistance)})`
            this.ctx.lineWidth = 0.5
            this.ctx.stroke()
          }
        }
      })
    },

    handleMouseMove(e) {
      const rect = this.canvas.getBoundingClientRect()
      this.mouse.x = e.clientX - rect.left
      this.mouse.y = e.clientY - rect.top
    },

    handleMouseLeave() {
      this.mouse.x = null
      this.mouse.y = null
    }
  }
}
</script>

<style lang="scss" scoped>
.particle-effect {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  pointer-events: none;
}

.particle-canvas {
  width: 100%;
  height: 100%;
}
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| count | Number | 150 | 粒子数量 |
| color | String | '#00d4ff' | 粒子颜色 |
| size | Number | 2 | 粒子大小基准值 |
| linkDistance | Number | 120 | 粒子连线最大距离 |
| speed | Number | 0.3 | 粒子运动速度 |

---

## 使用方式

```vue
<template>
  <div class="bi-dashboard">
    <!-- 粒子背景 -->
    <ParticleEffect :count="100" color="#00d4ff" />
    
    <!-- 大屏内容 -->
    <div class="bi-content">
      ...
    </div>
  </div>
</template>

<style lang="scss" scoped>
.bi-dashboard {
  position: relative;
  width: 100%;
  height: 100vh;
}

.bi-content {
  position: relative;
  z-index: 1;
}
</style>
```

> 注意：该组件使用 `position: absolute + pointer-events: none`，适合作为绝对定位背景层使用。父容器需要设置 `position: relative`。
