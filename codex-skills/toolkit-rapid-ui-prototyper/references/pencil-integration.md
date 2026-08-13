# Pencil MCP 集成

Pencil MCP 作为可选的辅助工具，用于需要精确设计稿的场景。

## 使用场景

- 用户明确要求「用 Pencil 设计」
- B2B 复杂表单需要精确布局
- 需要团队 review 设计稿
- 设计稿需要后续迭代优化

## 不需要使用 Pencil 的场景

- 快速原型验证
- 简单页面（登录、列表、详情）
- 用户已提供详细需求描述

## Pencil MCP 使用流程

```
1. 用户说「用 Pencil 设计登录页」
       ↓
2. 调用 pencil-mcp 的 open_document('new') 创建新文件
       ↓
3. 使用 batch_design 创建设计稿
   - I(): 插入元素（frame, rectangle, text, 等）
   - U(): 更新元素属性
       ↓
4. 使用 get_screenshot 获取设计预览
       ↓
5. 用户确认设计稿
       ↓
6. 调用 toolkit-rapid-ui-prototyper 将设计转换为代码
   - 读取设计稿中的布局、颜色、间距
   - 生成对应的 HTML/CSS
       ↓
7. 输出 prototypes/*.html
```

## Pencil 操作示例

```javascript
// 创建新设计文档
pencil.open_document('new')

// 创建设计稿结构
I('body', { type: 'frame', layout: 'vertical', name: 'LoginPage' })
I('LoginPage', { type: 'rectangle', name: 'Header', fill: '#6366f1' })
I('LoginPage', { type: 'rectangle', name: 'FormCard', fill: '#ffffff' })
U('FormCard/Title', { text: '登录', fontSize: 24 })

// 获取预览
get_screenshot('LoginPage')
```

## Pencil 与 toolkit-rapid-ui-prototyper 衔接

```markdown
当用户说「用 Pencil 设计 xxx，然后用 vibe 生成代码」时：

1. Pencil 阶段：创建设计稿（.pen 文件）
2. toolkit-rapid-ui-prototyper 阶段：
   - 读取设计稿中的布局和样式信息
   - 结合用户自然语言需求
   - 生成对应的 HTML/CSS 代码
3. 输出到 prototypes/ 目录
```
