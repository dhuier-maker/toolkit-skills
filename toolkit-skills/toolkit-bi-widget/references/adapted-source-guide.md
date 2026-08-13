# 适配后的来源指南

# BI 大屏可视化组件开发指南

## Profile

你是一位**BI 大屏组件作者**，专精在 the project's visualization component library 工程内开发**单个可复用组件**（echarts / map / progress / text / threejs / panels / kpi / interaction / config-panel 九类模板）。你的输出是**一个组件文件夹 + 配置面板 + 打包测试**，不是整页大屏（那是 toolkit-bi-dashboard 的职责）。组件必须支持配置化、跨主题、独立打包。

## 触发方式

### 核心触发词（已包含在 description 中）

| 触发词 | 组件类型 |
|--------|---------|
| 创建组件、开发组件、新建大屏组件 | 通用组件 |
| BI组件开发 | 通用组件 |
| 生成图表组件 | echarts 类 |
| 生成地图组件 | map 类 |
| 生成数据卡片 | panels/kpi 类 |
| 组件配置面板、组件props定义 | config-panel 类 |
| 组件打包测试 | 打包流程 |
| 3D城市、3D地球、3D粒子 | threejs 类 |
| 科技弹窗、数字孪生 | interaction/threejs 类 |
| 六边形KPI | kpi 类 |

### 扩展触发词

| 触发词 | 对应模板 | 模板库 |
|--------|---------|--------|
| 柱状图、饼图、折线图、雷达图 | ChartBar/ChartPie/ChartLine/ChartRadar | echarts |
| 半圆环形图、城市排名、性别比例图 | SemicircleChart/CityRankingList/GenderRatioChart | echarts |
| 生成文本组件、标题、时间、跑马灯 | TextTitle/TextTime/TextMarquee | text |
| 3D飞线、3D柱状图、3D浮动标注、数据叠加层 | FlyLine3D/Bar3D/FloatingLabel3D/DataOverlay | threejs |
| 全景、AI识别卡片 | Panorama/AiRecognitionCard | threejs/kpi |
| 详情弹窗 | TechModal | interaction |
| 底部导航、天气面板、日历面板 | BottomNavTabs/WeatherPanel/CalendarPanel | interaction |
| 3D景区标记 | Scenic3DMarker | map |
| 地图悬浮数字、地图数据标注 | MapFloatNumber | map |
| 热力图开关 | HeatmapToggle | map |

## 技术栈兼容性

**基础技术栈**：Vue 3.2.13 + Composition API / ECharts 5.x / Element Plus 2.5.3 / 高德地图 API / vue-i18n

**3D/WebGL 技术栈**：Three.js r150+ / @types/three / OrbitControls / GLTFLoader / FBXLoader / OBJLoader / DRACOLoader / Three-stdlib

**3D数据处理**：@tweenjs/tween.js (动画) / stats.js (性能监控) / dat.gui (调试面板)

**地理3D**：Three-geo / Deck.gl (可选) / Mapbox GL JS (可选集成)

## 工程路径
组件开发目录：`the project's visualization component library/src/packages/`

## 约束条件

### 适用范围
- 仅适用于 the project's visualization component library 工程规范的组件开发
- 组件必须遵循 Props 定义规范（包含完整元数据）
- 必须提供国际化配置（中英文）

### 用户确认点
1. **组件创建前**：确认组件名称、类型（图表/地图/数据卡片/文本）
2. **Props 定义时**：确认数据结构和配置项

### 停止条件
- 用户明确说"取消"或"停止"
- 用户未提供必要的组件信息（如组件名称）

### 不适用场景
- 非 Vue 3 技术栈
- 非 the project's visualization component library 工程规范
- 非 BI 大屏类组件（如表单组件、业务页面组件）
- React/Angular 组件开发

### 依赖要求
- 必须在 the project's visualization component library 项目目录下执行
- 需要预先安装 ECharts、Element Plus、vue-i18n 等依赖

---

## 一、目录结构规范

每个组件必须遵循以下目录结构：

```
ComponentName/
├── index.js                    # 组件入口（固定模板）
└── src/
    ├── index.vue               # 主组件
    ├── components/             # 配置面板组件目录
    │   ├── PropName1.vue       # 单个配置项面板
    │   ├── PropName2.vue
    │   └── style/              # 配置面板样式目录
    ├── locale/                 # 国际化目录
    │   ├── index.js            # i18n配置
    │   └── lang/
    │       ├── zh-cn.json      # 中文
    │       └── en.json         # 英文
    ├── static/                 # 静态资源
    │   ├── img/                # 图片资源
    │   └── map/                # 地图数据
    └── font.scss               # 字体样式（可选）
```

## 二、组件入口文件 (index.js)

所有组件入口文件使用相同模板：

```javascript
// eslint-disable-next-line
__webpack_public_path__ = window[process.env.VUE_APP_PROCESS_ENV_KEY][process.env.VUE_EXTEND_COMPONENT_PUBLIC_PATH_KEY]
// 从 './src/index.vue' 文件导入组件
import comp from './src/index.vue';

// 默认导出该组件，以便其他模块可以使用
export default comp;
```

## 三、Props 定义规范（核心）

每个 prop 必须包含完整的元数据，用于可视化平台的配置面板生成。核心规则：

- **分组键**：`data`（数据配置）、`style`（样式配置）、`style-composing`（排版配置）
- **必填元数据**：`type`、`default`、`desc`、`name`、`groupKey`、`groupName`、`sort`
- **动态数据**：数据类 prop 必须标记 `useDynamic: true`
- **配置面板**：复杂属性使用 `configurationTemplate: () => import('./components/Xxx.vue')`
- **数值范围**：数值类属性设置 `min`/`max`

> 完整元数据字段说明、Props 定义示例和各类属性模板见 [references/props-specification.md](references/props-specification.md)。

---

## 四、配置面板组件规范

详见 [references/config-panel-templates.md](references/config-panel-templates.md)，包含基本结构和常用配置面板组件模板（数值输入、颜色选择器、渐变色选择器、选择器等）。

---

## 五、国际化配置规范

### 5.1 locale/index.js
```javascript
import { createI18n } from 'vue-i18n';
import cn from './lang/zh-cn.json';
import en from './lang/en.json';
import languageMgt from '@/utils/langMgt';

const i18n = createI18n({
  locale: languageMgt.getLanguage(),
  legacy: false,
  globalInjection: true,
  messages: {
    cn,
    en,
  },
});

export default i18n;
```

### 5.2 locale/lang/zh-cn.json
```json
{
  "dataConfiguration": "数据配置",
  "styleConfiguration": "样式配置",
  "layout": "排版",
  "dataSpecification": "数据说明",
  "displayContent": "展示内容",
  "horizontalAlignment": "水平排列方式",
  "date": "日期",
  "dateConfiguration": "日期配置"
}
```

### 5.3 locale/lang/en.json
```json
{
  "dataConfiguration": "Data Configuration",
  "styleConfiguration": "Style Configuration",
  "layout": "Layout",
  "dataSpecification": "Data Specification",
  "displayContent": "Display Content",
  "horizontalAlignment": "Horizontal Alignment",
  "date": "Date",
  "dateConfiguration": "Date Configuration"
}
```


---

## 六、组件类型模板

详见 [references/component-type-templates.md](references/component-type-templates.md)，包含：
- 6.1 ECharts 图表类组件
- 6.2 地图类组件
- 6.3 进度/排名类组件
- 6.4 文本类组件

---

## 七、开发完成后的自动化流程

组件开发完成后自动执行：修改测试页面 import → 启动 `npm run serve` → 打开 http://localhost:3000 预览 → 用户反馈循环 → 满意后询问是否打包。

> 完整测试预览步骤、打包命令、流程图和格式化脚本见 [references/automation-and-packaging.md](references/automation-and-packaging.md)。

---

## 八、打包流程

> 详见 [references/automation-and-packaging.md](references/automation-and-packaging.md)，包含打包命令、批量打包方式、输出位置和外部依赖配置。

---

## 九、开发流程清单

### 创建新组件时：

1. **创建目录结构**
   ```bash
   cd front/the project's visualization component library/src/packages
   mkdir -p ComponentName/src/{components,locale/lang,static/img}
   ```

2. **创建入口文件** `index.js`（使用固定模板）

3. **创建主组件** `src/index.vue`
   - 定义 props（包含完整元数据）
   - 实现组件逻辑
   - 添加样式

4. **创建配置面板组件** `src/components/`
   - 为需要可视化配置的属性创建配置面板
   - 使用 inject 获取和更新配置值

5. **创建国际化文件**
   - `locale/index.js`
   - `locale/lang/zh-cn.json`
   - `locale/lang/en.json`

6. **自动测试预览**（新增）
   - 修改 `src/pages/extendComponentTest/index.vue` 的 import
   - 启动开发服务器：`npm run serve`
   - 打开 http://localhost:3000 预览组件
   - 根据用户反馈迭代修改

7. **自动打包**（新增）
   - 用户满意后询问是否打包
   - 是：自动执行 `$env:BUILD_COMPONENTS="ComponentName"; npm run build:lib`
   - 否：返回打包命令供用户手动执行

8. **上传到可视化平台**
   将 `lib/ComponentName.zip` 上传到可视化平台的组件库

### 开发完成后自动化流程（推荐）

当组件开发完成后，Codex 会自动执行以下流程：

```
1. 更新测试页面 import 语句
2. 启动 npm run serve
3. 提示用户打开 http://localhost:3000 预览
4. 等待用户反馈
   ├─ 不满意 → 修改组件 → 刷新预览 → 重复步骤4
   └─ 满意 → 询问是否打包
       ├─ 是 → 自动执行打包命令 → 完成
       └─ 否 → 返回打包命令给用户
```

## 十、最佳实践

### 9.1 Props 设计原则
- 数据类属性放在 `data` 组，样式类放在 `style` 组
- 合理设置 sort 值，常用配置排在前面
- 为数值类属性设置合理的 min/max 范围
- 复杂配置使用 configurationTemplate 提供可视化面板

### 9.2 性能优化
- 使用 `markRaw` 包装 ECharts 实例避免响应式开销
- watch 使用 `deep: true` 时注意性能影响
- 使用 ResizeObserver 替代 window.resize 监听容器变化

### 9.3 样式规范
- 使用 `scoped` 样式避免污染
- 颜色使用 CSS 变量便于主题切换
- 动画使用 CSS animation 而非 JS 动画

### 9.4 国际化
- 所有用户可见文本使用 i18n
- 配置面板标题、描述也需要国际化
- 使用 `i18n.global.t()` 获取翻译文本

---


---

## 十一、完整开发示例

详见 [references/full-example.md](references/full-example.md)，以 BarChartComponent 为例演示完整的 7 文件创建流程（index.js、index.vue、BarWidth.vue、locale/index.js、zh-cn.json、en.json）。

---

## 十二、组件开发检查清单

### 必须项 ✓

- [ ] **文件末尾换行符**：所有文件必须以换行符结尾
- [ ] **UTF-8 编码**：含中文的文件必须使用 UTF-8 编码
- [ ] **Props 元数据完整**：每个属性包含 `desc`, `name`, `groupKey`, `groupName`, `sort`
- [ ] **动态数据标记**：`dynamicData` 属性必须标记 `useDynamic: true`
- [ ] **数据格式示例**：提供 `jsonExample` 作为数据格式参考
- [ ] **示例数据**：提供 realistic 示例数据（非空数组/对象）
- [ ] **国际化文件**：配套 `locale/index.js` 和 `locale/lang/zh-cn.json`

### 建议项 ○

- [ ] **弹窗集成**：弹窗/详情面板集成在组件内部，通过 `ref` 状态控制
- [ ] **主题色变量**：使用 SCSS 变量定义主题色
- [ ] **样式属性隐藏**：高级样式属性使用 `hidden: true`
- [ ] **滚动条样式**：滚动区域自定义 scrollbar 样式
- [ ] **emit 事件**：点击事件同时 emit 通知父组件

---


---

## 十三、常见问题与解决方案

详见 [references/troubleshooting.md](references/troubleshooting.md)，包含：
1. 文件末尾换行符问题
2. 中文字符编码问题
3. Prettier 格式化问题
4. 弹窗组件设计问题
5. 示例数据缺失问题

---

## 十四、Props 元数据模板

> 基础属性、动态数据属性、样式属性模板见 [references/props-specification.md](references/props-specification.md)。

---

## 十五、弹窗样式模板

> 详情弹窗 SCSS 样式见 [references/modal-and-ui-styles.md](references/modal-and-ui-styles.md)。

---

## 十六、开发完成后自动格式化

> 格式化命令和换行符修复脚本见 [references/automation-and-packaging.md](references/automation-and-packaging.md)。

---

## 十七、模板库 (templates/)

按分类组织的 BI 大屏可视化组件模板库，支持9类模板：echarts / map / progress / text / threejs / panels / kpi / interaction / config-panel。

> 完整目录结构、触发词→模板映射见 `templates/_index.md`。使用方式：根据用户触发词在 `_index.md` 中查找分类 → 打开具体模板文件获取可复用代码 → 根据需求调整。
