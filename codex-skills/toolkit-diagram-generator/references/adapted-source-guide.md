# 适配后的来源指南

# Professional Diagram Generator

## Step 1: Identify Diagram Type

Read the user's request and match it to an engine and reference file.

### Routing Table

| User Intent Keywords | Engine | Code Fence | Reference File |
|---------------------|--------|------------|----------------|
| UML, class, sequence, activity, state, component, use case, deployment | PlantUML | ```plantuml | [plantuml-uml.md](references/plantuml-uml.md) |
| Cloud, AWS, Azure, GCP, Kubernetes, Alibaba, serverless | PlantUML | ```plantuml | [plantuml-cloud.md](references/plantuml-cloud.md) |
| Network, LAN, WAN, Cisco, topology, datacenter | PlantUML | ```plantuml | [plantuml-network.md](references/plantuml-network.md) |
| Security, IAM, zero-trust, encryption, firewall, compliance | PlantUML | ```plantuml | [plantuml-security.md](references/plantuml-security.md) |
| ArchiMate, TOGAF, enterprise architecture, EA, motivation | PlantUML | ```plantuml | [plantuml-archimate.md](references/plantuml-archimate.md) |
| BPMN, workflow, approval, EIP, value stream, process | PlantUML | ```plantuml | [plantuml-bpmn.md](references/plantuml-bpmn.md) |
| Data pipeline, ETL, data lake, warehouse, analytics, BI | PlantUML | ```plantuml | [plantuml-data-analytics.md](references/plantuml-data-analytics.md) |
| IoT, sensor, edge, smart home, digital twin, fleet | PlantUML | ```plantuml | [plantuml-iot.md](references/plantuml-iot.md) |
| Mind map, brainstorm, topic decomposition, decision tree | PlantUML | ```plantuml | [plantuml-mindmap.md](references/plantuml-mindmap.md) |
| Layered architecture, microservices, system tiers, tech stack | HTML/CSS | (no fence) | [html-architecture.md](references/html-architecture.md) |
| Info card, knowledge summary, data highlight, event card | HTML/CSS | (no fence) | [html-infocard.md](references/html-infocard.md) |
| Bar, line, scatter, heatmap, radar, word cloud, data chart | Vega-Lite/Vega | ```vega-lite / ```vega | [vega.md](references/vega.md) |
| Concept map, knowledge graph, free spatial layout | Canvas | ```canvas | [canvas.md](references/canvas.md) |
| Dependency, call graph, module hierarchy, package tree | DOT | ```dot | [graphviz.md](references/graphviz.md) |
| KPI, timeline, roadmap, SWOT, funnel, org chart, infographic | Infographic | ```infographic | [infographic.md](references/infographic.md) |

### Ambiguity Resolution

| Ambiguous Request | Default Choice | Alternative |
|------------------|----------------|-------------|
| "architecture toolkit-diagram-generator" | plantuml-archimate | html-architecture (if layered/tiered system) |
| "mind map" | plantuml-mindmap | canvas (if free spatial layout needed) |
| "chart" / "data visualization" | vega | infographic (if template-based) |
| "info graphic" | infographic | html-infocard (if single-topic card) |
| "network toolkit-diagram-generator" | plantuml-network | plantuml-cloud (if cloud network) |

## Step 2: Read Reference File

After identifying the toolkit-diagram-generator type, read the corresponding reference file for engine-specific syntax, stencils, and examples.

**For PlantUML diagrams**: Also read [plantuml-basics.md](references/plantuml-basics.md) for shared rules that apply to ALL PlantUML types.

**For stencil icons**: Read files in [stencils/](stencils/) only when you need specific icon names not listed in the type reference.

## Step 3: Generate Diagram Code

Follow the syntax rules from the reference file exactly.

### Universal Rules (All Engines)

1. **Syntax accuracy first** — Invalid syntax = broken toolkit-diagram-generator. Always verify against reference before output.
2. **Incremental creation** — For complex diagrams, build in steps: framework → elements → connections → styling.
3. **No placeholder data** — Use realistic example values, not "TODO" or "xxx".
4. **HTML safety** — For HTML-embedded diagrams (architecture, infocard): NEVER output `<script>`, `on*` event handlers, `javascript:` URIs, or `<iframe>`. Embed HTML directly in Markdown WITHOUT code fences. Keep HTML continuous (no blank lines within the block).
5. **JSON validity** — For Vega/Canvas/Infographic: Always output valid JSON with double quotes, no trailing commas.
6. **Code fence** — PlantUML uses ```plantuml or ```puml (NEVER ```text). DOT uses ```dot. Vega-Lite uses ```vega-lite. Canvas uses ```canvas. Infographic uses ```infographic.
