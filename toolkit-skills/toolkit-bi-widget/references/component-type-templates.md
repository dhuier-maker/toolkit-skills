## 六、组件类型模板

> **完整模板代码请参考 `references/component-templates.md` 文件**

### 6.1 ECharts 图表类组件

适用于：柱状图、饼图、折线图、雷达图、散点图等

**完整模板：**
- **柱状图** → `references/component-templates.md` 第一节
- **饼图/环形图/玫瑰图** → `references/component-templates.md` 第五节
- **折线图/面积图** → `references/component-templates.md` 第六节
- **雷达图** → `references/component-templates.md` 第七节

**主组件结构：**
```vue
<template>
  <div ref="chartRef" class="chart-container"></div>
</template>

<script setup>
import { markRaw, defineProps, defineExpose, ref, watch, onUnmounted, onMounted } from 'vue';
import * as echarts from 'echarts';
import i18n from './locale/index';

const props = defineProps({
  // 数据配置
  chartData: {
    type: Object,
    default: () => ({ /* 默认数据结构 */ }),
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },
  // 样式配置...
});

const chartRef = ref(null);
const chart = ref(null);

// 颜色转换函数（支持渐变）
const convertColor = (colorConfig) => {
  if (typeof colorConfig === 'string') return colorConfig;
  if (colorConfig.type === 'solid') return colorConfig.color;
  if (colorConfig.type === 'linear') {
    return new echarts.graphic.LinearGradient(
      colorConfig.x || 0,
      colorConfig.y || 0,
      colorConfig.x2 || 0,
      colorConfig.y2 || 1,
      colorConfig.colorStops || []
    );
  }
  return colorConfig;
};

// 初始化图表
const initChart = () => {
  if (!chartRef.value) return;
  if (chart.value) chart.value.dispose();

  chart.value = markRaw(echarts.init(chartRef.value));

  const option = {
    backgroundColor: 'transparent',
    // ECharts 配置...
  };

  chart.value.setOption(option, true);
};

// 监听配置变化
watch(
  () => [props.chartData, /* 其他props */],
  () => { setTimeout(() => initChart(), 500); },
  { deep: true }
);

// 窗口resize处理
const handleResize = () => chart.value?.resize();

onMounted(() => {
  initChart();
  window.addEventListener('resize', handleResize);
  const resizeObserver = new ResizeObserver(() => handleResize());
  if (chartRef.value) resizeObserver.observe(chartRef.value);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  chart.value?.dispose();
});

defineExpose({ chart, initChart });
</script>

<style lang="scss" scoped>
.chart-container {
  width: 100%;
  height: 100%;
}
</style>
```

### 6.2 地图类组件

适用于：点位地图、热力图、飞线图、边界地图等

**完整模板：** `references/component-templates.md` 第二节

**关键依赖：**
```javascript
import AMapLoader from '@amap/amap-jsapi-loader';
```

**初始化模式：**
```javascript
const initMap = () => {
  AMapLoader.reset();
  AMapLoader.load({
    key: 'YOUR_AMAP_KEY',
    version: '2.0',
    Loca: { version: '2.0.0' },
    plugins: ['AMap.DistrictSearch', 'AMap.Polyline', 'AMap.convertFrom'],
  }).then((AMap) => {
    chart.value = new AMap.Map('map-container', {
      // 地图配置
    });
    // 添加图层、标记点等
  });
};
```

**安全配置（onMounted中）：**
```javascript
window._AMapSecurityConfig = {
  securityJsCode: 'YOUR_SECURITY_CODE',
};
```

### 6.3 进度/排名类组件

适用于：排名进度条、数据卡片、统计数字等

**完整模板：**
- **排名进度条** → `references/component-templates.md` 第三节
- **数字翻牌器** → `references/component-templates.md` 第九节 9.1
- **统计卡片** → `references/component-templates.md` 第九节 9.2

**特点：**
- 纯CSS/动画实现，不依赖ECharts
- 支持动画配置（时长、循环等）
- 使用CSS变量实现动态样式

**动画配置示例：**
```javascript
const getAnimationDuration = computed(() => {
  const duration = props.animateDuration / 1000;
  const count = props.openAnimate ? 'infinite' : 0;
  return {
    animationDuration: duration + 's',
    animationIterationCount: count,
  };
});
```

### 6.4 文本类组件

适用于：标题、时间显示、跑马灯文本等

**完整模板：**
- **标题组件** → `references/component-templates.md` 第八节 8.1
- **时间显示组件** → `references/component-templates.md` 第八节 8.2
- **跑马灯组件** → `references/component-templates.md` 第八节 8.3

**时间显示配置：**
```javascript
import dayjs from 'dayjs';

watch(
  () => ({ time: props.time, date: props.date, dateConfig: props.dateConfig }),
  (val) => {
    clearTimer();
    if (val.time) {
      dateTimeText.value = dayjs(new Date()).format('HH:mm:ss');
      timer.value = setInterval(() => {
        dateTimeText.value = dayjs(new Date()).format('HH:mm:ss');
      }, 1000);
    }
    if (val.date) {
      // 日期格式化逻辑
    }
  },
  { deep: true, immediate: true }
);
```

**跑马灯动画：**
```javascript
const autoScrollFn = () => {
  const contentWidth = textContent.value?.getBoundingClientRect()?.width;
  const containerWidth = textContainer.value?.getBoundingClientRect()?.width;
  if (contentWidth > containerWidth) {
    boxAnimate.value = scrollContent.value?.animate(
      [{ transform: 'translateX(0)' }, { transform: 'translateX(-50%)' }],
      { duration: props.animationTime, fill: 'forwards' }
    );
    boxAnimate.value.onfinish = () => {
      clearAnimate();
      autoScrollFn();
    };
  }
};
```

