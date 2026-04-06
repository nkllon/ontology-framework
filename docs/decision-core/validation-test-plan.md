# Validation Test Plan

## Positive

- `python3 validate_decision_core.py`
  - expects `RDFLIB_PARSE_OK`
  - expects `SHACL_CONFORMS=true`

## Negative

- `python3 validate_decision_core.py /Users/lou/oracle/negative-decision-no-validation.ttl`
  - expects `SHACL_CONFORMS=false`
- `python3 validate_decision_core.py /Users/lou/oracle/negative-evidence-missing-confidence.ttl`
  - expects `SHACL_CONFORMS=false`
- `python3 validate_decision_core.py /Users/lou/oracle/negative-workflow-no-preflight.ttl`
  - expects `SHACL_CONFORMS=false`
- `python3 validate_decision_core.py /Users/lou/oracle/negative-classification-no-code.ttl`
  - expects `SHACL_CONFORMS=false`
- `python3 validate_decision_core.py /Users/lou/oracle/negative-recovered-artifact-missing-file.ttl`
  - expects `SHACL_CONFORMS=false`

## Semantic sanity checks

- Evidence layer must include the April 2025 cluster and the July 2025 alternatives branch.
- Workflow layer must show that preflight classification gates execution before downstream action.

## Stabilization checks

- Every ontology file must use the same base namespace.
- Namespace changes must not be used to represent repository or branch identity.
- Provenance must stay explicit through repository, branch, commit, and source file properties.
- Any future vocabulary change must keep the positive SHACL run green.
