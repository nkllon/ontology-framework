# Oracle Bridge Ontology

## Purpose

This bridge exists because the Oracle-related ontologies in the repository form
useful layers, but they do not yet say explicitly how those layers fit together.

The bridge ontology lives at:

- [models/decision-core/oracle-bridge.ttl](/Volumes/lemon/gemini/ontology-framework/models/decision-core/oracle-bridge.ttl)

## What It Connects

It connects four things that were previously only adjacent:

- OCI service discovery
- stakeholder and cloud-positioning concerns
- Oracle semantic runtime
- Oracle deployment and runtime substrate

## Bridge Assertions

### OCI Discovery To Semantic Runtime

This assertion links:

- `oracle-oci-discovery-ontology.ttl`
- `oracle_rdf.ttl`

Meaning:

- OCI service concepts, especially database and platform concepts, need an
  explicit handoff into Oracle semantic runtime concepts

### Semantic Runtime To Deployment

This assertion links:

- `oracle_rdf.ttl`
- `oracle_deployment.ttl`

Meaning:

- semantic storage concepts are not enough on their own
- the model also needs a deployment target and transformed-source path

### Discovery To Stakeholder Layer

This assertion links:

- `oracle-oci-discovery-ontology.ttl`
- `oci.ttl`

Meaning:

- stakeholder preference analysis should reference stable discovery concepts
  instead of inventing a parallel ontology of cloud-service identity

### Runtime To Infrastructure

This assertion links:

- `oracle_rdf.ttl`
- `oracle_deployment.ttl`
- `infrastructure/oracle/infrastructure.ttl`

Meaning:

- Oracle semantic runtime and deployment depend on database endpoint, service,
  user, and tablespace substrate

## Gaps Captured

The bridge also records the business-domain gaps that are still missing:

- Fusion Applications
- ERP
- HCM
- SCM
- CX
- E-Business Suite

## Why This Matters

Without this bridge, the repository has a stack but not a coherent Oracle
system map.

With the bridge, the repo can now say:

- where discovery concepts belong
- where stakeholder concerns attach
- where semantic runtime begins
- where deployment and database substrate take over

That gives you a proper Oracle ontology surface instead of unrelated Oracle
files that happen to coexist.
