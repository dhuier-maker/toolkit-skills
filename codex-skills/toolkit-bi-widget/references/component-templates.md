# 组件模板参考

## 一、ECharts 柱状图完整模板

### 目录结构
```
MultiBarChart/
├── index.js
└── src/
    ├── index.vue
    ├── components/
    │   ├── BarWidth.vue
    │   ├── BarColor.vue
    │   ├── BarBorderRadius.vue
    │   ├── ChartOrientation.vue
    │   ├── XAxisLineColor.vue
    │   ├── YAxisLineColor.vue
    │   ├── LabelColor.vue
    │   ├── TooltipBackgroundColor.vue
    │   └── style/
    ├── locale/
    │   ├── index.js
    │   └── lang/
    │       ├── zh-cn.json
    │       └── en.json
    ├── static/
    │   └── img/
    └── font.scss
```

### index.vue 完整代码
```vue
<template>
  <div ref="chartRef" class="multi-bar-chart"></div>
</template>

<script setup>
import { markRaw, defineProps, defineExpose, ref, watch, onUnmounted, onMounted } from 'vue';
import * as echarts from 'echarts';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  chartData: {
    type: Object,
    default: () => ({
      categories: ['类别1', '类别2', '类别3', '类别4', '类别5', '类别6'],
      values: [84, 70, 61, 79, 50, 58],
    }),
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  // ========== 样式配置 - 柱体 ==========
  chartOrientation: {
    type: String,
    default: 'vertical',
    desc: '图表方向',
    name: '图表方向',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
    configurationTemplate: () => import('./components/ChartOrientation.vue'),
  },

  barWidth: {
    type: Number,
    default: 30,
    desc: '柱体宽度',
    name: '柱体宽度',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
    min: 10,
    max: 100,
    configurationTemplate: () => import('./components/BarWidth.vue'),
  },

  barBorderRadius: {
    type: [Array, Number],
    default: () => [10, 10, 0, 0],
    desc: '柱体圆角 [左上, 右上, 右下, 左下]',
    name: '柱体圆角',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
    configurationTemplate: () => import('./components/BarBorderRadius.vue'),
  },

  barColors: {
    type: Array,
    default: () => [
      {
        type: 'linear',
        x: 0,
        y: 0,
        x2: 0,
        y2: 1,
        colorStops: [
          { offset: 0, color: '#00D9FF' },
          { offset: 1, color: '#0066FF' },
        ],
      },
    ],
    desc: '柱体颜色（支持渐变）',
    name: '柱体颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
    configurationTemplate: () => import('./components/BarColors.vue'),
  },

  // ========== 样式配置 - X轴 ==========
  xAxisShow: {
    type: Boolean,
    default: true,
    desc: '是否显示X轴',
    name: '显示X轴',
    groupKey: 'style',
    groupName: 'X轴配置',
    sort: 10,
  },

  xAxisLineColor: {
    type: String,
    default: 'rgba(255, 255, 255, 0.2)',
    desc: 'X轴线颜色',
    name: 'X轴线颜色',
    groupKey: 'style',
    groupName: 'X轴配置',
    sort: 11,
    configurationTemplate: () => import('./components/XAxisLineColor.vue'),
  },

  xAxisLabelColor: {
    type: String,
    default: '#ffffff',
    desc: 'X轴标签颜色',
    name: 'X轴标签颜色',
    groupKey: 'style',
    groupName: 'X轴配置',
    sort: 12,
    configurationTemplate: () => import('./components/XAxisLabelColor.vue'),
  },

  xAxisLabelFontSize: {
    type: Number,
    default: 14,
    desc: 'X轴标签字体大小',
    name: 'X轴标签字号',
    groupKey: 'style',
    groupName: 'X轴配置',
    sort: 13,
    min: 10,
    max: 30,
  },

  // ========== 样式配置 - Y轴 ==========
  yAxisShow: {
    type: Boolean,
    default: true,
    desc: '是否显示Y轴',
    name: '显示Y轴',
    groupKey: 'style',
    groupName: 'Y轴配置',
    sort: 20,
  },

  yAxisSplitLineShow: {
    type: Boolean,
    default: true,
    desc: '是否显示Y轴分割线',
    name: '显示分割线',
    groupKey: 'style',
    groupName: 'Y轴配置',
    sort: 21,
  },

  yAxisSplitLineColor: {
    type: String,
    default: 'rgba(255, 255, 255, 0.1)',
    desc: 'Y轴分割线颜色',
    name: '分割线颜色',
    groupKey: 'style',
    groupName: 'Y轴配置',
    sort: 22,
    configurationTemplate: () => import('./components/YAxisSplitLineColor.vue'),
  },

  // ========== 样式配置 - 标签 ==========
  showLabel: {
    type: Boolean,
    default: true,
    desc: '是否显示柱顶标签',
    name: '显示标签',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 30,
  },

  labelColor: {
    type: String,
    default: '#ffffff',
    desc: '标签文字颜色',
    name: '标签颜色',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 31,
    configurationTemplate: () => import('./components/LabelColor.vue'),
  },

  labelFontSize: {
    type: Number,
    default: 14,
    desc: '标签字体大小',
    name: '标签字号',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 32,
    min: 10,
    max: 30,
  },

  // ========== 样式配置 - 提示框 ==========
  showTooltip: {
    type: Boolean,
    default: true,
    desc: '是否显示提示框',
    name: '显示提示框',
    groupKey: 'style',
    groupName: '提示框配置',
    sort: 40,
  },

  tooltipBackgroundColor: {
    type: String,
    default: 'rgba(0, 0, 0, 0.8)',
    desc: '提示框背景颜色',
    name: '提示框背景色',
    groupKey: 'style',
    groupName: '提示框配置',
    sort: 41,
    configurationTemplate: () => import('./components/TooltipBackgroundColor.vue'),
  },

  // ========== 样式配置 - 网格 ==========
  gridTop: {
    type: Number,
    default: 60,
    desc: '网格上边距',
    name: '上边距',
    groupKey: 'style',
    groupName: '网格配置',
    sort: 50,
    min: 0,
    max: 200,
  },

  gridBottom: {
    type: Number,
    default: 60,
    desc: '网格下边距',
    name: '下边距',
    groupKey: 'style',
    groupName: '网格配置',
    sort: 51,
    min: 0,
    max: 200,
  },

  gridLeft: {
    type: Number,
    default: 60,
    desc: '网格左边距',
    name: '左边距',
    groupKey: 'style',
    groupName: '网格配置',
    sort: 52,
    min: 0,
    max: 200,
  },

  gridRight: {
    type: Number,
    default: 60,
    desc: '网格右边距',
    name: '右边距',
    groupKey: 'style',
    groupName: '网格配置',
    sort: 53,
    min: 0,
    max: 200,
  },
});

const chartRef = ref(null);
const chart = ref(null);

// 转换颜色配置为 ECharts 格式
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

  try {
    if (chart.value) chart.value.dispose();
    chart.value = markRaw(echarts.init(chartRef.value));

    const categories = props.chartData?.categories || [];
    const values = props.chartData?.values || [];

    if (categories.length === 0 || values.length === 0) return;

    const isHorizontal = props.chartOrientation === 'horizontal';

    const option = {
      backgroundColor: 'transparent',
      tooltip: {
        show: props.showTooltip,
        trigger: 'axis',
        confine: true,
        backgroundColor: props.tooltipBackgroundColor,
        borderColor: '#333',
        borderWidth: 1,
        textStyle: { color: '#fff', fontSize: 14 },
      },
      grid: {
        top: props.gridTop,
        bottom: props.gridBottom,
        left: props.gridLeft,
        right: props.gridRight,
        containLabel: true,
      },
      xAxis: [{
        type: isHorizontal ? 'value' : 'category',
        data: isHorizontal ? undefined : categories,
        show: props.xAxisShow,
        boundaryGap: isHorizontal ? undefined : true,
        axisLine: {
          show: true,
          lineStyle: { color: props.xAxisLineColor },
        },
        axisTick: { show: false },
        axisLabel: {
          color: props.xAxisLabelColor,
          fontSize: props.xAxisLabelFontSize,
          interval: 0,
        },
      }],
      yAxis: [{
        type: isHorizontal ? 'category' : 'value',
        data: isHorizontal ? categories : undefined,
        show: props.yAxisShow,
        axisLine: { show: false },
        axisTick: { show: false },
        axisLabel: { color: '#fff', fontSize: 14 },
        splitLine: isHorizontal ? undefined : {
          show: props.yAxisSplitLineShow,
          lineStyle: { color: props.yAxisSplitLineColor, type: 'dashed' },
        },
      }],
      series: [{
        type: 'bar',
        name: '数据',
        data: values,
        barWidth: props.barWidth,
        itemStyle: {
          color: props.barColors?.length > 0
            ? convertColor(props.barColors[0])
            : convertColor({
              type: 'linear',
              x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: '#00D9FF' },
                { offset: 1, color: '#0066FF' },
              ],
            }),
          borderRadius: Array.isArray(props.barBorderRadius)
            ? props.barBorderRadius
            : [props.barBorderRadius, props.barBorderRadius, 0, 0],
        },
        label: {
          show: props.showLabel,
          position: 'top',
          color: props.labelColor,
          fontSize: props.labelFontSize,
        },
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(0, 0, 0, 0.5)',
          },
        },
      }],
    };

    chart.value.setOption(option, true);
  } catch (error) {
    console.error('初始化图表失败:', error);
  }
};

// 监听配置变化
watch(
  () => [
    props.chartData,
    props.chartOrientation,
    props.barWidth,
    props.barBorderRadius,
    props.barColors,
    props.xAxisShow,
    props.xAxisLineColor,
    props.xAxisLabelColor,
    props.xAxisLabelFontSize,
    props.yAxisShow,
    props.yAxisSplitLineShow,
    props.yAxisSplitLineColor,
    props.showLabel,
    props.labelColor,
    props.labelFontSize,
    props.showTooltip,
    props.tooltipBackgroundColor,
    props.gridTop,
    props.gridBottom,
    props.gridLeft,
    props.gridRight,
  ],
  () => { setTimeout(() => initChart(), 500); },
  { deep: true }
);

// 窗口大小变化时重新渲染
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
.multi-bar-chart {
  width: 100%;
  height: 100%;
}
</style>
```

---

## 二、地图组件完整模板

### index.vue 核心结构
```vue
<template>
  <div id="map" ref="chartRef" class="point-map"></div>
</template>

<script setup>
import { defineProps, defineExpose, ref, watch, onUnmounted, onMounted, provide } from 'vue';
import AMapLoader from '@amap/amap-jsapi-loader';
import i18n from './locale/index';

const props = defineProps({
  // 地图数据
  dynamicData: {
    type: Object,
    default: () => ({
      points: [
        { name: '点位1', value: [119.418678, 26.812159], introduction: '描述信息' },
      ],
    }),
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  // 地图中心点
  mapCenter: {
    type: Array,
    default: () => [119.55451, 26.672242],
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 2,
    configurationTemplate: () => import('./components/MapCenter.vue'),
  },

  // 地图缩放等级
  mapZoom: {
    type: Number,
    default: 9,
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 3,
    configurationTemplate: () => import('./components/MapZoom.vue'),
  },
});

const chartRef = ref(null);
const chart = ref(null);

// 响应式地图状态
const currentMapCenter = ref(props.mapCenter);
const currentMapZoom = ref(props.mapZoom);

// 提供注入
provide('mapCenter', {
  mapCenter: currentMapCenter,
  setMapCenter: (center) => { currentMapCenter.value = center; },
});

provide('mapZoom', {
  mapZoom: currentMapZoom,
  setMapZoom: (zoom) => { currentMapZoom.value = zoom; },
});

// 初始化地图
const initMap = (points) => {
  AMapLoader.reset();
  AMapLoader.load({
    key: 'YOUR_AMAP_KEY',
    version: '2.0',
    Loca: { version: '2.0.0' },
    plugins: ['AMap.DistrictSearch', 'AMap.Polyline'],
  }).then((AMap) => {
    chart.value = new AMap.Map('map', {
      layers: [new AMap.TileLayer.Satellite()],
      mapStyle: 'amap://styles/whitesmoke',
      center: props.mapCenter,
      zoom: props.mapZoom,
    });

    // 监听地图事件
    chart.value.on('moveend', function() {
      const center = chart.value.getCenter();
      currentMapCenter.value = [center.lng, center.lat];
    });

    chart.value.on('zoomend', function() {
      currentMapZoom.value = chart.value.getZoom();
    });

    // 添加标记点
    points.forEach((item) => {
      const marker = new AMap.Marker({
        position: item.value,
        label: { content: item.name, direction: 'bottom' },
      });
      chart.value.add(marker);
    });
  });
};

// 监听数据变化
watch(
  () => props.dynamicData,
  (val) => {
    chart.value?.destroy();
    chart.value = null;
    initMap(val.points);
  },
  { deep: true, immediate: true }
);

// 监听中心点变化
watch(
  () => props.mapCenter,
  (val) => {
    if (chart.value && val?.length === 2) {
      chart.value.setCenter(val);
    }
  },
  { deep: true }
);

// 监听缩放变化
watch(
  () => props.mapZoom,
  (val) => {
    if (chart.value) chart.value.setZoom(val);
  }
);

onMounted(() => {
  window._AMapSecurityConfig = {
    securityJsCode: 'YOUR_SECURITY_CODE',
  };
});

onUnmounted(() => {
  chart.value?.destroy();
});

defineExpose({ chart });
</script>

<style lang="scss" scoped>
#map {
  height: 100%;
  width: 100%;
}
</style>
```

---

## 三、排名进度条组件完整模板

### index.vue 核心结构
```vue
<template>
  <div class="rank-progress-container">
    <template v-for="(item, index) in rankOptions" :key="index">
      <div class="rank-item" :style="{ marginBottom: props.marginBottom + 'px' }">
        <div class="rank-icon" :style="getRankBg(item.rowNum)">
          <span>TOP{{ item.rowNum }}</span>
        </div>
        <div class="progress-wrapper">
          <div class="label-row">
            <span class="dot"></span>
            <span class="label-text" :style="{ color: fontColor, fontSize: fontSize + 'px' }">
              {{ item.label }}
            </span>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" :style="getAnimationStyle">
              <span
                v-for="(cube, cubeIndex) in cubeCount"
                :key="cubeIndex"
                class="cube"
                :style="getCubeStyle(cubeIndex, item)"
              ></span>
            </div>
            <div class="progress-bg">
              <span
                v-for="(cube, cubeIndex) in cubeCount"
                :key="cubeIndex"
                class="cube"
                :style="getCubeBgStyle(cubeIndex)"
              ></span>
            </div>
          </div>
        </div>
        <div class="value-text" :style="{ color: fontColor, fontSize: fontSize + 'px' }">
          {{ item.value }}
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { defineProps, defineExpose, ref, computed, watch } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  dynamicData: {
    type: Array,
    default: () => [
      { label: '项目A', value: 9970, rowNum: 1, percent: '90%' },
      { label: '项目B', value: 8656, rowNum: 2, percent: '77%' },
      { label: '项目C', value: 8519, rowNum: 3, percent: '75%' },
    ],
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  cubeColor: {
    type: String,
    default: '#01AFFF',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
    configurationTemplate: () => import('./components/CubeColor.vue'),
  },

  cubeCount: {
    type: Number,
    default: 25,
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
    configurationTemplate: () => import('./components/CubeCount.vue'),
  },

  cubeSize: {
    type: Number,
    default: 6,
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
    configurationTemplate: () => import('./components/CubeSize.vue'),
  },

  marginBottom: {
    type: Number,
    default: 14,
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
    configurationTemplate: () => import('./components/MarginBottom.vue'),
  },

  openAnimate: {
    type: Boolean,
    default: true,
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 6,
    configurationTemplate: () => import('./components/OpenAnimate.vue'),
  },

  animateDuration: {
    type: Number,
    default: 5000,
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 7,
    configurationTemplate: () => import('./components/AnimateDuration.vue'),
  },
});

const fontColor = ref('#fff');
const fontSize = ref('14');
const rankOptions = ref([]);

// 动画样式
const getAnimationStyle = computed(() => {
  const duration = props.animateDuration / 1000;
  const count = props.openAnimate ? 'infinite' : 0;
  return {
    animationDuration: duration * 2 + 's',
    animationIterationCount: count,
  };
});

// 排名背景
const getRankBg = (index) => {
  const images = {
    1: require('./static/img/red.png'),
    2: require('./static/img/yellow.png'),
    3: require('./static/img/blue.png'),
  };
  return {
    background: `url(${images[index] || images[3]})`,
    backgroundSize: '100% 100%',
    backgroundRepeat: 'no-repeat',
  };
};

// 方块样式
const getCubeStyle = (index, data) => {
  const percent = parseFloat(data.percent) / 100;
  const nowCubeCount = Math.floor(props.cubeCount * percent);
  let background = 'RGBA(255,255,255,.0)';

  if (index <= nowCubeCount) {
    background = props.cubeColor;
  }

  return {
    marginLeft: index === 0 ? '2px' : '0',
    marginRight: '3px',
    width: props.cubeSize * 2 + 'px',
    transform: 'skew(45deg)',
    background,
  };
};

// 背景方块样式
const getCubeBgStyle = (index) => ({
  marginLeft: index === 0 ? '2px' : '0',
  marginRight: '3px',
  width: props.cubeSize * 2 + 'px',
  transform: 'skew(45deg)',
  background: 'RGBA(1, 49, 48, 1)',
});

// 监听数据变化
watch(
  () => props.dynamicData,
  (val) => { rankOptions.value = val; },
  { deep: true, immediate: true }
);

defineExpose({ rankOptions });
</script>

<style lang="scss" scoped>
.rank-progress-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.rank-item {
  display: flex;
  align-items: center;
  max-height: 42px;
  width: 100%;
}

.rank-icon {
  width: 46px;
  height: 18px;
  font-size: 13px;
  margin-right: 12px;
}

.progress-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 0 2px;
}

.label-row {
  display: flex;
  align-items: center;
  margin-bottom: 3px;
  height: 22px;
}

.dot {
  width: 4px;
  height: 4px;
  background: rgba(1, 175, 255, 0.5);
  margin-right: 6px;
}

.label-text {
  color: #fff;
  font-size: 14px;
}

.progress-bar {
  position: relative;
  width: 100%;
  height: 14px;
  overflow: hidden;
  clip-path: polygon(0 0, calc(100% - 17px) 0, 100% 100%, 0% 100%);
  border: 1px solid rgba(151, 151, 151, 1);
}

.progress-fill {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  z-index: 100;
  animation: progressAni;
}

.progress-bg {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
}

.cube {
  display: inline-block;
}

.value-text {
  margin-left: 40px;
  font-size: 14px;
  color: #fff;
}

@keyframes progressAni {
  0% { clip-path: inset(0 100% 0 0); }
  50% { clip-path: inset(0 0% 0 0); }
}
</style>
```

---

## 四、配置面板组件模板

### 颜色选择器 (ColorPicker.vue)
```vue
<template>
  <CommonLayout title="颜色选择">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-color-picker v-model="localValue" show-alpha />
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>

<script setup>
import { inject, ref, watch } from 'vue';
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';

const { colorValue, setColorValue } = inject('colorValue');
const localValue = ref(colorValue.value);

watch(() => colorValue.value, (val) => { localValue.value = val; }, { immediate: true });
watch(localValue, (val) => { setColorValue(val); });
</script>
```

### 数值输入 (NumberInput.vue)
```vue
<template>
  <CommonLayout :title="title">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-input-number
            v-model="localValue"
            :min="min"
            :max="max"
            :step="step"
            style="width: 100%"
          />
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>

<script setup>
import { inject, ref, watch } from 'vue';
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';

const props = defineProps({
  title: { type: String, default: '数值配置' },
  min: { type: Number, default: 0 },
  max: { type: Number, default: 100 },
  step: { type: Number, default: 1 },
  injectKey: { type: String, required: true },
});

const { [props.injectKey]: value, [`set${props.injectKey.charAt(0).toUpperCase() + props.injectKey.slice(1)}`]: setValue } = inject(props.injectKey);
const localValue = ref(value.value);

watch(() => value.value, (val) => { localValue.value = val; }, { immediate: true });
watch(localValue, (val) => { setValue(val); });
</script>
```

### 选择器 (SelectOption.vue)
```vue
<template>
  <CommonLayout :title="title">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-select v-model="localValue" style="width: 100%">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>

<script setup>
import { inject, ref, watch } from 'vue';
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';

const props = defineProps({
  title: { type: String, default: '选项配置' },
  options: { type: Array, default: () => [] },
  injectKey: { type: String, required: true },
});

const { [props.injectKey]: value, [`set${props.injectKey.charAt(0).toUpperCase() + props.injectKey.slice(1)}`]: setValue } = inject(props.injectKey);
const localValue = ref(value.value);

watch(() => value.value, (val) => { localValue.value = val; }, { immediate: true });
watch(localValue, (val) => { setValue(val); });
</script>
```

### 开关配置 (SwitchOption.vue)
```vue
<template>
  <CommonLayout :title="title">
    <template v-slot:content>
      <CommonContent>
        <template v-slot:content-detail>
          <el-switch v-model="localValue" />
        </template>
      </CommonContent>
    </template>
  </CommonLayout>
</template>

<script setup>
import { inject, ref, watch } from 'vue';
import CommonLayout from '@/pages/digital/digital-setting/components/common/CommonLayout.vue';
import CommonContent from '@/pages/digital/digital-setting/components/common/CommonContent.vue';

const props = defineProps({
  title: { type: String, default: '开关配置' },
  injectKey: { type: String, required: true },
});

const { [props.injectKey]: value, [`set${props.injectKey.charAt(0).toUpperCase() + props.injectKey.slice(1)}`]: setValue } = inject(props.injectKey);
const localValue = ref(value.value);

watch(() => value.value, (val) => { localValue.value = val; }, { immediate: true });
watch(localValue, (val) => { setValue(val); });
</script>
```

---

## 五、饼图组件完整模板

### index.vue 核心结构（支持环形图、玫瑰图）
```vue
<template>
  <div ref="chartRef" class="pie-chart"></div>
</template>

<script setup>
import { markRaw, defineProps, defineExpose, ref, watch, onUnmounted, onMounted } from 'vue';
import * as echarts from 'echarts';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  chartData: {
    type: Array,
    default: () => [
      { name: '类别A', value: 1048 },
      { name: '类别B', value: 735 },
      { name: '类别C', value: 580 },
      { name: '类别D', value: 484 },
      { name: '类别E', value: 300 },
    ],
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  // ========== 样式配置 ==========
  pieType: {
    type: String,
    default: 'ring', // 'ring' | 'rose' | 'solid'
    desc: '饼图类型',
    name: '饼图类型',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
    configurationTemplate: () => import('./components/PieType.vue'),
  },

  innerRadius: {
    type: Number,
    default: 50,
    desc: '内半径百分比（环形图有效）',
    name: '内半径',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
    min: 0,
    max: 80,
    configurationTemplate: () => import('./components/InnerRadius.vue'),
  },

  outerRadius: {
    type: Number,
    default: 70,
    desc: '外半径百分比',
    name: '外半径',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
    min: 30,
    max: 100,
  },

  colors: {
    type: Array,
    default: () => ['#00D9FF', '#0066FF', '#FF6B6B', '#4ECDC4', '#FFE66D'],
    desc: '颜色序列',
    name: '颜色序列',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
    configurationTemplate: () => import('./components/Colors.vue'),
  },

  showLabel: {
    type: Boolean,
    default: true,
    desc: '是否显示标签',
    name: '显示标签',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 10,
  },

  labelPosition: {
    type: String,
    default: 'outside', // 'outside' | 'inside' | 'center'
    desc: '标签位置',
    name: '标签位置',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 11,
    configurationTemplate: () => import('./components/LabelPosition.vue'),
  },

  labelFontSize: {
    type: Number,
    default: 14,
    desc: '标签字号',
    name: '标签字号',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 12,
    min: 10,
    max: 30,
  },

  showLegend: {
    type: Boolean,
    default: true,
    desc: '是否显示图例',
    name: '显示图例',
    groupKey: 'style',
    groupName: '图例配置',
    sort: 20,
  },

  legendPosition: {
    type: String,
    default: 'bottom', // 'top' | 'bottom' | 'left' | 'right'
    desc: '图例位置',
    name: '图例位置',
    groupKey: 'style',
    groupName: '图例配置',
    sort: 21,
    configurationTemplate: () => import('./components/LegendPosition.vue'),
  },
});

const chartRef = ref(null);
const chart = ref(null);

const initChart = () => {
  if (!chartRef.value) return;

  try {
    if (chart.value) chart.value.dispose();
    chart.value = markRaw(echarts.init(chartRef.value));

    const isRose = props.pieType === 'rose';
    const isRing = props.pieType === 'ring';

    const legendOrient = ['left', 'right'].includes(props.legendPosition) ? 'vertical' : 'horizontal';
    const legendPos = {
      top: props.legendPosition === 'top' ? 'top' : props.legendPosition === 'bottom' ? 'bottom' : 'middle',
      left: props.legendPosition === 'left' ? 'left' : props.legendPosition === 'right' ? 'right' : 'center',
    };

    const option = {
      backgroundColor: 'transparent',
      tooltip: {
        trigger: 'item',
        confine: true,
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        borderColor: '#333',
        textStyle: { color: '#fff', fontSize: 14 },
      },
      legend: {
        show: props.showLegend,
        orient: legendOrient,
        top: legendPos.top,
        left: legendPos.left,
        textStyle: { color: '#fff', fontSize: 12 },
      },
      color: props.colors,
      series: [{
        type: 'pie',
        radius: isRing
          ? [`${props.innerRadius}%`, `${props.outerRadius}%`]
          : [0, `${props.outerRadius}%`],
        center: ['50%', '50%'],
        roseType: isRose ? 'area' : false,
        itemStyle: {
          borderRadius: 6,
          borderColor: 'rgba(0, 0, 0, 0.3)',
          borderWidth: 2,
        },
        label: {
          show: props.showLabel,
          position: props.labelPosition,
          color: '#fff',
          fontSize: props.labelFontSize,
          formatter: '{b}: {d}%',
        },
        labelLine: {
          show: props.showLabel && props.labelPosition === 'outside',
          lineStyle: { color: 'rgba(255, 255, 255, 0.3)' },
        },
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)',
          },
        },
        data: props.chartData,
      }],
    };

    chart.value.setOption(option, true);
  } catch (error) {
    console.error('初始化饼图失败:', error);
  }
};

watch(
  () => [props.chartData, props.pieType, props.innerRadius, props.outerRadius, props.colors, props.showLabel, props.labelPosition, props.labelFontSize, props.showLegend, props.legendPosition],
  () => { setTimeout(() => initChart(), 500); },
  { deep: true }
);

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
.pie-chart {
  width: 100%;
  height: 100%;
}
</style>
```

---

## 六、折线图组件完整模板

### index.vue 核心结构（支持多折线、面积图）
```vue
<template>
  <div ref="chartRef" class="line-chart"></div>
</template>

<script setup>
import { markRaw, defineProps, defineExpose, ref, watch, onUnmounted, onMounted } from 'vue';
import * as echarts from 'echarts';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  chartData: {
    type: Object,
    default: () => ({
      categories: ['1月', '2月', '3月', '4月', '5月', '6月'],
      series: [
        { name: '系列A', data: [120, 132, 101, 134, 90, 230] },
        { name: '系列B', data: [220, 182, 191, 234, 290, 330] },
      ],
    }),
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  // ========== 样式配置 ==========
  showArea: {
    type: Boolean,
    default: false,
    desc: '是否显示面积',
    name: '显示面积',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
    configurationTemplate: () => import('./components/ShowArea.vue'),
  },

  smooth: {
    type: Boolean,
    default: true,
    desc: '是否平滑曲线',
    name: '平滑曲线',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
    configurationTemplate: () => import('./components/Smooth.vue'),
  },

  lineColors: {
    type: Array,
    default: () => ['#00D9FF', '#0066FF', '#FF6B6B', '#4ECDC4'],
    desc: '线条颜色序列',
    name: '线条颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
    configurationTemplate: () => import('./components/LineColors.vue'),
  },

  lineWidth: {
    type: Number,
    default: 2,
    desc: '线条宽度',
    name: '线条宽度',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
    min: 1,
    max: 10,
  },

  showSymbol: {
    type: Boolean,
    default: true,
    desc: '是否显示数据点',
    name: '显示数据点',
    groupKey: 'style',
    groupName: '数据点配置',
    sort: 10,
  },

  symbolSize: {
    type: Number,
    default: 6,
    desc: '数据点大小',
    name: '数据点大小',
    groupKey: 'style',
    groupName: '数据点配置',
    sort: 11,
    min: 2,
    max: 20,
  },

  // X轴配置
  xAxisLineColor: {
    type: String,
    default: 'rgba(255, 255, 255, 0.2)',
    desc: 'X轴线颜色',
    name: 'X轴线颜色',
    groupKey: 'style',
    groupName: 'X轴配置',
    sort: 20,
  },

  xAxisLabelColor: {
    type: String,
    default: '#ffffff',
    desc: 'X轴标签颜色',
    name: 'X轴标签颜色',
    groupKey: 'style',
    groupName: 'X轴配置',
    sort: 21,
  },

  // Y轴配置
  yAxisSplitLineShow: {
    type: Boolean,
    default: true,
    desc: '是否显示Y轴分割线',
    name: '显示分割线',
    groupKey: 'style',
    groupName: 'Y轴配置',
    sort: 30,
  },

  yAxisSplitLineColor: {
    type: String,
    default: 'rgba(255, 255, 255, 0.1)',
    desc: 'Y轴分割线颜色',
    name: '分割线颜色',
    groupKey: 'style',
    groupName: 'Y轴配置',
    sort: 31,
  },

  // 网格配置
  gridTop: { type: Number, default: 60 },
  gridBottom: { type: Number, default: 60 },
  gridLeft: { type: Number, default: 60 },
  gridRight: { type: Number, default: 60 },
});

const chartRef = ref(null);
const chart = ref(null);

const convertColor = (colorConfig) => {
  if (typeof colorConfig === 'string') return colorConfig;
  if (colorConfig.type === 'linear') {
    return new echarts.graphic.LinearGradient(
      colorConfig.x || 0, colorConfig.y || 0,
      colorConfig.x2 || 0, colorConfig.y2 || 1,
      colorConfig.colorStops || []
    );
  }
  return colorConfig;
};

const initChart = () => {
  if (!chartRef.value) return;

  try {
    if (chart.value) chart.value.dispose();
    chart.value = markRaw(echarts.init(chartRef.value));

    const categories = props.chartData?.categories || [];
    const seriesData = props.chartData?.series || [];

    const series = seriesData.map((item, index) => {
      const color = props.lineColors[index % props.lineColors.length];
      return {
        name: item.name,
        type: 'line',
        data: item.data,
        smooth: props.smooth,
        showSymbol: props.showSymbol,
        symbolSize: props.symbolSize,
        lineStyle: {
          width: props.lineWidth,
          color: color,
        },
        areaStyle: props.showArea ? {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: color + '80' },
            { offset: 1, color: color + '10' },
          ]),
        } : undefined,
        itemStyle: { color: color },
      };
    });

    const option = {
      backgroundColor: 'transparent',
      tooltip: {
        trigger: 'axis',
        confine: true,
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        borderColor: '#333',
        textStyle: { color: '#fff', fontSize: 14 },
      },
      legend: {
        textStyle: { color: '#fff', fontSize: 12 },
        top: 10,
      },
      grid: {
        top: props.gridTop,
        bottom: props.gridBottom,
        left: props.gridLeft,
        right: props.gridRight,
        containLabel: true,
      },
      xAxis: [{
        type: 'category',
        data: categories,
        boundaryGap: false,
        axisLine: { lineStyle: { color: props.xAxisLineColor } },
        axisTick: { show: false },
        axisLabel: { color: props.xAxisLabelColor, fontSize: 12 },
      }],
      yAxis: [{
        type: 'value',
        axisLine: { show: false },
        axisTick: { show: false },
        axisLabel: { color: '#fff', fontSize: 12 },
        splitLine: {
          show: props.yAxisSplitLineShow,
          lineStyle: { color: props.yAxisSplitLineColor, type: 'dashed' },
        },
      }],
      series,
    };

    chart.value.setOption(option, true);
  } catch (error) {
    console.error('初始化折线图失败:', error);
  }
};

watch(
  () => [props.chartData, props.showArea, props.smooth, props.lineColors, props.lineWidth, props.showSymbol, props.symbolSize],
  () => { setTimeout(() => initChart(), 500); },
  { deep: true }
);

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
.line-chart {
  width: 100%;
  height: 100%;
}
</style>
```

---

## 七、雷达图组件完整模板

### index.vue 核心结构
```vue
<template>
  <div ref="chartRef" class="radar-chart"></div>
</template>

<script setup>
import { markRaw, defineProps, defineExpose, ref, watch, onUnmounted, onMounted } from 'vue';
import * as echarts from 'echarts';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  chartData: {
    type: Object,
    default: () => ({
      indicators: [
        { name: '销售', max: 100 },
        { name: '管理', max: 100 },
        { name: '信息技术', max: 100 },
        { name: '客服', max: 100 },
        { name: '研发', max: 100 },
        { name: '市场', max: 100 },
      ],
      series: [
        { name: '预算分配', value: [60, 73, 85, 40, 90, 88] },
        { name: '实际开销', value: [80, 50, 95, 60, 85, 70] },
      ],
    }),
    desc: i18n.global.t('dataSpecification'),
    name: i18n.global.t('displayContent'),
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  // ========== 样式配置 ==========
  shape: {
    type: String,
    default: 'polygon', // 'polygon' | 'circle'
    desc: '雷达图形状',
    name: '形状',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
    configurationTemplate: () => import('./components/RadarShape.vue'),
  },

  areaColors: {
    type: Array,
    default: () => [
      { fill: 'rgba(0, 217, 255, 0.3)', stroke: '#00D9FF' },
      { fill: 'rgba(0, 102, 255, 0.3)', stroke: '#0066FF' },
    ],
    desc: '区域颜色配置',
    name: '区域颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
    configurationTemplate: () => import('./components/AreaColors.vue'),
  },

  splitNumber: {
    type: Number,
    default: 5,
    desc: '分割层数',
    name: '分割层数',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
    min: 3,
    max: 10,
  },

  axisLineColor: {
    type: String,
    default: 'rgba(255, 255, 255, 0.3)',
    desc: '轴线颜色',
    name: '轴线颜色',
    groupKey: 'style',
    groupName: '轴配置',
    sort: 10,
  },

  splitLineColor: {
    type: String,
    default: 'rgba(255, 255, 255, 0.1)',
    desc: '分割线颜色',
    name: '分割线颜色',
    groupKey: 'style',
    groupName: '轴配置',
    sort: 11,
  },

  splitAreaColors: {
    type: Array,
    default: () => ['rgba(255, 255, 255, 0.05)', 'rgba(255, 255, 255, 0.1)'],
    desc: '分割区域颜色',
    name: '分割区域颜色',
    groupKey: 'style',
    groupName: '轴配置',
    sort: 12,
  },

  labelColor: {
    type: String,
    default: '#ffffff',
    desc: '标签颜色',
    name: '标签颜色',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 20,
  },

  labelFontSize: {
    type: Number,
    default: 12,
    desc: '标签字号',
    name: '标签字号',
    groupKey: 'style',
    groupName: '标签配置',
    sort: 21,
    min: 10,
    max: 24,
  },
});

const chartRef = ref(null);
const chart = ref(null);

const initChart = () => {
  if (!chartRef.value) return;

  try {
    if (chart.value) chart.value.dispose();
    chart.value = markRaw(echarts.init(chartRef.value));

    const indicators = props.chartData?.indicators || [];
    const seriesData = props.chartData?.series || [];

    const series = seriesData.map((item, index) => {
      const colorConfig = props.areaColors[index % props.areaColors.length];
      return {
        name: item.name,
        value: item.value,
        areaStyle: { color: colorConfig.fill },
        lineStyle: { color: colorConfig.stroke, width: 2 },
        itemStyle: { color: colorConfig.stroke },
      };
    });

    const option = {
      backgroundColor: 'transparent',
      tooltip: {
        trigger: 'item',
        confine: true,
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        borderColor: '#333',
        textStyle: { color: '#fff', fontSize: 14 },
      },
      legend: {
        textStyle: { color: '#fff', fontSize: 12 },
        bottom: 10,
      },
      radar: {
        indicator: indicators,
        shape: props.shape,
        splitNumber: props.splitNumber,
        axisName: {
          color: props.labelColor,
          fontSize: props.labelFontSize,
        },
        axisLine: {
          lineStyle: { color: props.axisLineColor },
        },
        splitLine: {
          lineStyle: { color: props.splitLineColor },
        },
        splitArea: {
          areaStyle: {
            color: props.splitAreaColors,
          },
        },
      },
      series: [{
        type: 'radar',
        data: series,
      }],
    };

    chart.value.setOption(option, true);
  } catch (error) {
    console.error('初始化雷达图失败:', error);
  }
};

watch(
  () => [props.chartData, props.shape, props.areaColors, props.splitNumber, props.axisLineColor, props.splitLineColor, props.labelColor, props.labelFontSize],
  () => { setTimeout(() => initChart(), 500); },
  { deep: true }
);

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
.radar-chart {
  width: 100%;
  height: 100%;
}
</style>
```

---

## 八、文本组件模板

### 8.1 标题组件 (TitleText)
```vue
<template>
  <div class="title-container" :style="containerStyle">
    <div class="title-text" :style="textStyle">{{ text }}</div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  text: {
    type: String,
    default: '大屏标题',
    desc: '标题文本',
    name: '标题文本',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  fontSize: {
    type: Number,
    default: 32,
    desc: '字体大小',
    name: '字体大小',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
    min: 12,
    max: 72,
    configurationTemplate: () => import('./components/FontSize.vue'),
  },

  fontColor: {
    type: String,
    default: '#ffffff',
    desc: '字体颜色',
    name: '字体颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
    configurationTemplate: () => import('./components/FontColor.vue'),
  },

  fontWeight: {
    type: String,
    default: 'bold',
    desc: '字体粗细',
    name: '字体粗细',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
    configurationTemplate: () => import('./components/FontWeight.vue'),
  },

  textAlign: {
    type: String,
    default: 'center',
    desc: '文本对齐',
    name: '文本对齐',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
    configurationTemplate: () => import('./components/TextAlign.vue'),
  },

  textShadow: {
    type: Boolean,
    default: true,
    desc: '是否显示文字阴影',
    name: '文字阴影',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 6,
  },

  shadowColor: {
    type: String,
    default: 'rgba(0, 217, 255, 0.8)',
    desc: '阴影颜色',
    name: '阴影颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 7,
  },

  background: {
    type: String,
    default: 'linear-gradient(90deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 102, 255, 0.1) 100%)',
    desc: '背景样式',
    name: '背景样式',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 10,
  },
});

const containerStyle = computed(() => ({
  background: props.background,
  textAlign: props.textAlign,
}));

const textStyle = computed(() => ({
  fontSize: props.fontSize + 'px',
  color: props.fontColor,
  fontWeight: props.fontWeight,
  textShadow: props.textShadow ? `0 0 10px ${props.shadowColor}, 0 0 20px ${props.shadowColor}` : 'none',
}));
</script>

<style lang="scss" scoped>
.title-container {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 20px;
}

.title-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
```

### 8.2 时间显示组件 (DateTimeDisplay)
```vue
<template>
  <div class="datetime-container">
    <div v-if="showDate" class="date-text" :style="dateStyle">{{ dateText }}</div>
    <div v-if="showTime" class="time-text" :style="timeStyle">{{ timeText }}</div>
    <div v-if="showWeek" class="week-text" :style="weekStyle">{{ weekText }}</div>
  </div>
</template>

<script setup>
import { defineProps, ref, computed, watch, onUnmounted } from 'vue';
import dayjs from 'dayjs';
import i18n from './locale/index';

const props = defineProps({
  showDate: {
    type: Boolean,
    default: true,
    desc: '显示日期',
    name: '显示日期',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 1,
  },

  showTime: {
    type: Boolean,
    default: true,
    desc: '显示时间',
    name: '显示时间',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
  },

  showWeek: {
    type: Boolean,
    default: false,
    desc: '显示星期',
    name: '显示星期',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
  },

  dateFormat: {
    type: String,
    default: 'YYYY-MM-DD',
    desc: '日期格式',
    name: '日期格式',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
    configurationTemplate: () => import('./components/DateFormat.vue'),
  },

  timeFormat: {
    type: String,
    default: 'HH:mm:ss',
    desc: '时间格式',
    name: '时间格式',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
  },

  fontSize: {
    type: Number,
    default: 24,
    desc: '字体大小',
    name: '字体大小',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 10,
    min: 12,
    max: 72,
  },

  fontColor: {
    type: String,
    default: '#00D9FF',
    desc: '字体颜色',
    name: '字体颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 11,
  },

  layout: {
    type: String,
    default: 'horizontal', // 'horizontal' | 'vertical'
    desc: '布局方向',
    name: '布局方向',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 20,
  },

  separator: {
    type: String,
    default: ' ',
    desc: '日期时间分隔符',
    name: '分隔符',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 21,
  },
});

const dateText = ref('');
const timeText = ref('');
const weekText = ref('');
const timer = ref(null);

const weekDays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];

const updateDateTime = () => {
  const now = dayjs();
  if (props.showDate) {
    dateText.value = now.format(props.dateFormat);
  }
  if (props.showTime) {
    timeText.value = now.format(props.timeFormat);
  }
  if (props.showWeek) {
    weekText.value = weekDays[now.day()];
  }
};

const dateStyle = computed(() => ({
  fontSize: props.fontSize + 'px',
  color: props.fontColor,
}));

const timeStyle = computed(() => ({
  fontSize: props.fontSize + 'px',
  color: props.fontColor,
}));

const weekStyle = computed(() => ({
  fontSize: (props.fontSize * 0.8) + 'px',
  color: props.fontColor,
}));

watch(
  () => [props.showDate, props.showTime, props.showWeek, props.dateFormat, props.timeFormat],
  () => {
    clearInterval(timer.value);
    updateDateTime();
    timer.value = setInterval(updateDateTime, 1000);
  },
  { immediate: true }
);

onUnmounted(() => {
  clearInterval(timer.value);
});
</script>

<style lang="scss" scoped>
.datetime-container {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  &[data-layout="vertical"] {
    flex-direction: column;
  }
}
</style>
```

### 8.3 跑马灯组件 (MarqueeText)
```vue
<template>
  <div class="marquee-container" ref="containerRef">
    <div class="marquee-content" ref="contentRef" :style="contentStyle">
      <span class="text" :style="textStyle">{{ text }}</span>
      <span v-if="needScroll" class="text" :style="textStyle">{{ text }}</span>
    </div>
  </div>
</template>

<script setup>
import { defineProps, ref, computed, watch, onMounted, onUnmounted } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  text: {
    type: String,
    default: '这是一条跑马灯滚动文本，用于展示公告或重要信息。',
    desc: '滚动文本',
    name: '滚动文本',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  speed: {
    type: Number,
    default: 50,
    desc: '滚动速度（像素/秒）',
    name: '滚动速度',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 2,
    min: 10,
    max: 200,
    configurationTemplate: () => import('./components/ScrollSpeed.vue'),
  },

  fontSize: {
    type: Number,
    default: 16,
    desc: '字体大小',
    name: '字体大小',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
    min: 12,
    max: 48,
  },

  fontColor: {
    type: String,
    default: '#ffffff',
    desc: '字体颜色',
    name: '字体颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
  },

  direction: {
    type: String,
    default: 'left', // 'left' | 'right'
    desc: '滚动方向',
    name: '滚动方向',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
  },

  pauseOnHover: {
    type: Boolean,
    default: true,
    desc: '悬停暂停',
    name: '悬停暂停',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 6,
  },
});

const containerRef = ref(null);
const contentRef = ref(null);
const needScroll = ref(false);
const animationId = ref(null);

const textStyle = computed(() => ({
  fontSize: props.fontSize + 'px',
  color: props.fontColor,
  whiteSpace: 'nowrap',
  display: 'inline-block',
  padding: '0 50px',
}));

const contentStyle = computed(() => ({
  display: 'flex',
  animationPlayState: 'paused',
}));

const checkScroll = () => {
  if (!containerRef.value || !contentRef.value) return;
  const containerWidth = containerRef.value.offsetWidth;
  const textWidth = contentRef.value.querySelector('.text')?.offsetWidth || 0;
  needScroll.value = textWidth > containerWidth;
};

const startAnimation = () => {
  if (!needScroll.value || !contentRef.value) return;

  const textEl = contentRef.value.querySelector('.text');
  if (!textEl) return;

  const textWidth = textEl.offsetWidth;
  const duration = (textWidth * 2) / props.speed;

  contentRef.value.style.animation = `marquee-${props.direction} ${duration}s linear infinite`;
};

watch(
  () => [props.text, props.speed, props.direction],
  () => {
    checkScroll();
    startAnimation();
  },
  { immediate: true }
);

onMounted(() => {
  checkScroll();
  startAnimation();
  window.addEventListener('resize', checkScroll);
});

onUnmounted(() => {
  window.removeEventListener('resize', checkScroll);
});
</script>

<style lang="scss" scoped>
.marquee-container {
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.marquee-content {
  display: flex;
}

@keyframes marquee-left {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

@keyframes marquee-right {
  0% { transform: translateX(-50%); }
  100% { transform: translateX(0); }
}
</style>
```

---

## 九、数据卡片组件模板

### 9.1 数字翻牌器组件 (NumberFlipCard)
```vue
<template>
  <div class="flip-card-container">
    <div v-if="showTitle" class="card-title" :style="titleStyle">{{ title }}</div>
    <div class="number-wrapper">
      <div v-for="(digit, index) in displayDigits" :key="index" class="digit-box" :style="digitBoxStyle">
        <span class="digit" :style="digitStyle">{{ digit }}</span>
      </div>
      <div v-if="suffix" class="suffix" :style="suffixStyle">{{ suffix }}</div>
    </div>
    <div v-if="showTrend" class="trend" :style="trendStyle">
      <span :class="trendClass">{{ trendText }}</span>
    </div>
  </div>
</template>

<script setup>
import { defineProps, ref, computed, watch, onMounted } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  value: {
    type: Number,
    default: 12345,
    desc: '数值',
    name: '数值',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 1,
  },

  title: {
    type: String,
    default: '数据统计',
    desc: '标题',
    name: '标题',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 2,
  },

  showTitle: {
    type: Boolean,
    default: true,
    desc: '显示标题',
    name: '显示标题',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 3,
  },

  suffix: {
    type: String,
    default: '',
    desc: '后缀（单位）',
    name: '单位',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 4,
  },

  digitCount: {
    type: Number,
    default: 6,
    desc: '数字位数',
    name: '数字位数',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 5,
    min: 1,
    max: 12,
  },

  digitFontSize: {
    type: Number,
    default: 36,
    desc: '数字字号',
    name: '数字字号',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 10,
    min: 16,
    max: 72,
  },

  digitColor: {
    type: String,
    default: '#00D9FF',
    desc: '数字颜色',
    name: '数字颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 11,
  },

  digitBgColor: {
    type: String,
    default: 'rgba(0, 0, 0, 0.3)',
    desc: '数字背景色',
    name: '数字背景色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 12,
  },

  titleFontSize: {
    type: Number,
    default: 16,
    desc: '标题字号',
    name: '标题字号',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 20,
  },

  titleColor: {
    type: String,
    default: '#ffffff',
    desc: '标题颜色',
    name: '标题颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 21,
  },

  showTrend: {
    type: Boolean,
    default: false,
    desc: '显示趋势',
    name: '显示趋势',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 30,
  },

  trendValue: {
    type: Number,
    default: 0,
    desc: '趋势值（正数上升，负数下降）',
    name: '趋势值',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 3,
  },

  animation: {
    type: Boolean,
    default: true,
    desc: '数字滚动动画',
    name: '滚动动画',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 40,
  },

  animationDuration: {
    type: Number,
    default: 2000,
    desc: '动画时长（毫秒）',
    name: '动画时长',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 41,
  },
});

const currentValue = ref(0);
const displayDigits = ref([]);

const titleStyle = computed(() => ({
  fontSize: props.titleFontSize + 'px',
  color: props.titleColor,
}));

const digitBoxStyle = computed(() => ({
  background: props.digitBgColor,
  borderRadius: '4px',
  margin: '0 2px',
}));

const digitStyle = computed(() => ({
  fontSize: props.digitFontSize + 'px',
  color: props.digitColor,
  fontWeight: 'bold',
}));

const suffixStyle = computed(() => ({
  fontSize: (props.digitFontSize * 0.5) + 'px',
  color: props.digitColor,
  marginLeft: '8px',
}));

const trendStyle = computed(() => ({
  fontSize: (props.titleFontSize * 0.9) + 'px',
}));

const trendClass = computed(() => ({
  'trend-up': props.trendValue > 0,
  'trend-down': props.trendValue < 0,
}));

const trendText = computed(() => {
  if (props.trendValue > 0) return `↑ ${props.trendValue}%`;
  if (props.trendValue < 0) return `↓ ${Math.abs(props.trendValue)}%`;
  return '— 0%';
});

const formatDigits = (num) => {
  const str = String(Math.abs(num)).padStart(props.digitCount, '0');
  return str.split('').slice(-props.digitCount);
};

const animateValue = (start, end, duration) => {
  if (!props.animation) {
    currentValue.value = end;
    displayDigits.value = formatDigits(end);
    return;
  }

  const startTime = performance.now();
  const animate = (currentTime) => {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easeProgress = 1 - Math.pow(1 - progress, 3); // easeOutCubic
    currentValue.value = Math.floor(start + (end - start) * easeProgress);
    displayDigits.value = formatDigits(currentValue.value);

    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  };
  requestAnimationFrame(animate);
};

watch(
  () => props.value,
  (newVal) => {
    animateValue(currentValue.value, newVal, props.animationDuration);
  },
  { immediate: true }
);
</script>

<style lang="scss" scoped>
.flip-card-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.card-title {
  margin-bottom: 16px;
}

.number-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.digit-box {
  width: auto;
  min-width: 30px;
  height: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px 8px;
}

.digit {
  font-family: 'Orbitron', 'Digital', monospace;
}

.suffix {
  align-self: flex-end;
  margin-bottom: 8px;
}

.trend {
  margin-top: 12px;
}

.trend-up {
  color: #4ECDC4;
}

.trend-down {
  color: #FF6B6B;
}
</style>
```

### 9.2 统计卡片组件 (StatCard)
```vue
<template>
  <div class="stat-card" :style="cardStyle">
    <div class="card-icon" v-if="showIcon">
      <img v-if="iconUrl" :src="iconUrl" alt="icon" class="icon-img" />
      <div v-else class="icon-default" :style="iconStyle">{{ iconText }}</div>
    </div>
    <div class="card-content">
      <div class="card-label" :style="labelStyle">{{ label }}</div>
      <div class="card-value" :style="valueStyle">
        <span class="value-number">{{ formattedValue }}</span>
        <span v-if="unit" class="value-unit" :style="unitStyle">{{ unit }}</span>
      </div>
      <div v-if="showCompare" class="card-compare" :style="compareStyle">
        <span :class="compareClass">{{ compareText }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue';
import i18n from './locale/index';

const props = defineProps({
  label: {
    type: String,
    default: '统计项',
    desc: '标签文本',
    name: '标签文本',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 1,
  },

  value: {
    type: Number,
    default: 8888,
    desc: '数值',
    name: '数值',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    useDynamic: true,
    sort: 2,
  },

  unit: {
    type: String,
    default: '',
    desc: '单位',
    name: '单位',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 3,
  },

  showIcon: {
    type: Boolean,
    default: true,
    desc: '显示图标',
    name: '显示图标',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 10,
  },

  iconUrl: {
    type: String,
    default: '',
    desc: '图标URL',
    name: '图标URL',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 11,
  },

  iconText: {
    type: String,
    default: '📊',
    desc: '图标文字（无图标时显示）',
    name: '图标文字',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 12,
  },

  cardBgColor: {
    type: String,
    default: 'linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 102, 255, 0.1) 100%)',
    desc: '卡片背景',
    name: '卡片背景',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 20,
  },

  borderColor: {
    type: String,
    default: 'rgba(0, 217, 255, 0.3)',
    desc: '边框颜色',
    name: '边框颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 21,
  },

  labelFontSize: {
    type: Number,
    default: 14,
    desc: '标签字号',
    name: '标签字号',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 30,
  },

  labelColor: {
    type: String,
    default: 'rgba(255, 255, 255, 0.7)',
    desc: '标签颜色',
    name: '标签颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 31,
  },

  valueFontSize: {
    type: Number,
    default: 32,
    desc: '数值字号',
    name: '数值字号',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 32,
  },

  valueColor: {
    type: String,
    default: '#00D9FF',
    desc: '数值颜色',
    name: '数值颜色',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 33,
  },

  showCompare: {
    type: Boolean,
    default: false,
    desc: '显示同比/环比',
    name: '显示对比',
    groupKey: 'style',
    groupName: i18n.global.t('styleConfiguration'),
    sort: 40,
  },

  compareValue: {
    type: Number,
    default: 0,
    desc: '对比值（百分比）',
    name: '对比值',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 4,
  },

  compareType: {
    type: String,
    default: '同比', // '同比' | '环比'
    desc: '对比类型',
    name: '对比类型',
    groupKey: 'data',
    groupName: i18n.global.t('dataConfiguration'),
    sort: 5,
  },
});

const cardStyle = computed(() => ({
  background: props.cardBgColor,
  border: `1px solid ${props.borderColor}`,
}));

const iconStyle = computed(() => ({
  fontSize: '32px',
}));

const labelStyle = computed(() => ({
  fontSize: props.labelFontSize + 'px',
  color: props.labelColor,
}));

const valueStyle = computed(() => ({
  fontSize: props.valueFontSize + 'px',
  color: props.valueColor,
}));

const unitStyle = computed(() => ({
  fontSize: (props.valueFontSize * 0.4) + 'px',
  color: props.valueColor,
}));

const compareStyle = computed(() => ({
  fontSize: (props.labelFontSize * 0.9) + 'px',
}));

const formattedValue = computed(() => {
  if (props.value >= 10000) {
    return (props.value / 10000).toFixed(1) + '万';
  }
  return props.value.toLocaleString();
});

const compareClass = computed(() => ({
  'compare-up': props.compareValue > 0,
  'compare-down': props.compareValue < 0,
}));

const compareText = computed(() => {
  const prefix = props.compareValue > 0 ? '↑' : '↓';
  return `${props.compareType} ${prefix} ${Math.abs(props.compareValue)}%`;
});
</script>

<style lang="scss" scoped>
.stat-card {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.card-icon {
  flex-shrink: 0;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.icon-default {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.card-label {
  line-height: 1.4;
}

.card-value {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.value-number {
  font-weight: bold;
  font-family: 'Orbitron', 'Digital', monospace;
}

.value-unit {
  margin-left: 4px;
}

.card-compare {
  margin-top: 4px;
}

.compare-up {
  color: #4ECDC4;
}

.compare-down {
  color: #FF6B6B;
}
</style>
```

---

## DotMatrixPanel 点阵面板

深蓝科技风格面板，头部带点阵装饰纹理，适用于智慧乡村、智慧民宗等深蓝科技主题大屏。

```vue
<template>
  <div class="dot-matrix-panel" :style="panelStyle">
    <!-- 头部区域 -->
    <div class="panel-header">
      <div class="header-left">
        <!-- 点阵装饰 -->
        <div class="dot-matrix">
          <span v-for="i in 9" :key="i" class="dot"></span>
        </div>
        <!-- 图标 -->
        <div v-if="icon" class="header-icon">
          <img v-if="iconUrl" :src="iconUrl" class="icon-img" />
          <span v-else class="icon-default">{{ icon }}</span>
        </div>
        <!-- 标题 -->
        <span class="header-title">{{ title }}</span>
      </div>
      <div class="header-right">
        <slot name="header-extra"></slot>
      </div>
    </div>
    <!-- 内容区域 -->
    <div class="panel-content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  title: {
    type: String,
    default: '面板标题',
    desc: '面板标题文字',
    name: '标题',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  icon: {
    type: String,
    default: '',
    desc: '标题图标（文字或emoji）',
    name: '图标',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  iconUrl: {
    type: String,
    default: '',
    desc: '图标图片URL',
    name: '图标URL',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 3,
  },
  width: {
    type: [String, Number],
    default: '100%',
    desc: '面板宽度',
    name: '宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  height: {
    type: [String, Number],
    default: 'auto',
    desc: '面板高度',
    name: '高度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  theme: {
    type: String,
    default: 'dark',
    desc: '主题风格：dark-深蓝科技, red-党建红金, light-浅色商务',
    name: '主题',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    configurationTemplate: [
      { value: 'dark', label: '深蓝科技' },
      { value: 'red', label: '党建红金' },
      { value: 'light', label: '浅色商务' },
    ],
  },
});

const panelStyle = computed(() => ({
  width: typeof props.width === 'number' ? `${props.width}px` : props.width,
  height: typeof props.height === 'number' ? `${props.height}px` : props.height,
}));
</script>

<style lang="scss" scoped>
.dot-matrix-panel {
  background: rgba(5, 25, 55, 0.75);
  border: 1px solid var(--primary-color, #00a8e8);
  border-radius: 4px;
  overflow: hidden;

  // 深蓝科技主题
  --primary-color: #00a8e8;
  --dot-color: #00a8e8;
  --title-color: #ffffff;
  --header-bg: transparent;

  &.theme-red {
    --primary-color: #e74c3c;
    --dot-color: #ffd700;
    --title-color: #ffffff;
  }

  &.theme-light {
    background: #ffffff;
    --primary-color: #4a90e2;
    --dot-color: #4a90e2;
    --title-color: #333333;
  }
}

.panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  border-bottom: 1px solid rgba(0, 168, 232, 0.3);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.dot-matrix {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3px;
  width: 24px;

  .dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--dot-color);
    opacity: 0.8;
  }
}

.header-icon {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;

  .icon-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .icon-default {
    font-size: 16px;
  }
}

.header-title {
  font-size: 16px;
  font-weight: 500;
  color: var(--title-color);
}

.panel-content {
  padding: 16px;
}
</style>
```

---

## CornerDecoratedPanel 四角装饰面板

面板四角带有装饰性线条/图案，增强科技感。适用于智慧党建、智慧养老等需要突出边框效果的大屏。

```vue
<template>
  <div class="corner-panel" :class="[`theme-${theme}`]" :style="panelStyle">
    <!-- 四角装饰 -->
    <div class="corner corner-tl"></div>
    <div class="corner corner-tr"></div>
    <div class="corner corner-bl"></div>
    <div class="corner corner-br"></div>

    <!-- 头部区域 -->
    <div class="panel-header">
      <div class="header-left">
        <!-- 图标 -->
        <div v-if="icon" class="header-icon">
          <img v-if="iconUrl" :src="iconUrl" class="icon-img" />
          <span v-else class="icon-default">{{ icon }}</span>
        </div>
        <!-- 标题 -->
        <span class="header-title">{{ title }}</span>
      </div>
      <div class="header-right">
        <slot name="header-extra"></slot>
      </div>
    </div>

    <!-- 内容区域 -->
    <div class="panel-content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  title: {
    type: String,
    default: '面板标题',
    desc: '面板标题文字',
    name: '标题',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  icon: {
    type: String,
    default: '',
    desc: '标题图标',
    name: '图标',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  iconUrl: {
    type: String,
    default: '',
    desc: '图标图片URL',
    name: '图标URL',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 3,
  },
  width: {
    type: [String, Number],
    default: '100%',
    desc: '面板宽度',
    name: '宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  height: {
    type: [String, Number],
    default: 'auto',
    desc: '面板高度',
    name: '高度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  theme: {
    type: String,
    default: 'dark',
    desc: '主题风格',
    name: '主题',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    configurationTemplate: [
      { value: 'dark', label: '深蓝科技' },
      { value: 'red', label: '党建红金' },
      { value: 'light', label: '浅色商务' },
    ],
  },
  cornerStyle: {
    type: String,
    default: 'line',
    desc: '四角装饰样式：line-线条, square-方块, lshape-L形',
    name: '四角样式',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
    configurationTemplate: [
      { value: 'line', label: '线条' },
      { value: 'square', label: '方块' },
      { value: 'lshape', label: 'L形' },
    ],
  },
});

const panelStyle = computed(() => ({
  width: typeof props.width === 'number' ? `${props.width}px` : props.width,
  height: typeof props.height === 'number' ? `${props.height}px` : props.height,
}));
</script>

<style lang="scss" scoped>
.corner-panel {
  position: relative;
  background: rgba(5, 25, 55, 0.75);
  border: 1px solid var(--primary-color, #00a8e8);
  border-radius: 4px;
  overflow: hidden;

  --primary-color: #00a8e8;
  --corner-color: #00a8e8;
  --glow-color: rgba(0, 168, 232, 0.5);

  &.theme-red {
    --primary-color: #e74c3c;
    --corner-color: #ffd700;
    --glow-color: rgba(231, 76, 60, 0.5);
  }

  &.theme-light {
    background: #ffffff;
    --primary-color: #e8e8e8;
    --corner-color: #4a90e2;
    --glow-color: transparent;
  }
}

// 四角装饰
.corner {
  position: absolute;
  width: 20px;
  height: 20px;
  pointer-events: none;

  &::before,
  &::after {
    content: '';
    position: absolute;
    background: var(--corner-color);
  }
}

.corner-tl {
  top: -1px;
  left: -1px;
  &::before { width: 20px; height: 2px; top: 0; left: 0; }
  &::after { width: 2px; height: 20px; top: 0; left: 0; }
}

.corner-tr {
  top: -1px;
  right: -1px;
  &::before { width: 20px; height: 2px; top: 0; right: 0; }
  &::after { width: 2px; height: 20px; top: 0; right: 0; }
}

.corner-bl {
  bottom: -1px;
  left: -1px;
  &::before { width: 20px; height: 2px; bottom: 0; left: 0; }
  &::after { width: 2px; height: 20px; bottom: 0; left: 0; }
}

.corner-br {
  bottom: -1px;
  right: -1px;
  &::before { width: 20px; height: 2px; bottom: 0; right: 0; }
  &::after { width: 2px; height: 20px; bottom: 0; right: 0; }
}

.panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  border-bottom: 1px solid rgba(0, 168, 232, 0.3);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.header-icon {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;

  .icon-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .icon-default {
    font-size: 16px;
  }
}

.header-title {
  font-size: 16px;
  font-weight: 500;
  color: #ffffff;
}

.panel-content {
  padding: 16px;
}
</style>
```

---

## GradientHeaderPanel 渐变头部面板

浅色商务主题面板，头部为蓝色渐变背景条。适用于智慧街道等浅色主题大屏。

```vue
<template>
  <div class="gradient-header-panel" :class="[`theme-${theme}`]" :style="panelStyle">
    <!-- 头部区域 - 渐变背景 -->
    <div class="panel-header">
      <div class="header-left">
        <!-- 箭头图标 -->
        <span class="header-arrow">▶</span>
        <!-- 图标 -->
        <div v-if="icon" class="header-icon">
          <img v-if="iconUrl" :src="iconUrl" class="icon-img" />
          <span v-else class="icon-default">{{ icon }}</span>
        </div>
        <!-- 标题 -->
        <span class="header-title">{{ title }}</span>
      </div>
      <div class="header-right">
        <!-- 标签插槽 -->
        <slot name="header-tag">
          <span v-if="tag" class="header-tag">{{ tag }}</span>
        </slot>
        <!-- 更多按钮 -->
        <span v-if="showMore" class="more-link" @click="$emit('more')">更多 >>></span>
      </div>
    </div>

    <!-- 内容区域 -->
    <div class="panel-content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    default: '面板标题',
    desc: '面板标题文字',
    name: '标题',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  icon: {
    type: String,
    default: '',
    desc: '标题图标',
    name: '图标',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  iconUrl: {
    type: String,
    default: '',
    desc: '图标图片URL',
    name: '图标URL',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 3,
  },
  tag: {
    type: String,
    default: '',
    desc: '头部右侧标签文字，如"本月"',
    name: '标签',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 4,
  },
  showMore: {
    type: Boolean,
    default: false,
    desc: '是否显示"更多"链接',
    name: '显示更多',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 5,
  },
  width: {
    type: [String, Number],
    default: '100%',
    desc: '面板宽度',
    name: '宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  height: {
    type: [String, Number],
    default: 'auto',
    desc: '面板高度',
    name: '高度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  theme: {
    type: String,
    default: 'light',
    desc: '主题风格',
    name: '主题',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    configurationTemplate: [
      { value: 'light', label: '浅色商务' },
      { value: 'dark', label: '深蓝科技' },
    ],
  },
});

defineEmits(['more']);
</script>

<style lang="scss" scoped>
.gradient-header-panel {
  background: #ffffff;
  border: 1px solid #e8e8e8;
  border-radius: 4px;
  overflow: hidden;
}

.panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 16px;
  background: linear-gradient(90deg, #4a90e2, #5b9bd5);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

.header-arrow {
  font-size: 12px;
  color: #ffffff;
}

.header-icon {
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;

  .icon-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: brightness(0) invert(1); // 白色化
  }

  .icon-default {
    font-size: 14px;
    color: #ffffff;
  }
}

.header-title {
  font-size: 14px;
  font-weight: 500;
  color: #ffffff;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.header-tag {
  padding: 2px 8px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  font-size: 12px;
  color: #ffffff;
}

.more-link {
  font-size: 12px;
  color: #ffffff;
  cursor: pointer;

  &:hover {
    text-decoration: underline;
  }
}

.panel-content {
  padding: 16px;
  background: #ffffff;
}

// 深色主题变体
.theme-dark {
  background: rgba(5, 25, 55, 0.75);
  border-color: #00a8e8;

  .panel-header {
    background: transparent;
    border-bottom: 1px solid rgba(0, 168, 232, 0.3);
  }

  .panel-content {
    background: transparent;
  }

  .header-title,
  .header-arrow,
  .more-link {
    color: #ffffff;
  }

  .header-tag {
    background: rgba(0, 168, 232, 0.3);
    color: #00a8e8;
  }
}
</style>
```

---

## HexagonKPI 六边形KPI卡片

六边形形状的KPI数据卡片，适用于智慧乡村样板间等需要独特视觉效果的深蓝科技大屏。

```vue
<template>
  <div class="hexagon-kpi" :style="cardStyle">
    <div class="hexagon-shape">
      <div class="hexagon-content">
        <div class="kpi-value">
          <span class="value-number">{{ displayValue }}</span>
          <span v-if="unit" class="value-unit">{{ unit }}</span>
        </div>
        <div class="kpi-label">{{ label }}</div>
      </div>
    </div>
    <div v-if="icon" class="kpi-icon">
      <img v-if="iconUrl" :src="iconUrl" class="icon-img" />
      <span v-else class="icon-default">{{ icon }}</span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  label: {
    type: String,
    default: '指标名称',
    desc: 'KPI指标名称',
    name: '标签',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  value: {
    type: [Number, String],
    default: 0,
    desc: 'KPI数值',
    name: '数值',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  unit: {
    type: String,
    default: '',
    desc: '数值单位',
    name: '单位',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 3,
  },
  icon: {
    type: String,
    default: '',
    desc: '图标',
    name: '图标',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 4,
  },
  iconUrl: {
    type: String,
    default: '',
    desc: '图标URL',
    name: '图标URL',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 5,
  },
  size: {
    type: Number,
    default: 120,
    desc: '六边形尺寸（像素）',
    name: '尺寸',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  color: {
    type: String,
    default: '#00a8e8',
    desc: '主题颜色',
    name: '颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
});

const displayValue = computed(() => {
  if (typeof props.value === 'number') {
    return props.value.toLocaleString();
  }
  return props.value;
});

const cardStyle = computed(() => ({
  '--hex-size': `${props.size}px`,
  '--hex-color': props.color,
}));
</script>

<style lang="scss" scoped>
.hexagon-kpi {
  position: relative;
  width: var(--hex-size);
  height: calc(var(--hex-size) * 1.1547);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.hexagon-shape {
  width: 100%;
  height: 100%;
  background: var(--hex-color);
  clip-path: polygon(
    50% 0%,
    100% 25%,
    100% 75%,
    50% 100%,
    0% 75%,
    0% 25%
  );
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(0, 168, 232, 0.4);
}

.hexagon-content {
  text-align: center;
  padding: 10px;
}

.kpi-value {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 4px;
}

.value-number {
  font-size: calc(var(--hex-size) * 0.2);
  font-weight: bold;
  color: #ffffff;
  font-family: 'Orbitron', 'Digital', monospace;
}

.value-unit {
  font-size: calc(var(--hex-size) * 0.08);
  color: rgba(255, 255, 255, 0.8);
}

.kpi-label {
  margin-top: 4px;
  font-size: calc(var(--hex-size) * 0.1);
  color: rgba(255, 255, 255, 0.9);
}

.kpi-icon {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--hex-color);
  border-radius: 50%;
  box-shadow: 0 0 10px var(--hex-color);

  .icon-img {
    width: 20px;
    height: 20px;
    object-fit: contain;
    filter: brightness(0) invert(1);
  }

  .icon-default {
    font-size: 16px;
    color: #ffffff;
  }
}
</style>
```

---

## PersonStatusCard 人员状态卡片

显示人员头像、姓名、状态信息的卡片组件。适用于智慧党建、智慧养老等需要展示人员信息的大屏。

```vue
<template>
  <div class="person-status-card" :class="[`status-${status}`]">
    <div class="avatar-wrapper">
      <img v-if="avatarUrl" :src="avatarUrl" class="avatar-img" />
      <div v-else class="avatar-placeholder">
        <span>{{ name.charAt(0) }}</span>
      </div>
      <div class="status-dot"></div>
    </div>
    <div class="person-info">
      <div class="person-name">{{ name }}</div>
      <div v-if="role" class="person-role">{{ role }}</div>
      <div v-if="extraInfo" class="person-extra">{{ extraInfo }}</div>
    </div>
    <div v-if="statusText" class="status-tag">{{ statusText }}</div>
  </div>
</template>

<script setup>
const props = defineProps({
  name: {
    type: String,
    default: '姓名',
    desc: '人员姓名',
    name: '姓名',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  avatarUrl: {
    type: String,
    default: '',
    desc: '头像图片URL',
    name: '头像URL',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  role: {
    type: String,
    default: '',
    desc: '角色/职位',
    name: '角色',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 3,
  },
  extraInfo: {
    type: String,
    default: '',
    desc: '额外信息（如积分、部门等）',
    name: '额外信息',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 4,
  },
  status: {
    type: String,
    default: 'online',
    desc: '状态：online-在线, offline-离线, busy-忙碌, normal-正常',
    name: '状态',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 5,
    configurationTemplate: [
      { value: 'online', label: '在线' },
      { value: 'offline', label: '离线' },
      { value: 'busy', label: '忙碌' },
      { value: 'normal', label: '正常' },
    ],
  },
  statusText: {
    type: String,
    default: '',
    desc: '状态文字标签',
    name: '状态文字',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 6,
  },
});
</script>

<style lang="scss" scoped>
.person-status-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(5, 25, 55, 0.5);
  border-radius: 8px;
  border: 1px solid rgba(0, 168, 232, 0.3);
}

.avatar-wrapper {
  position: relative;
  flex-shrink: 0;
}

.avatar-img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #00a8e8, #0077b6);
  display: flex;
  align-items: center;
  justify-content: center;

  span {
    font-size: 20px;
    font-weight: bold;
    color: #ffffff;
  }
}

.status-dot {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 2px solid rgba(5, 25, 55, 0.8);
}

.status-online .status-dot {
  background: #52c41a;
  box-shadow: 0 0 6px #52c41a;
}

.status-offline .status-dot {
  background: #f5222d;
}

.status-busy .status-dot {
  background: #faad14;
}

.status-normal .status-dot {
  background: #00a8e8;
}

.person-info {
  flex: 1;
  min-width: 0;
}

.person-name {
  font-size: 14px;
  font-weight: 500;
  color: #ffffff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.person-role {
  margin-top: 2px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
}

.person-extra {
  margin-top: 4px;
  font-size: 12px;
  color: #00a8e8;
}

.status-tag {
  flex-shrink: 0;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  background: rgba(0, 168, 232, 0.2);
  color: #00a8e8;
}

.status-online .status-tag {
  background: rgba(82, 196, 26, 0.2);
  color: #52c41a;
}

.status-offline .status-tag {
  background: rgba(245, 34, 45, 0.2);
  color: #f5222d;
}
</style>
```

---

## AIRecognitionCard AI识别卡片

显示AI识别类型和数据的卡片，带圆形AI图标。适用于智慧街道等包含AI识别功能的大屏。

```vue
<template>
  <div class="ai-recognition-card">
    <div class="ai-icon">
      <span class="ai-text">AI</span>
    </div>
    <div class="card-content">
      <div class="recognition-type">{{ type }}</div>
      <div class="recognition-data">
        <span class="data-current" :class="dataClass">{{ current }}</span>
        <span class="data-separator">/</span>
        <span class="data-total">{{ total }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  type: {
    type: String,
    default: '识别类型',
    desc: 'AI识别类型名称',
    name: '类型',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  current: {
    type: Number,
    default: 0,
    desc: '当前识别数量',
    name: '当前数',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  total: {
    type: Number,
    default: 0,
    desc: '总数量',
    name: '总数',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 3,
  },
  status: {
    type: String,
    default: 'normal',
    desc: '状态：success-成功/绿色, warning-警告/橙色, normal-普通/蓝色',
    name: '状态',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 4,
    configurationTemplate: [
      { value: 'success', label: '成功' },
      { value: 'warning', label: '警告' },
      { value: 'normal', label: '普通' },
    ],
  },
});

const dataClass = computed(() => `status-${props.status}`);
</script>

<style lang="scss" scoped>
.ai-recognition-card {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  background: rgba(74, 144, 226, 0.1);
  border: 1px solid rgba(74, 144, 226, 0.3);
  border-radius: 8px;
  min-width: 100px;
}

.ai-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #4a90e2, #5b9bd5);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.ai-text {
  font-size: 12px;
  font-weight: bold;
  color: #ffffff;
}

.card-content {
  flex: 1;
}

.recognition-type {
  font-size: 12px;
  color: #333333;
  margin-bottom: 2px;
}

.recognition-data {
  font-size: 16px;
  font-weight: bold;
}

.data-current {
  &.status-success {
    color: #52c41a;
  }
  &.status-warning {
    color: #faad14;
  }
  &.status-normal {
    color: #4a90e2;
  }
}

.data-separator {
  color: #999999;
  margin: 0 2px;
}

.data-total {
  color: #666666;
}

// 深色主题
@media (prefers-color-scheme: dark) {
  .ai-recognition-card {
    background: rgba(0, 168, 232, 0.1);
    border-color: rgba(0, 168, 232, 0.3);
  }

  .recognition-type {
    color: rgba(255, 255, 255, 0.8);
  }

  .data-total {
    color: rgba(255, 255, 255, 0.6);
  }
}
</style>
```

---

## MapFloatNumber 地图悬浮数字

在地图上悬浮显示的大数字组件，适用于文旅大数据等需要在地图上突出显示核心数据的场景。

```vue
<template>
  <div class="map-float-number" :class="[`position-${position}`]" :style="containerStyle">
    <div class="number-wrapper">
      <div class="number-value" :style="{ color: numberColor }">
        {{ displayValue }}
      </div>
      <div class="number-label">{{ label }}</div>
      <div class="number-decoration"></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  label: {
    type: String,
    default: '实时客流',
    desc: '数字标签文字',
    name: '标签',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  value: {
    type: [Number, String],
    default: 0,
    desc: '显示数值',
    name: '数值',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  position: {
    type: String,
    default: 'top-left',
    desc: '悬浮位置：top-left, top-right, bottom-left, bottom-right, center',
    name: '位置',
    groupKey: 'layout',
    groupName: '布局配置',
    sort: 1,
    configurationTemplate: [
      { value: 'top-left', label: '左上' },
      { value: 'top-right', label: '右上' },
      { value: 'bottom-left', label: '左下' },
      { value: 'bottom-right', label: '右下' },
      { value: 'center', label: '居中' },
    ],
  },
  color: {
    type: String,
    default: '#00d4aa',
    desc: '数字颜色',
    name: '颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  fontSize: {
    type: Number,
    default: 48,
    desc: '数字字号（像素）',
    name: '字号',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
});

const displayValue = computed(() => {
  if (typeof props.value === 'number') {
    return props.value.toLocaleString();
  }
  return props.value;
});

const numberColor = computed(() => props.color);

const containerStyle = computed(() => ({
  '--number-font-size': `${props.fontSize}px`,
}));
</script>

<style lang="scss" scoped>
.map-float-number {
  position: absolute;
  z-index: 100;
  pointer-events: none;
}

.position-top-left {
  top: 20px;
  left: 20px;
}

.position-top-right {
  top: 20px;
  right: 20px;
}

.position-bottom-left {
  bottom: 20px;
  left: 20px;
}

.position-bottom-right {
  bottom: 20px;
  right: 20px;
}

.position-center {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.number-wrapper {
  position: relative;
  text-align: center;
}

.number-value {
  font-size: var(--number-font-size);
  font-weight: bold;
  font-family: 'Orbitron', 'Digital', monospace;
  text-shadow: 0 0 20px currentColor, 0 0 40px currentColor;
  line-height: 1;
}

.number-label {
  margin-top: 8px;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
}

.number-decoration {
  margin-top: 8px;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, transparent, #00a8e8, transparent);
  border-radius: 2px;
}
</style>
```

---

## SemicircleChart 半圆环形图

开口向上的半圆环形图，适用于智慧街道党建民生等场景。

```vue
<template>
  <div class="semicircle-chart" ref="chartRef" :style="{ width: `${width}px`, height: `${height}px` }"></div>
</template>

<script setup>
import { ref, onMounted, watch, onUnmounted } from 'vue';
import * as echarts from 'echarts';

const props = defineProps({
  data: {
    type: Array,
    default: () => [
      { name: '主题党日', value: 35, color: '#faad14' },
      { name: '党课', value: 20, color: '#52c41a' },
      { name: '组织生活', value: 5, color: '#1890ff' },
    ],
    desc: '数据数组，每项包含name、value、color',
    name: '数据',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 1,
  },
  width: {
    type: Number,
    default: 300,
    desc: '图表宽度',
    name: '宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  height: {
    type: Number,
    default: 180,
    desc: '图表高度',
    name: '高度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  radius: {
    type: Array,
    default: () => ['40%', '70%'],
    desc: '环形内外半径',
    name: '半径',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
  },
});

const chartRef = ref(null);
let chartInstance = null;

const initChart = () => {
  if (!chartRef.value) return;

  chartInstance = echarts.init(chartRef.value);

  const total = props.data.reduce((sum, item) => sum + item.value, 0);

  const option = {
    series: [
      {
        type: 'pie',
        radius: props.radius,
        center: ['50%', '100%'],
        startAngle: 180,
        endAngle: 360,
        data: props.data.map(item => ({
          name: item.name,
          value: item.value,
          itemStyle: {
            color: item.color,
          },
        })),
        label: {
          show: true,
          position: 'outside',
          formatter: '{b}\n{c}',
          color: '#ffffff',
          fontSize: 12,
        },
        labelLine: {
          show: true,
          length: 10,
          length2: 20,
          lineStyle: {
            color: 'rgba(255, 255, 255, 0.3)',
          },
        },
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)',
          },
        },
      },
    ],
  };

  chartInstance.setOption(option);
};

onMounted(() => {
  initChart();
});

watch(() => [props.data, props.width, props.height], () => {
  if (chartInstance) {
    chartInstance.dispose();
    initChart();
  }
}, { deep: true });

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.dispose();
  }
});
</script>

<style lang="scss" scoped>
.semicircle-chart {
  background: transparent;
}
</style>
```

---

## CityRankingList 城市排名列表

带横向进度条的城市排名列表组件，适用于文旅大数据客流来源排名等场景。

```vue
<template>
  <div class="city-ranking-list">
    <!-- 顶部标签切换 -->
    <div v-if="tabs.length > 0" class="tab-header">
      <span
        v-for="tab in tabs"
        :key="tab.value"
        class="tab-item"
        :class="{ active: activeTab === tab.value }"
        @click="activeTab = tab.value; $emit('tab-change', tab.value)"
      >
        {{ tab.label }}
      </span>
    </div>

    <!-- 排名列表 -->
    <div class="ranking-list">
      <div
        v-for="(item, index) in listData"
        :key="item.name"
        class="ranking-item"
      >
        <div class="item-header">
          <span class="rank-number" :class="`rank-${index + 1}`">{{ index + 1 }}</span>
          <span class="city-name">{{ item.name }}</span>
          <span class="city-value">{{ item.value.toLocaleString() }}</span>
        </div>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: `${item.percent}%` }"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  data: {
    type: Array,
    default: () => [
      { name: '上海', value: 62398 },
      { name: '重庆', value: 56535 },
      { name: '广东', value: 50121 },
      { name: '浙江', value: 45678 },
      { name: '北京', value: 38902 },
    ],
    desc: '排名数据数组',
    name: '数据',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 1,
  },
  tabs: {
    type: Array,
    default: () => [
      { label: '省内', value: 'in' },
      { label: '省外', value: 'out' },
    ],
    desc: '标签切换选项',
    name: '标签',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 2,
  },
  defaultTab: {
    type: String,
    default: 'out',
    desc: '默认选中标签',
    name: '默认标签',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 3,
  },
});

const emit = defineEmits(['tab-change']);

const activeTab = ref(props.defaultTab);

const listData = computed(() => {
  const maxValue = Math.max(...props.data.map(item => item.value));
  return props.data.map(item => ({
    ...item,
    percent: (item.value / maxValue) * 100,
  }));
});
</script>

<style lang="scss" scoped>
.city-ranking-list {
  width: 100%;
}

.tab-header {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.tab-item {
  padding: 6px 16px;
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
  background: transparent;
  color: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(0, 168, 232, 0.3);
  transition: all 0.3s;

  &.active {
    background: #00a8e8;
    color: #ffffff;
    border-color: #00a8e8;
  }

  &:hover:not(.active) {
    background: rgba(0, 168, 232, 0.1);
  }
}

.ranking-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ranking-item {
  padding: 8px 0;
}

.item-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.rank-number {
  width: 20px;
  height: 20px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: bold;
  background: rgba(0, 168, 232, 0.2);
  color: #00a8e8;

  &.rank-1 {
    background: linear-gradient(135deg, #ffd700, #ffb703);
    color: #ffffff;
  }
  &.rank-2 {
    background: linear-gradient(135deg, #c0c0c0, #a0a0a0);
    color: #ffffff;
  }
  &.rank-3 {
    background: linear-gradient(135deg, #cd7f32, #b87333);
    color: #ffffff;
  }
}

.city-name {
  flex: 1;
  font-size: 14px;
  color: #ffffff;
}

.city-value {
  font-size: 14px;
  font-weight: bold;
  color: #00a8e8;
}

.progress-bar {
  height: 6px;
  background: rgba(0, 168, 232, 0.2);
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #00a8e8, #00d4aa);
  border-radius: 3px;
  transition: width 0.5s ease;
}
</style>
```

---

## TechModal 科技感弹窗

带复杂边框设计的科技感弹窗组件，上下边框有内凹缺口，四角有装饰。

```vue
<template>
  <div v-if="visible" class="tech-modal-overlay" @click.self="$emit('close')">
    <div class="tech-modal" :style="modalStyle">
      <!-- 四角装饰 -->
      <div class="corner corner-tl"></div>
      <div class="corner corner-tr"></div>
      <div class="corner corner-bl"></div>
      <div class="corner corner-br"></div>

      <!-- 关闭按钮 -->
      <button class="close-btn" @click="$emit('close')">
        <span>×</span>
      </button>

      <!-- 标题栏 -->
      <div class="modal-header">
        <div class="header-indicator"></div>
        <span class="header-title">{{ title }}</span>
      </div>

      <!-- 内容区域 -->
      <div class="modal-content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  visible: {
    type: Boolean,
    default: false,
    desc: '是否显示弹窗',
    name: '可见',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 1,
  },
  title: {
    type: String,
    default: '数据分析',
    desc: '弹窗标题',
    name: '标题',
    groupKey: 'basic',
    groupName: '基础配置',
    sort: 2,
  },
  width: {
    type: Number,
    default: 600,
    desc: '弹窗宽度（像素）',
    name: '宽度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  height: {
    type: Number,
    default: 400,
    desc: '弹窗高度（像素）',
    name: '高度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
});

defineEmits(['close']);

const modalStyle = computed(() => ({
  width: `${props.width}px`,
  height: `${props.height}px`,
}));
</script>

<style lang="scss" scoped>
.tech-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.tech-modal {
  position: relative;
  background: rgba(5, 25, 55, 0.95);
  border: 1px solid #00a8e8;
  border-radius: 4px;
  box-shadow: 0 0 30px rgba(0, 168, 232, 0.4);

  // 使用clip-path实现上下内凹缺口
  clip-path: polygon(
    0 0,
    30% 0,
    32% 10px,
    68% 10px,
    70% 0,
    100% 0,
    100% 100%,
    70% 100%,
    68% calc(100% - 10px),
    32% calc(100% - 10px),
    30% 100%,
    0 100%
  );
}

.corner {
  position: absolute;
  width: 16px;
  height: 16px;
  pointer-events: none;

  &::before,
  &::after {
    content: '';
    position: absolute;
    background: #ffb703;
  }
}

.corner-tl {
  top: 0;
  left: 0;
  &::before { width: 16px; height: 2px; top: 0; left: 0; }
  &::after { width: 2px; height: 16px; top: 0; left: 0; }
}

.corner-tr {
  top: 0;
  right: 0;
  &::before { width: 16px; height: 2px; top: 0; right: 0; }
  &::after { width: 2px; height: 16px; top: 0; right: 0; }
}

.corner-bl {
  bottom: 0;
  left: 0;
  &::before { width: 16px; height: 2px; bottom: 0; left: 0; }
  &::after { width: 2px; height: 16px; bottom: 0; left: 0; }
}

.corner-br {
  bottom: 0;
  right: 0;
  &::before { width: 16px; height: 2px; bottom: 0; right: 0; }
  &::after { width: 2px; height: 16px; bottom: 0; right: 0; }
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #00a8e8;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;

  span {
    font-size: 18px;
    color: #ffffff;
    line-height: 1;
  }

  &:hover {
    background: #00d4ff;
  }
}

.modal-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(0, 168, 232, 0.3);
}

.header-indicator {
  width: 4px;
  height: 18px;
  background: #00a8e8;
  border-radius: 2px;
}

.header-title {
  font-size: 16px;
  font-weight: 500;
  color: #ffffff;
}

.modal-content {
  padding: 20px;
  height: calc(100% - 60px);
  overflow: auto;
}
</style>
```
