# 主题系统模板

> 基于 21 个 BI 大屏设计分析提炼的 6 套主题系统，CSS 变量驱动一键切换。

| 主题 | Key | cssKey | 触发词 | 适用场景 |
|------|-----|--------|--------|----------|
| **深蓝科技** | techBlue | tech-blue | 智慧乡村、科技感大屏、深色大屏、产业振兴、智慧城市、态势感知 | 智慧城市、乡村、社区、监控 |
| **青绿生态** | ecoGreen | eco-green | 生态大屏、水利大屏、农业大屏、碳排放大屏、文旅生态 | 生态环境、水利水务、智慧农业 |
| **党建红金** | partyRed | party-red | 党建大屏、红色主题、政务大屏、廉政大屏 | 党建、政务、廉政 |
| **暖橙数据** | warmOrange | warm-orange | 经济大屏、产业大屏、GDP大屏、招商大屏 | 经济分析、产业发展、招商引资 |
| **紫蓝深邃** | deepPurple | deep-purple | 数字孪生大屏、3D大屏、城市大脑大屏 | 数字孪生、3D可视化、城市大脑 |
| **浅色商务** | lightBusiness | light-business | 浅色大屏、商务大屏、报表大屏、企业大屏 | 企业报表、会议室、SaaS仪表盘 |

### 向后兼容映射

| 旧键名 | 新键名 | 说明 |
|--------|--------|------|
| darkTech | techBlue | 深蓝科技主题重命名 |
| tourism | ecoGreen | 文旅主题归入青绿生态 |
| lightBright | lightBusiness | 浅色商务重命名 |
| partyRed | partyRed | 保持不变 |

## 模板文件

| 文件 | 内容 |
|------|------|
| [dark-tech.md](dark-tech.md) | 6 套主题完整配置：JS 配置、CSS 变量、SCSS 样式、ThemeProvider、ThemeSelector、使用方式 |
| [party-red.md](party-red.md) | 党建红金主题补充样式：祥云装饰、五角星、飘带 |
| [light-bright.md](light-bright.md) | 浅色商务主题补充样式：卡片阴影、Tab组件 |
| [tourism.md](tourism.md) | 青绿生态主题补充样式：水波纹、波浪装饰 |

## 每个主题包含的内容

1. **主题配置文件** (`themes/index.js`) — JS 主题对象（colors/gradients/decoration/animation/map/chart/font 配置）
2. **CSS 变量生成器** (`themes/css-variables.js`) — 从主题配置生成 CSS 变量
3. **主题 SCSS 变量** (`themes/theme-variables.scss`) — CSS 变量引用的 SCSS 变量
4. **通用组件样式** (`themes/common-components.scss`) — 面板、标题、卡片、角标、光条、动画
5. **ThemeProvider.vue** — 主题切换组件（含向后兼容映射）
6. **ThemeSelector.vue** — 6 主题选择器组件
7. **CSS 变量完整定义** — 6 套主题的 CSS 变量可直接复制使用

## 在 SKILL.md 中配置主题触发词

```
| 触发词 | 生成的主题 | cssKey |
|--------|------------|--------|
| 科技蓝大屏、深色大屏、科技大屏（默认） | techBlue | tech-blue |
| 生态大屏、青绿大屏、水利大屏、农业大屏 | ecoGreen | eco-green |
| 党建大屏、政务大屏、廉政大屏 | partyRed | party-red |
| 暖橙大屏、经济大屏、产业大屏、GDP大屏 | warmOrange | warm-orange |
| 紫蓝大屏、数字孪生大屏、3D大屏 | deepPurple | deep-purple |
| 浅色大屏、商务大屏、报表大屏、企业大屏 | lightBusiness | light-business |
```

## 主题选型速查

| 你要做什么大屏 | 推荐主题 |
|--------------|---------|
| 智慧乡村/社区总览 | techBlue（深蓝科技） |
| 生态/水利/农业 | ecoGreen（青绿生态） |
| 党建/政务/廉政 | partyRed（党建红金） |
| 经济/产业/GDP | warmOrange（暖橙数据） |
| 数字孪生/3D/城市大脑 | deepPurple（紫蓝深邃） |
| 企业报表/会议室/移动端 | lightBusiness（浅色商务） |
