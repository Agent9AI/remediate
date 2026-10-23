# Remediate demonstration guide

**Project:** [Remediate by Agent9](https://github.com/Agent9AI/remediate)

**Status:** Planned demonstration and acceptance criteria. Integration, performance, and execution outcomes remain unverified until recorded by the build.

**Presentation targets:** 90 seconds and approximately four minutes. These are our rehearsal targets, not official event slots.

## The outcome the audience should remember

> Remediate turns a Tenable finding into a tested application update and the evidence an engineer needs to review it.

Start with a recognizable operational problem: a customer portal needs an update while login, search, and upload must keep working. End with a review-ready candidate change, executed checks, supporting security observations, and clearly stated remaining gaps.

The surprise is a convincing false success. The application's checks pass, but the actual serving runtime contradicts the proposed remediation. Remediate catches the mismatch, opens the supporting artifact on request, prepares a permitted correction, and produces fresh evidence for the corrected candidate.

The useful update is the payoff. The contradiction, voice interaction, and judge challenge make the quality of that outcome observable.

## First implementation milestone: a real Tenable read

The owner has confirmed access to a Tenable account with Hexa for testing. That establishes an available test account; it does not establish that our connector, scanner access, or any particular tool already works.

Move these checks into the first build milestone:

- Authenticate to the actual service and record the advertised tool contracts.
- Retrieve one suitable finding through an authorized read.
- Record finding ID, asset identity, original observation time, and retrieval time.
- Map the finding explicitly to the controlled application recipe.
- Determine whether the account and available tools can read relevant completed lab scan results.

Display `observed_at` separately from `retrieved_at`. A live retrieval can contain an older observation.

Prefer a deliberately provisioned lab asset whose finding and application recipe can be matched directly. If the rehearsal uses a separate sandbox, show that relationship and retain the original target's verification as pending.

**Optional confirmation:** read a completed, authorized lab rescan result if the account and tools support it. An operator may arrange that scan separately. The demonstration does not require scan-launch tools, production writes, or closure of a production finding. A scan result that predates the candidate cannot confirm that candidate.

The day-by-day build plan describes a sequence of completion gates. Multiple milestones may be completed in one session; no milestone requires waiting for a new calendar day.

## Five moments to make excellent

### 1. Show the application and the proposed change

Within the first 30 seconds, establish what must survive the update. Use a compact baseline/candidate table with meaningful login, search, and upload assertions, plus an actual application view. Keep the candidate diff one interaction away.

### 2. Reveal a disclosed false success

Publish and identify the wrong-runtime challenge fixture. Functional checks pass, while the security assessment remains contradicted or pending according to the available evidence.

Show the observation chain:

1. HTTP test destination.
2. Container identity and image digest.
3. Serving process and relevant configuration.
4. Observed runtime and applicable advisory condition.

A changed file, mutable image tag, or unrelated command-line PHP version is insufficient evidence about the process serving the application. Runner observations must establish the relationship.

### 3. Let a spoken question open the exact artifact

Suggested interaction:

> Reviewer: "Show me the runtime that actually served that request."

The answer identifies the current attempt and opens the corresponding observation. Spoken explanations should be short: the conclusion, why it matters, and where the evidence is visible.

If the reviewer interrupts, stop old synthesis and playback, discard late audio, and preserve the rehearsal's state. A separate request is required to cancel the rehearsal. Keep push-to-talk available in a noisy room.

### 4. Let the judge challenge the result

Offer one of two published cases:

- **Default:** present a successful result from an earlier candidate as evidence for the current candidate. The controller or independent verifier rejects the identity mismatch.
- **Technical follow-up:** revoke a grant while an operation is queued, then attempt execution. The service denies it at execution time.

Use explicitly scoped challenge fixtures. They must exercise the ordinary validation path, not a presentation-only status toggle or an unrestricted administrative bypass.

### 5. Deliver a review package

Finish with the candidate diff, exact artifact identity, assertion outcomes, runtime observations, and remaining gaps. Run the independent bundle verifier outside the main interface.

Its output should identify which checks succeeded: artifact integrity, subject identity, required evidence, and internal consistency. Hashes and signatures do not establish that a compromised runner executed honestly. A signing key supplied only inside an untrusted bundle does not establish an independent trust relationship.

## Ninety-second presentation

Use a real completed run for a compact recording or walkthrough, with a live challenge if the format permits. Editing a longer run into a short presentation is acceptable when elapsed time and replay provenance remain clear.

| Time | Screen and narration |
| --- | --- |
| 0:00–0:15 | Show the Tenable finding, mapped lab application, and observation time. "This portal needs an update. These customer workflows must survive." |
| 0:15–0:35 | Show baseline/candidate checks and actual execution events. "Remediate prepares a bounded candidate and runs the same accepted checks." |
| 0:35–0:55 | Reveal passing functional checks beside the runtime contradiction. "The tests passed, but the fix did not reach the serving runtime." Ask by voice to show the observation. |
| 0:55–1:15 | Show the corrected candidate and fresh evidence. Reject an earlier candidate's result when presented for this candidate. |
| 1:15–1:30 | Open the change and review bundle. "This is the update, what was tested, what supports the remediation, and what remains unverified." |

Do not imply that a longer execution completed in 90 seconds.

## Four-minute live demonstration

| Time | Action | Evidence the audience sees |
| --- | --- | --- |
| 0:00–0:35 | Read the finding, show its application mapping, ask for the rehearsal, and confirm bounded scope once. | Actual source, asset, observation time, recipe, and grant. |
| 0:35–1:20 | Start the baseline and candidate with preloaded dependencies and speech models. | Actual runner events and accepted assertions. Agent outputs appear as verification requirements, a diff, and an assessment. |
| 1:20–2:05 | The disclosed fixture passes application checks but retains the wrong serving runtime. Ask why, then interrupt to request the artifact. | Distinct functional and security outcomes; the exact runtime observation opens. |
| 2:05–2:55 | Prepare a correction within the grant when its scope permits, then execute a fresh attempt. | New candidate identity, fresh observations, and workflow outcomes. |
| 2:55–3:30 | Offer the stale-evidence challenge. Explain the rejection in one sentence. | Validation of identity through the real controller or verifier. |
| 3:30–4:00 | Export and inspect the review bundle. State the next human decision. | Candidate change, measured usage and duration, evidence limits, and production verification status. |

Measure this sequence early. If actual execution cannot fit, simplify the supported application/build path or use a clearly labeled replay segment. Cached dependencies and warmed models may be prepared before the talk; execution results must retain their actual provenance.

Keep the revoked-grant challenge, detailed agent comparison, and full trace inspection available for questions.

## Proof gates before making public claims

| Proposed claim | Evidence required |
| --- | --- |
| Integrated with Hexa | Successful authentication, actual tool discovery, and finding retrieval from the service. |
| Remediation confirmed by Tenable | A relevant authorized post-change observation for the correct target and candidate relationship. Initial finding retrieval alone is insufficient. |
| Addresses the selected exposure | Runtime/component identity, applicable advisory conditions, and every observation required by the declared verification plan. |
| Preserves application behavior | Meaningful assertions for the declared workflows, equivalent relevant configuration, and inspectable results. Scope the claim to those workflows. |
| Agent-produced correction | Candidate diffs and tool records showing the permitted change, followed by fresh execution. |
| Three roles improve outcomes | Matched cases and approximately equal budgets against a simpler baseline. Until measured, describe the role separation and permissions. |
| Responsive voice | End-to-end measurements on the declared demo hardware while the rehearsal runs. The build plan's latency figures remain targets. |
| Local speech | The actual speech execution path and outbound behavior; hosted reasoning and Tenable traffic remain separately disclosed. |
| Low operating cost | Recorded usage with account and hardware assumptions. A configured budget is a control, not a measured cost result. |
| Independently verifiable bundle | Explicit integrity, identity, consistency, and trust checks, with their limits stated. |
| Production remediated | Separate evidence covering the deployed production target. A sandbox outcome cannot supply this claim. |

## Demonstration readiness checklist

- [ ] One real Hexa finding is mapped to the controlled application with source and observation time visible.
- [ ] A useful candidate update executes against the accepted workflows.
- [ ] The wrong-runtime fixture is disclosed and detected from runner evidence.
- [ ] A spoken question opens the exact supporting artifact for the current attempt.
- [ ] Interruption stops old audio without changing the job unexpectedly.
- [ ] A judge-selected stale result is rejected through the ordinary validation path.
- [ ] A corrected candidate produces a fresh review package.
- [ ] A clean installation in a second environment executes the published application recipe and verifies its newly produced evidence bundle; replay/inspection alone does not satisfy this gate.
- [ ] Duration and model usage are measured, with warm/cold and replay conditions identified.
- [ ] Live, fixture, and replay provenance are visible at the relevant results.
- [ ] Infrastructure failure or missing evidence yields an honest pending/inconclusive outcome.
- [ ] The final screen identifies the reviewable change and what remains unverified.

## Presentation discipline

Lead with the application outcome and security finding. Show agent roles through useful outputs rather than a long transcript. Keep voice concise and evidence one interaction away. End on the completed review package after the challenge.

The primary stack and bounded release scope remain unchanged. Additional providers, phone calls, extra application stacks, and more agent roles are not needed to make this demonstration strong.
