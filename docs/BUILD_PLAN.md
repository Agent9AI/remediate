# Remediate by Agent9 — SWARM build plan

> Canonical engineering specification, revised 2026-10-23 from the full [Word brief](reference/Agent9-Remediate-SWARM-Build-Plan-2026-10-23.docx). This retains its complete engineering content, with the owner updates below integrated. The Word file is the original historical snapshot.

### Owner updates incorporated

- Product: **Remediate by Agent9**. Repository: https://github.com/Agent9AI/remediate .
- The owner has a **Tenable account with Hexa for testing**. Day 1 now includes actual authenticated discovery and a finding read; account access is not a completed integration test.
- Day labels are **ordered milestones**. Finish multiple milestones in one session when their completion criteria pass; do not wait for calendar dates.
- The actual team-and-idea form is due **November 1, 2026**. Its verified questions and draft answers are in [SUBMISSION.md](SUBMISSION.md).
- The demo's useful payoff is a tested, review-ready update. The false-success catch and judge challenge demonstrate why its evidence matters; see [DEMO.md](DEMO.md).
- Implementation remains planned. Use [PROJECT_STATE.md](PROJECT_STATE.md) for actual status and [ROADMAP.md](ROADMAP.md) for progress.

Engineering specification for the development team

23 October 2026

### Product decision

Build Remediate by Agent9 as an open source system that turns a Tenable finding into a tested, reviewable application update. It creates a baseline and candidate environment, executes identical application workflows, checks the actual candidate runtime, and packages the resulting evidence. The operator can inspect and question that evidence through an interruptible voice interface.

The submission is one product with one coherent demonstration. Reuse the owner's existing source as internal implementation material. The integrated system described here is to be built and validated; performance figures below are acceptance targets, not measured results.

### The engineering distinction

Every verdict belongs to an exact candidate, target, test manifest, advisory snapshot, and execution attempt. If any of those identities changes, the previous verdict cannot authorize a new candidate. This rule is enforced by the controller, independently of agent prose.

The demonstration must include a plausible false success: application tests pass, but the available evidence cannot establish that the serving runtime addresses the vulnerability. Remediate identifies the gap, shows the exact artifact, prepares a correction, and repeats the checks. A successful second candidate produces a review bundle with remaining production verification explicitly pending.

### Contest release scope

- One containerized PHP application in the PHP 8.4 family, with login, search, and upload workflows and synthetic data.

- One authorized Tenable finding read through Hexa MCP, plus a clearly labeled import fixture for reproducible evaluation.

- Three agent roles, a deterministic controller, and a bounded runner.

- Browser voice with local speech recognition and synthesis; one optional hosted speech adapter.

- A candidate diff, image identity, test results, and a portable evidence bundle with an independent verification command.

- A public repository with a working example, a small MCP interface, and one operating skill.

### Release boundaries

The contest build prepares changes for human review. Production deployment and closure of production findings remain outside its execution tools. Support for additional application stacks, phone calls, SMS, multiple simultaneous operators, and an integration marketplace follow a successful first release.

SWARM Global is scheduled for November 2 to 6, with pitches on November 5. Use seven ordered build milestones with three contributor responsibilities; complete several in one session when their exit criteria pass, and finish early when possible. Retain time for integration and presentation before the exact organizer deadline. The prior Black Hat recap emphasizes practical impact; it is useful guidance rather than a published Global scoring formula. [S01, S02]

## Product workflow and implementation stack

### The operator experience

The operator connects a Tenable source or opens a labeled fixture, selects the finding and application recipe, and reviews a proposed rehearsal. The approval identifies the target, allowed changes, fixed checks, execution limit, and model budget. The system then executes the approved job while displaying the actual agent activities and runner events.

The review screen has a baseline and candidate comparison, an evidence panel, a concise decision explanation, and voice or text input. Selecting an assertion opens its trace; selecting a security conclusion opens the observed runtime and advisory evidence. A visible input transcript lets the operator correct misheard identifiers before any consequential action.

### Chosen stack

| Component | Implementation | Purpose |
| --- | --- | --- |
| Web interface | Vite and TypeScript | Reuse compatible UI code and keep one application surface. |
| Local service | Node.js and TypeScript | Run the API, controller, agents, and tool authorization. |
| State | SQLite plus an artifact directory | Durable jobs, grants, attempts, events, and evidence without another account. |
| Execution | Rootless Podman and OCI images | Run baseline and candidate in separate environments. |
| Application checks | Playwright Test | Execute assertions and capture traces for the same workflows. |
| Speech input | Moonshine Voice browser WASM | Local streaming transcription. |
| Speech output | Phonon 31m English browser WASM | Local streaming speech without a speech API key. |
| Reasoning | One configurable model adapter | Isolated agent contexts with bounded token and call budgets. |
| External interface | MCP tools backed by the same service | Reuse the authorization and evidence rules across clients. |

Podman is available as free open source container tooling. Playwright traces expose executed interactions and supporting browser state. Those tools supply useful primitives; the application still needs explicit isolation policy and meaningful assertions. [S03, S04]

### Agent responsibilities

| Role | Output | Enforced limit |
| --- | --- | --- |
| Exposure analyst | Finding interpretation, advisory conditions, affected component, verification plan | Reads approved sources; cannot change code or assign a passing verdict. |
| Change engineer | Candidate patch and explanation | Writes only the candidate workspace and allowed files; cannot change accepted tests. |
| Verification agent | Evidence assessment, contradictions, remaining gaps | Reads outputs and requests another bounded run; cannot edit the candidate. |

## Evidence identity and workflow state

### Identity attached to every result

Record a run identifier and attempt identifier with the finding source, asset identity, repository commit, build context hash, resulting image digest, observed serving runtime, approved test manifest hash, synthetic data seed, relevant configuration hash, and advisory snapshot hash. Redact secrets before storing readable configuration; keep secret values out of exported artifacts.

The approved recipe establishes the target and permitted operation. Each built candidate receives its own immutable identity. The final review decision references that identity and its evidence. Modifying a candidate requires fresh execution and review; changing the scope requires a new grant.

### Separate result dimensions

| Dimension | Permitted states | Interpretation |
| --- | --- | --- |
| Application behavior | Passed, failed, inconclusive | What the approved workflows demonstrated. |
| Candidate remediation | Supported, contradicted, pending | Whether the available security evidence supports the stated remediation for this candidate. |
| Production verification | Pending, externally verified | Whether separate authorized evidence covers the deployed production target. |

Do not collapse these dimensions into a single green secure label. A verified image identity plus successful application checks is still insufficient when a required advisory condition or scanner result is missing. A stale result from a different target or attempt is rejected, rather than summarized as current evidence.

### State transitions

Jobs move through DRAFT, AWAITING_GRANT, BASELINE, CANDIDATE_BUILD, REHEARSAL, ASSESSMENT, and REVIEWABLE. Expected alternatives are BLOCKED, INCONCLUSIVE, CANCEL_REQUESTED, CANCELLED, and FAILED. The controller validates every transition and records the event that caused it.

Persist state changes and work dispatch through a transactional outbox. Workers use idempotency keys and leases. On restart, recover known completed outputs; an ambiguous external operation is surfaced for inspection before retry. Do not promise exactly once execution across arbitrary external services.

### Portable review bundle

Export a human-readable report, machine-readable manifest, candidate diff, image references, raw assertion results, traces, observed runtime metadata, advisory references, authorization summary, and cost or timing records. Include a reproduction recipe and the limits of the evidence.

Use an in-toto Statement v1 structure for the artifact subject and a versioned Remediate predicate for the checks. The standard binds a statement to an artifact digest; our predicate defines what the particular rehearsal checked. [S05]

The verify command recalculates artifact hashes and validates identities, required checks, and internal consistency. Its output explicitly distinguishes integrity checks from the truth of execution claims. Optional runner signatures require an independently configured trust key. A key embedded in the bundle alone does not establish trusted provenance, and neither hashes nor signatures prove that the runner host was uncompromised.

## Authorization and execution boundaries

### Bounded job grants

A grant contains the authenticated principal, job and recipe identity, allowed targets, source and tool identity, pinned tool contract, argument constraints, permitted file paths, expiry, maximum attempts, and resource budget. Store grants in the service and check them before dispatch and again at execution. Browser presentation is an explanation of the grant, not the authority that enforces it.

Revalidation matters when a queued action begins after revocation. New and queued actions must fail immediately after a grant is revoked. For running work, request cancellation, record whether it stopped, and preserve the partial result. Stopping audio and stopping a rehearsal are different operations.

### Tool contracts

Expose narrow tools such as inspect_finding, inspect_recipe, propose_candidate, run_rehearsal, inspect_evidence, and request_cancellation. Pin the source, descriptions, input and output schemas, annotations, and contract hash. Contract changes invalidate the corresponding approval until reviewed. Pinning metadata does not prove an unchanged implementation behind it.

Grant creation is an authenticated UI operation. Agents can request access but cannot approve it. The local service requires a session token and strict origin checks. Incoming MCP calls use the same controller and authorization. Provider credentials remain in the service and never enter tool results or application containers.

### Runner policy

Use a dedicated unprivileged runner identity, isolated temporary directories, resource limits, a fixed lifecycle, and explicit network rules. Mount the test harness read-only from outside the candidate workspace. Candidate code cannot access the host container socket, controller database, provider credentials, unrelated workspaces, or arbitrary host mounts.

The initial execution adapter starts approved recipes with typed parameters. It does not expose arbitrary host shell commands to the agents. Resolve paths and reject traversal or symlink escapes. Separate dependency acquisition from the restricted test run; cache only pinned artifacts and record their identities.

### Runtime observation

Determine the actual image and serving process through trusted runner inspection. An application endpoint reporting its own version is supplemental evidence. This prevents a changed configuration file or a different command-line binary from standing in for the runtime that served the application.

### Untrusted content

Treat advisory text, scanner output, repository comments, application pages, and external tool descriptions as data. They cannot create grants, change targets, disable checks, or authorize new tools. Exercise specific malicious-content fixtures as acceptance cases. Report the tested controls without claiming universal resistance to prompt injection.

## Local voice implementation

### Selected speech configuration

Use the current Moonshine Voice browser package, @moonshine-ai/moonshine-wasm, with the English Small Streaming model as the initial quality setting. The documented interface provides interim text and completed lines. Current English streaming checkpoints use MIT; pin the exact model and package version. [S06, S07]

Use phonon-tts with gradium/phonon-31m-en for speech output. The English q8 weights are 64.5 MB and Apache 2.0. This is the chosen commercial-friendly checkpoint; the 40m family has different, non-commercial terms. Gradium announced the new release on October 20 and 21. [S08, S09]

The browser package runs in a worker, streams audio, caches downloaded files, and supports cancellation. Threaded CPU execution requires cross-origin isolation; retain the documented single-thread path. Account for separately scheduled audio when interrupting playback. [S10]

Use one stock voice from the published voice assets. Preserve its license notice and validate pronunciation of technical terms. Do not make custom voice cloning part of the release. [S11]

### Hardware preflight

On first use, show download progress, verify pinned asset hashes, test microphone capture, load both speech models, and run a short recognition and synthesis check. Record browser capabilities, measured model load time, memory pressure, and response timing. The complete download and runtime memory exceed the TTS weights file size.

Test the actual demonstration laptop while the application rehearsal is running. If the default model misses the agreed resource or latency target, use Moonshine Tiny Streaming only if it preserves target and version recognition on the acceptance set. Otherwise select the explicit hosted recognition fallback. Speech quality and latency remain to be measured; vendor benchmark results are not our application results.

### Cost and account behavior

The default speech path runs on the user's device after model download. It needs microphone permission and compute, but no speech-provider account or recurring speech API charge. Hosted reasoning still incurs its own cost. Clearly show the active processing locations in settings.

Keep the speech adapter replaceable. Kokoro remains a practical local TTS fallback if Phonon fails the release audition. The fallback is a contingency, not a requirement to maintain two complete speech stacks for the first submission. [S12]

### The first voice interaction

The reviewer asks which check failed. The service retrieves the exact current result and returns a short answer with evidence identifiers and a panel-selection instruction. Speech reads the answer while the UI opens the referenced assertion. Questions about unverified claims return the actual gap, even when the change engineer described its work as successful.

## Voice behavior and collaboration

### Shared state for speech and screen

Voice and text use the same session, job revision, evidence index, and action APIs. The answer envelope contains spoken_text, evidence_refs, view_action, and optional proposed_action. Validate evidence references against the current job before delivery. The interface displays which run the answer describes.

Exact status questions can be answered from structured state without invoking an LLM. Open-ended explanations retrieve only the relevant evidence and use the existing reasoning adapter. This reduces cost and prevents every spoken question from starting another agent workflow.

### Interruption pipeline

Capture the microphone with echo cancellation where supported and keep speech work off the UI thread. Use interim transcription only to update the display and prepare read-only local evidence retrieval. Initiate a consequential request only after a completed, confirmed utterance.

When the reviewer interrupts, increment a generation identifier, cancel synthesis, stop queued playback nodes, and discard chunks from the old generation. Cancel the old answer request where possible. The rehearsal continues unless the operator separately requests its cancellation. A visible push-to-talk mode provides a dependable alternative in a noisy room.

### Pronunciation and action clarity

Display identifiers exactly. Read long identifiers in a deliberate spoken form, but preserve their original bytes in the evidence record. A phrase such as the second server must resolve to a visible selection before a proposed action is prepared. Low-confidence or ambiguous targets require a choice; they never trigger a guessed operation.

### Collaborative review

The demonstration supports a reviewer and presenter questioning the same session, with one authenticated control owner. Maintain an editable transcript and a visible evidence panel. Multi-user identity, speaker recognition, and a conference calling system are later work.

An optional event-driven interruption can announce a newly recorded contradiction, such as a stale result discovered during a review. It must refer to a deterministic controller event and provide a dismiss or mute control. Do not add open-ended monitoring of a room conversation to the first release.

### Hosted contingency

Implement one explicit Cloudflare speech adapter if the local acceptance gate fails. Use Whisper large v3 turbo for completed utterances; add Flux only if native streaming materially improves the measured experience. Keep local speech output when it passes. This avoids requiring separate speech vendor accounts.

Cloudflare currently includes 10,000 AI neurons daily. Its listed Whisper turbo rate is about $0.0005 per audio minute. At that rate, 100 input minutes are approximately $0.05 before allowances and other charges. This is speech recognition only, not total system cost. Free allocation is shared across Workers AI usage and is not a guarantee of sustained capacity. [S13]

## Tenable integration and the application recipe

### Live finding ingestion

Use an authorized Hexa MCP connection for the primary demonstration. Discover its actual advertised tools, pin the relevant contracts, and implement its required authentication in the backend. Do not hard-code an imagined tool name or assume the reused bearer-token adapter is sufficient.

Normalize the retrieved finding into source, finding identifier, asset identity, observed component, observation time, severity context, and evidence references. Preserve the raw response as an artifact with appropriate redaction. The mapping to an application recipe is explicit and reviewable.

A bundled JSON fixture supports development and repeatability. The UI shows live or fixture provenance. If live access cannot be validated, retain the functioning import workflow and describe the integration accurately; do not apply a live-integration badge without an actual successful read.

### First application

Use a small PHP 8.4 customer portal that the team can legally distribute and reproduce. Implement meaningful login, search, and upload assertions. Pin the baseline and candidate versions and image digests during the first engineering spike against the then-current vendor advisory. The October PHP disclosures provide the initial case, with their configuration conditions preserved. [S14]

The fixed test manifest includes expected login success and failure, search result contents, and upload persistence or rejection behavior. Record the data seed and environment configuration. Capture assertion outcomes and traces from the test runner. Baseline failure makes the comparison inconclusive until the baseline is repaired or the scope is revised with approval.

### Recipe schema

| Field group | Required content |
| --- | --- |
| Application | App ID, repository URL or local path, commit, owner-selected target mapping |
| Build | Context paths, baseline image, candidate constraints, pinned dependencies |
| Runtime | Startup recipe, ports, readiness checks, synthetic data initialization |
| Tests | Manifest hash, approved commands, expected assertions, timeouts |
| Security | Advisory snapshot, affected component, applicable conditions, required observations |
| Limits | Allowed files, network destinations, CPU and memory, duration, maximum attempts |

### Rehearsal rules

Run baseline and candidate with equivalent relevant configuration and the same approved tests. Scope failures precisely: application regression, security contradiction, missing evidence, or infrastructure error. Do not allow the agent to relabel a failed assertion as an infrastructure issue without supporting evidence.

Scanner confirmation of the candidate is included where the test setup can provide it. Missing scanner evidence remains pending when it is required by the verification plan. Production verification remains a separate recorded outcome.

## Demonstration and acceptance tests

### Four minute presentation target

1. Show one finding and its application mapping. Ask by voice for the proposed rehearsal and display the bounded approval.

2. Start a real run using warmed images. Show the baseline and candidate assertions and actual role activities.

3. Present the intentionally published false-success fixture. Functional checks pass while evidence reveals the wrong or unchanged serving runtime. The controller withholds a supported remediation verdict.

4. Ask how the system knows. Open the observed runtime and candidate artifacts while the voice explains the mismatch. Prepare the correction and execute a fresh attempt.

5. Export the review bundle. Run the independent verifier against it. Let the judge select a stale-evidence challenge or a revoked-grant replay; the expected rejection is visible.

6. State exactly what remains unverified and show the next human decision.

Label deliberately introduced fixtures and saved replay runs. Cache build dependencies and model weights, while identifying which execution results were generated live. Publish the challenge fixtures so others can inspect the demonstration. Adjust the sequence to the actual pitch time.

### Required behavioral cases

| Case | Pass condition |
| --- | --- |
| Compatible update | Correct workflow results and evidence scoped to the exact candidate. |
| Application regression | Original assertion remains failed and its baseline comparison is available. |
| Wrong serving runtime | Functional success cannot produce a supported security verdict. |
| Stale or wrong-target result | Controller rejects the result for the current candidate. |
| Modified test manifest | Rehearsal is blocked until a newly approved manifest is used. |
| Revoked queued action | Backend denies the action before execution. |
| Direct call without a grant | Same denial as the visible interface. |
| Malicious tool or page text | No increase in tool authority or change of target. |
| Restart or duplicate delivery | No unaccounted duplicate action; state and artifacts reconcile. |
| Speech interruption | Old audio stops and cannot reappear; the job continues unless separately cancelled. |

### Voice acceptance targets

On the declared demonstration laptop after warm-up, target median response start within 1.5 seconds and p95 within 3 seconds for short evidence questions. Target audible interruption within 250 ms. These are release goals, not claims about current performance. Measure the whole interaction from the end of user speech to useful speech output.

Use at least 30 utterances covering technical terms, versions, interruptions, ambiguous targets, and background noise. All consequential targets must resolve visibly before authorization. A failed voice gate activates the fallback and preserves the text workflow.

## Development milestones and ownership

### First engineering spike

Before expanding the system, prove four things: Hexa can return an authorized finding with an explicit lab mapping; the PHP baseline and candidate can run the frozen workflows; the service can enforce a grant against a direct call; and browser speech works on the intended laptop. Timebox the voice comparison so a fresh model does not consume the project.

### Delivery plan

| Window | Owner focus | Demonstrable completion |
| --- | --- | --- |
| Day 1 | All contributors | Shared contracts, app recipe, authenticated Hexa finding read and lab mapping, source baseline, browser speech preflight. |
| Days 2 and 3 | Runner and controller owners | Executed comparison, grant enforcement, export, portable verifier, stale-evidence rejection. |
| Day 4 | Controller and integration owner | End-to-end live finding integration, three roles, bounded candidate repair, complete review flow. |
| Day 5 | Interface and voice owner | Grounded voice, interruption, evidence navigation, explicit action previews. |
| Days 6 and 7 | All contributors | Negative cases, clean installation, benchmark, documented release, pitch and backup replay. |

The runner owner owns evidence and its verifier. The controller owner owns integration and authorization. The interface owner owns speech and presentation. Integrate their contracts from day one. Complete the build as early as possible; use remaining time, including the November 2 to 4 event window, for feedback and final fixes. Verify the actual organizer deadline and freeze before the November 5 pitch.

### Critical path

The build is viable when one finding, one app, one candidate, and one evidence bundle work together. The next milestone is reliable refusal of a false remediation claim. Voice is integrated against that established job and evidence API. This ordering keeps the demonstration grounded in actual execution.

### Scope reductions if time tightens

First remove SMS, telephony, extra providers, model debates, custom voices, and additional application stacks. Next remove multi-user collaboration and optional proactive announcements. Preserve the real application rehearsal, exact candidate identity, backend authorization, evidence review, and a dependable voice or text interface.

If three agent roles fail to improve results within the same budget, keep the same contracts and simplify their orchestration. The separation of authority and independent runner evidence remains valuable even with fewer model calls.

### Evaluation against a simpler baseline

Compare one-agent and three-role configurations on the same published cases and approximately equal resource limits. Record correct dispositions, unsupported conclusions, manual interventions, time to reviewable evidence, and cost. Publish raw results and failed cases; do not invent a percentage improvement in advance.

Before submission, perform one clean installation on a second machine or clean environment. Recreate a run from the recipe, verify its bundle, and record actual requirements. Avoid an undocumented developer-only setup.

## Repository contracts and operational costs

### Proposed code organization

| Location | Responsibility |
| --- | --- |
| apps/web | Review interface, transcript, browser audio, artifact viewer |
| apps/service | HTTP and MCP entry points, controller, persistence, worker queue |
| packages/contracts | Versioned job, grant, recipe, result, and voice schemas |
| packages/agents | Analyst, change engineer, verifier, provider adapter |
| packages/execution | Authorized tool dispatch and isolated runner adapters |
| packages/evidence | Manifest builder, report exporter, independent verifier |
| packages/voice | Local speech adapters and the optional hosted adapter |
| integrations/tenable | Discovery, authentication, finding normalization |
| fixtures/php-portal | Distributable app, synthetic data, fixed tests, challenge cases |
| skills/remediate | Operating instructions for external agent clients |

Reuse the supplied repository's compatible discovery, MCP client, contract normalization, interface, and activity components. Move them behind the new contracts and extend enforcement in the service. Browser session grants and tool-name heuristics are not substitutes for the new authorization model. Keep origin notices where required. [S15]

### Contracts to freeze first

Job stores state, recipe revision, current candidate, grant, attempts, and budgets. EvidenceItem stores producer, run and candidate identity, kind, timestamp, digest, and locator. Verdict stores separate functional, candidate-security, and production states with required evidence references. VoiceReply stores spoken text, referenced evidence, panel selection, and any proposed action. Validate every external payload against its schema.

### Low cost operating model

Local speech has no metered API charge. Local containers and storage require the user's hardware. A live reasoning model uses one configured provider credential or an already available local model. The owner has confirmed a Tenable account with Hexa for testing; successful authentication, tool discovery, and a real finding read remain to be verified. The open source project must not depend on introductory credits to function.

Set an application budget for each rehearsal, initially a configurable estimated $1 model ceiling and two repair revisions. Reserve estimated input and output costs before dispatch, cap outputs, count retries, and show actual provider usage when available. This is an application control, not a guarantee of the provider's final invoice. Avoid LLM calls for simple status retrieval and cache unchanged evidence summaries by their exact inputs.

A zero-key replay allows inspection and verification of saved artifacts, with its provenance displayed. Live agent reasoning requires the configured model; do not present replay as newly generated analysis.

The release should include a prerequisite checker, one documented launch path, source and model license inventory, export redaction controls, and an explanation of outbound data. The contribution guide expects a public repository and runnable documentation; use a permissive core license. [S16]

## Sources and engineering references

Sources were checked on 23 October 2026. Model packages, checkpoints, tool schemas, and container images should be pinned at implementation. Social announcements were used to locate releases; technical choices rely on the linked primary documentation and model cards. All proposed performance and cost limits in the plan remain to be measured or configured.

S01  [Tenable October 16 digest and Global schedule](https://exchange.tenable.com/digest/2026-10-16/)

S02  [Tenable Black Hat SWARM build recap](https://www.tenable.com/blog/agentic-ai-for-cyber-defenders-what-security-teams-built-at-black-hat-usa-2026)

S03  [Podman project](https://podman.io/)

S04  [Playwright Trace Viewer](https://playwright.dev/docs/trace-viewer)

S05  [in-toto Statement v1 specification](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md)

S06  [Moonshine Voice JavaScript quickstart](https://moonshine-voice.readthedocs.io/en/latest/quickstart/)

S07  [Moonshine current model architectures and licenses](https://moonshine-voice.readthedocs.io/en/latest/models/available-models/)

S08  [Phonon 31m English model card and license](https://huggingface.co/gradium/phonon-31m-en)

S09  [Gradium Phonon release announcement dated October 21](https://gradium.ai/blog/gradium-releases-phonon)

S10  [Phonon browser streaming and cancellation guide](https://github.com/gradium-ai/xn-ptts/blob/main/ptts-wasm/js/README.md)

S11  [Gradium stock voice assets and license](https://huggingface.co/gradium/phonon-voices)

S12  [Kokoro 82M model card](https://huggingface.co/hexgrad/Kokoro-82M)

S13  [Cloudflare Workers AI pricing updated October 20](https://developers.cloudflare.com/workers-ai/platform/pricing/)

S14  [PHP 2026 security announcements](https://www.php.net/archive/2026.php)

S15  [Owner supplied source repository for implementation reuse](https://github.com/Agent9AI/hitch)

S16  [CyberAgents Exchange contribution guide](https://github.com/tenable/cyberagents-exchange/blob/main/CONTRIBUTING.md)

S17  [Gradium release post on X](https://x.com/GradiumAI/status/2112563128487514512)

S18  [Developer demonstration on LinkedIn](https://www.linkedin.com/posts/glenn-sonna-99b18261_we-partnered-with-gradium-to-bring-day-zero-activity-7518327763888463873-QXXj)

### First work items

Assign the three owners. Freeze the shared schemas. Build the PHP recipe and the evidence exporter. Enforce one grant from end to end. Run the browser speech audition. Integrate the live Tenable read and agent roles against those contracts. The first review should examine an executed run and its bundle.
