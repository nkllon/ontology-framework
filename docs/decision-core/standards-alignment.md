# Decision Core Standards Alignment

## Verified Sources

The following standards sources were opened and verified in this turn:

- [PROV-O](https://www.w3.org/TR/prov-o/)
- [SHACL](https://www.w3.org/TR/shacl/)
- [SKOS Reference](https://www.w3.org/TR/skos-reference/)

## Immediate Alignments Applied

The current package now applies the minimal alignment that improves
interoperability without changing the model's thesis.

Applied now:

- `:Validation` is a subclass of `prov:Activity`
- `:Workflow` is a subclass of `prov:Activity`
- `:PreflightCheck` already inherits from `:Validation`, so it now aligns
  transitively as a provenance activity
- `:produces` is a subproperty of `prov:generated`

Why:

- validations and workflows are process-like, not entity-like
- evidence was already modeled as a provenance entity
- this gives the package a clean process/entity split without renaming the core
  vocabulary

## Intentionally Deferred

### SKOS for Classification Codes

`SKOS` is only worth adding if classification codes become a genuine controlled
vocabulary with external mappings or expansion pressure.

Deferred for now:

- `skos:ConceptScheme` for classification states
- replacing or aliasing `:classificationCode` with `skos:notation`

Reason:

- the current classification set is small
- adding SKOS now would increase ceremony without improving the core package

### Deeper PROV-O Enrichment

Deferred for now:

- `prov:wasDerivedFrom`
- `prov:hadPrimarySource`
- additional provenance activity chains for every recovered artifact

Reason:

- the current custom provenance fields already carry the archaeological identity
  needed for v1
- deeper PROV-O mapping is better done after the target repo and publication
  namespace are fixed

### Naming Cleanup

The class name `Validation` is usable, but it can read ambiguously beside SHACL
validation.

Possible later rename:

- `ValidationActivity`
- `ValidationRun`

Reason for deferral:

- the current name is understandable
- renaming now would create churn without changing model behavior

## Keep Custom

These terms should remain custom for now:

- `Policy`
- `Requirement`
- `Decision`
- `ChangeLog`
- `Outcome`
- `TrustedSkill`
- `RepositoryRoot`
- `BranchLineage`
- `ArtifactCluster`
- `RecoveredRole`
- `RecoveredArtifact`
- `ReportArtifact`

## Repo Landing Recommendation

The package should stay standalone while the namespace remains provisional.
When it moves, the best target repo is the precursor home:

- `ontology-framework`

That repo matches the recovered lineage and already has ontology-first tooling
and CI history, which makes it the right place for the first landing PR.
