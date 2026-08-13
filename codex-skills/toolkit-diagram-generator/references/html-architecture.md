# HTML/CSS Architecture Diagram Reference

**Engine**: HTML/CSS (embedded) | **Code Fence**: NONE — embed HTML directly in Markdown

## Critical Rules

### Rule 1: Direct HTML Embedding
Write architecture diagrams as direct HTML in Markdown. **NEVER** use code blocks (```html). The HTML should be embedded directly in the document without any fencing.

### Rule 2: No Empty Lines in HTML Structure
Do NOT add any empty lines within the HTML architecture toolkit-diagram-generator structure. Keep the entire HTML block continuous to prevent parsing errors.

### Rule 3: Incremental Creation Approach
1. **First**: Create the overall framework (wrapper, sidebars, main structure) and define all CSS styles
2. **Second**: Add layer containers with titles
3. **Third**: Fill in components layer by layer
4. **Fourth**: Add detailed content and refinements

### Rule 4: Flexible Layout Structure
- **Single Column**: Main content only (for simple architectures)
- **Two Column**: Main content + one sidebar (left or right)
- **Three Column**: Full layout with both sidebars (for complex systems)
  - **Left Sidebar**: Supporting systems (monitoring, operations, analytics)
  - **Main Content**: Core architecture layers (user, application, data, infrastructure)
  - **Right Sidebar**: Cross-cutting concerns (security, compliance, governance)

### Rule 5: Layer-Based Organization
Each layer should have:
- Clear semantic meaning (User, Application, AI/Logic, Data, Infrastructure)
- Consistent color coding
- Grid-based layout for components
- Appropriate nesting for sub-components

### Rule 6: Color Semantics
- **User Layer** — user-facing interfaces and clients
- **Application Layer** — business logic and API services
- **AI/Logic Layer** — intelligence, rules, processing engines
- **Data Layer** — databases, caches, storage
- **Infrastructure Layer** — containers, networking, DevOps
- **External Services** — third-party APIs (typically dashed border)

### Rule 7: Security
NEVER output `<script>`, `on*` event handlers, `javascript:` URIs, or `<iframe>`.

## Style Templates

| # | Style | File | Suitable For |
|---|-------|------|-------------|
| 1 | Steel Blue | [styles/steel-blue.md](../architecture/styles/steel-blue.md) | Consulting, banking, government |
| 2 | Ember Warm | [styles/ember-warm.md](../architecture/styles/ember-warm.md) | Retail, education, lifestyle |
| 3 | Neon Dark | [styles/neon-dark.md](../architecture/styles/neon-dark.md) | Tech talks, gaming, cybersecurity |
| 4 | Stark Block | [styles/stark-block.md](../architecture/styles/stark-block.md) | Creative studios, indie devs |
| 5 | Ocean Teal | [styles/ocean-teal.md](../architecture/styles/ocean-teal.md) | Travel, logistics, green tech |
| 6 | Dusk Glow | [styles/dusk-glow.md](../architecture/styles/dusk-glow.md) | Social media, entertainment |
| 7 | Rose Bloom | [styles/rose-bloom.md](../architecture/styles/rose-bloom.md) | Fashion, luxury, premium |
| 8 | Sage Forest | [styles/sage-forest.md](../architecture/styles/sage-forest.md) | Healthcare, agritech, clean energy |
| 9 | Frost Clean | [styles/frost-clean.md](../architecture/styles/frost-clean.md) | Developer docs, minimalist SaaS |
| 10 | Indigo Deep | [styles/indigo-deep.md](../architecture/styles/indigo-deep.md) | Enterprise white papers |
| 11 | Pastel Mix | [styles/pastel-mix.md](../architecture/styles/pastel-mix.md) | SaaS, startups, general tech |
| 12 | Slate Dark | [styles/slate-dark.md](../architecture/styles/slate-dark.md) | Enterprise dark mode, internal tools |

## Layout Templates

| # | Layout | File | Best For |
|---|--------|------|----------|
| 1 | Three-Column | [layouts/three-column.md](../architecture/layouts/three-column.md) | Complex systems with cross-cutting concerns |
| 2 | Single Stack | [layouts/single-stack.md](../architecture/layouts/single-stack.md) | Simple services, focused documentation |
| 3 | Left Sidebar | [layouts/left-sidebar.md](../architecture/layouts/left-sidebar.md) | DevOps-centric views |
| 4 | Right Sidebar | [layouts/right-sidebar.md](../architecture/layouts/right-sidebar.md) | Security/compliance emphasis |

## Examples

See [examples/architecture/](../examples/architecture/) for complete toolkit-diagram-generator examples.
