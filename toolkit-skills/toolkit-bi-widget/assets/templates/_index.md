# 模板库目录索引

本目录包含按分类组织的 BI 大屏可视化组件开发模板，每个模板文件包含完整可复用的 Vue 组件代码。

## 目录结构

```
templates/
├── _index.md                    # 模板目录 + 分类说明 + 触发词映射
├── echarts/                     # ECharts 图表组件
│   ├── README.md
│   ├── bar.md                   # 柱状图
│   ├── pie.md                   # 饼图/环形图/玫瑰图
│   ├── line.md                  # 折线图/面积图
│   └── radar.md                 # 雷达图
├── map/                         # 地图组件
│   ├── README.md
│   └── china-map.md             # 中国地图
├── progress/                    # 进度/排名组件
│   ├── README.md
│   ├── ranking-list.md          # 排名列表
│   └── progress-bar.md          # 进度条
├── text/                        # 文本组件
│   ├── README.md
│   ├── title.md                 # 标题组件
│   ├── datetime.md              # 日期时间组件
│   └── marquee.md               # 跑马灯组件
├── threejs/                     # 3D/WebGL 组件
│   ├── README.md
│   ├── city-3d.md               # 3D城市
│   ├── earth-3d.md              # 3D地球
│   ├── map-3d.md                # 3D地图
│   ├── particle-3d.md           # 3D粒子
│   ├── fly-line-3d.md           # 3D飞线
│   └── bar-3d.md                # 3D柱状图
├── panels/                      # 面板组件
│   ├── README.md
│   ├── dot-matrix.md            # 点阵面板
│   ├── corner-decorated.md      # 四角装饰面板
│   └── gradient-header.md       # 渐变头部面板
├── kpi/                         # KPI卡片
│   ├── README.md
│   ├── hexagon.md               # 六边形KPI
│   ├── person-status.md         # 人员状态卡片
│   └── ai-recognition.md        # AI识别卡片
├── interaction/                 # 交互组件
│   ├── README.md
│   ├── tech-modal.md            # 科幻弹窗
│   ├── bottom-nav-tabs.md       # 底部导航标签
│   ├── weather-panel.md         # 天气面板
│   └── calendar-panel.md        # 日历面板
└── config-panel/                # 配置面板组件
    ├── README.md
    ├── number-input.md          # 数值输入
    ├── color-picker.md          # 颜色选择器
    ├── gradient-picker.md       # 渐变色选择器
    └── select.md                # 选择器
```

## 触发词 -> 模板分类映射

### ECharts 图表类
| 触发词 | 模板文件 |
|--------|----------|
| 柱状图、生成柱状图、柱图 | `templates/echarts/bar.md` |
| 饼图、环形图、玫瑰图、生成饼图、圆环图 | `templates/echarts/pie.md` |
| 折线图、面积图、生成折线图、曲线图、趋势图 | `templates/echarts/line.md` |
| 雷达图、生成雷达图 | `templates/echarts/radar.md` |
| 生成图表组件、图表组件、ECharts组件 | `templates/echarts/README.md` |

### 地图类
| 触发词 | 模板文件 |
|--------|----------|
| 生成地图、地图组件、中国地图、点位地图 | `templates/map/china-map.md` |
| 高德地图、AMap、地图可视化 | `templates/map/README.md` |

### 进度/排名类
| 触发词 | 模板文件 |
|--------|----------|
| 排名列表、城市排名列表、CityRankingList、进度条排名、客流来源排名 | `templates/progress/ranking-list.md` |
| 进度条、进度组件、排名进度条 | `templates/progress/progress-bar.md` |
| 排名进度组件、生成排名进度 | `templates/progress/README.md` |

### 文本类
| 触发词 | 模板文件 |
|--------|----------|
| 标题、标题组件、大屏标题 | `templates/text/title.md` |
| 时间、日期时间、时钟、当前时间 | `templates/text/datetime.md` |
| 跑马灯、滚动文本、公告 | `templates/text/marquee.md` |
| 文本组件、生成文本组件 | `templates/text/README.md` |

### 3D/WebGL 类
| 触发词 | 模板文件 |
|--------|----------|
| 3D城市、City3D、智慧城市3D、城市可视化、三维城市模型 | `templates/threejs/city-3d.md` |
| 3D地球、Earth3D、三维地球、全球数据可视化、世界地图3D | `templates/threejs/earth-3d.md` |
| 3D地图、Map3D、三维地图、地形3D、区域3D | `templates/threejs/map-3d.md` |
| 3D粒子、Particle3D、粒子特效、粒子系统、炫酷粒子 | `templates/threejs/particle-3d.md` |
| 3D飞线、FlyLine3D、数据飞线、迁徙图3D、流向可视化 | `templates/threejs/fly-line-3d.md` |
| 3D柱状图、Bar3D、立体柱状图、三维图表 | `templates/threejs/bar-3d.md` |
| Three.js组件、3D可视化、WebGL特效 | `templates/threejs/README.md` |

### 面板类
| 触发词 | 模板文件 |
|--------|----------|
| 点阵面板、DotMatrixPanel、科技感面板 | `templates/panels/dot-matrix.md` |
| 四角装饰面板、CornerDecoratedPanel、发光边框面板 | `templates/panels/corner-decorated.md` |
| 渐变头部面板、GradientHeaderPanel、蓝色头部面板、浅色面板 | `templates/panels/gradient-header.md` |
| 深色面板、面板组件 | `templates/panels/README.md` |

### KPI 卡片类
| 触发词 | 模板文件 |
|--------|----------|
| 六边形KPI、HexagonKPI、蜂巢卡片、六边形数据卡片 | `templates/kpi/hexagon.md` |
| 人员状态卡片、PersonStatusCard、头像卡片、党员卡片 | `templates/kpi/person-status.md` |
| AI识别卡片、AIRecognitionCard、智能识别组件 | `templates/kpi/ai-recognition.md` |
| KPI卡片、数据卡片、生成数据卡片 | `templates/kpi/README.md` |

### 交互类
| 触发词 | 模板文件 |
|--------|----------|
| 科技弹窗、TechModal、详情弹窗、数据弹窗 | `templates/interaction/tech-modal.md` |
| 底部导航、BottomNavTabs、TAB切换 | `templates/interaction/bottom-nav-tabs.md` |
| 天气面板、WeatherPanel、天气预报 | `templates/interaction/weather-panel.md` |
| 日历面板、CalendarPanel、日程面板 | `templates/interaction/calendar-panel.md` |

### 地图增强类
| 触发词 | 模板文件 |
|--------|----------|
| 3D景区标记、Scenic3DMarker、景区图标 | `templates/map/scenic-3d-marker.md` |
| 地图悬浮数字、MapFloatNumber、地图数据标注 | `templates/map/map-float-number.md` |
| 热力图开关、HeatmapToggle、热力图按钮 | `templates/map/heatmap-toggle.md` |

### 图表增强类
| 触发词 | 模板文件 |
|--------|----------|
| 半圆环形图、SemicircleChart、半圆饼图 | `templates/echarts/semicircle-chart.md` |
| 城市排名、CityRankingList、进度条排名 | `templates/echarts/city-ranking-list.md` |
| 性别比例图、GenderRatioChart、人口比例图 | `templates/echarts/gender-ratio-chart.md` |

### 3D增强类
| 触发词 | 模板文件 |
|--------|----------|
| 3D浮动标注、FloatingLabel3D、3D数据标签 | `templates/threejs/floating-label-3d.md` |
| 数据叠加层、DataOverlay、3D数据面板 | `templates/threejs/data-overlay.md` |

### 配置面板类
| 触发词 | 模板文件 |
|--------|----------|
| 数值输入、数字配置、数值配置面板 | `templates/config-panel/number-input.md` |
| 颜色选择器、颜色配置、颜色面板 | `templates/config-panel/color-picker.md` |
| 渐变色选择器、渐变配置、渐变色面板 | `templates/config-panel/gradient-picker.md` |
| 选择器、下拉选择、选项配置 | `templates/config-panel/select.md` |
| 组件配置面板、configurationTemplate | `templates/config-panel/README.md` |

## 使用方式

1. 根据用户触发词在 `_index.md` 中查找对应分类
2. 打开对应分类的 `README.md` 了解该分类支持的所有组件类型
3. 打开具体的模板文件（如 `bar.md`），获取完整可复用的 Vue 组件代码
4. 参考模板中的 Props 定义、ECharts 配置、配置面板和国际化文件结构
