# Root Project Map

## Purpose

This map records the repositories and artifact clusters most relevant to the recovered
"structure -> validation -> traceability" line of development.

## Conclusion

The strongest precursor line is in `louspringer/ontology-framework`.
The follow-up archaeology across `notes`, `roadmap`, `org-spec`, and `first-source`
did not reveal an earlier or stronger root artifact for the decision-assurance model.

## Ranked Repository Roots

### 1. `/Volumes/lemon/gemini/ontology-framework`

Why it matters:
- Earliest domain ontology seed tied to Oracle/OCI.
- First clear validation and governance modeling.
- Contains the best anti-hype / anti-brute-force analysis branch.

Key clusters:
- `2024-10-31`: `oracle-oci-discovery-ontology.ttl`
- `2025-03-08` to `2025-03-09`: `session.ttl`, Oracle RDF session/model work
- `2025-04-12` to `2025-04-21`: validation, maintenance, checkin, traceability models
- `2025-07-08`: modeling alternatives and targeted hybrid architecture branch

Candidate spine files:
- `oracle-oci-discovery-ontology.ttl`
- `ontologist.prompt`
- `guidance/modules/validation.ttl`
- `issue_planning_process.md`
- `models/project_maintenance.ttl`
- `session.ttl`

Exploratory branches:
- `origin/cursor/evaluate-modeling-alternatives-to-ontologies-1411`
- `origin/feature/spore-validation-integration`

### 2. `/Volumes/lemon/Downloads/jimmy-hopper-ontology`

Why it matters:
- Rich ontology and SHACL work.
- Strong on structure and constraints.
- Too late and too domain-specific to be the root precursor.

Key signal:
- `evro.ttl`
- `mindtools/*.ttl`
- `prompts/exploratory-guidance.md`

### 3. `/Volumes/lemon/gemini/concept-modeling`

Why it matters:
- Strong schema/validation language.
- Reads more like a tool framework than a proto-governance ontology.

Key signal:
- `schemas/*.json`
- `README.md`
- `concept_modeling/models/project.py`

## Follow-up Repositories Checked

### `/Volumes/lemon/gemini/notes`

Result:
- No relevant early conceptual material.
- Repository begins in `2025-11-21`.

### `/Volumes/lemon/gemini/roadmap`

Result:
- Oldest repository scanned (`2019`), but signal is product/app config, not
  ontology, validation, or decision-assurance architecture.
- No meaningful precursor artifacts found.

### `/Volumes/lemon/gemini/org-spec`

Result:
- Useful TTL work, but late (`2025-12`) and focused on organizational data modeling.
- Not earlier than the ontology-framework line.

### `/Volumes/lemon/gemini/first-source`

Result:
- Builds RDF/TTL from Gmail material and extracts decisions from threads.
- Also late (`2025-12`) and downstream of the earlier modeling stance.

## Reconstructed Through-Line

The line that matters is:

`structure first -> validate continuously -> trace decisions -> govern changes`

## Trusted Skill Inputs

The local skill corpus is trusted input for reconstructing the execution layer.
The highest-value skill for the missing unification model is:

### `/Users/lou/.codex/skills/eudorus-control-tower/SKILL.md`

Reusable patterns harvested:
- preflight must run before live operations
- preflight classification is the single source of truth for blocked vs runnable state
- conclusions must not outrun classification evidence
- live state fetch only after authoritative preflight
- compare against prior artifacts, not memory alone
- blockers and next actions must come from evidence, not guesswork

This skill is the clearest operational expression of:

`validation gates action -> evidence constrains conclusions -> prior artifacts anchor delta analysis`

Secondary useful skill:

### `/Users/lou/.codex/skills/daily-ops-story-report/SKILL.md`

Reusable patterns harvested:
- gather evidence before conclusions
- partition work into causal stories, not a changelog
- model at least scope, trigger, constraint, evidence, decision, outcome, next step, and risk
- persist both TTL and SHACL artifacts

That line appears first as a domain seed in Oracle/OCI learning ontology work,
then becomes operational in the ontology-framework validation and maintenance
cluster, and finally becomes self-aware in the July branch that rejects
unnecessary replacement or scale mythology.

## Most Likely Proto-Model

If only one repository root is used for unification, use:

`/Volumes/lemon/gemini/ontology-framework`

If only one precursor cluster is used, use:

`2025-04-12` to `2025-04-21`

If only one branch is used for the anti-scale stance, use:

`origin/cursor/evaluate-modeling-alternatives-to-ontologies-1411`
