# Data Analytics Pipeline Diagram Reference

**Engine**: PlantUML | **Code Fence**: ```plantuml | **Shared Rules**: [plantuml-basics.md](plantuml-basics.md)

## Quick Start

Define data sources → Declare ingestion/ETL icons → Connect to storage/warehouse → Add BI/visualization → Wrap in ```plantuml fence.

## Analytics & ETL Stencils

| Category | Stencils | Purpose |
|----------|----------|---------|
| Query Engine | `athena`, `athena_data_source_connectors` | Serverless SQL on S3 data |
| ETL | `glue`, `glue_crawlers`, `glue_data_catalog`, `aws_glue_data_quality`, `aws_glue_for_ray` | Data integration & cataloging |
| Streaming | `kinesis`, `kinesis_data_streams`, `kinesis_data_firehose`, `kinesis_data_analytics`, `kinesis_video_streams` | Real-time data streaming |
| MapReduce | `emr`, `emr_engine`, `emr_engine_mapr_m3`, `emr_engine_mapr_m5` | Big data processing (Spark, Hive) |
| Data Warehouse | `redshift`, `redshift_ra3`, `redshift_streaming_ingestion`, `redshift_ml` | Columnar analytics warehouse |
| Search | `opensearch_service_data_node`, `opensearch_ingestion`, `cloudsearch` | Full-text search & log analytics |
| BI | `quicksight` | Dashboards & visualizations |
| Data Lake | `lake_formation`, `s3`, `glacier`, `glacier_deep_archive` | Governed data lake storage |
| Streaming Kafka | `msk`, `msk_connect` | Managed Kafka streaming |

## Database Stencils

| Category | Stencils | Purpose |
|----------|----------|---------|
| Relational | `aurora`, `aurora_instance`, `rds`, `rds_instance`, `rds_mysql_instance`, `rds_postgresql_instance` | Transactional databases |
| NoSQL | `dynamodb`, `dynamodb_table`, `dynamodb_global_secondary_index`, `dynamodb_stream` | Key-value & document store |
| Graph | `neptune` | Graph database |
| In-Memory | `elasticache`, `elasticache_for_redis`, `elasticache_for_memcached` | Cache & session store |
| Document | `documentdb`, `documentdb_with_mongodb_compatibility` | Document database |
| Ledger | `quantum_ledger_database` | Immutable transaction log |
| Wide-Column | `keyspaces` | Cassandra-compatible |

## Connection Semantics

| Syntax | Meaning | Use Case |
|--------|---------|----------|
| `A --> B` | Solid arrow | Batch data flow / API call |
| `A ..> B` | Dashed arrow | Streaming / async / CDC |
| `A -- B` | Solid line | Bidirectional sync |
| `A --> B : "label"` | Labeled connection | Describe data format or volume |

## Quick Example

```plantuml
@startuml
left to right direction
mxgraph.aws4.s3 "Data Lake\n(S3)" as s3
mxgraph.aws4.glue "Glue\nETL" as glue
mxgraph.aws4.redshift "Redshift" as rs
mxgraph.aws4.quicksight "QuickSight" as qs

s3 --> glue
glue --> rs
rs --> qs
@enduml
```

## Examples

See [examples/data-analytics/](../examples/data-analytics/) for complete toolkit-diagram-generator examples.
