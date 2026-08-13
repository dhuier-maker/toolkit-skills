# ArchiMate Enterprise Architecture Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Quick Start

Add `!include <archimate/Archimate>` → Declare typed elements → Connect with `Rel_*` macros → Group into layers with `rectangle` → Wrap in ```plantuml fence.

## Critical Rules

- Must include `!include <archimate/Archimate>` before using any macros
- Element syntax: `Layer_Type(alias, "Label")`
- Relationship syntax: `Rel_Type(fromAlias, toAlias, "label")`
- Use `rectangle "Layer" { ... }` to group elements into ArchiMate layers
- Directional suffixes `_Up`, `_Down`, `_Left`, `_Right` control relationship direction

## Element Macros

### Business Layer

| Macro | ArchiMate Element |
|-------|-------------------|
| `Business_Actor(id, "Label")` | Business Actor |
| `Business_Role(id, "Label")` | Business Role |
| `Business_Process(id, "Label")` | Business Process |
| `Business_Function(id, "Label")` | Business Function |
| `Business_Service(id, "Label")` | Business Service |
| `Business_Event(id, "Label")` | Business Event |
| `Business_Interface(id, "Label")` | Business Interface |
| `Business_Collaboration(id, "Label")` | Business Collaboration |
| `Business_Object(id, "Label")` | Business Object |
| `Business_Product(id, "Label")` | Business Product |
| `Business_Contract(id, "Label")` | Business Contract |
| `Business_Representation(id, "Label")` | Business Representation |

### Application Layer

| Macro | ArchiMate Element |
|-------|-------------------|
| `Application_Component(id, "Label")` | Application Component |
| `Application_Service(id, "Label")` | Application Service |
| `Application_Function(id, "Label")` | Application Function |
| `Application_Interface(id, "Label")` | Application Interface |
| `Application_Process(id, "Label")` | Application Process |
| `Application_Interaction(id, "Label")` | Application Interaction |
| `Application_Event(id, "Label")` | Application Event |
| `Application_Collaboration(id, "Label")` | Application Collaboration |
| `Application_DataObject(id, "Label")` | Application Data Object |

### Technology Layer

| Macro | ArchiMate Element |
|-------|-------------------|
| `Technology_Device(id, "Label")` | Technology Device |
| `Technology_Node(id, "Label")` | Technology Node |
| `Technology_SystemSoftware(id, "Label")` | System Software |
| `Technology_Artifact(id, "Label")` | Technology Artifact |
| `Technology_CommunicationNetwork(id, "Label")` | Communication Network |
| `Technology_Path(id, "Label")` | Technology Path |
| `Technology_Service(id, "Label")` | Technology Service |
| `Technology_Process(id, "Label")` | Technology Process |
| `Technology_Function(id, "Label")` | Technology Function |
| `Technology_Interface(id, "Label")` | Technology Interface |

### Motivation Layer

| Macro | ArchiMate Element |
|-------|-------------------|
| `Motivation_Stakeholder(id, "Label")` | Stakeholder |
| `Motivation_Driver(id, "Label")` | Driver |
| `Motivation_Assessment(id, "Label")` | Assessment |
| `Motivation_Goal(id, "Label")` | Goal |
| `Motivation_Outcome(id, "Label")` | Outcome |
| `Motivation_Principle(id, "Label")` | Principle |

## Relationship Macros

| Macro | Meaning |
|-------|---------|
| `Rel_Access` | Access |
| `Rel_Aggregation` | Aggregation |
| `Rel_Assignment` | Assignment |
| `Rel_Association` | Association |
| `Rel_Composition` | Composition |
| `Rel_Flow` | Flow |
| `Rel_Influence` | Influence |
| `Rel_Realization` | Realization |
| `Rel_Serving` | Serving |
| `Rel_Specialization` | Specialization |
| `Rel_Triggering` | Triggering |

## Examples

See [examples/archimate/](../examples/archimate/) for complete toolkit-diagram-generator examples.
