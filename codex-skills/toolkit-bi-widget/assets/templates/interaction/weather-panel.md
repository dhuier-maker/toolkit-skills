# 天气面板模板 (WeatherPanel)

完整参考：`references/component-templates.md` WeatherPanel 章节

## 功能介绍

天气面板组件，展示当前天气信息（图标 + 温度 + 描述 + 湿度 + 风力）和3日天气预报迷你卡片。适用于智慧乡村、智慧社区等大屏的天气信息展示区域。

## 使用场景

- 大屏顶部/侧边天气信息展示
- 智慧乡村气象数据面板
- 文旅大屏景区天气展示

## Props 定义

### 数据配置 (groupKey: 'data', groupName: '数据配置')

```javascript
currentWeather: {
  type: Object,
  default: () => ({
    temp: 26,
    description: '多云',
    icon: 'cloudy',
    humidity: 65,
    wind: '东南风 3级',
  }),
  desc: '当前天气数据',
  name: '当前天气',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 1,
  useDynamic: true,
  childConfig: [
    { field: 'temp', label: '温度(°C)', type: 'Number' },
    { field: 'description', label: '天气描述', type: 'String' },
    { field: 'icon', label: '天气图标(sunny/cloudy/rainy/snowy/overcast)', type: 'String' },
    { field: 'humidity', label: '湿度(%)', type: 'Number' },
    { field: 'wind', label: '风力信息', type: 'String' },
  ],
},
forecast: {
  type: Array,
  default: () => [
    { date: '明天', tempHigh: 28, tempLow: 20, icon: 'sunny' },
    { date: '后天', tempHigh: 25, tempLow: 18, icon: 'cloudy' },
    { date: '大后天', tempHigh: 22, tempLow: 16, icon: 'rainy' },
  ],
  desc: '3日天气预报数据',
  name: '天气预报',
  groupKey: 'data',
  groupName: '数据配置',
  sort: 2,
  useDynamic: true,
  childConfig: [
    { field: 'date', label: '日期', type: 'String' },
    { field: 'tempHigh', label: '最高温(°C)', type: 'Number' },
    { field: 'tempLow', label: '最低温(°C)', type: 'Number' },
    { field: 'icon', label: '天气图标', type: 'String' },
  ],
},
```

### 样式配置 (groupKey: 'style', groupName: '样式配置')

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/lightBusiness-浅色商务',
  name: '主题',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 1,
  configurationTemplate: [
    { value: 'techBlue', label: '深蓝科技' },
    { value: 'partyRed', label: '党建红金' },
    { value: 'warmOrange', label: '暖橙数据' },
    { value: 'lightBusiness', label: '浅色商务' },
    { value: 'deepPurple', label: '紫蓝深邃' },
      { value: 'ecoGreen', label: '青绿生态' },
  ],
},
```

## 天气图标映射

```javascript
const weatherIcons = {
  sunny: '☀️',
  cloudy: '⛅',
  rainy: '🌧️',
  snowy: '❄️',
  overcast: '☁️',
  thunderstorm: '⛈️',
  foggy: '🌫️',
}
```

## 完整代码

```vue
<template>
  <div class="weather-panel" :class="[`theme-${theme}`]">
    <!-- 当前天气 -->
    <div class="current-weather">
      <div class="weather-main">
        <span class="weather-icon">{{ iconMap[currentWeather.icon] || '⛅' }}</span>
        <div class="weather-info">
          <span class="temperature">{{ currentWeather.temp }}<span class="temp-unit">°C</span></span>
          <span class="description">{{ currentWeather.description }}</span>
        </div>
      </div>
      <div class="weather-detail">
        <div class="detail-item">
          <span class="detail-label">湿度</span>
          <span class="detail-value">{{ currentWeather.humidity }}%</span>
        </div>
        <div class="detail-item">
          <span class="detail-label">风力</span>
          <span class="detail-value">{{ currentWeather.wind }}</span>
        </div>
      </div>
    </div>

    <!-- 分割线 -->
    <div class="divider"></div>

    <!-- 3日预报 -->
    <div class="forecast-row">
      <div v-for="day in forecast" :key="day.date" class="forecast-card">
        <span class="forecast-date">{{ day.date }}</span>
        <span class="forecast-icon">{{ iconMap[day.icon] || '⛅' }}</span>
        <div class="forecast-temp">
          <span class="temp-high">{{ day.tempHigh }}°</span>
          <span class="temp-separator">/</span>
          <span class="temp-low">{{ day.tempLow }}°</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  currentWeather: {
    type: Object,
    default: () => ({
      temp: 26,
      description: '多云',
      icon: 'cloudy',
      humidity: 65,
      wind: '东南风 3级',
    }),
    desc: '当前天气数据',
    name: '当前天气',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 1,
    useDynamic: true,
    childConfig: [
      { field: 'temp', label: '温度(°C)', type: 'Number' },
      { field: 'description', label: '天气描述', type: 'String' },
      { field: 'icon', label: '天气图标(sunny/cloudy/rainy/snowy/overcast)', type: 'String' },
      { field: 'humidity', label: '湿度(%)', type: 'Number' },
      { field: 'wind', label: '风力信息', type: 'String' },
    ],
  },
  forecast: {
    type: Array,
    default: () => [
      { date: '明天', tempHigh: 28, tempLow: 20, icon: 'sunny' },
      { date: '后天', tempHigh: 25, tempLow: 18, icon: 'cloudy' },
      { date: '大后天', tempHigh: 22, tempLow: 16, icon: 'rainy' },
    ],
    desc: '3日天气预报数据',
    name: '天气预报',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 2,
    useDynamic: true,
    childConfig: [
      { field: 'date', label: '日期', type: 'String' },
      { field: 'tempHigh', label: '最高温(°C)', type: 'Number' },
      { field: 'tempLow', label: '最低温(°C)', type: 'Number' },
      { field: 'icon', label: '天气图标', type: 'String' },
    ],
  },
  theme: {
    type: String,
    default: 'techBlue',
    desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/lightBusiness-浅色商务',
    name: '主题',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
    configurationTemplate: [
      { value: 'techBlue', label: '深蓝科技' },
      { value: 'partyRed', label: '党建红金' },
    { value: 'warmOrange', label: '暖橙数据' },
      { value: 'lightBusiness', label: '浅色商务' },
    { value: 'deepPurple', label: '紫蓝深邃' },
      { value: 'ecoGreen', label: '青绿生态' },
    ],
  },
})

const iconMap = {
  sunny: '☀️',
  cloudy: '⛅',
  rainy: '🌧️',
  snowy: '❄️',
  overcast: '☁️',
  thunderstorm: '⛈️',
  foggy: '🌫️',
}
</script>

<style lang="scss" scoped>
.weather-panel {
  padding: 16px;
  border-radius: 8px;
  background: var(--weather-bg);
  border: 1px solid var(--weather-border-color);
}

/* 当前天气 */
.current-weather {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.weather-main {
  display: flex;
  align-items: center;
  gap: 12px;
}

.weather-icon {
  font-size: 40px;
  line-height: 1;
  filter: drop-shadow(0 0 6px var(--weather-glow-color));
}

.weather-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.temperature {
  font-size: 28px;
  font-weight: 700;
  color: var(--weather-text-primary);
  line-height: 1.1;

  .temp-unit {
    font-size: 14px;
    font-weight: 400;
    color: var(--weather-text-secondary);
  }
}

.description {
  font-size: 13px;
  color: var(--weather-text-secondary);
}

.weather-detail {
  display: flex;
  flex-direction: column;
  gap: 6px;
  align-items: flex-end;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 6px;
}

.detail-label {
  font-size: 11px;
  color: var(--weather-text-muted);
}

.detail-value {
  font-size: 13px;
  color: var(--weather-text-primary);
  font-weight: 500;
}

/* 分割线 */
.divider {
  height: 1px;
  margin: 12px 0;
  background: var(--weather-border-color);
}

/* 3日预报 */
.forecast-row {
  display: flex;
  gap: 8px;
}

.forecast-card {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 8px 4px;
  border-radius: 6px;
  background: var(--weather-card-bg);
  border: 1px solid var(--weather-card-border);
  transition: all 0.2s;

  &:hover {
    border-color: var(--weather-accent-color);
    box-shadow: 0 0 8px var(--weather-glow-color);
  }
}

.forecast-date {
  font-size: 11px;
  color: var(--weather-text-muted);
}

.forecast-icon {
  font-size: 22px;
  line-height: 1;
}

.forecast-temp {
  display: flex;
  align-items: baseline;
  gap: 2px;
  font-size: 12px;
}

.temp-high {
  color: var(--weather-temp-high);
  font-weight: 600;
}

.temp-separator {
  color: var(--weather-text-muted);
  margin: 0 1px;
}

.temp-low {
  color: var(--weather-text-secondary);
}

/* ========== 主题变量 ========== */

/* techBlue 深蓝科技 */
.theme-techBlue {
  --weather-bg: rgba(6, 30, 65, 0.85);
  --weather-border-color: rgba(0, 168, 232, 0.2);
  --weather-card-bg: rgba(0, 168, 232, 0.06);
  --weather-card-border: rgba(0, 168, 232, 0.12);
  --weather-accent-color: #00a8e8;
  --weather-glow-color: rgba(0, 168, 232, 0.3);
  --weather-text-primary: #e0f4ff;
  --weather-text-secondary: rgba(224, 244, 255, 0.7);
  --weather-text-muted: rgba(224, 244, 255, 0.4);
  --weather-temp-high: #ff9f43;
}

/* partyRed 党建红金 */
.theme-partyRed {
  --weather-bg: rgba(60, 10, 10, 0.85);
  --weather-border-color: rgba(220, 50, 50, 0.2);
  --weather-card-bg: rgba(220, 50, 50, 0.06);
  --weather-card-border: rgba(220, 50, 50, 0.12);
  --weather-accent-color: #dc3232;
  --weather-glow-color: rgba(220, 50, 50, 0.3);
  --weather-text-primary: #ffe0e0;
  --weather-text-secondary: rgba(255, 224, 224, 0.7);
  --weather-text-muted: rgba(255, 224, 224, 0.4);
  --weather-temp-high: #ff9f43;
}

/* lightBusiness 浅色商务 */
.theme-lightBusiness {
  --weather-bg: rgba(255, 255, 255, 0.9);
  --weather-border-color: rgba(0, 120, 200, 0.12);
  --weather-card-bg: rgba(0, 120, 200, 0.04);
  --weather-card-border: rgba(0, 120, 200, 0.08);
  --weather-accent-color: #0078c8;
  --weather-glow-color: rgba(0, 120, 200, 0.15);
  --weather-text-primary: #1a1a2e;
  --weather-text-secondary: rgba(26, 26, 46, 0.65);
  --weather-text-muted: rgba(26, 26, 46, 0.35);
  --weather-temp-high: #e85d04;
}
/* ecoGreen 青绿生态 */
.theme-ecoGreen {
  --panel-bg: rgba(10,30,50,0.85);
  --border-color: rgba(0,180,150,0.18);
  --border-glow: rgba(0,180,150,0.4);
  --text-primary: #ffffff;
  --text-secondary: rgba(255,255,255,0.7);
  --accent-color: #00b496;
  --header-bg: rgba(0,180,150,0.08);
  --dot-color: rgba(0,180,150,0.3);
}

</style>
```

## 主题变量支持 (theme prop)

### 主题色值对照表

| CSS 变量 | techBlue (深蓝科技) | partyRed (党建红金) | lightBusiness (浅色商务) | ecoGreen (青绿生态) |
|----------|---------------------|---------------------|------------------------|
| --weather-bg | rgba(6,30,65,0.85) | rgba(60,10,10,0.85) | rgba(255,255,255,0.9) |
| --weather-border-color | rgba(0,168,232,0.2) | rgba(220,50,50,0.2) | rgba(0,120,200,0.12) |
| --weather-card-bg | rgba(0,168,232,0.06) | rgba(220,50,50,0.06) | rgba(0,120,200,0.04) |
| --weather-card-border | rgba(0,168,232,0.12) | rgba(220,50,50,0.12) | rgba(0,120,200,0.08) |
| --weather-accent-color | #00a8e8 | #dc3232 | #0078c8 |
| --weather-glow-color | rgba(0,168,232,0.3) | rgba(220,50,50,0.3) | rgba(0,120,200,0.15) |
| --weather-text-primary | #e0f4ff | #ffe0e0 | #1a1a2e |
| --weather-text-secondary | rgba(224,244,255,0.7) | rgba(255,224,224,0.7) | rgba(26,26,46,0.65) |
| --weather-text-muted | rgba(224,244,255,0.4) | rgba(255,224,224,0.4) | rgba(26,26,46,0.35) |
| --weather-temp-high | #ff9f43 | #ff9f43 | #e85d04 |

### 主题 Props 定义

```javascript
theme: {
  type: String,
  default: 'techBlue',
  desc: '主题风格：techBlue-深蓝科技/partyRed-党建红金/lightBusiness-浅色商务',
  name: '主题',
  groupKey: 'style',
  groupName: '样式配置',
  sort: 1,
  configurationTemplate: [
    { value: 'techBlue', label: '深蓝科技' },
    { value: 'partyRed', label: '党建红金' },
    { value: 'warmOrange', label: '暖橙数据' },
    { value: 'lightBusiness', label: '浅色商务' },
    { value: 'deepPurple', label: '紫蓝深邃' },
      { value: 'ecoGreen', label: '青绿生态' },
  ],
},
```

### 主题 CSS 变量映射

```javascript
const themeVariables = {
  techBlue: {
    '--weather-bg': 'rgba(6,30,65,0.85)',
    '--weather-border-color': 'rgba(0,168,232,0.2)',
    '--weather-card-bg': 'rgba(0,168,232,0.06)',
    '--weather-card-border': 'rgba(0,168,232,0.12)',
    '--weather-accent-color': '#00a8e8',
    '--weather-glow-color': 'rgba(0,168,232,0.3)',
    '--weather-text-primary': '#e0f4ff',
    '--weather-text-secondary': 'rgba(224,244,255,0.7)',
    '--weather-text-muted': 'rgba(224,244,255,0.4)',
    '--weather-temp-high': '#ff9f43',
  },
  partyRed: {
    '--weather-bg': 'rgba(60,10,10,0.85)',
    '--weather-border-color': 'rgba(220,50,50,0.2)',
    '--weather-card-bg': 'rgba(220,50,50,0.06)',
    '--weather-card-border': 'rgba(220,50,50,0.12)',
    '--weather-accent-color': '#dc3232',
    '--weather-glow-color': 'rgba(220,50,50,0.3)',
    '--weather-text-primary': '#ffe0e0',
    '--weather-text-secondary': 'rgba(255,224,224,0.7)',
    '--weather-text-muted': 'rgba(255,224,224,0.4)',
    '--weather-temp-high': '#ff9f43',
  },
  lightBusiness: {
    '--weather-bg': 'rgba(255,255,255,0.9)',
    '--weather-border-color': 'rgba(0,120,200,0.12)',
    '--weather-card-bg': 'rgba(0,120,200,0.04)',
    '--weather-card-border': 'rgba(0,120,200,0.08)',
    '--weather-accent-color': '#0078c8',
    '--weather-glow-color': 'rgba(0,120,200,0.15)',
    '--weather-text-primary': '#1a1a2e',
    '--weather-text-secondary': 'rgba(26,26,46,0.65)',
    '--weather-text-muted': 'rgba(26,26,46,0.35)',
    '--weather-temp-high': '#e85d04',
  },
  ecoGreen: {
    '--tab-bg': 'rgba(0,229,195,0.06)',
    '--tab-border-color': 'rgba(0,229,195,0.2)',
    '--tab-text-color': 'rgba(224,255,240,0.6)',
    '--tab-hover-bg': 'rgba(0,229,195,0.1)',
    '--tab-active-bg': 'rgba(0,229,195,0.15)',
    '--tab-active-border': '#00E5C3',
    '--tab-active-text': '#E0FFF0',
    '--tab-glow-color': 'rgba(0,229,195,0.4)',
    '--tab-glow-inner': 'rgba(0,229,195,0.08)',
  },
  warmOrange: {
    '--tab-bg': 'rgba(255,140,66,0.06)',
    '--tab-border-color': 'rgba(255,140,66,0.2)',
    '--tab-text-color': 'rgba(255,240,224,0.6)',
    '--tab-hover-bg': 'rgba(255,140,66,0.1)',
    '--tab-active-bg': 'rgba(255,140,66,0.15)',
    '--tab-active-border': '#FF8C42',
    '--tab-active-text': '#FFF0E0',
    '--tab-glow-color': 'rgba(255,140,66,0.4)',
    '--tab-glow-inner': 'rgba(255,140,66,0.08)',
  },
  deepPurple: {
    '--tab-bg': 'rgba(168,85,247,0.06)',
    '--tab-border-color': 'rgba(168,85,247,0.2)',
    '--tab-text-color': 'rgba(232,224,255,0.6)',
    '--tab-hover-bg': 'rgba(168,85,247,0.1)',
    '--tab-active-bg': 'rgba(168,85,247,0.15)',
    '--tab-active-border': '#A855F7',
    '--tab-active-text': '#E8E0FF',
    '--tab-glow-color': 'rgba(168,85,247,0.4)',
    '--tab-glow-inner': 'rgba(168,85,247,0.08)',
  },
}
```
