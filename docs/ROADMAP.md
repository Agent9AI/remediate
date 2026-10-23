# Flexible day-by-day build plan

The seven days are **ordered milestones with exit criteria**. They are not mandatory calendar days. A focused session can finish several milestones; a difficult milestone may take more than one session. Advance when dependent work is demonstrably complete. Parallelize independent tasks against agreed contracts.

Staffing assumption: three contributor responsibilities, not a confirmed three-person team. One person may cover several responsibilities.

| Owner role | Responsibility |
| --- | --- |
| Runner and evidence | Application recipe, execution, assertions, runtime observations, export and verifier |
| Controller and integrations | Shared schemas, state, grants, Hexa, agent roles, model budget |
| Interface and voice | Review UI, transcript, audio, evidence navigation, action previews |

## Day 1 — Prove the foundation

- [ ] Freeze initial `Job`, `RunSubject`, `ExecutionGrant`, `ApplicationRecipe`, `EvidenceItem`, `Verdict`, and `VoiceReply` contracts.
- [ ] Inspect compatible owner-supplied source and record exact files/commits selected for reuse.
- [ ] Establish the first service/UI execution path and one documented development command.
- [ ] Authenticate to Hexa, discover actual tools, and retrieve one authorized finding.
- [ ] Preserve finding provenance, `observed_at`, and `retrieved_at`; explicitly map it to the controlled lab application.
- [ ] Establish the PHP baseline and frozen login/search/upload assertions.
- [ ] Enforce one grant in the service against a direct request.
- [ ] Audition browser recognition/synthesis on the demo hardware and choose the passing configuration.

**Exit:** a real finding read, a runnable application baseline, one enforced grant, and a measured speech preflight. Record precise blockers rather than checking off a fixture as live integration.

## Day 2 — Execute a real comparison

Depends on the relevant Day 1 contracts and baseline.

- [ ] Build isolated baseline and candidate environments with explicit resource/network policy.
- [ ] Keep accepted tests read-only outside the candidate workspace.
- [ ] Run identical workflows with equivalent relevant configuration and seeded data.
- [ ] Bind the tested HTTP target to container, image digest, serving process, and observed runtime.
- [ ] Persist jobs, attempts, state transitions, and actual events.
- [ ] Produce separate functional, candidate-security, and production states.

**Exit:** one actual candidate comparison with inspectable assertion and runtime evidence. Agent reasoning is not required for this milestone.

## Day 3 — Make results portable and enforceable

- [ ] Export a human report, machine-readable manifest, candidate diff, observations, and traces.
- [ ] Implement the independent bundle verifier and document its trust limits.
- [ ] Reject stale, wrong-candidate, wrong-target, and changed-test evidence.
- [ ] Enforce revocation at execution for queued work.
- [ ] Reconcile interruption/restart and duplicate work with durable state and idempotency.

**Exit:** the verifier and controller reject the published negative cases, and a bundle can be inspected outside the UI.

## Day 4 — Add bounded agent work

- [ ] Implement one reasoning provider adapter with explicit usage accounting and limits.
- [ ] Add analyst, change engineer, and verifier contexts with distinct permissions.
- [ ] Use the actual Hexa findings adapter in the end-to-end job flow.
- [ ] Permit at most the configured correction attempts and track each candidate separately.
- [ ] Complete one finding-to-reviewable-candidate path.

**Exit:** actual agent-produced permitted changes and their execution evidence are available. The controller still owns statuses.

## Day 5 — Make voice and evidence work together

- [ ] Connect speech to the same session, job revision, and action API as the UI.
- [ ] Return evidence references and panel navigation with spoken explanations.
- [ ] Stop synthesis, queued playback, and stale answer chunks when interrupted.
- [ ] Resolve action targets visibly and preserve the existing grant rules.
- [ ] Provide push-to-talk and text operation.
- [ ] Measure at least 30 representative utterances under concurrent rehearsal load.

**Exit:** a reviewer can ask for the failed check or serving runtime and see the exact artifact, with reliable interruption. Record measured results rather than target values.

## Day 6 — Validate the contender

- [ ] Pass the behavioral cases in `VALIDATION.md`.
- [ ] Run the published false-success fixture and corrected candidate.
- [ ] Measure the complete demonstration path, cost, and timing.
- [ ] Compare one-agent and three-role configurations on matched cases/budgets.
- [ ] Exercise the judge-selected stale-evidence challenge.
- [ ] Keep the candidate result and remaining production verification explicit.

**Exit:** a useful end-to-end outcome plus its challenge cases work together. Every public quantitative claim has recorded evidence.

## Day 7 — Reproduce, document, and rehearse

- [ ] Perform a clean installation in a second environment.
- [ ] Execute the published application recipe in that clean environment, verify its newly produced evidence bundle, and record actual prerequisites.
- [ ] Finalize model/dependency/license inventory, data-flow guidance, and setup instructions.
- [ ] Rehearse the pitch in the actual allotted format.
- [ ] Prepare a clearly labeled replay fallback and publish challenge fixtures.
- [ ] Update project state, submission claims, demo evidence, and session handoff.

**Exit:** another engineer can follow the documentation, execute the published recipe in the second environment, and verify its newly produced bundle. Keep zero-key replay as a separate onboarding/fallback mode. The demo ends with a review-ready update and evidence.

## Submission and event dates

These are external checkpoints; milestone labels above remain flexible.

- **Before November 1, 2026:** the team-and-idea form must be submitted by an authorized team member. Confirm roster privately and retain the receipt. The form gives no time or timezone; avoid last-minute assumptions. See `SUBMISSION.md`.
- **November 2–6:** SWARM Global window according to the organizer source recorded in the build plan.
- **November 5:** pitch date according to that source; verify the actual slot and any subsequent organizer updates.
- Complete the build early if possible and use remaining time for feedback, measured improvements, and rehearsal.

## Scope decisions under time pressure

Preserve the real application comparison, exact candidate identity, enforced authorization, evidence export, and dependable review interface. Remove extra stacks/providers, SMS/telephony, custom voices, multiple simultaneous operators, and optional proactive speech first.

If three agent roles do not improve the measured outcome within the same budget, simplify orchestration while retaining the separation of authority and independent execution evidence. If a voice configuration misses its quality gate, use the explicit contingency and retain text operation.

## Session handoff

Record completed gates, evidence paths, failed cases, unresolved blockers, and the next dependency-ready task in `PROJECT_STATE.md` and `SESSION_LOG.md`. A single session may check off Day 1 through Day 3 if all their evidence exists.
