# Security policy

Remediate is in its planning/foundation stage. There is no supported application release or production security guarantee yet.

## Reporting a concern

Do not put credentials, private Tenable findings, exploitable customer details, or sensitive targets into a public issue. Use GitHub's private vulnerability-reporting interface if the repository exposes it. If it is not enabled, ask the maintainer for a private reporting channel without including sensitive details. A dedicated channel has not yet been established.

Public issues may describe nonsensitive design concerns or reproducible behavior using the published synthetic fixtures.

## Development boundaries

Use controlled applications and synthetic data. The existence of a Tenable account is not authorization to scan or change arbitrary assets. Keep approved target scope explicit and observe the grant model in the build plan.

The first release prepares a candidate and evidence for human review. It does not claim that a successful rehearsal proves production is remediated. Bundle integrity checks do not prove the runner host was uncompromised.

See [architecture](docs/ARCHITECTURE.md), [Tenable integration](docs/TENABLE.md), and [validation](docs/VALIDATION.md) for the proposed controls and their acceptance criteria.
