## 核心模板

### 1. package.json

```json
{
  "name": "bi-dashboard",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "2.7.16",
    "vue-router": "3.5.3",
    "element-ui": "2.15.9",
    "echarts": "5.2.2",
    "axios": "0.21.1"
  },
  "devDependencies": {
    "@vitejs/plugin-vue2": "^2.3.1",
    "vite": "^4.5.0",
    "sass": "^1.69.0"
  }
}
```

### 2. vite.config.js

```javascript
import { defineConfig } from 'vite'
import vue2 from '@vitejs/plugin-vue2'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [vue2()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://your-api-server',
        changeOrigin: true
      }
    }
  }
})
```

### 3. main.js

```javascript
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@/styles/common.css'

Vue.config.productionTip = false
Vue.use(ElementUI)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

### 4. common.css（CSS 变量）

```css
:root {
  /* 主色调 */
  --primary-color: #1e3a5f;
  --primary-light: #3498db;
  --primary-dark: #0d1b2a;

  /* 辅助色 */
  --accent-color: #f5a623;
  --success-color: #27ae60;
  --warning-color: #e67e22;
  --danger-color: #e74c3c;

  /* 背景色 */
  --bg-dark: #0d1b2a;
  --bg-light: #1b2838;
  --bg-card: rgba(30, 58, 95, 0.6);

  /* 文字色 */
  --text-primary: #ffffff;
  --text-secondary: #87ceeb;
  --text-muted: #6c7a89;

  /* 边框色 */
  --border-color: rgba(52, 152, 219, 0.3);

  /* 图表色板 */
  --chart-blue: #3498db;
  --chart-green: #2ecc71;
  --chart-orange: #f39c12;
  --chart-purple: #9b59b6;
  --chart-pink: #e91e63;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif;
  font-size: 14px;
  line-height: 1.5;
  color: var(--text-primary);
}

/* 滚动条样式 */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb {
  background: var(--primary-light);
  border-radius: 3px;
}
```

### 5. Header.vue（顶部导航）

```vue
<template>
  <div class="page-header">
    <div class="header-left">
      <span class="back-btn" @click="goHome" v-if="showBack">
        <i class="el-icon-arrow-left"></i>
      </span>
      <span class="header-title">{{ title }}</span>
    </div>
    <div class="header-center">
      <span class="current-time">{{ currentTime }}</span>
      <span class="weather-info">
        <i class="el-icon-sunny"></i>
        <span>26°C 晴</span>
      </span>
    </div>
    <div class="header-right">
      <el-select v-model="dateType" placeholder="请选择" size="small" @change="handleDateChange">
        <el-option label="今日" value="TODAY" />
        <el-option label="本周" value="WEEK" />
        <el-option label="本月" value="MONTH" />
        <el-option label="本年" value="YEAR" />
      </el-select>
      <el-button size="small" icon="el-icon-refresh" @click="handleRefresh">刷新</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DashboardHeader',
  props: {
    title: { type: String, default: '数据展示大屏' },
    showBack: { type: Boolean, default: false }
  },
  data() {
    return {
      dateType: 'TODAY',
      currentTime: '',
      timer: null
    }
  },
  mounted() {
    this.updateTime()
    this.timer = setInterval(this.updateTime, 1000)
  },
  beforeDestroy() {
    if (this.timer) clearInterval(this.timer)
  },
  methods: {
    updateTime() {
      const now = new Date()
      this.currentTime = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')} ${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`
    },
    handleDateChange(val) { this.$emit('date-change', val) },
    handleRefresh() { this.$emit('refresh') },
    goHome() { this.$router.push('/') }
  }
}
</script>

<style lang="scss" scoped>
.page-header {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  background: rgba(13, 27, 42, 0.9);
  border-bottom: 1px solid var(--border-color);
}
.header-left { display: flex; align-items: center; }
.back-btn {
  width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 50%;
  cursor: pointer;
  margin-right: 16px;
  transition: all 0.3s;
  &:hover { background: var(--primary-light); border-color: var(--primary-light); }
  i { font-size: 18px; color: var(--text-primary); }
}
.header-title { font-size: 24px; font-weight: bold; color: var(--text-primary); letter-spacing: 2px; }
.header-center { display: flex; align-items: center; gap: 24px; }
.current-time { font-size: 18px; color: var(--text-primary); font-family: 'Courier New', monospace; }
.weather-info { display: flex; align-items: center; gap: 8px; font-size: 16px; color: var(--text-secondary); i { font-size: 20px; color: var(--accent-color); } }
.header-right { display: flex; align-items: center; gap: 16px; }
</style>
```

### 6. DataCard.vue（数据卡片）

```vue
<template>
  <div class="data-card" :class="{ clickable: clickable }" @click="handleClick">
    <div class="data-card-icon">{{ icon }}</div>
    <div class="data-card-content">
      <div class="data-card-title">{{ title }}</div>
      <div class="data-card-value-row">
        <span class="data-card-value">{{ formatValue(value) }}</span>
        <span class="data-card-unit">{{ unit }}</span>
      </div>
      <div class="data-card-change" :class="changeClass">
        <span v-if="change !== null && change !== undefined">
          {{ change >= 0 ? '↑' : '↓' }} {{ Math.abs(change) }}%
        </span>
        <span v-if="changeLabel">{{ changeLabel }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DataCard',
  props: {
    icon: { type: String, default: '📊' },
    title: { type: String, default: '' },
    value: { type: [Number, String], default: 0 },
    unit: { type: String, default: '' },
    change: { type: Number, default: null },
    changeLabel: { type: String, default: '' },
    clickable: { type: Boolean, default: false }
  },
  computed: {
    changeClass() {
      if (this.change === null || this.change === undefined) return ''
      return this.change >= 0 ? 'up' : 'down'
    }
  },
  methods: {
    formatValue(val) {
      return typeof val === 'number' ? val.toLocaleString() : val
    },
    handleClick() {
      if (this.clickable) this.$emit('click')
    }
  }
}
</script>

<style lang="scss" scoped>
.data-card {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  transition: all 0.3s;
  &.clickable {
    cursor: pointer;
    &:hover {
      border-color: var(--primary-light);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
    }
  }
}
.data-card-icon { font-size: 32px; margin-right: 12px; line-height: 1; }
.data-card-content { flex: 1; min-width: 0; }
.data-card-title { font-size: 14px; color: var(--text-secondary); margin-bottom: 8px; }
.data-card-value-row { display: flex; align-items: baseline; }
.data-card-value { font-size: 28px; font-weight: bold; color: var(--text-primary); line-height: 1.2; }
.data-card-unit { font-size: 14px; color: var(--text-secondary); margin-left: 4px; }
.data-card-change {
  font-size: 12px;
  margin-top: 8px;
  &.up { color: var(--success-color); }
  &.down { color: var(--danger-color); }
}
</style>
```

### 7. ChartBar.vue（柱状图）

```vue
<template>
  <div class="chart-bar">
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartBar',
  props: {
    data: { type: Array, default: () => [] },
    horizontal: { type: Boolean, default: true }
  },
  data() {
    return { chart: null }
  },
  watch: {
    data() { this.updateChart() }
  },
  mounted() {
    this.chart = echarts.init(this.$refs.chartRef)
    this.updateChart()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    if (this.chart) this.chart.dispose()
  },
  methods: {
    updateChart() {
      if (!this.chart) return
      const names = this.data.map(d => d.name)
      const values = this.data.map(d => d.value)

      const option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: { type: 'shadow' },
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 210, 255, 0.3)',
          textStyle: { color: '#fff' }
        },
        grid: {
          left: '3%', right: '12%', top: '3%', bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value',
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: 'rgba(255, 255, 255, 0.5)', fontSize: 10 },
          splitLine: { lineStyle: { color: 'rgba(0, 212, 255, 0.1)' } }
        },
        yAxis: {
          type: 'category',
          data: names,
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: '#87ceeb', fontSize: 11 }
        },
        series: [{
          type: 'bar',
          data: values,
          barWidth: 14,
          itemStyle: {
            borderRadius: [0, 4, 4, 0],
            color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
              { offset: 0, color: 'rgba(0, 212, 255, 0.3)' },
              { offset: 1, color: 'rgba(0, 212, 255, 0.9)' }
            ])
          },
          label: {
            show: true, position: 'right',
            color: '#00d4ff', fontSize: 11,
            fontFamily: 'JetBrains Mono, monospace'
          }
        }]
      }
      this.chart.setOption(option)
    },
    handleResize() {
      if (this.chart) this.chart.resize()
    }
  }
}
</script>

<style lang="scss" scoped>
.chart-bar, .chart-container { width: 100%; height: 100%; }
</style>
```

### 8. ChartPie.vue（饼图）

```vue
<template>
  <div class="chart-pie">
    <div v-if="title" class="chart-title">{{ title }}</div>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartPie',
  props: {
    title: { type: String, default: '' },
    data: { type: Array, default: () => [] },
    radius: { type: Array, default: () => ['35%', '65%'] },
    showLabel: { type: Boolean, default: true }
  },
  data() {
    return { chart: null }
  },
  watch: {
    data() { this.updateChart() }
  },
  mounted() {
    this.chart = echarts.init(this.$refs.chartRef)
    this.updateChart()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    if (this.chart) this.chart.dispose()
  },
  methods: {
    updateChart() {
      if (!this.chart) return
      const option = {
        tooltip: {
          trigger: 'item',
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 210, 255, 0.3)',
          textStyle: { color: '#fff' },
          formatter: '{b}: {c} ({d}%)'
        },
        legend: {
          show: this.showLabel,
          orient: 'horizontal',
          bottom: '5%',
          left: 'center',
          textStyle: { color: '#87ceeb', fontSize: 11 },
          itemWidth: 10,
          itemHeight: 10
        },
        series: [{
          type: 'pie',
          radius: this.radius,
          center: ['50%', '45%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 4,
            borderColor: '#0a0e17',
            borderWidth: 2
          },
          label: {
            show: this.showLabel,
            position: 'inside',
            formatter: '{b}\n{d}%',
            color: '#fff',
            fontSize: 10
          },
          labelLine: { show: false },
          emphasis: {
            label: { show: true, fontSize: 12, fontWeight: 'bold' },
            itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)' }
          },
          data: this.data,
          color: ['#00d2ff', '#00ff88', '#f5a623', '#9b59b6', '#e91e63', '#1abc9c']
        }]
      }
      this.chart.setOption(option)
    },
    handleResize() {
      if (this.chart) this.chart.resize()
    }
  }
}
</script>

<style lang="scss" scoped>
.chart-pie { width: 100%; height: 100%; }
.chart-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin-bottom: 12px; }
.chart-container { width: 100%; height: calc(100% - 40px); }
</style>
```

### 9. ChartLine.vue（折线图）

```vue
<template>
  <div class="chart-line">
    <div v-if="title" class="chart-title">{{ title }}</div>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartLine',
  props: {
    title: { type: String, default: '' },
    xData: { type: Array, default: () => [] },
    yData: { type: Array, default: () => [] },
    yName: { type: String, default: '' },
    smooth: { type: Boolean, default: true },
    areaStyle: { type: Boolean, default: true },
    showSymbol: { type: Boolean, default: false }
  },
  data() {
    return { chart: null }
  },
  watch: {
    xData() { this.updateChart() },
    yData() { this.updateChart() }
  },
  mounted() {
    this.chart = echarts.init(this.$refs.chartRef)
    this.updateChart()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    if (this.chart) this.chart.dispose()
  },
  methods: {
    updateChart() {
      if (!this.chart) return
      const option = {
        tooltip: {
          trigger: 'axis',
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 210, 255, 0.3)',
          textStyle: { color: '#fff' }
        },
        grid: {
          left: '3%', right: '4%', top: '8%', bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: this.xData,
          boundaryGap: false,
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: 'rgba(255, 255, 255, 0.5)', fontSize: 11 }
        },
        yAxis: {
          type: 'value',
          name: this.yName,
          nameTextStyle: { color: '#87ceeb', fontSize: 11 },
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: 'rgba(255, 255, 255, 0.5)', fontSize: 11 },
          splitLine: { lineStyle: { color: 'rgba(0, 212, 255, 0.1)' } }
        },
        series: [{
          type: 'line',
          data: this.yData,
          smooth: this.smooth,
          symbol: this.showSymbol ? 'circle' : 'none',
          symbolSize: 6,
          lineStyle: {
            color: '#00d4ff',
            width: 2
          },
          itemStyle: {
            color: '#00d4ff'
          },
          areaStyle: this.areaStyle ? {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: 'rgba(0, 212, 255, 0.4)' },
              { offset: 1, color: 'rgba(0, 212, 255, 0.05)' }
            ])
          } : null
        }]
      }
      this.chart.setOption(option)
    },
    handleResize() {
      if (this.chart) this.chart.resize()
    }
  }
}
</script>

<style lang="scss" scoped>
.chart-line { width: 100%; height: 100%; }
.chart-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin-bottom: 12px; }
.chart-container { width: 100%; height: calc(100% - 40px); }
</style>
```

### 10. App.vue（入口组件）

```vue
<template>
  <div id="app" class="dashboard-container">
    <router-view />
  </div>
</template>

<script>
export default { name: 'App' }
</script>

<style lang="scss">
.dashboard-container {
  width: 100%;
  height: 100%;
  background: rgba(13, 27, 42, 0.85);
  color: #fff;
  font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif;
}
</style>
```

### 10. router/index.js（路由配置）

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue')
  }
]

const router = new VueRouter({
  mode: 'hash',
  routes
})

export default router
```

### 11. api/index.js（API 封装）

```javascript
import axios from 'axios'

const BASE_URL = '/api'

const request = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' }
})

// 请求拦截器
request.interceptors.request.use(
  config => {
    // 可在此添加 token 等请求头
    // config.headers['Authorization'] = 'Bearer ' + token
    return config
  },
  error => Promise.reject(error)
)

// 响应拦截器
request.interceptors.response.use(
  response => {
    const { data } = response
    if (data.code === 200 || data.code === 0) return data
    // 业务错误
    Vue.prototype.$message.error(data.msg || '请求失败')
    return Promise.reject(data)
  },
  error => {
    // 网络错误
    if (error.code === 'ECONNABORTED') {
      Vue.prototype.$message.error('请求超时，请稍后重试')
    } else if (error.response) {
      // 服务器错误
      const status = error.response.status
      const msgMap = {
        400: '参数错误',
        401: '未授权，请登录',
        403: '拒绝访问',
        404: '请求的资源不存在',
        500: '服务器内部错误'
      }
      Vue.prototype.$message.error(msgMap[status] || '网络异常')
    } else {
      Vue.prototype.$message.error('网络连接失败')
    }
    return Promise.reject(error)
  }
)

export default {
  // Dashboard 统计接口
  getDashboardHome: (params = {}) => request.get('/dashboard/home', { params }),
  getDashboardStats: (params = {}) => request.get('/dashboard/stats', { params }),

  // 业务模块接口（根据实际需求添加）
  getBusinessList: (params = {}) => request.get('/business/list', { params }),
  getBusinessDetail: (id) => request.get(`/business/${id}`),

  // 图表数据接口
  getChartData: (type, params = {}) => request.get(`/charts/${type}`, { params })
}
```

---

