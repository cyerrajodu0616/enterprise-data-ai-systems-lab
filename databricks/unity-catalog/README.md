# Unity Catalog: Problem-Driven Governance

Begin with access problems, not GRANT syntax:

- Finance can read aggregated financial data.
- A restricted team can access transaction-level data.
- Another domain can use behavioral data but not sensitive fields.
- Pipeline service identities can write only their assigned layers.
- An AI application can access only approved governed datasets.

Use these scenarios to study catalog/schema/table hierarchy, ownership, users/groups/service identities, privileges, least privilege, lineage, discovery, auditability, environment/domain design, and governed AI access. Classify each exercise by what the current environment can implement, simulate, or only design.

A governance product does not create good governance. Record policy ownership, grant approval and review, privilege-sprawl risk, incorrect grants, lineage limitations, operational processes, and organizational responsibility.
