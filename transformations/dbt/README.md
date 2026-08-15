# dbt Transformation Engineering

Introduce dbt when SQL model sprawl creates a need for dependency management, tests, documentation, model organization, and SQL-oriented lineage. dbt is not the scheduler and not a universal transformation mandate.

Responsibility map:

`Airflow -> orchestration`

`dbt -> SQL transformation/model dependency/testing/documentation`

`Spark/Databricks -> distributed computation/execution`

`Delta -> transactional table/storage semantics`

`Unity Catalog -> governance/catalog/access/lineage capabilities`

Choose direct SQL, dbt, PySpark, or a Databricks-native pipeline based on workload, complexity, scale, team capability, testing, maintainability, operations, and cost.
