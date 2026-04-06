# Decision Core Namespace Policy

## Status

The current Turtle files use a placeholder base namespace:

`https://example.com/decision-core#`

This is intentional for local design work. It avoids pretending the vocabulary
is published before the package is moved into its target repository.

## Freeze Rule

Until the target repository and publication path are chosen:

- do not invent additional base namespaces
- do not introduce repo-specific namespaces into the model
- keep all new ontology terms under the single decision-core namespace
- keep repository, branch, commit, and file identity in provenance properties
  instead of namespace changes

## Promotion Rule

When the package moves into its implementation repo, promote the namespace once
and only once. The replacement namespace should:

- be stable
- resolve to package documentation or published ontology files
- remain valid if the internal repo layout changes

## Candidate Promotion Targets

Pick one of these patterns later, not now:

- `https://ontology.louspringer.com/decision-core#`
- `https://louspringer.github.io/<repo>/decision-core#`
- `https://<target-domain>/ontology/decision-core#`

## Local Modeling Rule

Use the namespace to define:

- classes
- properties
- named example instances
- named recovered evidence instances
- named trusted workflow instances

Do not use the namespace to encode:

- local filesystem roots
- branch identity
- commit identity
- source file paths

Those belong in provenance fields such as:

- `:repoPath`
- `:repoRemote`
- `:branchName`
- `:commitHash`
- `:sourceFilePath`

## Versioning Rule

Treat namespace stability and ontology versioning separately.

- namespace should change only when the publication location changes
- ontology versions should change whenever the vocabulary or package structure
  changes materially

## Immediate Outcome

For the current local package, the model is considered stabilized if:

- every ontology file uses the same base namespace
- no repo-specific namespaces are introduced
- provenance remains explicit and file-level
- SHACL validation remains green after any vocabulary change
