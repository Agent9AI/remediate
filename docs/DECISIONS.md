# Decision log

Accepted project direction as of 2026-10-23. Record later decisions with date, reason, consequences, and which earlier decision they supersede. Owner instructions take precedence over this log.

| ID | Decision | Reason and consequence |
| --- | --- | --- |
| D001 | Product name is Remediate by Agent9; repository is `Agent9AI/remediate`. | Latest explicit owner choice. Use one product identity throughout docs and demo. |
| D002 | The full Word build plan becomes `BUILD_PLAN.md`; this repository is the continuing development record. | Future sessions must not depend on inaccessible chat history. Preserve the original Word snapshot for reference. |
| D003 | Day labels are ordered milestones, not calendar gates. | The owner wants to build early and may finish multiple days in a session. Exit criteria determine progress. |
| D004 | Hexa access is available for testing; perform the actual discovery and finding read in Day 1. | Owner-confirmed prerequisite removes the need to plan around missing account access. Successful authentication and reads still need evidence. |
| D005 | Full reuse of the owner's supplied source is authorized. | Audit and adopt compatible internals under Remediate contracts. Source reuse does not change the product objective or waive third-party notices. |
| D006 | First supported recipe is one PHP 8.4 application with login, search, and upload assertions. | A small complete workflow is reproducible. Select exact versions/configuration against the applicable advisory during implementation. |
| D007 | Use three scoped roles around a deterministic controller and independent runner. | Separate proposal, modification, and verification authority. Benchmark against a simpler agent configuration before claiming an advantage. |
| D008 | Evidence binds to exact candidate, target, tests, advisory/configuration, and attempt. | Stale or unrelated success cannot authorize a new result. Immutable digests replace mutable tags as identity. |
| D009 | Keep functional, candidate-security, and production outcomes separate. | Application compatibility and candidate evidence do not establish production remediation. |
| D010 | Prefer local browser speech with Moonshine Voice and Phonon 31m English, subject to a first-day audition. | Avoid recurring speech charges and extra accounts. Pin the exact licensed checkpoint; keep a narrowly scoped fallback. |
| D011 | One reasoning provider adapter initially; bounded spend and at most two repair revisions by default. | Keep cost and integration complexity controlled. The proposed $1 estimate is an application limit target, not a provider invoice guarantee. |
| D012 | Demo payoff is a tested, review-ready update; wrong-runtime detection is the surprise. | Show useful completed work, exact evidence, purposeful voice, and one judge-selected challenge. Disclose seeded fixtures. |
| D013 | First release prepares review artifacts; production deployment and finding closure are outside its tools. | Finish one useful supported workflow with clear evidence and a human decision. |
| D014 | Team submission is a separate milestone before November 1. | The supplied form requests team details and a short proposed idea; it is not the final build upload. Drafts must remain future tense until implementation evidence exists. |
| D015 | Use Apache-2.0 for original repository contributions. | Establish a permissive open source foundation. Imported code, models, and voices retain their own terms and notices. |

## Deferred scope

Phone calls, SMS, custom voice cloning, multiple concurrent operators, extra application stacks, multiple reasoning providers, production deployment automation, and an integration marketplace are follow-on work. Add them only after a specific user need and a completed core workflow justify the scope.

## Inputs and provenance

- Owner's supplied source for reuse: https://github.com/Agent9AI/hitch . Full reuse was authorized; file-level selection and compatibility still require an implementation audit.
- Original engineering brief: [Word snapshot](reference/Agent9-Remediate-SWARM-Build-Plan-2026-10-23.docx).
- Public repository quality reference: https://github.com/Chuck89760239/Hybrid-Edge-Cloud-Anomaly-Based-IDS-with-Agentic-AI-Threat-Hunting . It could not be retrieved anonymously at its exact URL on 2026-10-23 (HTTP 404). No claims about its contents or copied implementation are made. The requested high standard is being applied independently; review the reference later if it becomes accessible.

## Decision template

For a material change, record: date; owner or evidence; problem; decision; alternatives considered; affected contracts; migration work; verification required; and any superseded decision. Do not silently replace the stack because a new release appears.
