# 快速开发检查清单

创建 BI 大屏时，按以下清单检查：

## 地图相关
- [ ] 使用阿里 DataV GeoJSON API 获取地图数据
- [ ] 添加 loading 状态和 error 提示
- [ ] 异步加载后使用 `$nextTick` 初始化图表
- [ ] beforeDestroy 中 dispose 图表实例 / destroy 地图实例

## 高德地图相关
- [ ] 配置 `mapKey` 和 `securityJsCode`（2.0 版本必须）
- [ ] 数据中不使用中文智能引号 `""`，用 `「」` 替代
- [ ] InfoWindow 使用 `isCustom: true` + CSS 隐藏默认元素
- [ ] 打点点击只触发一个弹窗（InfoWindow 或侧边面板，不要两个都弹）
- [ ] 多层弹窗 z-index 按优先级递增
- [ ] 标记图标使用 SVG 而非 emoji，保证跨平台一致

## 3D 地球相关
- [ ] 不依赖外部纹理资源，使用本地生成或可靠 CDN
- [ ] scatter3D 数据格式：`[lng, lat, 0]` 贴在球面
- [ ] bar3D 数据格式：`[lng, lat, height]` 控制高度
- [ ] 飞线效果：period=3, trailLength=0.6, width=2

## ECharts 配置
- [ ] label 配置直接写属性，不用 textStyle
- [ ] 图表组件销毁时调用 dispose()
- [ ] 移除 resize 事件监听

## 样式规范
- [ ] 使用 CSS 变量定义主题色
- [ ] 面板使用玻璃效果 + 呼吸动画
- [ ] 目标分辨率 1920x1080

## UI 状态覆盖
- [ ] 每个数据面板有 Loading 状态（骨架屏或 spinner）
- [ ] Loading 超过 15s 显示"加载较慢"提示，60s 强制停止
- [ ] 每个数据面板有 Empty 状态（标题+说明+操作，不是空白）
- [ ] 每个数据面板有 Error 状态（原因+重试按钮）
- [ ] 超长数据 / 缺少可选字段时布局不崩溃（Edge 状态）
- [ ] Accent 颜色（`#00d4ff`）每屏最多出现 2 次
