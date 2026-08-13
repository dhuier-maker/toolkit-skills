# IoT Architecture Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Quick Start

Select device/sensor icons → Place edge gateways → Connect to cloud services → Group into zones → Wrap in ```plantuml fence.

## Core IoT Stencils

| Category | Stencils | Purpose |
|----------|----------|---------|
| IoT Platform | `iot_core`, `internet_of_things`, `iot_1click` | Central IoT hub / message broker |
| Edge/Gateway | `greengrass`, `iot_device_gateway`, `freertos`, `iot_expresslink` | Edge computing & device gateway |
| Greengrass | `iot_greengrass_component`, `iot_greengrass_nucleus`, `iot_greengrass_stream_manager` | Edge runtime components |
| Device Mgmt | `iot_device_management`, `iot_device_defender`, `iot_device_tester`, `iot_over_the_air_update` | Fleet provisioning, security, OTA |
| Analytics | `iot_analytics`, `iot_analytics_channel`, `iot_analytics_pipeline`, `iot_analytics_dataset`, `iot_analytics_data_store` | IoT data processing pipeline |
| Events/Rules | `iot_events`, `iot_device_defender_iot_device_jobs` | Event detection & job execution |
| Digital Twin | `iot_twinmaker`, `iot_sitewise`, `iot_sitewise_asset`, `iot_sitewise_asset_model` | Asset modeling & visualization |
| Fleet | `iot_fleetwise`, `iot_device_management_fleet` | Vehicle & device fleet telemetry |

## Device & Sensor Stencils

| Category | Stencils |
|----------|----------|
| Sensors | `sensor`, `iot_thing_temperature_sensor`, `iot_thing_humidity_sensor`, `iot_thing_vibration_sensor` |
| Actuators | `actuator`, `iot_thing_relay`, `iot_thing_stacklight` |
| Industrial | `factory`, `iot_thing_industrial_pc`, `iot_thing_plc` |
| Smart Home | `thermostat`, `alexa_enabled_device`, `alexa_smart_home_skill`, `camera`, `camera2` |
| Protocols | `mqtt_protocol`, `iot_lorawan_protocol`, `iot_greengrass_protocol` |
| Robotics | `robomaker`, `iot_roborunner` |

## Quick Example

```plantuml
@startuml
left to right direction
rectangle "Factory Floor" {
  mxgraph.aws4.sensor "Temp\nSensor" as s1
  mxgraph.aws4.iot_thing_plc "PLC" as plc
}
mxgraph.aws4.greengrass "Greengrass\nEdge" as gg
mxgraph.aws4.iot_core "IoT Core" as core
mxgraph.aws4.iot_analytics "IoT\nAnalytics" as analytics

s1 --> gg : MQTT
plc --> gg
gg --> core
core --> analytics
@enduml
```

## Examples

See [examples/iot/](../examples/iot/) for complete toolkit-diagram-generator examples.
