## Dashboard.vue 核心模板

### 三栏布局结构

```vue
<template>
  <div class="bi-dashboard">
    <!-- 底部背景图 -->
    <div class="bg-bottom">
      <img :src="bgImage" alt="背景"/>
    </div>

    <!-- 顶部标题 -->
    <header class="bi-header">
      <div class="header-line left"></div>
      <h1 class="header-title"><span class="title-text">{{ title }}</span></h1>
      <div class="header-line right"></div>
      <div class="header-time">
        <span class="time-value">{{ currentTime }}</span>
      </div>
    </header>

    <!-- 主体内容 -->
    <div class="bi-content">
      <!-- 左侧面板 -->
      <div class="side-panel left-panel">
        <!-- 业务数据概览 -->
        <div class="panel-frame">
          <div class="panel-title"><span class="title-bar"></span><span>业务数据概览</span></div>
          <div class="panel-content data-grid">
            <div class="data-item" v-for="item in businessData" :key="item.label" @click="handleBusinessClick(item)">
              <div class="data-icon">{{ item.icon }}</div>
              <div class="data-info">
                <div class="data-value">{{ item.value }}<span class="data-unit">{{ item.unit }}</span></div>
                <div class="data-label">{{ item.label }}</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 其他左侧面板模块... -->
      </div>

      <!-- 中间区域 -->
      <div class="center-area">
        <!-- 地图/图表/背景图展示区 -->
      </div>

      <!-- 右侧面板 -->
      <div class="side-panel right-panel">
        <!-- 图表/排行等模块... -->
      </div>
    </div>

    <!-- 详情弹窗 -->
    <div v-if="detailVisible" class="detail-panel" :style="detailPanelStyle" @click.stop>
      <div class="detail-header">
        <span class="detail-title">{{ detailTitle }}</span>
        <span class="detail-close" @click="closeDetail">×</span>
      </div>
      <div class="detail-content">
        <!-- 详情内容 -->
      </div>
    </div>

    <!-- 遮罩 -->
    <div v-if="detailVisible" class="detail-backdrop" @click="closeDetail"></div>
  </div>
</template>

<script>
import api from '@/api'

export default {
  name: 'Dashboard',
  data() {
    return {
      // 大屏标题
      title: '数据展示大屏',
      currentTime: '',
      timer: null,

      // 背景图
      bgImage: require('@/asset/bg.png'),

      // 业务数据
      businessData: [
        { icon: '🏨', label: '酒店民宿', value: 128, unit: '家', type: 'hotel' },
        { icon: '🍜', label: '餐饮美食', value: 256, unit: '家', type: 'catering' },
        { icon: '🎫', label: '门票种类', value: 45, unit: '种', type: 'ticket' },
        { icon: '📖', label: '游玩攻略', value: 89, unit: '篇', type: 'guide' }
      ],

      // 图表数据
      barData: [],
      lineData: { xData: [], yData: [] },
      pieData: [],

      // 详情弹窗
      detailVisible: false,
      detailTitle: '',
      detailPanelStyle: {},
      detailList: [],

      // 当前选中业务类型
      currentBusinessType: null
    }
  },
  mounted() {
    this.updateTime()
    this.timer = setInterval(this.updateTime, 1000)
    this.fetchData()
  },
  beforeDestroy() {
    if (this.timer) clearInterval(this.timer)
  },
  methods: {
    // 更新时间
    updateTime() {
      const now = new Date()
      this.currentTime = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`
    },

    // 获取数据
    async fetchData() {
      try {
        const res = await api.getDashboardHome()
        if (res.code === 200) {
          this.businessData = res.data.businessData || this.businessData
          this.barData = res.data.barData || []
          this.lineData = res.data.lineData || { xData: [], yData: [] }
          this.pieData = res.data.pieData || []
        }
      } catch (error) {
        console.error('获取数据失败:', error)
      }
    },

    // 业务卡片点击
    handleBusinessClick(item) {
      this.currentBusinessType = item.type
      this.detailTitle = item.label
      this.fetchDetailData(item.type)
    },

    // 获取详情数据
    async fetchDetailData(type) {
      try {
        const res = await api.getBusinessList({ type })
        if (res.code === 200) {
          this.detailList = res.data || []
          this.detailVisible = true
          this.setPosition()
        }
      } catch (error) {
        console.error('获取详情失败:', error)
      }
    },

    // 设置弹窗位置
    setPosition() {
      const event = window.event
      if (event && event.clientX) {
        const x = Math.min(event.clientX + 10, window.innerWidth - 400)
        const y = Math.min(event.clientY + 10, window.innerHeight - 500)
        this.detailPanelStyle = { left: x + 'px', top: y + 'px' }
      }
    },

    // 关闭详情
    closeDetail() {
      this.detailVisible = false
      this.currentBusinessType = null
    },

    // 刷新数据
    handleRefresh() {
      this.fetchData()
    }
  }
}
</script>

<style lang="scss" scoped>
.bi-dashboard {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  background: var(--bg-dark);
}

.bg-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 300px;
  pointer-events: none;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.6;
  }
}

.bi-header {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 32px;
  background: linear-gradient(180deg, rgba(13, 27, 42, 0.95) 0%, rgba(13, 27, 42, 0.8) 100%);
  border-bottom: 1px solid var(--border-color);
  position: relative;
  z-index: 10;
}

.header-line {
  width: 200px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
  &.left { margin-right: 20px; }
  &.right { margin-left: 20px; }
}

.header-title {
  font-size: 28px;
  font-weight: bold;
  color: var(--text-primary);
  letter-spacing: 4px;
  text-shadow: 0 0 20px var(--cyan-glow);
}

.header-time {
  position: absolute;
  right: 32px;
  .time-value {
    font-size: 18px;
    color: var(--text-secondary);
    font-family: 'Courier New', monospace;
  }
}

.bi-content {
  display: flex;
  height: calc(100vh - 64px);
  padding: 12px;
  gap: 12px;
}

.side-panel {
  width: 320px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  overflow-y: auto;
}

.center-area {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
}

.panel-frame {
  background: var(--panel-bg, rgba(0, 20, 40, 0.6));
  border: 1px solid var(--glass-border, rgba(0, 150, 255, 0.15));
  border-radius: 8px;
  padding: 14px;
}

.panel-title {
  display: flex;
  align-items: center;
  font-size: 16px;
  color: var(--text-primary);
  margin-bottom: 14px;
  .title-bar {
    width: 3px;
    height: 16px;
    background: var(--cyan);
    margin-right: 8px;
    border-radius: 2px;
  }
}

.data-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.data-item {
  display: flex;
  align-items: center;
  padding: 12px;
  background: rgba(0, 20, 40, 0.5);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
  &:hover {
    background: rgba(0, 212, 255, 0.1);
    transform: translateY(-2px);
  }
}

.data-icon {
  font-size: 28px;
  margin-right: 10px;
}

.data-info {
  flex: 1;
  min-width: 0;
}

.data-value {
  font-size: 22px;
  font-weight: bold;
  color: var(--text-primary);
  .data-unit {
    font-size: 12px;
    color: var(--text-secondary);
    margin-left: 2px;
  }
}

.data-label {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 4px;
}
</style>
```

### 核心样式变量

```scss
$cyan: #00d4ff;
$cyan-glow: rgba(0, 212, 255, 0.5);
$gold: #ffd700;
$glass-border: rgba(0, 212, 255, 0.18);
$panel-bg: rgba(13, 27, 42, 0.85);
$white: #ffffff;
$text-ghost: rgba(255, 255, 255, 0.6);
$text-dim: rgba(255, 255, 255, 0.4);
```

### 呼吸动画

```scss
@keyframes breathe {
  0%, 100% {
    box-shadow: 0 0 8px rgba(0, 212, 255, 0.15);
    border-color: rgba(0, 212, 255, 0.18);
  }
  50% {
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.35);
    border-color: rgba(0, 212, 255, 0.35);
  }
}

.panel-frame {
  animation: breathe 3s ease-in-out infinite;
}
```

### 详情弹窗样式

```scss
.detail-backdrop {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  z-index: 9998;
}

.detail-panel {
  position: fixed;
  width: 380px;
  max-height: 500px;
  background: linear-gradient(135deg, rgba(13, 25, 41, 0.98) 0%, rgba(10, 14, 26, 0.98) 100%);
  border: 1px solid var(--glass-border, rgba(0, 212, 255, 0.18));
  border-radius: 8px;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.detail-header {
  display: flex;
  align-items: center;
  padding: 12px 14px;
  background: rgba(0, 212, 255, 0.08);
  border-bottom: 1px solid rgba(0, 212, 255, 0.12);
}

.detail-title { font-size: 14px; color: $white; }
.detail-total { margin-left: 10px; font-size: 11px; color: $text-ghost; background: rgba(0, 212, 255, 0.15); padding: 2px 8px; border-radius: 10px; }
.detail-back { margin-left: auto; margin-right: 10px; font-size: 12px; color: $cyan; cursor: pointer; }
.detail-close { font-size: 18px; color: $text-ghost; cursor: pointer; }

.detail-content {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
}

.detail-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.detail-item {
  display: flex;
  align-items: center;
  padding: 10px;
  background: rgba(0, 20, 40, 0.5);
  border-radius: 6px;
  cursor: pointer;
  &:hover { background: rgba(0, 212, 255, 0.06); }
}

.detail-item-index {
  width: 22px; height: 22px; line-height: 22px; text-align: center;
  background: rgba(0, 212, 255, 0.2);
  border-radius: 4px;
  font-size: 11px; color: $cyan;
  margin-right: 10px;
}

.detail-item-content { flex: 1; }
.detail-item-name { font-size: 13px; color: $white; margin-bottom: 4px; }
.detail-item-info { display: flex; gap: 8px; font-size: 11px; }
.detail-item-arrow { font-size: 16px; color: $text-ghost; }

.info-price { color: #f56c6c; font-weight: 500; }
.info-original { color: $text-dim; text-decoration: line-through; }
.info-tag { background: rgba(0, 212, 255, 0.15); padding: 1px 6px; border-radius: 3px; color: $cyan; }
```

### 排名样式

```scss
.rank-badge {
  width: 20px;
  height: 20px;
  line-height: 20px;
  text-align: center;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
  margin-right: 12px;
  
  &.gold {
    background: linear-gradient(135deg, #f5a623, #ffd700);
    color: #000;
  }
  &.silver {
    background: linear-gradient(135deg, #c0c0c0, #e8e8e8);
    color: #000;
  }
  &.bronze {
    background: linear-gradient(135deg, #cd7f32, #e5a668);
    color: #000;
  }
}

.rank-item {
  display: flex;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid var(--border-color);
  &:last-child { border-bottom: none; }
}

.rank-content { flex: 1; min-width: 0; }
.rank-name { font-size: 14px; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.rank-value { font-size: 12px; color: var(--text-secondary); }
```

---

