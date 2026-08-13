# 品牌核心资产协议（5 步硬流程）

> 触发条件：任务涉及具体品牌——用户提了产品名/公司名/明确客户。走协议前必须已通过「#0 事实验证先于假设」确认品牌/产品存在。

## 核心理念：资产 > 规范

| 资产类型 | 识别度贡献 | 必需性 |
|---|---|---|
| **Logo** | 最高 | **任何品牌都必须有** |
| **产品图/渲染图** | 极高 | **实体产品必须有** |
| **UI 截图/界面素材** | 极高 | **数字产品必须有** |
| **色值** | 中 | 辅助 |
| **字体** | 低 | 辅助 |

**翻译成执行规则**：
- 只抽色值 + 字体、不找 logo / 产品图 / UI → **违反本协议**
- 用 CSS 剪影/SVG 手画替代真实产品图 → **违反本协议**
- 找不到资产不告诉用户、也不 AI 生成，硬做 → **违反本协议**

---

## Step 1 · 问（资产清单一次问全）

按清单逐项问，不要只问「有 brand guidelines 吗？」：

```
关于 <brand/product>，你手上有以下哪些资料？我按优先级列：
1. Logo（SVG / 高清 PNG）—— 任何品牌必备
2. 产品图 / 官方渲染图 —— 实体产品必备
3. UI 截图 / 界面素材 —— 数字产品必备
4. 色值清单（HEX / RGB / 品牌色盘）
5. 字体清单（Display / Body）
6. Brand guidelines PDF / Figma design system / 品牌官网链接

有的直接发我，没有的我去搜/抓/生成。
```

---

## Step 2 · 搜官方渠道（按资产类型）

| 资产 | 搜索路径 |
|---|---|
| **Logo** | `<brand>.com/brand` · `<brand>.com/press` · `<brand>.com/press-kit` · `brand.<brand>.com` · 官网 header 的 inline SVG |
| **产品图/渲染图** | `<brand>.com/<product>` 产品详情页 hero image + gallery · 官方 YouTube launch film 截帧 · 官方新闻稿附图 |
| **UI 截图** | App Store / Google Play 产品页截图 · 官网 screenshots section · 产品官方演示视频截帧 |
| **色值** | 官网 inline CSS / Tailwind config / brand guidelines PDF |
| **字体** | 官网 `<link rel="stylesheet">` 引用 · Google Fonts 追踪 · brand guidelines |

`WebSearch` 兜底关键词：
- Logo 找不到 → `<brand> logo download SVG`、`<brand> press kit`
- 产品图找不到 → `<brand> <product> official renders`
- UI 找不到 → `<brand> app screenshots`

---

## Step 3 · 下载资产 · 按类型三条兜底路径

### 3.1 Logo（任何品牌必需）

三条路径按成功率递减：
1. 独立 SVG/PNG 文件（最理想）：
   ```bash
   curl -o assets/<brand>-brand/logo.svg https://<brand>.com/logo.svg
   ```
2. 官网 HTML 全文提取 inline SVG（80% 场景必用）：
   ```bash
   curl -A "Mozilla/5.0" -L https://<brand>.com -o assets/<brand>-brand/homepage.html
   # 然后 grep <svg>...</svg> 提取 logo 节点
   ```
3. 官方社交媒体 avatar（最后手段）

### 3.2 产品图/渲染图（实体产品必需）

1. **官方产品页 hero image**（最高优先级）
2. **官方 press kit**
3. **官方 launch video 截帧**：`yt-dlp` + ffmpeg
4. **Wikimedia Commons**
5. **AI 生成兜底**（nano-banana-pro）：以真实产品图作为参考

```bash
curl -A "Mozilla/5.0" -L "<hero-image-url>" -o assets/<brand>-brand/product-hero.png
```

### 3.3 UI 截图（数字产品必需）

- App Store / Google Play 产品截图
- 官网 screenshots section
- 产品演示视频截帧
- 产品官方 Twitter/X 发布截图
- 用户有账号时，直接截屏真实产品界面

### 3.4 素材质量门槛「5-10-2-8」原则（铁律）

> Logo 有就必须用（不适用「5-10-2-8」）；其他素材遵循此门槛。

| 维度 | 标准 | 反模式 |
|---|---|---|
| **5 轮搜索** | 多渠道交叉搜，不是一轮就停 | 第一页结果直接用 |
| **10 个候选** | 至少凑 10 个备选才开始筛 | 只抓 2 个 |
| **选 2 个好的** | 精选 2 个作为最终素材 | 全都用 |
| **每个 8/10 分以上** | 不够 8 分宁可不用户 | 凑数 7 分素材 |

**8/10 评分维度**：
1. **分辨率** · ≥2000px（印刷/大屏 ≥3000px）
2. **版权清晰度** · 官方 > 公共领域 > 免费素材 > 疑似盗图（0分）
3. **与品牌气质契合度**
4. **光线/构图/风格一致性**
5. **独立叙事能力**

---

## Step 4 · 验证 + 提取

| 资产 | 验证动作 |
|---|---|
| **Logo** | 文件存在 + SVG/PNG 可打开 + 至少两个版本（深底/浅底用）+ 透明背景 |
| **产品图** | 至少一张 2000px+ + 去背或干净背景 + 多个角度 |
| **UI 截图** | 分辨率真实 + 是最新版本 + 无用户数据污染 |
| **色值** | `grep -hoE '#[0-9A-Fa-f]{6}' assets/<brand>-brand/*.{svg,html,css} \| sort \| uniq -c \| sort -rn \| head -20`，过滤黑白灰 |

**警惕示范品牌污染**：产品截图里常有用户 demo 的品牌色（如某工具截图演示喜茶红），那不是该工具的色。

**品牌多切面**：同一品牌的官网营销色和产品 UI 色经常不同。两套都是真的——根据交付场景选合适的切面。

---

## Step 5 · 固化为 `brand-spec.md` 文件

```markdown
# <Brand> · Brand Spec
> 采集日期：YYYY-MM-DD
> 资产来源：<列出下载来源>
> 资产完整度：<完整 / 部分 / 推断>

## 🎯 核心资产（一等公民）

### Logo
- 主版本：`assets/<brand>-brand/logo.svg`
- 浅底反色版：`assets/<brand>-brand/logo-white.svg`
- 使用场景：<片头/片尾/角落水印/全局>
- 禁用变形：<不能拉伸/改色/加描边>

### 产品图（实体产品必填）
- 主视角：`assets/<brand>-brand/product-hero.png`
- 细节图：`assets/<brand>-brand/product-detail-1.png`
- 场景图：`assets/<brand>-brand/product-scene.png`

### UI 截图（数字产品必填）
- 主页：`assets/<brand>-brand/ui-home.png`
- 核心功能：`assets/<brand>-brand/ui-feature-<name>.png`

## 🎨 辅助资产

### 色板
- Primary: #XXXXXX
- Background: #XXXXXX
- Ink: #XXXXXX
- Accent: #XXXXXX
- 禁用色: <品牌明确不用的色系>

### 字型
- Display: <font stack>
- Body: <font stack>
- Mono（数据 HUD 用）: <font stack>

### 签名细节 / 禁区 / 气质关键词
```

**写完 spec 后的执行纪律**：
- 所有 HTML 必须引用 `brand-spec.md` 里的资产文件路径
- Logo 作为 `<img>` 引用真实文件，不重画
- 产品图作为 `<img>` 引用真实文件，不用 CSS 剪影代替
- CSS 变量从 spec 注入：`:root { --brand-primary: ...; }`

---

## 全流程失败的兜底

| 缺失 | 处理 |
|---|---|
| **Logo 完全找不到** | **停下问用户** |
| **产品图找不到** | nano-banana-pro AI 生成 → 向用户索取 → 诚实 placeholder |
| **UI 截图找不到** | 向用户索取截屏 → 官方演示视频截帧 |
| **色值完全找不到** | 按「设计方向顾问模式」推荐 3 个方向 |

**禁止**：找不到资产就静默用 CSS 剪影/通用渐变硬做。**宁可停下问，也不要凑**。

## 反例（真实踩过的坑）

- **Kimi 动画**：凭记忆猜「应该是橙色」，实际 Kimi 是 `#1783FF` 蓝色——返工一遍
- **Lovart 设计**：把产品截图里演示品牌的喜茶红当成 Lovart 自己的色
- **DJI Pocket 4**：走了旧版只抽色值的协议，没下载 DJI logo 和产品图，用 CSS 剪影代替——做出来是「通用黑底+橙 accent 的科技动画」

## 协议代价 vs 不做代价

| 场景 | 时间 |
|---|---|
| 正确走完协议 | **30 分钟** |
| 不做协议的代价 | 返工 1-2 小时，甚至重做 |
