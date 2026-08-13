# 阶段 0: 配置初始化

**自动执行**
1. 检查当前目录是否存在 `doc/project.config.json`
2. 如存在，读取配置
3. 如不存在：
   - 询问用户项目名称和工作目录
   - 或使用默认值
4. 创建 `doc/project.config.json`
5. 初始化工作流状态文件

## Spring Boot backend项目检测

- 检测当前工作目录是否存在 `pom.xml` 且包含 `project-backend` 父模块
- **或** 用户需求中提到"project-specific"、"the project's existing framework"、"project"等关键词
- 如检测到，询问用户：
  > "检测到Spring Boot backend项目环境，是否使用the project's existing framework模板规范？
  > - 使用模板规范：将按照the project's existing framework标准生成代码（Entity、DTO、Mapper、Service、Controller等）
  > - 不使用：按通用 Spring Boot 规范生成代码"
- **使用模板规范**：
  - 如需创建新模块 → 调用 `toolkit-spring-module` 创建模块
  - 后续代码生成遵循the project's existing framework模板规范
- **不使用** → 继续主流程，按通用规范生成代码

## 需求类型标记

- 在需求分析前，根据用户初始需求判断项目类型：
  - 用户提到"BI大屏"、"数据大屏"、"驾驶舱" → 标记为 `toolkit-bi-dashboard` 类型
  - 用户提到"封面图"、"背景图"、"PPT插图"、"海报"、"商品图"、"Banner" → 标记为 `toolkit-visual-asset-generator (ai)` 类型
  - 用户提到"数据图表"、"ECharts图表"、"生成图表"、"SVG图标"、"后台图表" → 标记为 `toolkit-visual-asset-generator (svg)` 类型
  - 用户提到"AI绘图"、"生成图片"且描述模糊 → 标记为 `toolkit-image-prompt-writer → toolkit-visual-asset-generator` 联动类型
  - 其他 → 标记为通用类型

## 设计系统生成（toolkit-ui-system-designer）

- 根据需求类型自动调用 toolkit-ui-system-designer 生成设计系统
- 输出设计规范到 `doc/design-system.md`
- 作为后续原型和开发的规范基础

| 需求类型 | toolkit-ui-system-designer 参数 | 输出内容 |
|----------|------------------------|----------|
| 后台管理 | `--design-system -s vue3` | 设计风格、配色、布局、组件推荐 |
| BI 大屏 | `--design-system --domain bi` | BI 模板推荐、科技暗黑风格、科技青配色 |
| 移动端 | `--design-system -s uniapp` | 移动端规范、极简移动风格 |
| 通用类型 | `--design-system` | 通用设计系统 |

**设计系统文件结构**：
```yaml
# doc/design-system.md 示例
设计风格:
  名称: 现代简约
  关键词: 简约、干净、专业

配色方案:
  主色: #1890ff
  辅色: #52c41a
  强调: #faad14
  背景: #ffffff

布局模式:
  名称: 侧边栏导航布局
  结构: Sidebar(固定宽度) + Header(全宽) + Content(自适应)

推荐组件:
  - Table
  - Form
  - Modal
  - Select
```

## 开发模式选择

- 检测是否已存在 `src/` 目录或 `doc/PRD.md`
- 如存在，询问用户：
  > "检测到已有项目，选择开发模式：
  > - 全量开发：完整开发所有功能
  > - 增量开发：只开发新增功能模块"
- **增量模式**：记录已有模块，只开发指定的新模块

## Worktree 隔离模式（可选）

- 询问用户是否使用 worktree 隔离开发：
  > "是否使用 Worktree 隔离模式？
  > - ① 是（完整隔离）：在独立分支上开发，完成后通过 PR 合并（推荐大型功能开发）
  > - ② 轻量隔离：后台会话直接编辑工作副本，不创建 worktree（适合增量开发、大型仓库）
  > - ③ 否（默认）：直接在当前分支上开发"
- **用户选择①（完整隔离）**：
  - 在阶段 4（后端开发）开始前调用 `EnterWorktree` 创建隔离工作树
  - 开发完成后通过 PR 合并回原分支
  - 在 `workflow-status.json` 中记录 `worktreeMode: true`、`bgIsolation: "worktree"` 和分支名
  - **baseRef 配置（v2.1.133+）**：在 `settings.json` 中配置 `worktree.baseRef` 控制新分支的起点：
    - `"fresh"`（默认）：从 `origin/<default-branch>` 创建新分支，适合干净起步
    - `"head"`：从当前 HEAD 创建新分支，适合在已有工作基础上继续开发
- **用户选择②（轻量隔离）**：
  - 在 `settings.json` 中设置 `worktree.bgIsolation: "none"`
  - 不调用 `EnterWorktree`，后台 Agent 直接编辑当前工作副本
  - 适合 git 状态复杂、worktree 不实用的场景
  - 在 `workflow-status.json` 中记录 `worktreeMode: false`、`bgIsolation: "none"`
- **用户选择③或不选择**：直接在当前分支开发（默认行为），`bgIsolation: null`
- **适用场景**：
  - ① 完整隔离：新功能开发、实验性改动、多人协作项目
  - ② 轻量隔离：增量开发、大型仓库、git 状态复杂
  - ③ 默认：单文件修复、小改动

## 进度估算

- 根据 API 数量估算项目规模和时间：
  - 小型（API < 20）：预计 4-6 小时
  - 中型（API 20-50）：预计 7-12 小时
  - 大型（API > 50）：预计 1-3 天
