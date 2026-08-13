# 网络关系布局模板

> 适用于网络关系/知识图谱场景，中间区域承载全宽网络关系图（ECharts graph 或 D3 force），左侧面板用于筛选与统计，右侧面板用于节点详情展示。

---

## 一、布局结构

```
┌─────────────────────────────────────────────────────────────┐
│                      顶部标题栏                              │
├──────────┬─────────────────────────────────┬────────────────┤
│          │                                 │                │
│ 统计面板  │     网络关系图                    │  详情面板      │
│ (280px)  │   (ECharts graph / D3 force)    │  (280px)      │
│          │                                 │                │
└──────────┴─────────────────────────────────┴────────────────┘
```

---

## 二、Dashboard.vue 核心模板

```vue
<template>
  <div class="network-relation-dashboard" :class="`theme-${currentTheme}`">
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
      <!-- 左侧统计面板 -->
      <aside class="side-panel left-panel">
        <!-- 搜索与筛选 -->
        <div class="panel-frame">
          <div class="panel-title">
            <span class="title-bar"></span>
            <span>筛选条件</span>
          </div>
          <div class="panel-content">
            <div class="filter-group">
              <input
                class="search-input"
                v-model="searchKeyword"
                placeholder="搜索节点..."
                @input="handleSearch"
              />
            </div>
            <div class="filter-group">
              <label class="filter-label">节点类型</label>
              <div class="filter-tags">
                <button
                  class="filter-tag"
                  v-for="category in nodeCategories"
                  :key="category.id"
                  :class="{ active: activeCategories.includes(category.id) }"
                  :style="{ '--tag-color': category.color }"
                  @click="toggleCategory(category.id)"
                >
                  {{ category.label }}
                </button>
              </div>
            </div>
            <div class="filter-group">
              <label class="filter-label">关系强度</label>
              <input
                type="range"
                class="strength-slider"
                v-model.number="minStrength"
                min="0"
                max="100"
                @change="handleStrengthChange"
              />
              <span class="strength-value">{{ minStrength }}%</span>
            </div>
          </div>
        </div>

        <!-- 统计概览 -->
        <div class="panel-frame">
          <div class="panel-title">
            <span class="title-bar"></span>
            <span>统计概览</span>
          </div>
          <div class="panel-content">
            <div class="stat-grid">
              <div class="stat-item" v-for="stat in stats" :key="stat.label">
                <span class="stat-value" :style="{ color: stat.color || 'var(--accent)' }">{{ stat.value }}</span>
                <span class="stat-label">{{ stat.label }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 关系类型分布 -->
        <div class="panel-frame">
          <div class="panel-title">
            <span class="title-bar"></span>
            <span>关系分布</span>
          </div>
          <div class="panel-content">
            <div class="relation-chart" ref="relationChartRef"></div>
          </div>
        </div>
      </aside>

      <!-- 中间网络关系图区域 -->
      <section class="center-area">
        <div class="graph-container" ref="graphContainer"></div>

        <!-- 图例 -->
        <div class="graph-legend">
          <div
            class="legend-item"
            v-for="category in nodeCategories"
            :key="category.id"
            @click="toggleCategory(category.id)"
          >
            <span class="legend-dot" :style="{ background: category.color }"></span>
            <span class="legend-text">{{ category.label }}</span>
          </div>
        </div>

        <!-- 缩放控制 -->
        <div class="zoom-controls">
          <button class="zoom-btn" @click="zoomIn">+</button>
          <span class="zoom-level">{{ Math.round(zoomLevel * 100) }}%</span>
          <button class="zoom-btn" @click="zoomOut">-</button>
          <button class="zoom-btn reset-btn" @click="zoomReset">重置</button>
        </div>
      </section>

      <!-- 右侧详情面板 -->
      <aside class="side-panel right-panel">
        <!-- 节点详情 -->
        <div class="panel-frame" v-if="selectedNode">
          <div class="panel-title">
            <span class="title-bar"></span>
            <span>节点详情</span>
          </div>
          <div class="panel-content">
            <div class="detail-header">
              <span class="node-badge" :style="{ background: getNodeCategoryColor(selectedNode.category) }">
                {{ selectedNode.category }}
              </span>
              <h3 class="node-name">{{ selectedNode.name }}</h3>
            </div>
            <div class="detail-fields">
              <div class="detail-field" v-for="field in selectedNode.fields" :key="field.label">
                <span class="field-label">{{ field.label }}</span>
                <span class="field-value">{{ field.value }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 关联节点 -->
        <div class="panel-frame" v-if="selectedNode">
          <div class="panel-title">
            <span class="title-bar"></span>
            <span>关联节点 ({{ relatedNodes.length }})</span>
          </div>
          <div class="panel-content">
            <div class="related-list">
              <div
                class="related-item"
                v-for="node in relatedNodes"
                :key="node.id"
                @click="selectNode(node)"
              >
                <span class="related-dot" :style="{ background: getNodeCategoryColor(node.category) }"></span>
                <span class="related-name">{{ node.name }}</span>
                <span class="related-relation">{{ node.relation }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 空状态 -->
        <div class="panel-frame empty-state" v-if="!selectedNode">
          <div class="panel-content">
            <div class="empty-icon">
              <svg viewBox="0 0 24 24" width="48" height="48" fill="var(--text-dim)">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
              </svg>
            </div>
            <p class="empty-text">点击节点查看详情</p>
          </div>
        </div>
      </aside>
    </main>
  </div>
</template>

<script>
import { ref, reactive, onMounted, onBeforeUnmount, computed, watch, nextTick } from 'vue'
import DateTimeDisplay from './components/DateTimeDisplay.vue'
import * as echarts from 'echarts'

export default {
  name: 'NetworkRelationDashboard',
  components: { DateTimeDisplay },
  props: {
    title: { type: String, default: '网络关系分析平台' },
    theme: { type: String, default: 'techBlue' },
    graphData: { type: Object, default: () => ({ nodes: [], links: [] }) },
    layoutType: { type: String, default: 'force' }, // 'force' | 'circular' | 'radial'
  },
  setup(props) {
    const graphContainer = ref(null)
    const relationChartRef = ref(null)
    const searchKeyword = ref('')
    const minStrength = ref(0)
    const zoomLevel = ref(1)
    const selectedNode = ref(null)
    const activeCategories = ref([])
    const currentTheme = computed(() => props.theme)

    let graphChart = null
    let relationChart = null

    // 节点分类
    const nodeCategories = reactive([
      { id: 'person', label: '人员', color: '#00d4ff' },
      { id: 'org', label: '组织', color: '#ff6b35' },
      { id: 'event', label: '事件', color: '#7cff3c' },
      { id: 'location', label: '地点', color: '#ff3c8e' },
    ])

    // 统计数据
    const stats = reactive([
      { label: '节点总数', value: '2,486', color: 'var(--accent)' },
      { label: '关系总数', value: '5,132', color: 'var(--accent)' },
      { label: '核心节点', value: '128', color: '#ff6b35' },
      { label: '孤立节点', value: '47', color: '#7cff3c' },
    ])

    // 关联节点
    const relatedNodes = computed(() => {
      if (!selectedNode.value) return []
      // 模拟关联节点数据
      return [
        { id: 'r1', name: '关联节点A', category: 'person', relation: '直属' },
        { id: 'r2', name: '关联节点B', category: 'org', relation: '隶属' },
        { id: 'r3', name: '关联节点C', category: 'event', relation: '参与' },
      ]
    })

    // 获取节点分类颜色
    const getNodeCategoryColor = (categoryId) => {
      const cat = nodeCategories.find(c => c.id === categoryId)
      return cat ? cat.color : 'var(--accent)'
    }

    // 初始化网络关系图
    const initGraph = () => {
      if (!graphContainer.value) return

      graphChart = echarts.init(graphContainer.value)

      const option = {
        tooltip: {
          trigger: 'item',
          backgroundColor: 'rgba(10, 22, 40, 0.9)',
          borderColor: 'rgba(0, 212, 255, 0.3)',
          textStyle: { color: '#fff', fontSize: 12 },
        },
        series: [{
          type: 'graph',
          layout: props.layoutType,
          roam: true,
          draggable: true,
          zoom: 1,
          label: {
            show: true,
            position: 'right',
            color: '#fff',
            fontSize: 11,
          },
          force: {
            repulsion: 300,
            gravity: 0.1,
            edgeLength: [80, 200],
            layoutAnimation: true,
          },
          emphasis: {
            focus: 'adjacency',
            lineStyle: { width: 4 },
          },
          lineStyle: {
            color: 'rgba(0, 212, 255, 0.3)',
            width: 1.5,
            curveness: 0.2,
          },
          data: props.graphData.nodes.map(node => ({
            ...node,
            symbolSize: node.symbolSize || 30,
            itemStyle: {
              color: getNodeCategoryColor(node.category),
              borderColor: 'rgba(0, 212, 255, 0.5)',
              borderWidth: 1,
            },
          })),
          links: props.graphData.links,
        }],
      }

      graphChart.setOption(option)

      // 节点点击事件
      graphChart.on('click', (params) => {
        if (params.dataType === 'node') {
          selectNode(params.data)
        }
      })

      // 缩放事件
      graphChart.on('graphroam', (params) => {
        if (params.zoom) {
          zoomLevel.value *= params.zoom
        }
      })
    }

    // 初始化关系分布图
    const initRelationChart = () => {
      if (!relationChartRef.value) return

      relationChart = echarts.init(relationChartRef.value)
      const option = {
        tooltip: { trigger: 'item' },
        series: [{
          type: 'pie',
          radius: ['40%', '70%'],
          avoidLabelOverlap: false,
          label: { show: false },
          emphasis: {
            label: { show: true, fontSize: 12, fontWeight: 'bold' },
          },
          data: [
            { value: 1248, name: '直属关系', itemStyle: { color: '#00d4ff' } },
            { value: 856, name: '隶属关系', itemStyle: { color: '#ff6b35' } },
            { value: 632, name: '参与关系', itemStyle: { color: '#7cff3c' } },
            { value: 428, name: '关联关系', itemStyle: { color: '#ff3c8e' } },
          ],
        }],
      }
      relationChart.setOption(option)
    }

    const selectNode = (node) => {
      selectedNode.value = {
        ...node,
        fields: node.fields || [
          { label: '类型', value: node.category || '-' },
          { label: '连接数', value: node.links || '0' },
          { label: '权重', value: node.weight || '1.0' },
          { label: '更新时间', value: '2026-05-18' },
        ],
      }
    }

    const toggleCategory = (categoryId) => {
      const idx = activeCategories.value.indexOf(categoryId)
      if (idx > -1) {
        activeCategories.value.splice(idx, 1)
      } else {
        activeCategories.value.push(categoryId)
      }
    }

    const handleSearch = () => {
      // 搜索节点逻辑
    }

    const handleStrengthChange = () => {
      // 关系强度筛选逻辑
    }

    const zoomIn = () => {
      if (!graphChart) return
      zoomLevel.value = Math.min(zoomLevel.value * 1.2, 5)
      graphChart.dispatchAction({ type: 'graphRoam', zoom: 1.2 })
    }

    const zoomOut = () => {
      if (!graphChart) return
      zoomLevel.value = Math.max(zoomLevel.value / 1.2, 0.2)
      graphChart.dispatchAction({ type: 'graphRoam', zoom: 1 / 1.2 })
    }

    const zoomReset = () => {
      if (!graphChart) return
      zoomLevel.value = 1
      graphChart.dispatchAction({ type: 'graphRoam', zoom: 1 })
    }

    const handleResize = () => {
      graphChart && graphChart.resize()
      relationChart && relationChart.resize()
    }

    const goBack = () => {}

    onMounted(() => {
      nextTick(() => {
        initGraph()
        initRelationChart()
      })
      window.addEventListener('resize', handleResize)
    })

    onBeforeUnmount(() => {
      window.removeEventListener('resize', handleResize)
      graphChart && graphChart.dispose()
      relationChart && relationChart.dispose()
      graphChart = null
      relationChart = null
    })

    return {
      graphContainer, relationChartRef,
      searchKeyword, minStrength, zoomLevel,
      selectedNode, activeCategories, currentTheme,
      nodeCategories, stats, relatedNodes,
      getNodeCategoryColor, selectNode, toggleCategory,
      handleSearch, handleStrengthChange,
      zoomIn, zoomOut, zoomReset, goBack,
    }
  },
}
</script>
```

---

## 三、核心样式（含主题变量）

```scss
/* ========== 主题变量 ========== */
.network-relation-dashboard {
  /* -- techBlue 深蓝科技风 -- */
  --bg-primary: #0a1628;
  --bg-panel: rgba(13, 27, 42, 0.85);
  --border-glow: rgba(0, 212, 255, 0.18);
  --accent: #00d4ff;
  --accent-glow: rgba(0, 212, 255, 0.5);
  --text-primary: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.6);
  --text-dim: rgba(255, 255, 255, 0.4);
  --input-bg: rgba(10, 22, 40, 0.6);
  --input-border: rgba(0, 212, 255, 0.25);
  --graph-bg: #060e1a;

  &.theme-partyRed {
    --bg-primary: #1a0a0a;
    --bg-panel: rgba(42, 13, 13, 0.85);
    --border-glow: rgba(255, 60, 60, 0.18);
    --accent: #ff3c3c;
    --accent-glow: rgba(255, 60, 60, 0.5);
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.6);
    --text-dim: rgba(255, 255, 255, 0.4);
    --input-bg: rgba(26, 10, 10, 0.6);
    --input-border: rgba(255, 60, 60, 0.25);
    --graph-bg: #0f0505;
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
    --input-bg: rgba(240, 244, 248, 0.8);
    --input-border: rgba(0, 120, 212, 0.25);
    --graph-bg: #e8edf2;
  }
}

/* ========== 布局样式 ========== */
.network-relation-dashboard {
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

/* ========== 筛选区域 ========== */
.filter-group {
  margin-bottom: 12px;

  &:last-child { margin-bottom: 0; }
}

.filter-label {
  display: block;
  font-size: 12px;
  color: var(--text-secondary);
  margin-bottom: 6px;
}

.search-input {
  width: 100%;
  padding: 8px 12px;
  background: var(--input-bg);
  border: 1px solid var(--input-border);
  border-radius: 4px;
  color: var(--text-primary);
  font-size: 13px;
  outline: none;
  transition: border-color 0.2s;

  &::placeholder { color: var(--text-dim); }
  &:focus { border-color: var(--accent); }
}

.filter-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.filter-tag {
  padding: 4px 10px;
  background: transparent;
  border: 1px solid var(--tag-color, var(--accent));
  border-radius: 12px;
  color: var(--tag-color, var(--accent));
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;

  &.active {
    background: var(--tag-color, var(--accent));
    color: #fff;
  }
}

.strength-slider {
  width: 100%;
  -webkit-appearance: none;
  height: 4px;
  background: var(--input-border);
  border-radius: 2px;
  outline: none;

  &::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 14px;
    height: 14px;
    background: var(--accent);
    border-radius: 50%;
    cursor: pointer;
  }
}

.strength-value {
  font-size: 12px;
  color: var(--accent);
  margin-left: 8px;
}

/* ========== 统计网格 ========== */
.stat-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.stat-value {
  font-size: 22px;
  font-weight: bold;
}

.stat-label {
  font-size: 11px;
  color: var(--text-secondary);
}

/* ========== 关系分布图 ========== */
.relation-chart {
  width: 100%;
  height: 160px;
}

/* ========== 中间关系图区域 ========== */
.center-area {
  flex: 1;
  position: relative;
  overflow: hidden;
  background: var(--graph-bg);
}

.graph-container {
  width: 100%;
  height: 100%;
}

/* ========== 图例 ========== */
.graph-legend {
  position: absolute;
  top: 16px;
  left: 16px;
  display: flex;
  gap: 16px;
  padding: 8px 14px;
  background: var(--bg-panel);
  border: 1px solid var(--border-glow);
  border-radius: 6px;
  backdrop-filter: blur(8px);
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.legend-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.legend-text {
  font-size: 12px;
  color: var(--text-secondary);
}

/* ========== 缩放控制 ========== */
.zoom-controls {
  position: absolute;
  bottom: 16px;
  right: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 10px;
  background: var(--bg-panel);
  border: 1px solid var(--border-glow);
  border-radius: 6px;
  backdrop-filter: blur(8px);
}

.zoom-btn {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 1px solid var(--border-glow);
  border-radius: 4px;
  color: var(--text-secondary);
  cursor: pointer;
  font-size: 14px;

  &:hover {
    color: var(--accent);
    border-color: var(--accent);
  }
}

.zoom-level {
  font-size: 12px;
  color: var(--text-secondary);
  min-width: 40px;
  text-align: center;
}

.reset-btn {
  width: auto;
  padding: 0 8px;
  font-size: 12px;
}

/* ========== 详情面板 ========== */
.detail-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.node-badge {
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 11px;
  color: #fff;
}

.node-name {
  font-size: 16px;
  font-weight: bold;
  color: var(--text-primary);
}

.detail-fields {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.detail-field {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6px 0;
  border-bottom: 1px solid var(--border-glow);

  &:last-child { border-bottom: none; }
}

.field-label {
  font-size: 12px;
  color: var(--text-secondary);
}

.field-value {
  font-size: 13px;
  color: var(--text-primary);
}

/* ========== 关联节点列表 ========== */
.related-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.related-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px;
  background: var(--input-bg);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background: rgba(0, 212, 255, 0.08);
    border-color: var(--accent);
  }
}

.related-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.related-name {
  flex: 1;
  font-size: 13px;
  color: var(--text-primary);
}

.related-relation {
  font-size: 11px;
  color: var(--text-dim);
}

/* ========== 空状态 ========== */
.empty-state {
  .panel-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 32px 12px;
  }
}

.empty-icon {
  margin-bottom: 12px;
  opacity: 0.5;
}

.empty-text {
  font-size: 13px;
  color: var(--text-dim);
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
| `title` | String | `'网络关系分析平台'` | 大屏标题 |
| `theme` | String | `'techBlue'` | 主题：`techBlue` / `partyRed` / `lightBusiness` |
| `graphData` | Object | `{ nodes: [], links: [] }` | 网络图数据（ECharts graph 格式） |
| `layoutType` | String | `'force'` | 布局类型：`force`（力导向）/ `circular`（环形）/ `radial`（径向） |

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
| `--input-bg` | `rgba(10,22,40,0.6)` | `rgba(26,10,10,0.6)` | `rgba(240,244,248,0.8)` |
| `--input-border` | `rgba(0,212,255,0.25)` | `rgba(255,60,60,0.25)` | `rgba(0,120,212,0.25)` |
| `--graph-bg` | `#060e1a` | `#0f0505` | `#e8edf2` |

---

## 七、使用指南

1. **数据格式**：`graphData` 需遵循 ECharts graph 数据格式，包含 `nodes` 和 `links` 数组
2. **布局类型**：`force` 适合自由探索，`circular` 适合层级展示，`radial` 适合中心辐射展示
3. **节点交互**：点击节点会在右侧面板展示详情和关联节点，点击关联节点可跳转
4. **筛选功能**：左侧面板支持关键词搜索、节点类型筛选、关系强度过滤
5. **主题切换**：通过 `theme` prop 切换主题，所有颜色通过 CSS 变量自动适配
6. **注意事项**：
   - ECharts 实例需要在 `onMounted` 中初始化，`onBeforeUnmount` 中销毁
   - 窗口 resize 时需调用 `chart.resize()` 更新图表尺寸
   - 大量节点时（>1000）建议开启 `large: true` 和 `largeThreshold` 优化渲染
   - 侧面板宽度较窄（280px），内容应精简，避免信息过载
