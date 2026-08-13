# Infographic Template Reference

**Engine**: Infographic DSL | **Code Fence**: ```infographic

> **CHECK TEMPLATES:** Wrong template names WILL cause render failures.

## Available Templates

### Feature List / Checklist
`list-grid-badge-card`, `list-grid-candy-card-lite`, `list-grid-ribbon-card`, `list-column-done-list`, `list-column-vertical-icon-arrow`, `list-column-simple-vertical-arrow`, `list-row-horizontal-icon-arrow`, `list-row-simple-illus`, `list-sector-plain-text`, `list-zigzag-down-compact-card`, `list-zigzag-down-simple`, `list-zigzag-up-compact-card`, `list-zigzag-up-simple`

### Timeline / Milestones
`sequence-timeline-simple`, `sequence-timeline-rounded-rect-node`, `sequence-timeline-simple-illus`

### Step-by-step Process
`sequence-snake-steps-simple`, `sequence-snake-steps-compact-card`, `sequence-snake-steps-underline-text`, `sequence-stairs-front-compact-card`, `sequence-stairs-front-pill-badge`, `sequence-ascending-steps`, `sequence-ascending-stairs-3d-underline-text`, `sequence-circular-simple`, `sequence-pyramid-simple`, `sequence-mountain-underline-text`, `sequence-cylinders-3d-simple`, `sequence-zigzag-steps-underline-text`, `sequence-zigzag-pucks-3d-simple`, `sequence-horizontal-zigzag-underline-text`, `sequence-horizontal-zigzag-simple-illus`, `sequence-color-snake-steps-horizontal-icon-line`

### Product Roadmap
`sequence-roadmap-vertical-simple`, `sequence-roadmap-vertical-plain-text`

### Funnel / Conversion
`sequence-filter-mesh-simple`, `sequence-funnel-simple`

### A vs B Comparison
`compare-binary-horizontal-underline-text-vs`, `compare-binary-horizontal-simple-fold`, `compare-binary-horizontal-badge-card-arrow`, `compare-hierarchy-left-right-circle-node-pill-badge`

### SWOT Analysis
`compare-swot`

### Priority Matrix 2×2
`quadrant-quarter-simple-card`, `quadrant-quarter-circular`, `quadrant-simple-illus`

### Org Tree / Hierarchy
`hierarchy-tree-tech-style-capsule-item`, `hierarchy-tree-curved-line-rounded-rect-node`, `hierarchy-tree-tech-style-badge-card`, `hierarchy-structure`

### Charts
`chart-pie-plain-text`, `chart-pie-compact-card`, `chart-pie-donut-plain-text`, `chart-pie-donut-pill-badge`, `chart-bar-plain-text`, `chart-column-simple`, `chart-line-plain-text`, `chart-wordcloud`

### Relation / Circle
`relation-circle-icon-badge`, `relation-circle-circular-progress`

## Syntax Structure

```plain
infographic <template-name>
data
  title Title
  desc Description
  items
    - label Label
      value 12.5
      desc Explanation
      icon mdi/rocket-launch
theme
  palette #3b82f6 #8b5cf6 #f97316
```

## Syntax Rules

- First line: `infographic <template-name>` (must match template list exactly)
- 2-space indentation
- `key value` pairs (space-separated, **NOT** `key: value`)
- `-` prefix for arrays
- Compare templates need exactly 2 root items with `children`
- SWOT needs exactly 4 items (Strengths/Weaknesses/Opportunities/Threats in English)
- Quadrant needs exactly 4 items with `children`
- List templates use `desc` not `value`
- `hierarchy-structure` max 3 levels
- Use `desc` not `description`
- Use `items` not `steps`

## Common Mistakes (will cause render failure)

```plain
❌ WRONG — Do NOT use YAML colon syntax:
template: list-grid-badge-card     ← wrong! no "template:" key
title: My Title                    ← wrong! colons are not allowed
items:                             ← wrong! no colon after items
  - label: Item One                ← wrong! no colon after label
    description: Some text         ← wrong! field is "desc" not "description"
    value: "100"                   ← wrong! no colon, and value must be numeric
steps:                             ← wrong! field is "items" not "steps"

✅ CORRECT — Space-separated key-value, 2-space indent:
infographic list-grid-badge-card
data
  title My Title
  items
    - label Item One
      desc Some text
      value 100
```

## Data Fields

| Field | Description | Example |
|-------|-------------|---------|
| `label` | Item title/name (required) | `label Q1 Sales` |
| `desc` | Description text | `desc $1.28B \| +20%` |
| `value` | Numeric value (charts/funnels only) | `value 128` |
| `time` | Time label (timeline templates only) | `time Q1 2024` |
| `icon` | Icon: `mdi/icon-name` ([Iconify](https://icon-sets.iconify.design/)) | `icon mdi/star` |

## Advanced Syntax & Examples

See [references/syntax.md](../infographic/references/syntax.md) and [references/templates.md](../infographic/references/templates.md) for detailed template descriptions and [references/examples.md](../infographic/references/examples.md) for complete examples.
