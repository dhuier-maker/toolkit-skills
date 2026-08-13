# Three.js 3D/WebGL 组件模板

> 高级 3D 可视化组件开发模板，适用于智慧城市、数字孪生、3D 地球、建筑可视化等场景。

---

## 一、Three.js 基础组件模板

### 1.1 通用 Three.js 组件骨架

所有 Three.js 组件的基础模板，包含场景初始化、渲染循环、资源清理。

```vue
<template>
  <div ref="containerRef" class="three-container">
    <canvas ref="canvasRef" class="three-canvas"></canvas>
    <!-- 可选：加载提示 -->
    <div v-if="loading" class="loading-overlay">
      <div class="loading-spinner"></div>
      <span>加载中...</span>
    </div>
    <!-- 可选：信息面板 -->
    <div v-if="showInfo" class="info-panel">
      <slot name="info"></slot>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, markRaw } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import i18n from './locale/index';

const props = defineProps({
  // ========== 场景配置 ==========
  backgroundColor: {
    type: String,
    default: '#0a1628',
    desc: '场景背景色',
    name: '背景色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  backgroundAlpha: {
    type: Number,
    default: 1,
    desc: '背景透明度',
    name: '背景透明度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
    min: 0,
    max: 1,
  },
  ambientLightIntensity: {
    type: Number,
    default: 0.6,
    desc: '环境光强度',
    name: '环境光',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    min: 0,
    max: 2,
  },
  directionalLightIntensity: {
    type: Number,
    default: 0.8,
    desc: '平行光强度',
    name: '平行光',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
    min: 0,
    max: 2,
  },

  // ========== 相机配置 ==========
  cameraPosition: {
    type: Object,
    default: () => ({ x: 0, y: 100, z: 200 }),
    desc: '相机初始位置',
    name: '相机位置',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 1,
  },
  cameraFov: {
    type: Number,
    default: 60,
    desc: '相机视场角',
    name: '视场角',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 2,
    min: 30,
    max: 120,
  },
  enableAutoRotate: {
    type: Boolean,
    default: true,
    desc: '是否自动旋转',
    name: '自动旋转',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 3,
  },
  autoRotateSpeed: {
    type: Number,
    default: 0.5,
    desc: '自动旋转速度',
    name: '旋转速度',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 4,
    min: 0.1,
    max: 5,
  },

  // ========== 交互配置 ==========
  enableZoom: {
    type: Boolean,
    default: true,
    desc: '是否允许缩放',
    name: '允许缩放',
    groupKey: 'interaction',
    groupName: '交互配置',
    sort: 1,
  },
  enablePan: {
    type: Boolean,
    default: true,
    desc: '是否允许平移',
    name: '允许平移',
    groupKey: 'interaction',
    groupName: '交互配置',
    sort: 2,
  },
  minDistance: {
    type: Number,
    default: 50,
    desc: '最小缩放距离',
    name: '最小距离',
    groupKey: 'interaction',
    groupName: '交互配置',
    sort: 3,
  },
  maxDistance: {
    type: Number,
    default: 1000,
    desc: '最大缩放距离',
    name: '最大距离',
    groupKey: 'interaction',
    groupName: '交互配置',
    sort: 4,
  },

  // ========== 数据配置 ==========
  dataUrl: {
    type: String,
    default: '',
    desc: '3D模型/数据URL',
    name: '数据源',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 1,
  },
  showInfo: {
    type: Boolean,
    default: false,
    desc: '是否显示信息面板',
    name: '信息面板',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 2,
  },
});

const emit = defineEmits(['ready', 'click', 'hover', 'progress']);

const containerRef = ref(null);
const canvasRef = ref(null);
const loading = ref(true);

// Three.js 核心对象（使用 markRaw 避免响应式）
let scene = null;
let camera = null;
let renderer = null;
let controls = null;
let animationId = null;

// 初始化场景
const initScene = () => {
  if (!containerRef.value) return;

  const container = containerRef.value;
  const width = container.clientWidth;
  const height = container.clientHeight;

  // 创建场景
  scene = markRaw(new THREE.Scene());
  scene.background = new THREE.Color(props.backgroundColor);
  scene.backgroundAlpha = props.backgroundAlpha;

  // 创建相机
  camera = markRaw(new THREE.PerspectiveCamera(
    props.cameraFov,
    width / height,
    0.1,
    10000
  ));
  camera.position.set(
    props.cameraPosition.x,
    props.cameraPosition.y,
    props.cameraPosition.z
  );

  // 创建渲染器
  renderer = markRaw(new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    antialias: true,
    alpha: true,
  }));
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1;

  // 创建控制器
  controls = markRaw(new OrbitControls(camera, renderer.domElement));
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.enableZoom = props.enableZoom;
  controls.enablePan = props.enablePan;
  controls.minDistance = props.minDistance;
  controls.maxDistance = props.maxDistance;
  controls.autoRotate = props.enableAutoRotate;
  controls.autoRotateSpeed = props.autoRotateSpeed;

  // 添加灯光
  addLights();

  // 触发 ready 事件
  emit('ready', { scene, camera, renderer, controls });
};

// 添加灯光
const addLights = () => {
  // 环境光
  const ambientLight = new THREE.AmbientLight(0xffffff, props.ambientLightIntensity);
  scene.add(ambientLight);

  // 平行光（主光源）
  const directionalLight = new THREE.DirectionalLight(0xffffff, props.directionalLightIntensity);
  directionalLight.position.set(100, 200, 100);
  directionalLight.castShadow = true;
  directionalLight.shadow.mapSize.width = 2048;
  directionalLight.shadow.mapSize.height = 2048;
  directionalLight.shadow.camera.near = 0.5;
  directionalLight.shadow.camera.far = 1000;
  directionalLight.shadow.camera.left = -200;
  directionalLight.shadow.camera.right = 200;
  directionalLight.shadow.camera.top = 200;
  directionalLight.shadow.camera.bottom = -200;
  scene.add(directionalLight);

  // 补光
  const fillLight = new THREE.DirectionalLight(0x4a90e2, 0.3);
  fillLight.position.set(-100, 100, -100);
  scene.add(fillLight);
};

// 动画循环
const animate = () => {
  animationId = requestAnimationFrame(animate);
  controls?.update();
  renderer?.render(scene, camera);
};

// 窗口大小变化处理
const handleResize = () => {
  if (!containerRef.value || !camera || !renderer) return;

  const width = containerRef.value.clientWidth;
  const height = containerRef.value.clientHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
};

// 清理资源
const dispose = () => {
  if (animationId) {
    cancelAnimationFrame(animationId);
  }

  // 递归清理场景中的对象
  scene?.traverse((object) => {
    if (object.geometry) {
      object.geometry.dispose();
    }
    if (object.material) {
      if (Array.isArray(object.material)) {
        object.material.forEach((material) => material.dispose());
      } else {
        object.material.dispose();
      }
    }
  });

  renderer?.dispose();
  controls?.dispose();

  scene = null;
  camera = null;
  renderer = null;
  controls = null;
};

// 监听 props 变化
watch(() => props.backgroundColor, (color) => {
  if (scene) scene.background = new THREE.Color(color);
});

watch(() => props.enableAutoRotate, (value) => {
  if (controls) controls.autoRotate = value;
});

watch(() => props.autoRotateSpeed, (value) => {
  if (controls) controls.autoRotateSpeed = value;
});

onMounted(() => {
  initScene();
  animate();
  window.addEventListener('resize', handleResize);
  loading.value = false;
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  dispose();
});

// 暴露方法供外部调用
defineExpose({
  scene: () => scene,
  camera: () => camera,
  renderer: () => renderer,
  controls: () => controls,
  dispose,
});
</script>

<style lang="scss" scoped>
.three-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.three-canvas {
  display: block;
  width: 100%;
  height: 100%;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(10, 22, 40, 0.8);
  color: #00a8e8;
  font-size: 14px;
  gap: 12px;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(0, 168, 232, 0.2);
  border-top-color: #00a8e8;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.info-panel {
  position: absolute;
  top: 20px;
  left: 20px;
  padding: 16px;
  background: rgba(5, 25, 55, 0.85);
  border: 1px solid rgba(0, 168, 232, 0.3);
  border-radius: 8px;
  color: #ffffff;
  font-size: 14px;
  max-width: 300px;
}
</style>
```

---

## 二、3D 城市组件 (City3D)

智慧城市可视化组件，支持建筑群、道路、区域边界等 3D 展示。

```vue
<template>
  <div ref="containerRef" class="city-3d-container">
    <canvas ref="canvasRef"></canvas>

    <!-- 数据面板 -->
    <div v-if="selectedBuilding" class="building-info-panel">
      <div class="panel-header">
        <span class="building-name">{{ selectedBuilding.name }}</span>
        <span class="close-btn" @click="selectedBuilding = null">×</span>
      </div>
      <div class="panel-content">
        <div class="info-row">
          <span class="label">建筑类型：</span>
          <span class="value">{{ selectedBuilding.type }}</span>
        </div>
        <div class="info-row">
          <span class="label">建筑面积：</span>
          <span class="value">{{ selectedBuilding.area }} m²</span>
        </div>
        <div class="info-row">
          <span class="label">楼层数：</span>
          <span class="value">{{ selectedBuilding.floors }} 层</span>
        </div>
      </div>
    </div>

    <!-- 图例 -->
    <div class="legend-panel">
      <div class="legend-title">建筑类型</div>
      <div class="legend-item">
        <span class="legend-color" style="background: #00a8e8;"></span>
        <span>商业建筑</span>
      </div>
      <div class="legend-item">
        <span class="legend-color" style="background: #52c41a;"></span>
        <span>住宅建筑</span>
      </div>
      <div class="legend-item">
        <span class="legend-color" style="background: #faad14;"></span>
        <span>公共设施</span>
      </div>
      <div class="legend-item">
        <span class="legend-color" style="background: #ff4d4f;"></span>
        <span>工业建筑</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, markRaw, computed } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  buildingData: {
    type: Array,
    default: () => [
      { id: 1, name: '商业中心A', type: 'commercial', x: 0, z: 0, width: 30, depth: 30, height: 80, area: 72000, floors: 20 },
      { id: 2, name: '住宅小区B', type: 'residential', x: 50, z: 30, width: 40, depth: 25, height: 50, area: 50000, floors: 15 },
      { id: 3, name: '医院', type: 'public', x: -40, z: -20, width: 50, depth: 40, height: 35, area: 70000, floors: 10 },
      { id: 4, name: '工厂C', type: 'industrial', x: 80, z: -50, width: 60, depth: 40, height: 20, area: 48000, floors: 3 },
    ],
    desc: '建筑数据数组',
    name: '建筑数据',
    groupKey: 'data',
    groupName: '数据配置',
    useDynamic: true,
    sort: 1,
  },
  regionBoundary: {
    type: Array,
    default: () => [
      { x: -100, z: -100 },
      { x: 150, z: -100 },
      { x: 150, z: 100 },
      { x: -100, z: 100 },
    ],
    desc: '区域边界坐标',
    name: '区域边界',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 2,
  },

  // ========== 样式配置 ==========
  groundColor: {
    type: String,
    default: '#0d1b2a',
    desc: '地面颜色',
    name: '地面颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  buildingColors: {
    type: Object,
    default: () => ({
      commercial: '#00a8e8',
      residential: '#52c41a',
      public: '#faad14',
      industrial: '#ff4d4f',
    }),
    desc: '各类型建筑颜色',
    name: '建筑颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  enableGlow: {
    type: Boolean,
    default: true,
    desc: '是否启用发光效果',
    name: '发光效果',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
  },
  glowIntensity: {
    type: Number,
    default: 0.5,
    desc: '发光强度',
    name: '发光强度',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
    min: 0,
    max: 1,
  },

  // ========== 相机配置 ==========
  cameraPosition: {
    type: Object,
    default: () => ({ x: 150, y: 200, z: 150 }),
    desc: '相机位置',
    name: '相机位置',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 1,
  },
  enableAutoRotate: {
    type: Boolean,
    default: true,
    desc: '自动旋转',
    name: '自动旋转',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 2,
  },
});

const emit = defineEmits(['building-click', 'ready']);

const containerRef = ref(null);
const canvasRef = ref(null);
const selectedBuilding = ref(null);

// Three.js 对象
let scene, camera, renderer, controls;
let buildings = [];
let raycaster, mouse;

// 建筑类型颜色映射
const getBuildingColor = (type) => {
  return props.buildingColors[type] || '#00a8e8';
};

// 初始化场景
const initScene = () => {
  const container = containerRef.value;
  const width = container.clientWidth;
  const height = container.clientHeight;

  // 场景
  scene = markRaw(new THREE.Scene());
  scene.background = new THREE.Color('#0a1628');
  scene.fog = new THREE.Fog('#0a1628', 200, 800);

  // 相机
  camera = markRaw(new THREE.PerspectiveCamera(60, width / height, 1, 2000));
  camera.position.set(props.cameraPosition.x, props.cameraPosition.y, props.cameraPosition.z);

  // 渲染器
  renderer = markRaw(new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    antialias: true,
  }));
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;

  // 控制器
  controls = markRaw(new OrbitControls(camera, renderer.domElement));
  controls.enableDamping = true;
  controls.autoRotate = props.enableAutoRotate;
  controls.autoRotateSpeed = 0.3;
  controls.maxPolarAngle = Math.PI / 2.2;
  controls.minDistance = 50;
  controls.maxDistance = 500;

  // 射线检测
  raycaster = markRaw(new THREE.Raycaster());
  mouse = markRaw(new THREE.Vector2());

  // 添加灯光
  addLights();

  // 创建地面
  createGround();

  // 创建建筑
  createBuildings();

  // 创建边界
  createBoundary();

  // 添加网格辅助
  addGridHelper();

  // 事件监听
  renderer.domElement.addEventListener('click', handleClick);
  renderer.domElement.addEventListener('mousemove', handleMouseMove);

  emit('ready', { scene, camera, renderer });
};

// 添加灯光
const addLights = () => {
  // 环境光
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
  scene.add(ambientLight);

  // 主光源
  const mainLight = new THREE.DirectionalLight(0xffffff, 0.8);
  mainLight.position.set(100, 200, 100);
  mainLight.castShadow = true;
  mainLight.shadow.mapSize.width = 2048;
  mainLight.shadow.mapSize.height = 2048;
  mainLight.shadow.camera.near = 10;
  mainLight.shadow.camera.far = 500;
  mainLight.shadow.camera.left = -200;
  mainLight.shadow.camera.right = 200;
  mainLight.shadow.camera.top = 200;
  mainLight.shadow.camera.bottom = -200;
  scene.add(mainLight);

  // 补光（蓝色调）
  const fillLight = new THREE.DirectionalLight(0x4a90e2, 0.3);
  fillLight.position.set(-100, 50, -100);
  scene.add(fillLight);
};

// 创建地面
const createGround = () => {
  const groundGeometry = new THREE.PlaneGeometry(500, 500);
  const groundMaterial = new THREE.MeshStandardMaterial({
    color: props.groundColor,
    roughness: 0.9,
    metalness: 0.1,
  });
  const ground = new THREE.Mesh(groundGeometry, groundMaterial);
  ground.rotation.x = -Math.PI / 2;
  ground.receiveShadow = true;
  scene.add(ground);
};

// 创建建筑
const createBuildings = () => {
  buildings = [];

  props.buildingData.forEach((data) => {
    // 建筑主体
    const geometry = new THREE.BoxGeometry(data.width, data.height, data.depth);
    const color = new THREE.Color(getBuildingColor(data.type));

    const material = new THREE.MeshStandardMaterial({
      color: color,
      roughness: 0.7,
      metalness: 0.3,
      emissive: props.enableGlow ? color : 0x000000,
      emissiveIntensity: props.enableGlow ? props.glowIntensity : 0,
    });

    const building = new THREE.Mesh(geometry, material);
    building.position.set(data.x, data.height / 2, data.z);
    building.castShadow = true;
    building.receiveShadow = true;

    // 存储建筑数据
    building.userData = { ...data };

    scene.add(building);
    buildings.push(building);

    // 添加顶部发光效果
    if (props.enableGlow) {
      const topGlow = createTopGlow(data.width, data.depth, color);
      topGlow.position.set(data.x, data.height + 0.5, data.z);
      scene.add(topGlow);
    }
  });
};

// 创建顶部发光效果
const createTopGlow = (width, depth, color) => {
  const geometry = new THREE.PlaneGeometry(width * 0.8, depth * 0.8);
  const material = new THREE.MeshBasicMaterial({
    color: color,
    transparent: true,
    opacity: 0.3,
    side: THREE.DoubleSide,
  });
  const glow = new THREE.Mesh(geometry, material);
  glow.rotation.x = -Math.PI / 2;
  return glow;
};

// 创建边界
const createBoundary = () => {
  if (!props.regionBoundary || props.regionBoundary.length < 3) return;

  const points = props.regionBoundary.map(p => new THREE.Vector3(p.x, 0.5, p.z));
  points.push(points[0]); // 闭合

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({
    color: 0x00a8e8,
    linewidth: 2,
  });
  const boundary = new THREE.Line(geometry, material);
  scene.add(boundary);

  // 边界发光区域
  const shape = new THREE.Shape();
  shape.moveTo(props.regionBoundary[0].x, props.regionBoundary[0].z);
  props.regionBoundary.slice(1).forEach(p => shape.lineTo(p.x, p.z));
  shape.lineTo(props.regionBoundary[0].x, props.regionBoundary[0].z);

  const boundaryGeometry = new THREE.ShapeGeometry(shape);
  const boundaryMaterial = new THREE.MeshBasicMaterial({
    color: 0x00a8e8,
    transparent: true,
    opacity: 0.05,
    side: THREE.DoubleSide,
  });
  const boundaryMesh = new THREE.Mesh(boundaryGeometry, boundaryMaterial);
  boundaryMesh.rotation.x = -Math.PI / 2;
  boundaryMesh.position.y = 0.1;
  scene.add(boundaryMesh);
};

// 添加网格辅助
const addGridHelper = () => {
  const gridHelper = new THREE.GridHelper(500, 50, 0x00a8e8, 0x0d1b2a);
  gridHelper.material.opacity = 0.2;
  gridHelper.material.transparent = true;
  scene.add(gridHelper);
};

// 点击处理
const handleClick = (event) => {
  const rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(buildings);

  if (intersects.length > 0) {
    const building = intersects[0].object;
    selectedBuilding.value = building.userData;
    emit('building-click', building.userData);

    // 高亮效果
    buildings.forEach(b => {
      b.material.emissiveIntensity = b === building ? 0.8 : props.glowIntensity;
    });
  }
};

// 鼠标移动处理
const handleMouseMove = (event) => {
  const rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(buildings);

  renderer.domElement.style.cursor = intersects.length > 0 ? 'pointer' : 'default';
};

// 动画循环
const animate = () => {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
};

// 窗口大小变化
const handleResize = () => {
  if (!containerRef.value) return;
  const width = containerRef.value.clientWidth;
  const height = containerRef.value.clientHeight;
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
};

// 清理资源
const dispose = () => {
  renderer?.dispose();
  controls?.dispose();
  buildings.forEach(b => {
    b.geometry.dispose();
    b.material.dispose();
  });
};

watch(() => props.buildingData, () => {
  // 移除旧建筑
  buildings.forEach(b => scene.remove(b));
  createBuildings();
}, { deep: true });

onMounted(() => {
  initScene();
  animate();
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  dispose();
});

defineExpose({ scene: () => scene, camera: () => camera, renderer: () => renderer });
</script>

<style lang="scss" scoped>
.city-3d-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: #0a1628;

  canvas {
    display: block;
    width: 100%;
    height: 100%;
  }
}

.building-info-panel {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 260px;
  background: rgba(5, 25, 55, 0.9);
  border: 1px solid rgba(0, 168, 232, 0.4);
  border-radius: 8px;
  overflow: hidden;

  .panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    background: rgba(0, 168, 232, 0.15);
    border-bottom: 1px solid rgba(0, 168, 232, 0.3);

    .building-name {
      font-size: 16px;
      font-weight: 500;
      color: #ffffff;
    }

    .close-btn {
      font-size: 20px;
      color: rgba(255, 255, 255, 0.6);
      cursor: pointer;

      &:hover {
        color: #ffffff;
      }
    }
  }

  .panel-content {
    padding: 16px;

    .info-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: 10px;
      font-size: 14px;

      .label {
        color: rgba(255, 255, 255, 0.6);
      }

      .value {
        color: #00a8e8;
        font-weight: 500;
      }
    }
  }
}

.legend-panel {
  position: absolute;
  bottom: 20px;
  left: 20px;
  padding: 12px 16px;
  background: rgba(5, 25, 55, 0.9);
  border: 1px solid rgba(0, 168, 232, 0.3);
  border-radius: 8px;

  .legend-title {
    font-size: 14px;
    font-weight: 500;
    color: #ffffff;
    margin-bottom: 10px;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 6px;
    font-size: 12px;
    color: rgba(255, 255, 255, 0.8);

    .legend-color {
      width: 16px;
      height: 16px;
      border-radius: 3px;
    }
  }
}
</style>
```

---

## 三、3D 地球组件 (Earth3D)

全球数据可视化组件，支持国家标记、飞线动画、热力点等。

```vue
<template>
  <div ref="containerRef" class="earth-3d-container">
    <canvas ref="canvasRef"></canvas>

    <!-- 数据面板 -->
    <div v-if="hoverData" class="hover-panel" :style="{ left: hoverData.x + 'px', top: hoverData.y + 'px' }">
      <div class="country-name">{{ hoverData.name }}</div>
      <div class="country-value">{{ hoverData.value }}</div>
    </div>

    <!-- 控制面板 -->
    <div class="control-panel">
      <button :class="{ active: showFlyLines }" @click="showFlyLines = !showFlyLines">飞线</button>
      <button :class="{ active: showHeatmap }" @click="showHeatmap = !showHeatmap">热力</button>
      <button :class="{ active: showLabels }" @click="showLabels = !showLabels">标签</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, markRaw, shallowRef } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  countryData: {
    type: Array,
    default: () => [
      { name: '中国', code: 'CN', lat: 35.86, lng: 104.19, value: 125000 },
      { name: '美国', code: 'US', lat: 37.09, lng: -95.71, value: 85000 },
      { name: '日本', code: 'JP', lat: 36.20, lng: 138.25, value: 45000 },
      { name: '德国', code: 'DE', lat: 51.16, lng: 10.45, value: 38000 },
      { name: '英国', code: 'GB', lat: 55.37, lng: -3.43, value: 32000 },
    ],
    desc: '国家数据',
    name: '国家数据',
    groupKey: 'data',
    groupName: '数据配置',
    useDynamic: true,
    sort: 1,
  },
  flyLineData: {
    type: Array,
    default: () => [
      { from: { lat: 35.86, lng: 104.19 }, to: { lat: 37.09, lng: -95.71 }, value: 5000 },
      { from: { lat: 35.86, lng: 104.19 }, to: { lat: 36.20, lng: 138.25 }, value: 3000 },
      { from: { lat: 37.09, lng: -95.71 }, to: { lat: 51.16, lng: 10.45 }, value: 2000 },
    ],
    desc: '飞线数据',
    name: '飞线数据',
    groupKey: 'data',
    groupName: '数据配置',
    useDynamic: true,
    sort: 2,
  },

  // ========== 样式配置 ==========
  earthColor: {
    type: String,
    default: '#0a1628',
    desc: '地球底色',
    name: '地球底色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  landColor: {
    type: String,
    default: '#1a3a5c',
    desc: '陆地颜色',
    name: '陆地颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  markerColor: {
    type: String,
    default: '#00a8e8',
    desc: '标记点颜色',
    name: '标记颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
  },
  flyLineColor: {
    type: String,
    default: '#00d4aa',
    desc: '飞线颜色',
    name: '飞线颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
  },
  earthRadius: {
    type: Number,
    default: 100,
    desc: '地球半径',
    name: '地球半径',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 5,
    min: 50,
    max: 200,
  },

  // ========== 动画配置 ==========
  autoRotate: {
    type: Boolean,
    default: true,
    desc: '自动旋转',
    name: '自动旋转',
    groupKey: 'animation',
    groupName: '动画配置',
    sort: 1,
  },
  rotateSpeed: {
    type: Number,
    default: 0.2,
    desc: '旋转速度',
    name: '旋转速度',
    groupKey: 'animation',
    groupName: '动画配置',
    sort: 2,
  },
  flyLineSpeed: {
    type: Number,
    default: 1,
    desc: '飞线速度',
    name: '飞线速度',
    groupKey: 'animation',
    groupName: '动画配置',
    sort: 3,
  },
});

const emit = defineEmits(['marker-click', 'ready']);

const containerRef = ref(null);
const canvasRef = ref(null);
const hoverData = ref(null);
const showFlyLines = ref(true);
const showHeatmap = ref(true);
const showLabels = ref(true);

let scene, camera, renderer, controls;
let earth, markers = [], flyLines = [];
let raycaster, mouse;

// 经纬度转3D坐标
const latLngToVector3 = (lat, lng, radius) => {
  const phi = (90 - lat) * (Math.PI / 180);
  const theta = (lng + 180) * (Math.PI / 180);

  const x = -radius * Math.sin(phi) * Math.cos(theta);
  const y = radius * Math.cos(phi);
  const z = radius * Math.sin(phi) * Math.sin(theta);

  return new THREE.Vector3(x, y, z);
};

// 初始化场景
const initScene = () => {
  const container = containerRef.value;
  const width = container.clientWidth;
  const height = container.clientHeight;

  // 场景
  scene = markRaw(new THREE.Scene());
  scene.background = new THREE.Color('#050a15');

  // 相机
  camera = markRaw(new THREE.PerspectiveCamera(60, width / height, 1, 2000));
  camera.position.set(0, 100, 250);

  // 渲染器
  renderer = markRaw(new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    antialias: true,
    alpha: true,
  }));
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // 控制器
  controls = markRaw(new OrbitControls(camera, renderer.domElement));
  controls.enableDamping = true;
  controls.autoRotate = props.autoRotate;
  controls.autoRotateSpeed = props.rotateSpeed;
  controls.minDistance = 150;
  controls.maxDistance = 500;
  controls.enablePan = false;

  // 射线检测
  raycaster = markRaw(new THREE.Raycaster());
  mouse = markRaw(new THREE.Vector2());

  // 添加灯光
  addLights();

  // 创建地球
  createEarth();

  // 创建标记点
  createMarkers();

  // 创建飞线
  createFlyLines();

  // 创建星空背景
  createStars();

  // 事件监听
  renderer.domElement.addEventListener('mousemove', handleMouseMove);
  renderer.domElement.addEventListener('click', handleClick);

  emit('ready', { scene, camera, renderer });
};

// 添加灯光
const addLights = () => {
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.3);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
  directionalLight.position.set(100, 200, 100);
  scene.add(directionalLight);

  // 蓝色调补光
  const blueLight = new THREE.PointLight(0x4a90e2, 0.5, 500);
  blueLight.position.set(-100, 50, -100);
  scene.add(blueLight);
};

// 创建地球
const createEarth = () => {
  // 地球主体
  const earthGeometry = new THREE.SphereGeometry(props.earthRadius, 64, 64);
  const earthMaterial = new THREE.MeshStandardMaterial({
    color: props.earthColor,
    roughness: 0.8,
    metalness: 0.2,
  });
  earth = new THREE.Mesh(earthGeometry, earthMaterial);
  scene.add(earth);

  // 大气层光晕
  const atmosphereGeometry = new THREE.SphereGeometry(props.earthRadius * 1.05, 64, 64);
  const atmosphereMaterial = new THREE.ShaderMaterial({
    vertexShader: `
      varying vec3 vNormal;
      void main() {
        vNormal = normalize(normalMatrix * normal);
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: `
      varying vec3 vNormal;
      void main() {
        float intensity = pow(0.7 - dot(vNormal, vec3(0.0, 0.0, 1.0)), 2.0);
        gl_FragColor = vec4(0.0, 0.66, 0.91, 1.0) * intensity;
      }
    `,
    blending: THREE.AdditiveBlending,
    side: THREE.BackSide,
    transparent: true,
  });
  const atmosphere = new THREE.Mesh(atmosphereGeometry, atmosphereMaterial);
  scene.add(atmosphere);

  // 经纬网格
  const gridMaterial = new THREE.LineBasicMaterial({
    color: 0x00a8e8,
    transparent: true,
    opacity: 0.15,
  });

  // 经线
  for (let i = 0; i < 24; i++) {
    const curve = new THREE.EllipseCurve(0, 0, props.earthRadius + 0.1, props.earthRadius + 0.1, 0, Math.PI * 2, false, 0);
    const points = curve.getPoints(64);
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    const line = new THREE.Line(geometry, gridMaterial);
    line.rotation.y = (i / 24) * Math.PI * 2;
    scene.add(line);
  }

  // 纬线
  for (let i = 1; i < 12; i++) {
    const radius = props.earthRadius * Math.cos((i / 12) * Math.PI);
    const y = props.earthRadius * Math.sin((i / 12) * Math.PI);
    const geometry = new THREE.RingGeometry(radius - 0.1, radius + 0.1, 64);
    const ring = new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({
      color: 0x00a8e8,
      transparent: true,
      opacity: 0.1,
      side: THREE.DoubleSide,
    }));
    ring.position.y = y;
    ring.rotation.x = Math.PI / 2;
    scene.add(ring);
  }
};

// 创建标记点
const createMarkers = () => {
  markers.forEach(m => scene.remove(m));
  markers = [];

  props.countryData.forEach((data) => {
    const position = latLngToVector3(data.lat, data.lng, props.earthRadius);

    // 标记点
    const markerGeometry = new THREE.SphereGeometry(2, 16, 16);
    const markerMaterial = new THREE.MeshBasicMaterial({
      color: props.markerColor,
    });
    const marker = new THREE.Mesh(markerGeometry, markerMaterial);
    marker.position.copy(position);
    marker.userData = data;
    scene.add(marker);
    markers.push(marker);

    // 发光光柱
    const pillarGeometry = new THREE.CylinderGeometry(0.5, 2, 15, 8);
    const pillarMaterial = new THREE.MeshBasicMaterial({
      color: props.markerColor,
      transparent: true,
      opacity: 0.6,
    });
    const pillar = new THREE.Mesh(pillarGeometry, pillarMaterial);
    pillar.position.copy(position.clone().multiplyScalar(1.075));
    pillar.lookAt(0, 0, 0);
    pillar.rotateX(Math.PI / 2);
    scene.add(pillar);
    markers.push(pillar);

    // 波纹效果
    const ringGeometry = new THREE.RingGeometry(2, 4, 32);
    const ringMaterial = new THREE.MeshBasicMaterial({
      color: props.markerColor,
      transparent: true,
      opacity: 0.5,
      side: THREE.DoubleSide,
    });
    const ring = new THREE.Mesh(ringGeometry, ringMaterial);
    ring.position.copy(position);
    ring.lookAt(0, 0, 0);
    ring.userData.isRing = true;
    ring.userData.baseScale = 1;
    scene.add(ring);
    markers.push(ring);
  });
};

// 创建飞线
const createFlyLines = () => {
  flyLines.forEach(f => scene.remove(f));
  flyLines = [];

  props.flyLineData.forEach((data) => {
    const startPoint = latLngToVector3(data.from.lat, data.from.lng, props.earthRadius);
    const endPoint = latLngToVector3(data.to.lat, data.to.lng, props.earthRadius);

    // 计算贝塞尔曲线控制点
    const midPoint = new THREE.Vector3().addVectors(startPoint, endPoint).multiplyScalar(0.5);
    const distance = startPoint.distanceTo(endPoint);
    midPoint.normalize().multiplyScalar(props.earthRadius + distance * 0.3);

    // 创建曲线
    const curve = new THREE.QuadraticBezierCurve3(startPoint, midPoint, endPoint);
    const points = curve.getPoints(100);

    // 飞线几何体
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    const material = new THREE.LineBasicMaterial({
      color: props.flyLineColor,
      transparent: true,
      opacity: 0.8,
    });
    const line = new THREE.Line(geometry, material);
    line.userData.curve = curve;
    line.userData.progress = Math.random();
    scene.add(line);
    flyLines.push(line);

    // 飞线上的移动点
    const dotGeometry = new THREE.SphereGeometry(1.5, 8, 8);
    const dotMaterial = new THREE.MeshBasicMaterial({
      color: props.flyLineColor,
    });
    const dot = new THREE.Mesh(dotGeometry, dotMaterial);
    dot.userData.curve = curve;
    dot.userData.progress = Math.random();
    scene.add(dot);
    flyLines.push(dot);
  });
};

// 创建星空背景
const createStars = () => {
  const starsGeometry = new THREE.BufferGeometry();
  const starPositions = [];

  for (let i = 0; i < 2000; i++) {
    const x = (Math.random() - 0.5) * 2000;
    const y = (Math.random() - 0.5) * 2000;
    const z = (Math.random() - 0.5) * 2000;
    starPositions.push(x, y, z);
  }

  starsGeometry.setAttribute('position', new THREE.Float32BufferAttribute(starPositions, 3));
  const starsMaterial = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 1,
    transparent: true,
    opacity: 0.8,
  });
  const stars = new THREE.Points(starsGeometry, starsMaterial);
  scene.add(stars);
};

// 鼠标移动处理
const handleMouseMove = (event) => {
  const rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(markers.filter(m => !m.userData.isRing));

  if (intersects.length > 0) {
    const data = intersects[0].object.userData;
    hoverData.value = {
      x: event.clientX - rect.left,
      y: event.clientY - rect.top,
      name: data.name,
      value: data.value?.toLocaleString() || '-',
    };
    renderer.domElement.style.cursor = 'pointer';
  } else {
    hoverData.value = null;
    renderer.domElement.style.cursor = 'default';
  }
};

// 点击处理
const handleClick = (event) => {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(markers.filter(m => !m.userData.isRing));

  if (intersects.length > 0) {
    emit('marker-click', intersects[0].object.userData);
  }
};

// 动画循环
let time = 0;
const animate = () => {
  requestAnimationFrame(animate);
  time += 0.01;

  controls.update();

  // 更新飞线动画
  flyLines.forEach((obj) => {
    if (obj.userData.curve) {
      obj.userData.progress += 0.005 * props.flyLineSpeed;
      if (obj.userData.progress > 1) obj.userData.progress = 0;

      if (obj.type === 'Mesh') {
        const point = obj.userData.curve.getPoint(obj.userData.progress);
        obj.position.copy(point);
      }
    }
  });

  // 更新波纹动画
  markers.forEach((marker) => {
    if (marker.userData.isRing) {
      const scale = 1 + Math.sin(time * 3) * 0.3;
      marker.scale.set(scale, scale, 1);
      marker.material.opacity = 0.5 - Math.sin(time * 3) * 0.3;
    }
  });

  renderer.render(scene, camera);
};

// 窗口大小变化
const handleResize = () => {
  if (!containerRef.value) return;
  const width = containerRef.value.clientWidth;
  const height = containerRef.value.clientHeight;
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
};

// 清理资源
const dispose = () => {
  markers.forEach(m => {
    m.geometry?.dispose();
    m.material?.dispose();
    scene.remove(m);
  });
  flyLines.forEach(f => {
    f.geometry?.dispose();
    f.material?.dispose();
    scene.remove(f);
  });
  renderer?.dispose();
  controls?.dispose();
};

watch(() => props.countryData, () => {
  createMarkers();
}, { deep: true });

watch(() => props.flyLineData, () => {
  createFlyLines();
}, { deep: true });

watch(showFlyLines, (value) => {
  flyLines.forEach(f => f.visible = value);
});

onMounted(() => {
  initScene();
  animate();
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  dispose();
});

defineExpose({ scene: () => scene, camera: () => camera, renderer: () => renderer });
</script>

<style lang="scss" scoped>
.earth-3d-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: radial-gradient(ellipse at center, #0a1628 0%, #050a15 100%);

  canvas {
    display: block;
    width: 100%;
    height: 100%;
  }
}

.hover-panel {
  position: absolute;
  padding: 12px 16px;
  background: rgba(5, 25, 55, 0.95);
  border: 1px solid rgba(0, 168, 232, 0.5);
  border-radius: 8px;
  pointer-events: none;
  transform: translate(10px, -50%);
  z-index: 100;

  .country-name {
    font-size: 14px;
    color: #ffffff;
    margin-bottom: 4px;
  }

  .country-value {
    font-size: 20px;
    font-weight: bold;
    color: #00a8e8;
  }
}

.control-panel {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;

  button {
    padding: 8px 20px;
    background: rgba(0, 168, 232, 0.2);
    border: 1px solid rgba(0, 168, 232, 0.4);
    border-radius: 20px;
    color: rgba(255, 255, 255, 0.7);
    font-size: 13px;
    cursor: pointer;
    transition: all 0.3s;

    &:hover {
      background: rgba(0, 168, 232, 0.3);
    }

    &.active {
      background: #00a8e8;
      border-color: #00a8e8;
      color: #ffffff;
    }
  }
}
</style>
```

---

## 四、3D 粒子系统组件 (Particle3D)

炫酷粒子特效组件，支持数据可视化粒子、科技感粒子流等效果。

```vue
<template>
  <div ref="containerRef" class="particle-3d-container">
    <canvas ref="canvasRef"></canvas>

    <!-- 数据展示 -->
    <div v-if="showStats" class="stats-panel">
      <div class="stat-item">
        <span class="stat-label">粒子数量</span>
        <span class="stat-value">{{ particleCount.toLocaleString() }}</span>
      </div>
      <div class="stat-item">
        <span class="stat-label">FPS</span>
        <span class="stat-value">{{ fps }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, markRaw, computed } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  particleCount: {
    type: Number,
    default: 10000,
    desc: '粒子数量',
    name: '粒子数量',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 1,
    min: 1000,
    max: 100000,
  },
  dataSource: {
    type: Array,
    default: () => null,
    desc: '数据源（可选，用于数据驱动粒子）',
    name: '数据源',
    groupKey: 'data',
    groupName: '数据配置',
    useDynamic: true,
    sort: 2,
  },

  // ========== 样式配置 ==========
  particleColor: {
    type: String,
    default: '#00a8e8',
    desc: '粒子主色',
    name: '粒子颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  particleColor2: {
    type: String,
    default: '#00d4aa',
    desc: '粒子渐变色',
    name: '渐变颜色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  particleSize: {
    type: Number,
    default: 2,
    desc: '粒子大小',
    name: '粒子大小',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
    min: 0.5,
    max: 10,
  },
  particleShape: {
    type: String,
    default: 'sphere',
    desc: '粒子分布形状：sphere-球形, cube-立方体, cone-锥形, spiral-螺旋',
    name: '分布形状',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
    configurationTemplate: [
      { value: 'sphere', label: '球形' },
      { value: 'cube', label: '立方体' },
      { value: 'cone', label: '锥形' },
      { value: 'spiral', label: '螺旋' },
    ],
  },
  spreadRadius: {
    type: Number,
    default: 200,
    desc: '扩散半径',
    name: '扩散半径',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 5,
    min: 50,
    max: 500,
  },

  // ========== 动画配置 ==========
  animationType: {
    type: String,
    default: 'flow',
    desc: '动画类型：flow-流动, explode-爆炸, wave-波动, orbit-环绕',
    name: '动画类型',
    groupKey: 'animation',
    groupName: '动画配置',
    sort: 1,
    configurationTemplate: [
      { value: 'flow', label: '流动' },
      { value: 'explode', label: '爆炸' },
      { value: 'wave', label: '波动' },
      { value: 'orbit', label: '环绕' },
    ],
  },
  animationSpeed: {
    type: Number,
    default: 1,
    desc: '动画速度',
    name: '动画速度',
    groupKey: 'animation',
    groupName: '动画配置',
    sort: 2,
    min: 0.1,
    max: 5,
  },
  enableGlow: {
    type: Boolean,
    default: true,
    desc: '是否启用发光',
    name: '发光效果',
    groupKey: 'animation',
    groupName: '动画配置',
    sort: 3,
  },

  // ========== 显示配置 ==========
  showStats: {
    type: Boolean,
    default: false,
    desc: '显示统计信息',
    name: '统计面板',
    groupKey: 'display',
    groupName: '显示配置',
    sort: 1,
  },
  autoRotate: {
    type: Boolean,
    default: true,
    desc: '自动旋转',
    name: '自动旋转',
    groupKey: 'display',
    groupName: '显示配置',
    sort: 2,
  },
});

const emit = defineEmits(['ready', 'particle-click']);

const containerRef = ref(null);
const canvasRef = ref(null);
const fps = ref(60);

let scene, camera, renderer, controls;
let particles, particleGeometry, particleMaterial;
let positions, colors, velocities;
let lastTime = performance.now();
let frameCount = 0;

// 初始化场景
const initScene = () => {
  const container = containerRef.value;
  const width = container.clientWidth;
  const height = container.clientHeight;

  // 场景
  scene = markRaw(new THREE.Scene());
  scene.background = new THREE.Color('#050a15');

  // 相机
  camera = markRaw(new THREE.PerspectiveCamera(75, width / height, 1, 2000));
  camera.position.set(0, 0, 300);

  // 渲染器
  renderer = markRaw(new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    antialias: true,
  }));
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // 控制器
  controls = markRaw(new OrbitControls(camera, renderer.domElement));
  controls.enableDamping = true;
  controls.autoRotate = props.autoRotate;
  controls.autoRotateSpeed = 0.5;

  // 创建粒子
  createParticles();

  // 添加环境光
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
  scene.add(ambientLight);

  emit('ready', { scene, camera, renderer });
};

// 创建粒子
const createParticles = () => {
  if (particles) {
    scene.remove(particles);
    particleGeometry.dispose();
    particleMaterial.dispose();
  }

  particleGeometry = new THREE.BufferGeometry();
  positions = new Float32Array(props.particleCount * 3);
  colors = new Float32Array(props.particleCount * 3);
  velocities = new Float32Array(props.particleCount * 3);

  const color1 = new THREE.Color(props.particleColor);
  const color2 = new THREE.Color(props.particleColor2);

  for (let i = 0; i < props.particleCount; i++) {
    const i3 = i * 3;

    // 根据形状生成位置
    let x, y, z;
    switch (props.particleShape) {
      case 'sphere':
        const phi = Math.random() * Math.PI * 2;
        const theta = Math.acos(2 * Math.random() - 1);
        const r = props.spreadRadius * Math.cbrt(Math.random());
        x = r * Math.sin(theta) * Math.cos(phi);
        y = r * Math.sin(theta) * Math.sin(phi);
        z = r * Math.cos(theta);
        break;

      case 'cube':
        x = (Math.random() - 0.5) * props.spreadRadius * 2;
        y = (Math.random() - 0.5) * props.spreadRadius * 2;
        z = (Math.random() - 0.5) * props.spreadRadius * 2;
        break;

      case 'cone':
        const angle = Math.random() * Math.PI * 2;
        const height = Math.random() * props.spreadRadius;
        const radius = height * 0.5;
        x = Math.cos(angle) * radius;
        y = height - props.spreadRadius / 2;
        z = Math.sin(angle) * radius;
        break;

      case 'spiral':
        const t = i / props.particleCount;
        const spiralAngle = t * Math.PI * 20;
        const spiralRadius = t * props.spreadRadius;
        x = Math.cos(spiralAngle) * spiralRadius;
        y = (t - 0.5) * props.spreadRadius * 2;
        z = Math.sin(spiralAngle) * spiralRadius;
        break;
    }

    positions[i3] = x;
    positions[i3 + 1] = y;
    positions[i3 + 2] = z;

    // 随机颜色渐变
    const mixRatio = Math.random();
    const mixedColor = color1.clone().lerp(color2, mixRatio);
    colors[i3] = mixedColor.r;
    colors[i3 + 1] = mixedColor.g;
    colors[i3 + 2] = mixedColor.b;

    // 初始速度
    velocities[i3] = (Math.random() - 0.5) * 0.5;
    velocities[i3 + 1] = (Math.random() - 0.5) * 0.5;
    velocities[i3 + 2] = (Math.random() - 0.5) * 0.5;
  }

  particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  particleGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  // 粒子材质
  particleMaterial = new THREE.PointsMaterial({
    size: props.particleSize,
    vertexColors: true,
    transparent: true,
    opacity: 0.8,
    blending: props.enableGlow ? THREE.AdditiveBlending : THREE.NormalBlending,
    sizeAttenuation: true,
  });

  particles = new THREE.Points(particleGeometry, particleMaterial);
  scene.add(particles);
};

// 更新粒子动画
const updateParticles = (time) => {
  const positionAttribute = particleGeometry.getAttribute('position');

  for (let i = 0; i < props.particleCount; i++) {
    const i3 = i * 3;

    switch (props.animationType) {
      case 'flow':
        // 流动效果
        positionAttribute.array[i3] += velocities[i3] * props.animationSpeed;
        positionAttribute.array[i3 + 1] += velocities[i3 + 1] * props.animationSpeed;
        positionAttribute.array[i3 + 2] += velocities[i3 + 2] * props.animationSpeed;

        // 边界检测
        const dist = Math.sqrt(
          positionAttribute.array[i3] ** 2 +
          positionAttribute.array[i3 + 1] ** 2 +
          positionAttribute.array[i3 + 2] ** 2
        );
        if (dist > props.spreadRadius) {
          positionAttribute.array[i3] *= 0.95;
          positionAttribute.array[i3 + 1] *= 0.95;
          positionAttribute.array[i3 + 2] *= 0.95;
        }
        break;

      case 'explode':
        // 爆炸效果
        const explodeSpeed = Math.sin(time * 0.001) * 0.5 + 0.5;
        const dir = new THREE.Vector3(
          positionAttribute.array[i3],
          positionAttribute.array[i3 + 1],
          positionAttribute.array[i3 + 2]
        ).normalize();
        positionAttribute.array[i3] += dir.x * explodeSpeed * props.animationSpeed;
        positionAttribute.array[i3 + 1] += dir.y * explodeSpeed * props.animationSpeed;
        positionAttribute.array[i3 + 2] += dir.z * explodeSpeed * props.animationSpeed;
        break;

      case 'wave':
        // 波动效果
        const waveX = positionAttribute.array[i3];
        const waveZ = positionAttribute.array[i3 + 2];
        positionAttribute.array[i3 + 1] = Math.sin(waveX * 0.05 + time * 0.002 * props.animationSpeed) * 20 +
                                          Math.sin(waveZ * 0.05 + time * 0.002 * props.animationSpeed) * 20;
        break;

      case 'orbit':
        // 环绕效果
        const orbitAngle = time * 0.001 * props.animationSpeed;
        const originalX = positions[i3];
        const originalZ = positions[i3 + 2];
        positionAttribute.array[i3] = originalX * Math.cos(orbitAngle) - originalZ * Math.sin(orbitAngle);
        positionAttribute.array[i3 + 2] = originalX * Math.sin(orbitAngle) + originalZ * Math.cos(orbitAngle);
        break;
    }
  }

  positionAttribute.needsUpdate = true;
};

// 动画循环
const animate = (time) => {
  requestAnimationFrame(animate);

  // FPS 计算
  frameCount++;
  if (time - lastTime >= 1000) {
    fps.value = frameCount;
    frameCount = 0;
    lastTime = time;
  }

  controls.update();
  updateParticles(time);
  renderer.render(scene, camera);
};

// 窗口大小变化
const handleResize = () => {
  if (!containerRef.value) return;
  const width = containerRef.value.clientWidth;
  const height = containerRef.value.clientHeight;
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
};

// 清理资源
const dispose = () => {
  particleGeometry?.dispose();
  particleMaterial?.dispose();
  renderer?.dispose();
  controls?.dispose();
};

watch(() => [props.particleCount, props.particleShape, props.spreadRadius], () => {
  createParticles();
});

watch(() => props.particleColor, () => {
  createParticles();
});

watch(() => props.particleSize, (value) => {
  if (particleMaterial) particleMaterial.size = value;
});

onMounted(() => {
  initScene();
  animate(0);
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  dispose();
});

defineExpose({ scene: () => scene, camera: () => camera, renderer: () => renderer });
</script>

<style lang="scss" scoped>
.particle-3d-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: #050a15;

  canvas {
    display: block;
    width: 100%;
    height: 100%;
  }
}

.stats-panel {
  position: absolute;
  top: 20px;
  left: 20px;
  padding: 16px;
  background: rgba(5, 25, 55, 0.9);
  border: 1px solid rgba(0, 168, 232, 0.3);
  border-radius: 8px;

  .stat-item {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 8px;

    &:last-child {
      margin-bottom: 0;
    }

    .stat-label {
      font-size: 12px;
      color: rgba(255, 255, 255, 0.6);
    }

    .stat-value {
      font-size: 14px;
      font-weight: bold;
      color: #00a8e8;
    }
  }
}
</style>
```

---

## 五、GLTF 模型加载组件 (Model3D)

加载外部 3D 模型文件（GLTF/GLB/FBX/OBJ），支持模型动画、材质配置。

```vue
<template>
  <div ref="containerRef" class="model-3d-container">
    <canvas ref="canvasRef"></canvas>

    <!-- 加载进度 -->
    <div v-if="loading" class="loading-panel">
      <div class="loading-bar">
        <div class="loading-progress" :style="{ width: loadProgress + '%' }"></div>
      </div>
      <span class="loading-text">{{ loadProgress }}%</span>
    </div>

    <!-- 模型信息面板 -->
    <div v-if="modelInfo && showInfo" class="model-info-panel">
      <div class="info-title">模型信息</div>
      <div class="info-row">
        <span>顶点数：</span>
        <span>{{ modelInfo.vertices?.toLocaleString() }}</span>
      </div>
      <div class="info-row">
        <span>面数：</span>
        <span>{{ modelInfo.faces?.toLocaleString() }}</span>
      </div>
      <div class="info-row">
        <span>材质数：</span>
        <span>{{ modelInfo.materials }}</span>
      </div>
    </div>

    <!-- 控制面板 -->
    <div class="control-panel">
      <button @click="resetCamera">重置视角</button>
      <button @click="toggleWireframe">{{ wireframe ? '实体' : '线框' }}</button>
      <button @click="toggleAnimation">{{ animationPlaying ? '暂停' : '播放' }}</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, markRaw } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';
import i18n from './locale/index';

const props = defineProps({
  // ========== 数据配置 ==========
  modelUrl: {
    type: String,
    default: '',
    desc: '模型文件URL（支持 .gltf/.glb/.fbx/.obj）',
    name: '模型URL',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 1,
  },
  modelScale: {
    type: Number,
    default: 1,
    desc: '模型缩放比例',
    name: '模型缩放',
    groupKey: 'data',
    groupName: '数据配置',
    sort: 2,
    min: 0.01,
    max: 100,
  },

  // ========== 样式配置 ==========
  backgroundColor: {
    type: String,
    default: '#0a1628',
    desc: '背景颜色',
    name: '背景色',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 1,
  },
  ambientLightIntensity: {
    type: Number,
    default: 0.5,
    desc: '环境光强度',
    name: '环境光',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 2,
  },
  directionalLightIntensity: {
    type: Number,
    default: 1,
    desc: '主光源强度',
    name: '主光源',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 3,
  },
  enableShadow: {
    type: Boolean,
    default: true,
    desc: '启用阴影',
    name: '阴影',
    groupKey: 'style',
    groupName: '样式配置',
    sort: 4,
  },

  // ========== 相机配置 ==========
  cameraPosition: {
    type: Object,
    default: () => ({ x: 0, y: 50, z: 100 }),
    desc: '相机位置',
    name: '相机位置',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 1,
  },
  autoRotate: {
    type: Boolean,
    default: true,
    desc: '自动旋转',
    name: '自动旋转',
    groupKey: 'camera',
    groupName: '相机配置',
    sort: 2,
  },

  // ========== 显示配置 ==========
  showInfo: {
    type: Boolean,
    default: true,
    desc: '显示模型信息',
    name: '模型信息',
    groupKey: 'display',
    groupName: '显示配置',
    sort: 1,
  },
  showGrid: {
    type: Boolean,
    default: true,
    desc: '显示网格',
    name: '网格',
    groupKey: 'display',
    groupName: '显示配置',
    sort: 2,
  },
});

const emit = defineEmits(['ready', 'load-progress', 'load-complete', 'error']);

const containerRef = ref(null);
const canvasRef = ref(null);
const loading = ref(false);
const loadProgress = ref(0);
const modelInfo = ref(null);
const wireframe = ref(false);
const animationPlaying = ref(true);

let scene, camera, renderer, controls;
let model = null;
let mixer = null;
let clock = null;
let animations = [];

// 初始化场景
const initScene = () => {
  const container = containerRef.value;
  const width = container.clientWidth;
  const height = container.clientHeight;

  // 场景
  scene = markRaw(new THREE.Scene());
  scene.background = new THREE.Color(props.backgroundColor);

  // 相机
  camera = markRaw(new THREE.PerspectiveCamera(50, width / height, 0.1, 10000));
  camera.position.set(props.cameraPosition.x, props.cameraPosition.y, props.cameraPosition.z);

  // 渲染器
  renderer = markRaw(new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    antialias: true,
    alpha: true,
  }));
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = props.enableShadow;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1;

  // 控制器
  controls = markRaw(new OrbitControls(camera, renderer.domElement));
  controls.enableDamping = true;
  controls.autoRotate = props.autoRotate;
  controls.autoRotateSpeed = 1;

  // 添加灯光
  addLights();

  // 添加网格
  if (props.showGrid) {
    addGrid();
  }

  // 时钟
  clock = markRaw(new THREE.Clock());

  // 加载模型
  if (props.modelUrl) {
    loadModel(props.modelUrl);
  }

  emit('ready', { scene, camera, renderer });
};

// 添加灯光
const addLights = () => {
  // 环境光
  const ambientLight = new THREE.AmbientLight(0xffffff, props.ambientLightIntensity);
  scene.add(ambientLight);

  // 主光源
  const mainLight = new THREE.DirectionalLight(0xffffff, props.directionalLightIntensity);
  mainLight.position.set(100, 200, 100);
  mainLight.castShadow = props.enableShadow;
  mainLight.shadow.mapSize.width = 2048;
  mainLight.shadow.mapSize.height = 2048;
  mainLight.shadow.camera.near = 0.5;
  mainLight.shadow.camera.far = 500;
  mainLight.shadow.camera.left = -100;
  mainLight.shadow.camera.right = 100;
  mainLight.shadow.camera.top = 100;
  mainLight.shadow.camera.bottom = -100;
  scene.add(mainLight);

  // 补光
  const fillLight = new THREE.DirectionalLight(0x4a90e2, 0.3);
  fillLight.position.set(-50, 50, -50);
  scene.add(fillLight);

  // 背光
  const backLight = new THREE.DirectionalLight(0xffffff, 0.2);
  backLight.position.set(0, 50, -100);
  scene.add(backLight);
};

// 添加网格
const addGrid = () => {
  const gridHelper = new THREE.GridHelper(200, 20, 0x00a8e8, 0x0d1b2a);
  gridHelper.material.opacity = 0.3;
  gridHelper.material.transparent = true;
  scene.add(gridHelper);
};

// 加载模型
const loadModel = (url) => {
  loading.value = true;
  loadProgress.value = 0;

  const extension = url.split('.').pop().toLowerCase();

  let loader;
  switch (extension) {
    case 'gltf':
    case 'glb':
      loader = new GLTFLoader();
      // 配置 DRACO 解码器（用于压缩模型）
      const dracoLoader = new DRACOLoader();
      dracoLoader.setDecoderPath('https://www.gstatic.com/draco/versioned/decoders/1.5.6/');
      loader.setDRACOLoader(dracoLoader);
      break;
    case 'fbx':
      loader = new FBXLoader();
      break;
    case 'obj':
      loader = new OBJLoader();
      break;
    default:
      emit('error', `不支持的模型格式: ${extension}`);
      loading.value = false;
      return;
  }

  loader.load(
    url,
    (result) => {
      // 处理不同格式的加载结果
      if (extension === 'gltf' || extension === 'glb') {
        model = result.scene;
        animations = result.animations || [];
      } else {
        model = result;
      }

      // 应用缩放
      model.scale.set(props.modelScale, props.modelScale, props.modelScale);

      // 计算模型边界框并居中
      const box = new THREE.Box3().setFromObject(model);
      const center = box.getCenter(new THREE.Vector3());
      model.position.sub(center);

      // 启用阴影
      if (props.enableShadow) {
        model.traverse((child) => {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
          }
        });
      }

      scene.add(model);

      // 计算模型信息
      calculateModelInfo();

      // 设置动画
      if (animations.length > 0) {
        mixer = new THREE.AnimationMixer(model);
        animations.forEach((clip) => {
          mixer.clipAction(clip).play();
        });
      }

      // 调整相机位置
      fitCameraToModel();

      loading.value = false;
      loadProgress.value = 100;
      emit('load-complete', model);
    },
    (progress) => {
      if (progress.lengthComputable) {
        loadProgress.value = Math.round((progress.loaded / progress.total) * 100);
        emit('load-progress', loadProgress.value);
      }
    },
    (error) => {
      console.error('模型加载失败:', error);
      emit('error', error.message);
      loading.value = false;
    }
  );
};

// 计算模型信息
const calculateModelInfo = () => {
  let vertices = 0;
  let faces = 0;
  let materials = new Set();

  model.traverse((child) => {
    if (child.isMesh) {
      const geometry = child.geometry;
      if (geometry.attributes.position) {
        vertices += geometry.attributes.position.count;
      }
      if (geometry.index) {
        faces += geometry.index.count / 3;
      } else if (geometry.attributes.position) {
        faces += geometry.attributes.position.count / 3;
      }
      if (child.material) {
        if (Array.isArray(child.material)) {
          child.material.forEach(m => materials.add(m));
        } else {
          materials.add(child.material);
        }
      }
    }
  });

  modelInfo.value = {
    vertices: Math.round(vertices),
    faces: Math.round(faces),
    materials: materials.size,
  };
};

// 调整相机位置以适应模型
const fitCameraToModel = () => {
  if (!model) return;

  const box = new THREE.Box3().setFromObject(model);
  const size = box.getSize(new THREE.Vector3());
  const maxDim = Math.max(size.x, size.y, size.z);

  const fov = camera.fov * (Math.PI / 180);
  let cameraDistance = maxDim / (2 * Math.tan(fov / 2));
  cameraDistance *= 1.5; // 留出一些空间

  camera.position.set(cameraDistance, cameraDistance * 0.5, cameraDistance);
  controls.target.set(0, 0, 0);
  controls.update();
};

// 重置相机
const resetCamera = () => {
  fitCameraToModel();
};

// 切换线框模式
const toggleWireframe = () => {
  wireframe.value = !wireframe.value;
  model?.traverse((child) => {
    if (child.isMesh && child.material) {
      if (Array.isArray(child.material)) {
        child.material.forEach(m => m.wireframe = wireframe.value);
      } else {
        child.material.wireframe = wireframe.value;
      }
    }
  });
};

// 切换动画播放
const toggleAnimation = () => {
  animationPlaying.value = !animationPlaying.value;
  if (mixer) {
    if (animationPlaying.value) {
      animations.forEach((clip) => {
        mixer.clipAction(clip).play();
      });
    } else {
      mixer.stopAllAction();
    }
  }
};

// 动画循环
const animate = () => {
  requestAnimationFrame(animate);

  const delta = clock.getDelta();
  controls.update();

  if (mixer && animationPlaying.value) {
    mixer.update(delta);
  }

  renderer.render(scene, camera);
};

// 窗口大小变化
const handleResize = () => {
  if (!containerRef.value) return;
  const width = containerRef.value.clientWidth;
  const height = containerRef.value.clientHeight;
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
};

// 清理资源
const dispose = () => {
  mixer?.stopAllAction();
  model?.traverse((child) => {
    if (child.geometry) child.geometry.dispose();
    if (child.material) {
      if (Array.isArray(child.material)) {
        child.material.forEach(m => m.dispose());
      } else {
        child.material.dispose();
      }
    }
  });
  renderer?.dispose();
  controls?.dispose();
};

watch(() => props.modelUrl, (url) => {
  if (url && scene) {
    if (model) {
      scene.remove(model);
    }
    loadModel(url);
  }
});

watch(() => props.modelScale, (scale) => {
  if (model) {
    model.scale.set(scale, scale, scale);
  }
});

onMounted(() => {
  initScene();
  animate();
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  dispose();
});

defineExpose({
  scene: () => scene,
  camera: () => camera,
  renderer: () => renderer,
  model: () => model,
  resetCamera,
  toggleWireframe,
  toggleAnimation,
});
</script>

<style lang="scss" scoped>
.model-3d-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: #0a1628;

  canvas {
    display: block;
    width: 100%;
    height: 100%;
  }
}

.loading-panel {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;

  .loading-bar {
    width: 200px;
    height: 4px;
    background: rgba(0, 168, 232, 0.2);
    border-radius: 2px;
    overflow: hidden;

    .loading-progress {
      height: 100%;
      background: linear-gradient(90deg, #00a8e8, #00d4aa);
      transition: width 0.3s;
    }
  }

  .loading-text {
    font-size: 14px;
    color: #00a8e8;
  }
}

.model-info-panel {
  position: absolute;
  top: 20px;
  right: 20px;
  padding: 16px;
  background: rgba(5, 25, 55, 0.9);
  border: 1px solid rgba(0, 168, 232, 0.3);
  border-radius: 8px;
  min-width: 180px;

  .info-title {
    font-size: 14px;
    font-weight: 500;
    color: #ffffff;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(0, 168, 232, 0.2);
  }

  .info-row {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    margin-bottom: 6px;

    span:first-child {
      color: rgba(255, 255, 255, 0.6);
    }

    span:last-child {
      color: #00a8e8;
    }
  }
}

.control-panel {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;

  button {
    padding: 8px 20px;
    background: rgba(0, 168, 232, 0.2);
    border: 1px solid rgba(0, 168, 232, 0.4);
    border-radius: 4px;
    color: #ffffff;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.3s;

    &:hover {
      background: rgba(0, 168, 232, 0.4);
    }
  }
}
</style>
```

---

## 六、使用指南

### 6.1 安装依赖

```bash
# 核心依赖
npm install three @types/three

# 可选依赖
npm install @tweenjs/tween.js stats.js dat.gui
```

### 6.2 组件类型选择

| 组件类型 | 适用场景 | 复杂度 |
|---------|---------|--------|
| **City3D** | 智慧城市、区域规划、建筑可视化 | 中 |
| **Earth3D** | 全球数据、国际贸易、人口迁徙 | 中 |
| **Particle3D** | 科技感背景、数据粒子、特效展示 | 低 |
| **Model3D** | 产品展示、建筑模型、角色动画 | 低 |

### 6.3 性能优化建议

1. **粒子数量控制**：移动端建议 < 10000，桌面端 < 50000
2. **模型优化**：使用 Draco 压缩，减少面数
3. **纹理优化**：使用压缩纹理格式（KTX2）
4. **LOD 策略**：根据距离切换模型精度
5. **实例化渲染**：相同几何体使用 InstancedMesh

### 6.4 资源推荐

- **免费模型**：Sketchfab、Poly Pizza、Turbosquid
- **纹理资源**：Poly Haven、AmbientCG
- **HDRI 环境**：Poly Haven HDRI
