# Decision Core Repo Integration Plan

## Purpose

This package is stable enough to move into a real repository once the target is
chosen. The goal of the move is to preserve ontology integrity, provenance, and
validation behavior without redesigning the model during migration.

## Recommended Package Surface

Move the following files as a single unit:

- `decision-core.ttl`
- `decision-core-core.ttl`
- `decision-core-evidence.ttl`
- `decision-core-workflows.ttl`
- `decision-core.shacl.ttl`
- `validate_decision_core.py`
- `requirements-decision-core.txt`
- `negative-decision-no-validation.ttl`
- `negative-evidence-missing-confidence.ttl`
- `negative-workflow-no-preflight.ttl`
- `negative-classification-no-code.ttl`
- `negative-recovered-artifact-missing-file.ttl`

Companion documents should move with the package unless the target repo already
has a stronger documentation structure:

- `decision-core-namespace.md`
- `decision-core-evidence.md`
- `validation-test-plan.md`
- `archaeology-findings.md`

## Repo Layout Recommendation

If the target repo has no ontology layout yet, use:

```text
ontology/
  decision-core/
    decision-core.ttl
    decision-core-core.ttl
    decision-core-evidence.ttl
    decision-core-workflows.ttl
    decision-core.shacl.ttl
    validate_decision_core.py
    requirements-decision-core.txt
    negative-*.ttl
    docs/
      decision-core-namespace.md
      decision-core-evidence.md
      validation-test-plan.md
      archaeology-findings.md
```

## CI Recommendation

Add the workflow template from:

- `.github/workflows/decision-core-validate.yml`

The CI gate should:

- run the positive SHACL validation
- run the negative fixtures and assert they fail
- fail fast if ontology dependencies drift or parsing breaks

## Promotion Rules

- promote the namespace once, after the target repo is chosen
- keep all repo, branch, commit, and file identities in provenance fields
- do not collapse the evidence layer into prose notes during migration
- do not weaken SHACL constraints just to simplify repo adoption

## Completion Criteria

The move is successful when:

- the package files are relocated without ontology breakage
- the positive validation still conforms
- the negative fixtures still fail for their intended reasons
- the namespace policy is updated exactly once for the target publication path
