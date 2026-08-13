# Mind Map Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Critical Rules

- Every toolkit-diagram-generator starts with `@startmindmap` and ends with `@endmindmap`
- Each hierarchy level is represented by repeating markers:
  - `*` style: `*` (root), `**` (level 1), `***` (level 2)
  - `+/-` style: `+` grows left branch, `-` grows right branch
- Keep one marker style consistent in the same local branch
- Use `left side` to switch subsequent branches to the left side of the root
- Multi-line node content: `**:Line 1\nLine 2;`
- Quick color coding: `*[#Orange] Root`, `**[#lightgreen] Child`
- Reusable themes: define `<style>` and apply stereotypes like `<<green>>`

## Node Syntax Cheat Sheet

| Pattern | Meaning | Example |
|---------|---------|---------|
| `* Root` | Root node with star syntax | `* Product Strategy` |
| `** Child` | First-level child | `** Goals` |
| `*** Grandchild` | Deeper hierarchy | `*** KPI` |
| `+ Root` | Root node with +/- syntax | `+ Architecture` |
| `++ Left branch` | Branch expanding on one side | `++ Services` |
| `-- Right branch` | Branch expanding on opposite side | `-- Risks` |
| `***_ Boxless` | Boxless/minimal child node | `***_ Notes` |
| `# Root` | Alternative root marker style | `# Topic` |
| `**:...;` | Multi-line block node | `**:Item A\nItem B;` |

## Branch Side and Direction

| Control | Syntax | Use Case |
|---------|--------|----------|
| Left-side split | `left side` | Split map into left/right groups from root |
| Top-to-bottom | `top to bottom direction` | Tree-like vertical hierarchy |
| Right-to-left | `right to left direction` | RTL reading flow |

## Styling Options

| Method | Syntax | Best For |
|--------|--------|----------|
| Inline node color | `**[#FFBBCC] Idea` | Fast per-node emphasis |
| Reusable class style | `<style> ... .green { ... } </style>` + `<<green>>` | Consistent visual themes |
| Depth-based style | `:depth(1) { ... }` | Global formatting by hierarchy depth |

## Recommended Color Palettes

### General-Purpose (Pastel)

| Role | Hex | Usage |
|------|-----|-------|
| Root | `#2196F3` | Central topic |
| Branch A | `#A5D6A7` | Category / group 1 |
| Branch B | `#90CAF9` | Category / group 2 |
| Branch C | `#CE93D8` | Category / group 3 |
| Branch D | `#FFE082` | Category / group 4 |
| Leaf | `#E0E0E0` | Detail nodes |

## Examples

See [examples/mindmap/](../examples/mindmap/) for complete toolkit-diagram-generator examples.
