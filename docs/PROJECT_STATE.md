# Project state

Updated: 2026-10-23. This file records evidence-backed development state, not aspirations.

## Current outcome

**Planning and repository foundation published to `main`. Application implementation has not started in this repository.**

The full Word build plan has been converted into the canonical Markdown specification. Supporting architecture, sprint, submission, demo, validation, contribution, and session documents capture the project for future humans and agents.

Foundation verification on 2026-10-23: the documentation check passed for 17 required files, 16 Markdown files, and 36 relative file links; the staged diff passed whitespace checks. The preserved Word snapshot is byte-identical to the supplied brief. Two independent reviews checked plan fidelity, submission accuracy, and architecture consistency. The complete foundation was published in commit `54fa8086df80fe45256096ad53901daeac6f998d`; its [GitHub documentation workflow](https://github.com/Agent9AI/remediate/actions/runs/40023507353) completed successfully. These checks do not establish application functionality.

## Owner decisions

| Item | Current decision |
| --- | --- |
| Product | Remediate by Agent9 |
| Repository | https://github.com/Agent9AI/remediate |
| Goal | A contender for Tenable SWARM with lasting open source value |
| Tenable access | Owner confirms a Tenable account with Hexa for testing |
| Source reuse | Full reuse of owner-supplied source is authorized |
| Costs | Minimize accounts and recurring cost; local speech preferred |
| Delivery pace | Build as early as possible; several day milestones can be completed in one session |
| Submission | Draft ready; form has not been submitted by this project workflow |
| Human team | Roster and team name not yet confirmed; three contributor roles are a staffing assumption |

## Capability ledger

| Capability | Status | Evidence / next verification |
| --- | --- | --- |
| Engineering handoff | implemented | Full plan and focused repository documents |
| Form question inspection | verified | Public form retrieved 2026-10-23; see `SUBMISSION.md` |
| Tenable account availability | owner-confirmed | Owner statement; not a runtime integration test |
| Hexa authentication and tool discovery | planned | Perform Day 1 read-only integration spike |
| Real finding and lab mapping | planned | Preserve source, asset, observed_at, retrieved_at, and mapping |
| PHP baseline/candidate runner | planned | Execute frozen workflows and observe serving runtime |
| Grants and durable controller | planned | Enforce direct-call and queued-action cases |
| Evidence export and verifier | planned | Validate exact identities and challenge stale results |
| Agent roles and bounded corrections | planned | Record actual proposals, diffs, and tool results |
| Browser voice | planned | Audition on intended machine under rehearsal load |
| Complete demo | planned | Pass the demo acceptance criteria |
| Clean install and measured results | planned | Run in a second environment and record actual outcomes |

`owner-confirmed` denotes a user-provided prerequisite, not an implemented capability. Do not turn it into an integration badge.

## Next session: Day 1 foundation

1. Establish the smallest runnable service and shared schemas.
2. Perform an authorized Hexa discovery and finding read using local secret configuration; keep raw tenant data out of git.
3. Identify a controlled lab application and explicit finding-to-recipe mapping.
4. Run the frozen PHP baseline workflows and record serving-runtime identity.
5. Enforce one bounded grant against a direct API/tool request.
6. Audition the selected speech stack on the intended hardware.

Continue into Day 2 as soon as these gates pass. Do not wait for the calendar.

## Open questions to resolve through implementation

- What authentication and tools does the actual Hexa connection expose?
- Which lab target and applicable advisory will be used? Which exact image versions/digests satisfy it?
- Can the account obtain candidate scanner evidence, and with what reachability and authorization?
- Which single reasoning provider is available for the first implemented adapter?
- Does the browser speech path meet the quality and latency targets on the actual demo machine?
- What is the actual pitch format and time allowance? The 90-second and four-minute scripts are our rehearsal targets.

## Honest claims today

The product is designed to create tested updates and reviewable evidence. Its integrated workflow is not built or measured yet. Do not describe production exposure as reduced, claim a completed Tenable verification loop, or publish numerical savings before execution evidence exists.
