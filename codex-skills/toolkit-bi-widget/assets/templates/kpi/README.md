# KPI卡片模板

适用于大屏数据卡片组件，包括六边形KPI、人员状态卡片、AI识别卡片等。

## 支持的模板

| 模板文件 | 说明 | 触发词 |
|----------|------|--------|
| `hexagon.md` | 六边形KPI卡片，六边形形状的数据展示卡片 | 六边形KPI、HexagonKPI、蜂巢卡片 |
| `person-status.md` | 人员状态卡片，头像+姓名+状态+角色 | 人员状态卡片、PersonStatusCard、党员卡片 |
| `ai-recognition.md` | AI识别卡片，AI图标+类型+数量+状态 | AI识别卡片、AIRecognitionCard、智能识别 |

## 通用特点

- 所有KPI卡片组件遵循相同的 Props 定义规范
- 支持图标显示（URL/文字）
- 深蓝科技风主题
- 完整参考：`references/component-templates.md` 对应章节

## 使用方式

1. 打开对应卡片类型的模板文件
2. 复制完整 Vue 组件代码
3. 根据实际数据修改默认值和 Props 配置
4. 创建配置面板组件（如需可视化配置）
5. 创建国际化文件