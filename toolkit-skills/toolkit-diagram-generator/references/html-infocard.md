# HTML/CSS Infocard Reference

**Engine**: HTML/CSS (embedded) | **Code Fence**: NONE — embed HTML directly in Markdown

## Critical Rules

### Rule 1: Direct HTML Embedding
Write info cards as direct HTML in Markdown. **NEVER** use code blocks (```html). The HTML should be embedded directly without any fencing.

### Rule 2: No Empty Lines in HTML Structure
Do NOT add any empty lines within the HTML info card structure. Keep the entire HTML block continuous.

### Rule 3: Content Analysis Before Layout
Analyze content along three dimensions before designing:

**Density** (determines breathing rhythm):

| Density | Content Volume | Visual Treatment |
|---------|---------------|-----------------|
| Low | ≤ 50 words core | "Big-character" composition. One oversized element dominates. Generous whitespace. |
| Medium | 50–200 words | Hero + supporting panels. 2–3 main blocks with clear hierarchy. |
| High | 200+ words | Asymmetric multi-column grids. Never equal-weight tiles. |

**Structure** (determines layout geometry):

| Structure | Signal | Layout Pattern |
|-----------|--------|---------------|
| Single point | One core concept | One anchor element dominates |
| Contrast | A vs B | Split panel, two poles |
| Hierarchy | Layers build on each other | Stacked modules, pyramid |
| Flow | Sequential steps | Vertical cascade, numbered items |
| Radial | Core + derivatives | Hub with surrounding panels |
| Parallel | Multiple equal concepts | Asymmetric grid |

**Mood** (determines color temperature):

| Mood | Visual Feel |
|------|------------|
| Reflective | More whitespace, serif-heavy, lower contrast |
| Sharp | Strong contrast, bold type, vivid accent |
| Warm | Earth tones, rounded feel, gentle rhythm |
| Technical | Monospace accents, grid-like density |

### Rule 4: Tone Sensing
Auto-select color palette based on content topic:

| Content Tone | Background | Accent | Trigger Keywords |
|---|---|---|---|
| Philosophical | `#FAF8F4` | `#7C6853` | cognition, thinking, meaning, philosophy |
| Technical | `#F5F7FA` | `#3D5A80` | architecture, algorithm, system, API, code |
| Literary | `#FBF9F1` | `#6B4E3D` | story, narrative, writing, poetry |
| Scientific | `#F4F8F6` | `#2D6A4F` | experiment, data, research, paper |
| Business | `#F4F3F0` | `#2D6A4F` | market, strategy, growth, finance |
| Creative | `#F6F3F2` | `#B8432F` | design, art, aesthetics, inspiration |
| Default | `#FAFAF8` | `#4A4A4A` | When no clear match |

When a style template is explicitly chosen, its colors take precedence over tone sensing.

### Rule 5: Title Protection
If the user provides a title explicitly, use it as-is. Put editorial interpretation into subtitle or summary.

### Rule 6: Typography Hierarchy
- Hero title: `32px–48px`, weight 700–900, tight letter-spacing (`-0.02em`)
- Subtitle: `16px–20px`, weight 400–500
- Body text: `14px–16px`, weight 400, line-height `1.6–1.7`
- Meta/tags: `11px–13px`, weight 500–700, uppercase with letter-spacing
- Body text color: never pure black — use `#1a1a1a`, `#333`, or `#4a4a4a`

### Rule 7: Visual Weight Distribution
At least one module should feel visually heavier than the others. Differentiate through scale, background tone, typographic weight, or accent rules.

### Rule 8: Security
NEVER output `<script>`, `on*` event handlers, `javascript:` URIs, or `<iframe>`.

## Layout Templates

| Layout | File | Best For |
|--------|------|----------|
| Hero Card | [layouts/hero-card.md](../infocard/layouts/hero-card.md) | Single-topic highlight |
| Bento Grid | [layouts/bento-grid.md](../infocard/layouts/bento-grid.md) | Multi-faceted content |
| Split Panel | [layouts/split-panel.md](../infocard/layouts/split-panel.md) | A vs B comparison |
| Timeline Flow | [layouts/timeline-flow.md](../infocard/layouts/timeline-flow.md) | Chronological events |
| Metric Board | [layouts/metric-board.md](../infocard/layouts/metric-board.md) | KPI dashboard |
| Stacked Modules | [layouts/stacked-modules.md](../infocard/layouts/stacked-modules.md) | Hierarchical information |

## Style Templates

| Style | File | Tone |
|-------|------|------|
| Editorial Warm | [styles/editorial-warm.md](../infocard/styles/editorial-warm.md) | Classic editorial |
| Tech Blueprint | [styles/tech-blueprint.md](../infocard/styles/tech-blueprint.md) | Technical documentation |
| Japanese Minimal | [styles/japanese-minimal.md](../infocard/styles/japanese-minimal.md) | Zen-inspired minimalism |
| Neo Brutalism | [styles/neo-brutalism.md](../infocard/styles/neo-brutalism.md) | Bold, raw design |
| Corporate Clean | [styles/corporate-clean.md](../infocard/styles/corporate-clean.md) | Professional business |
| Glassmorphism | [styles/glassmorphism.md](../infocard/styles/glassmorphism.md) | Modern frosted glass |
| Swiss Grid | [styles/swiss-grid.md](../infocard/styles/swiss-grid.md) | Structured, precise |
