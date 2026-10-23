# Validation and evidence requirements

Status: acceptance specification. Application cases below have not been executed in this repository. The documentation check is a separate, limited repository-maintenance check.

## Required behavioral cases

| Case | Required outcome | Evidence |
| --- | --- | --- |
| Compatible update | Accepted workflow outcomes scoped to exact candidate | Baseline/candidate assertions, run subjects, traces |
| Application regression | Original failed assertion remains failed | Assertion and baseline comparison |
| Wrong serving runtime | Functional pass cannot produce a supported remediation result | HTTP-target to process/image observation chain |
| Stale or wrong-target result | Reject evidence for a different current subject | Expected and observed identity mismatch |
| Changed test manifest | Prevent use under the old verification approval | Manifest digests and controller outcome |
| Revoked queued action | Deny before execution | Grant revocation and dispatch/execution events |
| Direct call without grant | Deny consistently across clients | API/MCP response and controller event |
| Malicious tool/page content | No expanded authority or changed target | Tested payload, allowed scope, resulting tool requests |
| Restart or duplicate delivery | Reconcile state without unaccounted duplicate action | Durable job/events, idempotency outcome, artifacts |
| Speech interruption | Old audio stops and cannot resume; job stays coherent | Timing and interaction record |
| Missing required security observation | Candidate-security result remains pending | Verification plan and explicit missing evidence |
| Baseline failure | Compatibility result remains inconclusive | Baseline failure and correct disposition |

Do not generalize success on the malicious-content fixtures into a claim of universal prompt-injection resistance.

## Core measurements

Record the exact code commit, recipe revision, candidate and test identities, environment, hardware, model/provider configuration, measured values, failures, and reproduction steps.

- End-to-end time from authorized finding selection to reviewable evidence.
- Execution/build time separately from model and voice time.
- Actual model usage and estimated/observed cost with pricing date.
- Correct dispositions and unsupported conclusions on the published cases.
- Manual interventions and repair attempts.
- Speech-recognition behavior for technical names, versions, ambiguity, and noise.
- Whole-response latency from end of user speech to first useful spoken output.
- Audible interruption latency and absence of stale audio.

The initial voice targets are median response start at most 1.5 seconds, p95 at most 3 seconds for short evidence questions after warm-up, and audible interruption at most 250 ms. These are targets, not results. Evaluate at least 30 utterances under concurrent rehearsal load and retain failed cases. Label a small sample as such.

## One-agent versus three-role comparison

Use the same public cases, tool affordances, evidence requirements, and approximately equal model/resource budgets. Record correct dispositions, unsupported claims, time, manual steps, and cost. Report raw cases and limitations rather than a favorable aggregate alone. The experiment determines whether orchestration adds value; authority separation and independent runner evidence remain required.

## Independent verification

The bundle verifier checks artifact hashes, subject identity, schema validity, required observations, and internal consistency. Reproduction in a second environment supplies additional execution evidence. A signature authenticates a statement only relative to an established trust configuration; it does not prove the runner host was uncompromised.

Keep these outputs distinct:

- Integrity/identity checks.
- Application assertions.
- Candidate security observations and missing requirements.
- Production verification.

## Documentation and public claims

Run `python3 scripts/check_docs.py` for relative-link and required-document checks. CI runs the same command. A passing documentation workflow does not validate application execution, Tenable integration, security effectiveness, or voice quality.

Before marking a capability verified, link its evidence from `PROJECT_STATE.md`. Before using a claim in the form or demo, check the claim-to-proof table in `DEMO.md`. Redact sensitive artifacts deliberately; public evidence should use the redistributable lab and synthetic data.

## Release gate

The release is ready when another engineer can perform a clean installation in a second environment, execute the published application recipe, verify its newly produced evidence bundle, understand its limitations, and reproduce the disclosed challenge outcomes. Record actual prerequisites and execution evidence. Keep zero-key replay and inspection as separate onboarding and demonstration fallback modes; they do not satisfy the reproduction gate.
