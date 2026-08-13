# 多TAB切换布局模板

> 适用于智慧乡村、智慧街道等需要多个TAB视图切换的BI大屏场景。

---

## 一、布局结构

```
┌─────────────────────────────────────────────────────────────┐
│                      顶部标题栏                              │
├──────────────┬─────────────────────────────┬────────────────┤
│              │                             │                │
│   左侧面板    │         中间区域             │    右侧面板     │
│   (可滚动)    │    (地图/航拍/3D场景)        │    (可滚动)     │
│              │                             │                │
├──────────────┴─────────────────────────────┴────────────────┤
│   [基层治理]  [智慧党建]  [智慧养老]  [产业振兴]              │
│                    底部导航栏 (胶囊按钮)                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、底部导航胶囊按钮模式（深蓝科技风）

```vue
<template>
  <div class="dashboard-container" :class="`theme-${currentTheme}`">
    <!-- 顶部标题栏 -->
    <header class="dashboard-header">
      <div class="header-left">
        <button class="admin-btn" @click="goAdmin">管理后台</button>
      </div>
      <div class="header-center">
        <h1 class="main-title">{{ title }}</h1>
      </div>
      <div class="header-right">
        <DateTimeDisplay />
      </div>
    </header>

    <!-- 主内容区域 -->
    <main class="dashboard-main">
      <!-- 左侧面板 -->
      <aside class="left-panel">
        <component :is="currentLeftPanel" :key="activeTab" />
      </aside>

      <!-- 中间区域 -->
      <section class="center-area">
        <component :is="currentCenterPanel" :key="activeTab" />
      </section>

      <!-- 右侧面板 -->
      <aside class="right-panel">
        <component :is="currentRightPanel" :key="activeTab" />
      </aside>
    </main>

    <!-- 底部导航栏 -->
    <nav class="bottom-nav">
      <button
        v-for="tab in tabs"
        :key="tab.value"
        class="nav-capsule"
        :class="{ active: activeTab === tab.value }"
        @click="switchTab(tab.value)"
      >
        {{ tab.label }}
      </button>
    </nav>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import DateTimeDisplay from './components/DateTimeDisplay.vue';

const tabViews = {
  governance: {
    left: 'GovernanceLeftPanel',
    center: 'GovernanceCenter',
    right: 'GovernanceRightPanel',
  },
  party: {
    left: 'PartyLeftPanel',
    center: 'PartyCenter',
    right: 'PartyRightPanel',
  },
  elderly: {
    left: 'ElderlyLeftPanel',
    center: 'ElderlyCenter',
    right: 'ElderlyRightPanel',
  },
  industry: {
    left: 'IndustryLeftPanel',
    center: 'IndustryCenter',
    right: 'IndustryRightPanel',
  },
};

export default {
  name: 'MultiTabDashboard',
  components: { DateTimeDisplay },
  props: {
    title: { type: String, default: '智慧乡村样板间' },
    theme: { type: String, default: 'dark' },
  },
  setup(props) {
    const activeTab = ref('governance');
    const currentTheme = computed(() => props.theme);

    const tabs = [
      { label: '基层治理', value: 'governance' },
      { label: '智慧党建', value: 'party' },
      { label: '智慧养老', value: 'elderly' },
      { label: '产业振兴', value: 'industry' },
    ];

    const currentLeftPanel = computed(() => tabViews[activeTab.value]?.left);
    const currentCenterPanel = computed(() => tabViews[activeTab.value]?.center);
    const currentRightPanel = computed(() => tabViews[activeTab.value]?.right);

    const switchTab = (tabValue) => { activeTab.value = tabValue; };
    const goAdmin = () => {};

    return {
      activeTab, currentTheme, tabs,
      currentLeftPanel, currentCenterPanel, currentRightPanel,
      switchTab, goAdmin,
    };
  },
};
</script>

<style lang="scss" scoped>
.dashboard-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary, #0a1628);
  overflow: hidden;
}

.dashboard-header {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 30px;
  background: linear-gradient(180deg, rgba(0, 168, 232, 0.15), transparent);
  border-bottom: 1px solid rgba(0, 168, 232, 0.3);
}

.header-left, .header-right { width: 200px; }

.admin-btn {
  padding: 8px 20px;
  background: rgba(0, 168, 232, 0.2);
  border: 1px solid #00a8e8;
  border-radius: 4px;
  color: #00a8e8;
  cursor: pointer;
  &:hover { background: rgba(0, 168, 232, 0.3); }
}

.main-title {
  font-size: 32px;
  font-weight: bold;
  color: #ffffff;
  text-shadow: 0 0 20px rgba(0, 168, 232, 0.5);
}

.dashboard-main {
  flex: 1;
  display: flex;
  padding: 20px;
  gap: 20px;
  overflow: hidden;
}

.left-panel, .right-panel {
  width: 380px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  overflow-y: auto;
  &::-webkit-scrollbar { width: 4px; }
  &::-webkit-scrollbar-thumb { background: rgba(0, 168, 232, 0.3); border-radius: 2px; }
}

.center-area {
  flex: 1;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
}

.bottom-nav {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 10px 0;
  background: linear-gradient(0deg, rgba(0, 168, 232, 0.1), transparent);
}

.nav-capsule {
  padding: 10px 30px;
  background: rgba(0, 168, 232, 0.1);
  border: 1px solid rgba(0, 168, 232, 0.3);
  border-radius: 20px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s;

  &:hover { background: rgba(0, 168, 232, 0.2); color: #ffffff; }

  &.active {
    background: linear-gradient(135deg, #ffb703, #fb8500);
    border-color: #ffb703;
    color: #ffffff;
    box-shadow: 0 0 20px rgba(255, 183, 3, 0.4);
  }
}
</style>
```

---

## 三、底部图标+文字导航模式（浅色商务风）

```vue
<template>
  <div class="dashboard-container light-theme">
    <header class="dashboard-header">
      <div class="header-left">
        <div class="logo-area">
          <img src="@/assets/china-mobile-logo.png" class="logo" />
          <span class="logo-text">中国移动 5G+</span>
        </div>
      </div>
      <div class="header-center">
        <h1 class="main-title">{{ title }}</h1>
      </div>
      <div class="header-right">
        <DateTimeDisplay />
        <button class="admin-btn" @click="goAdmin">后台管理</button>
      </div>
    </header>

    <main class="dashboard-main">
      <aside class="left-panel">
        <component :is="currentLeftPanel" :key="activeTab" />
      </aside>
      <section class="center-area">
        <component :is="currentCenterPanel" :key="activeTab" />
      </section>
      <aside class="right-panel">
        <component :is="currentRightPanel" :key="activeTab" />
      </aside>
    </main>

    <nav class="bottom-nav-bar">
      <button
        v-for="tab in tabs"
        :key="tab.value"
        class="nav-item"
        :class="{ active: activeTab === tab.value }"
        @click="switchTab(tab.value)"
      >
        <span class="nav-icon" v-html="tab.icon"></span>
        <span class="nav-text">{{ tab.label }}</span>
      </button>
    </nav>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import DateTimeDisplay from './components/DateTimeDisplay.vue';

const tabViews = {
  comprehensive: {
    left: 'ComprehensiveLeftPanel', center: 'ComprehensiveCenter', right: 'ComprehensiveRightPanel',
  },
  party: {
    left: 'PartyPeopleLeftPanel', center: 'PartyPeopleCenter', right: 'PartyPeopleRightPanel',
  },
  enterprise: {
    left: 'EnterpriseLeftPanel', center: 'EnterpriseCenter', right: 'EnterpriseRightPanel',
  },
};

export default {
  name: 'StreetDashboard',
  components: { DateTimeDisplay },
  setup() {
    const activeTab = ref('comprehensive');
    const tabs = [
      { label: '综合治理', value: 'comprehensive', icon: '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>' },
      { label: '党建民生', value: 'party', icon: '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>' },
      { label: '企业服务', value: 'enterprise', icon: '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/></svg>' },
    ];
    const currentLeftPanel = computed(() => tabViews[activeTab.value]?.left);
    const currentCenterPanel = computed(() => tabViews[activeTab.value]?.center);
    const currentRightPanel = computed(() => tabViews[activeTab.value]?.right);
    const switchTab = (tabValue) => { activeTab.value = tabValue; };
    const goAdmin = () => {};
    return { activeTab, tabs, currentLeftPanel, currentCenterPanel, currentRightPanel, switchTab, goAdmin };
  },
};
</script>

<style lang="scss" scoped>
.dashboard-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f5f7fa;
  overflow: hidden;
}

.dashboard-header {
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 30px;
  background: #ffffff;
  border-bottom: 1px solid #e8e8e8;
}

.header-left, .header-right { display: flex; align-items: center; gap: 20px; }
.logo-area { display: flex; align-items: center; gap: 10px; }
.logo { width: 30px; height: 30px; }
.logo-text { font-size: 14px; color: #0099ff; font-weight: 500; }
.main-title { font-size: 28px; font-weight: bold; color: #333333; }

.admin-btn {
  padding: 8px 16px;
  background: #0099ff;
  border: none;
  border-radius: 4px;
  color: #ffffff;
  cursor: pointer;
  &:hover { background: #0088e6; }
}

.dashboard-main {
  flex: 1;
  display: flex;
  padding: 20px;
  gap: 20px;
  overflow: hidden;
}

.left-panel, .right-panel { width: 360px; display: flex; flex-direction: column; gap: 16px; overflow-y: auto; }

.center-area {
  flex: 1;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  background: #ffffff;
  border: 1px solid #e8e8e8;
}

.bottom-nav-bar {
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(90deg, #4a90e2, #0066cc);
  padding: 0 20px;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 8px 40px;
  background: transparent;
  border: none;
  cursor: pointer;
  transition: all 0.3s;

  .nav-icon { color: rgba(255, 255, 255, 0.7); }
  .nav-text { font-size: 12px; color: rgba(255, 255, 255, 0.7); }

  &:hover, &.active {
    .nav-icon, .nav-text { color: #ffffff; }
  }

  &.active {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
  }
}
</style>
```

---

## 四、TAB切换动画效果

### 淡入淡出动画

```vue
<template>
  <transition name="fade" mode="out-in">
    <component :is="currentPanel" :key="activeTab" />
  </transition>
</template>

<style lang="scss" scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
```

### 滑动切换动画

```vue
<template>
  <transition :name="slideDirection" mode="out-in">
    <component :is="currentPanel" :key="activeTab" />
  </transition>
</template>

<script>
const slideDirection = computed(() => {
  const tabIndex = tabs.findIndex(t => t.value === activeTab.value);
  const prevTabIndex = tabs.findIndex(t => t.value === prevTab.value);
  return tabIndex > prevTabIndex ? 'slide-left' : 'slide-right';
});
</script>

<style lang="scss" scoped>
.slide-left-enter-active, .slide-left-leave-active,
.slide-right-enter-active, .slide-right-leave-active {
  transition: all 0.3s ease;
  position: absolute;
  width: 100%;
}
.slide-left-enter-from { transform: translateX(100%); opacity: 0; }
.slide-left-leave-to { transform: translateX(-100%); opacity: 0; }
.slide-right-enter-from { transform: translateX(-100%); opacity: 0; }
.slide-right-leave-to { transform: translateX(100%); opacity: 0; }
</style>
```

---

## 五、TAB视图面板配置示例

```javascript
// 基层治理视图
const governanceViews = {
  left: [
    { component: 'BasicDataPanel', title: '基础数据' },
    { component: 'ThreeAssetsPanel', title: '三资管理' },
    { component: 'ThreePublicPanel', title: '三务公开' },
  ],
  center: 'AerialView',
  right: [
    { component: 'MonitorPanel', title: '接入监控' },
    { component: 'PublicPointPanel', title: '公共点位监控' },
    { component: 'SmartCommPanel', title: '智慧通讯' },
  ],
};

// 产业振兴视图
const industryViews = {
  left: [
    { component: 'WeatherPanel', title: '气象监测' },
    { component: 'HistoryResourcePanel', title: '历史文化资源' },
    { component: 'EnterprisePanel', title: '优秀企业' },
  ],
  center: 'MapWithModal',
  right: [
    { component: 'ThreeIndustryPanel', title: '三产概况' },
    { component: 'AgriculturePanel', title: '农业概况' },
    { component: 'IndustryStylePanel', title: '产业风貌' },
  ],
};
```

---

## 六、使用指南

1. **确定TAB数量和名称**：根据业务需求规划TAB视图
2. **配置视图映射**：为每个TAB配置左右面板和中间区域组件
3. **选择导航样式**：深蓝科技风用胶囊按钮模式，浅色商务风用图标+文字导航模式
4. **实现TAB组件**：根据配置创建各视图的面板组件
5. **注意事项**：
   - 每个TAB视图的组件应独立，避免状态污染
   - 切换时注意销毁不必要的定时器和事件监听
   - 地图组件切换时注意资源释放
