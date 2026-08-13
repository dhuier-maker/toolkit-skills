# Three.js 最佳实践指南

> BI 大屏 3D/WebGL 组件开发最佳实践，涵盖性能优化、资源管理、常见问题解决方案。

---

## 一、性能优化策略

### 1.1 几何体优化

```javascript
// ❌ 不推荐：每个对象独立几何体
objects.forEach(obj => {
  const geometry = new THREE.BoxGeometry(1, 1, 1);
  const material = new THREE.MeshStandardMaterial();
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);
});

// ✅ 推荐：共享几何体和材质
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial();
objects.forEach(obj => {
  const mesh = new THREE.Mesh(geometry, material);
  mesh.position.copy(obj.position);
  scene.add(mesh);
});

// ✅ 更优：使用 InstancedMesh（大量相同几何体）
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial();
const instancedMesh = new THREE.InstancedMesh(geometry, material, count);

const matrix = new THREE.Matrix4();
for (let i = 0; i < count; i++) {
  matrix.setPosition(positions[i]);
  instancedMesh.setMatrixAt(i, matrix);
}
scene.add(instancedMesh);
```

### 1.2 材质优化

```javascript
// ✅ 使用 MeshStandardMaterial 替代 MeshPhongMaterial（PBR 更高效）
const material = new THREE.MeshStandardMaterial({
  color: 0x00a8e8,
  roughness: 0.7,
  metalness: 0.3,
});

// ✅ 避免每帧更新材质属性
// 使用 uniform 或自定义 shader 实现动态效果

// ✅ 合并材质
const mergedMaterial = new THREE.MeshStandardMaterial({
  vertexColors: true, // 使用顶点颜色替代多材质
});
```

### 1.3 渲染优化

```javascript
// ✅ 使用 FrustumCulling（默认开启）
object.frustumCulled = true;

// ✅ 控制渲染距离
camera.near = 1;
camera.far = 1000;

// ✅ 使用 LOD（细节层次）
const lod = new THREE.LOD();
lod.addLevel(highDetailMesh, 0);    // 近距离
lod.addLevel(mediumDetailMesh, 50); // 中距离
lod.addLevel(lowDetailMesh, 100);   // 远距离
scene.add(lod);

// ✅ 按需渲染（非持续动画场景）
let needsRender = true;
function render() {
  if (needsRender) {
    renderer.render(scene, camera);
    needsRender = false;
  }
}
controls.addEventListener('change', () => needsRender = true);
```

### 1.4 粒子系统优化

```javascript
// ✅ 使用 BufferGeometry + Points
const geometry = new THREE.BufferGeometry();
const positions = new Float32Array(count * 3);
geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

const material = new THREE.PointsMaterial({
  size: 2,
  vertexColors: true,
  sizeAttenuation: true,
});

const particles = new THREE.Points(geometry, material);

// ✅ 使用着色器实现高级粒子效果
const vertexShader = `
  attribute float size;
  varying vec3 vColor;
  void main() {
    vColor = color;
    vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
    gl_PointSize = size * (300.0 / -mvPosition.z);
    gl_Position = projectionMatrix * mvPosition;
  }
`;
```

---

## 二、内存管理

### 2.1 资源清理

```javascript
// ✅ 组件卸载时清理资源
onUnmounted(() => {
  // 清理几何体
  geometry?.dispose();

  // 清理材质（包括纹理）
  if (material) {
    if (material.map) material.map.dispose();
    if (material.normalMap) material.normalMap.dispose();
    material.dispose();
  }

  // 清理渲染器
  renderer?.dispose();

  // 清理控制器
  controls?.dispose();

  // 移除事件监听
  window.removeEventListener('resize', handleResize);
});

// ✅ 递归清理场景
function disposeScene(scene) {
  scene.traverse((object) => {
    if (object.geometry) {
      object.geometry.dispose();
    }
    if (object.material) {
      const materials = Array.isArray(object.material)
        ? object.material
        : [object.material];
      materials.forEach((material) => {
        // 清理所有纹理
        Object.keys(material).forEach((key) => {
          if (material[key] && typeof material[key].dispose === 'function') {
            material[key].dispose();
          }
        });
        material.dispose();
      });
    }
  });
}
```

### 2.2 纹理管理

```javascript
// ✅ 使用纹理加载管理器
const loadingManager = new THREE.LoadingManager();
loadingManager.onLoad = () => console.log('所有纹理加载完成');

const textureLoader = new THREE.TextureLoader(loadingManager);

// ✅ 纹理优化
const texture = textureLoader.load('texture.jpg', (tex) => {
  tex.generateMipmaps = false; // 不需要 mipmap 时禁用
  tex.minFilter = THREE.LinearFilter;
  tex.magFilter = THREE.LinearFilter;
});

// ✅ 使用压缩纹理格式（KTX2）
import { KTX2Loader } from 'three/examples/jsm/loaders/KTX2Loader.js';
const ktx2Loader = new KTX2Loader(loadingManager);
ktx2Loader.setTranscoderPath('basis/');
```

---

## 三、Vue 3 集成最佳实践

### 3.1 响应式处理

```javascript
import { ref, onMounted, onUnmounted, markRaw, shallowRef } from 'vue';

// ✅ 使用 markRaw 避免 Three.js 对象被响应式代理
let scene = null;
let camera = null;
let renderer = null;

onMounted(() => {
  scene = markRaw(new THREE.Scene());
  camera = markRaw(new THREE.PerspectiveCamera());
  renderer = markRaw(new THREE.WebGLRenderer());
});

// ✅ 或使用 shallowRef（仅顶层响应式）
const scene = shallowRef(null);
onMounted(() => {
  scene.value = new THREE.Scene();
});
```

### 3.2 Props 监听

```javascript
// ✅ 使用 watch 监听 props 变化
watch(
  () => props.data,
  (newData) => {
    updateScene(newData);
  },
  { deep: true }
);

// ✅ 批量监听多个 props
watch(
  () => [props.color, props.size, props.position],
  () => {
    updateMaterial();
  }
);

// ✅ 使用 watchEffect 自动追踪依赖
watchEffect(() => {
  if (mesh) {
    mesh.material.color.set(props.color);
  }
});
```

### 3.3 生命周期管理

```javascript
// ✅ 完整的生命周期管理
let animationId = null;
let scene, camera, renderer, controls;

onMounted(() => {
  initScene();
  animate();
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  // 停止动画循环
  if (animationId) {
    cancelAnimationFrame(animationId);
  }

  // 移除事件监听
  window.removeEventListener('resize', handleResize);

  // 清理 Three.js 资源
  dispose();
});

const animate = () => {
  animationId = requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
};
```

---

## 四、常见问题与解决方案

### 4.1 模型加载失败

```javascript
// ✅ 错误处理
loader.load(
  modelUrl,
  (gltf) => {
    // 成功回调
    scene.add(gltf.scene);
  },
  (progress) => {
    // 进度回调
    console.log(`加载进度: ${(progress.loaded / progress.total * 100).toFixed(2)}%`);
  },
  (error) => {
    // 错误回调
    console.error('模型加载失败:', error);
    // 显示错误提示或加载默认模型
    loadFallbackModel();
  }
);

// ✅ 跨域问题解决
// 1. 服务器配置 CORS
// 2. 使用代理
// 3. 使用 TextureLoader 的 crossOrigin 属性
textureLoader.crossOrigin = 'anonymous';
```

### 4.2 性能问题排查

```javascript
// ✅ 使用 Stats.js 监控帧率
import Stats from 'stats.js';
const stats = new Stats();
stats.showPanel(0);
document.body.appendChild(stats.dom);

function animate() {
  stats.begin();
  // 渲染代码
  stats.end();
  requestAnimationFrame(animate);
}

// ✅ 使用 Chrome DevTools Performance 分析
// 1. 记录性能剖面
// 2. 查看帧率和脚本执行时间
// 3. 定位性能瓶颈

// ✅ 使用 renderer.info 查看渲染信息
console.log('几何体数量:', renderer.info.memory.geometries);
console.log('纹理数量:', renderer.info.memory.textures);
console.log('绘制调用:', renderer.info.render.calls);
console.log('三角形数量:', renderer.info.render.triangles);
```

### 4.3 黑屏/白屏问题

```javascript
// ✅ 检查相机位置
console.log('相机位置:', camera.position);
console.log('相机朝向:', camera.getWorldDirection(new THREE.Vector3()));

// ✅ 检查场景内容
console.log('场景子对象数量:', scene.children.length);

// ✅ 检查渲染器尺寸
console.log('渲染器尺寸:', renderer.getSize(new THREE.Vector2()));

// ✅ 检查光源
scene.traverse((obj) => {
  if (obj.isLight) {
    console.log('光源:', obj.type, obj.intensity);
  }
});

// ✅ 检查材质
mesh.traverse((obj) => {
  if (obj.isMesh) {
    console.log('材质:', obj.material.type, obj.material.visible);
  }
});
```

### 4.4 模型尺寸问题

```javascript
// ✅ 自动调整模型大小
function fitModelToView(model, targetSize = 100) {
  const box = new THREE.Box3().setFromObject(model);
  const size = box.getSize(new THREE.Vector3());
  const maxDim = Math.max(size.x, size.y, size.z);
  const scale = targetSize / maxDim;
  model.scale.set(scale, scale, scale);
}

// ✅ 居中模型
function centerModel(model) {
  const box = new THREE.Box3().setFromObject(model);
  const center = box.getCenter(new THREE.Vector3());
  model.position.sub(center);
}

// ✅ 调整相机以适应模型
function fitCameraToModel(camera, controls, model) {
  const box = new THREE.Box3().setFromObject(model);
  const size = box.getSize(new THREE.Vector3());
  const center = box.getCenter(new THREE.Vector3());

  const maxDim = Math.max(size.x, size.y, size.z);
  const fov = camera.fov * (Math.PI / 180);
  let cameraDistance = maxDim / (2 * Math.tan(fov / 2));
  cameraDistance *= 1.5;

  camera.position.set(
    center.x + cameraDistance,
    center.y + cameraDistance * 0.5,
    center.z + cameraDistance
  );
  controls.target.copy(center);
  controls.update();
}
```

---

## 五、高级技巧

### 5.1 后处理效果

```javascript
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';

// ✅ 创建后处理器
const composer = new EffectComposer(renderer);
const renderPass = new RenderPass(scene, camera);
composer.addPass(renderPass);

// 添加发光效果
const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  0.5,  // 强度
  0.4,  // 半径
  0.85  // 阈值
);
composer.addPass(bloomPass);

// 渲染时使用 composer
function animate() {
  requestAnimationFrame(animate);
  composer.render();
}
```

### 5.2 自定义着色器

```javascript
// ✅ 自定义着色器材质
const vertexShader = `
  varying vec2 vUv;
  void main() {
    vUv = uv;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const fragmentShader = `
  uniform float uTime;
  uniform vec3 uColor;
  varying vec2 vUv;

  void main() {
    float wave = sin(vUv.x * 10.0 + uTime) * 0.5 + 0.5;
    gl_FragColor = vec4(uColor * wave, 1.0);
  }
`;

const material = new THREE.ShaderMaterial({
  vertexShader,
  fragmentShader,
  uniforms: {
    uTime: { value: 0 },
    uColor: { value: new THREE.Color(0x00a8e8) },
  },
});

// 更新 uniform
function animate(time) {
  material.uniforms.uTime.value = time * 0.001;
}
```

### 5.3 射线检测优化

```javascript
// ✅ 限制检测对象
const clickableObjects = [];
scene.traverse((obj) => {
  if (obj.userData.clickable) {
    clickableObjects.push(obj);
  }
});

raycaster.intersectObjects(clickableObjects);

// ✅ 使用层（Layer）分组
const INTERACTIVE_LAYER = 1;
interactiveObject.layers.set(INTERACTIVE_LAYER);
raycaster.layers.set(INTERACTIVE_LAYER);

// ✅ 节流鼠标事件
let lastIntersectTime = 0;
function onMouseMove(event) {
  const now = Date.now();
  if (now - lastIntersectTime < 50) return; // 50ms 节流
  lastIntersectTime = now;

  // 射线检测逻辑
}
```

---

## 六、调试技巧

### 6.1 使用 dat.gui 调试

```javascript
import * as dat from 'dat.gui';

const gui = new dat.GUI();

// 添加调试参数
const params = {
  color: '#00a8e8',
  intensity: 1.0,
  autoRotate: true,
};

gui.addColor(params, 'color').onChange((value) => {
  material.color.set(value);
});

gui.add(params, 'intensity', 0, 2).onChange((value) => {
  light.intensity = value;
});

gui.add(params, 'autoRotate').onChange((value) => {
  controls.autoRotate = value;
});
```

### 6.2 使用 Three.js Inspector

```javascript
// 在开发环境启用
if (process.env.NODE_ENV === 'development') {
  window.THREE = THREE;
  window.scene = scene;
  window.camera = camera;
  window.renderer = renderer;
}
```

### 6.3 控制台辅助函数

```javascript
// 输出场景树结构
function printSceneTree(object, indent = 0) {
  console.log(' '.repeat(indent) + object.type + ': ' + object.name);
  object.children.forEach((child) => printSceneTree(child, indent + 2));
}
printSceneTree(scene);

// 输出对象信息
function printObjectInfo(object) {
  console.log('类型:', object.type);
  console.log('位置:', object.position);
  console.log('旋转:', object.rotation);
  console.log('缩放:', object.scale);
  if (object.geometry) {
    console.log('几何体顶点:', object.geometry.attributes.position.count);
  }
  if (object.material) {
    console.log('材质类型:', object.material.type);
  }
}
```

---

## 七、部署优化

### 7.1 模型压缩

```bash
# 使用 glTF Pipeline 压缩
gltf-pipeline -i input.gltf -o output.glb -d

# 使用 Draco 压缩
gltf-pipeline -i input.gltf -o output.glb --draco.compressMeshes=true
```

### 7.2 纹理优化

```bash
# 转换为 KTX2 格式
toktx --encode etc1s input.png output.ktx2

# 压缩纹理
toktx --bcmp input.png output.ktx2
```

### 7.3 代码分割

```javascript
// ✅ 动态导入 Three.js
const THREE = await import('three');

// ✅ 按需加载加载器
async function loadModel(url) {
  const { GLTFLoader } = await import('three/examples/jsm/loaders/GLTFLoader.js');
  const loader = new GLTFLoader();
  return loader.loadAsync(url);
}
```
