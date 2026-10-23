# Contributing to Remediate

Thank you for helping build a useful, inspectable security workflow. Start with [AGENTS.md](AGENTS.md), [current state](docs/PROJECT_STATE.md), and the [roadmap](docs/ROADMAP.md).

## Choose a concrete outcome

Pick a dependency-ready milestone and identify its exit evidence. The day labels are flexible; several can be completed in one session. Avoid expanding the product before the core finding-to-candidate workflow works.

For implementation, agree on shared schemas before parallel changes. Keep the controller, runner, and interface responsibilities separate. Existing source may be reused under the owner's authorization, with a file-level compatibility review and required notices.

## Before a pull request

1. Explain the problem, the changed behavior, and the evidence that it works.
2. Run meaningful validation for the changed boundary. Use the cases in [VALIDATION.md](docs/VALIDATION.md).
3. For documentation changes, run `python3 scripts/check_docs.py` and review the rendered Markdown/diff. This check does not establish application functionality.
4. Update project state, relevant roadmap checkboxes, and the session log.
5. Record material decisions and any changed contract or migration requirement.
6. Keep secret configuration and sensitive findings outside git; publish only approved synthetic or sanitized artifacts.

Tests should challenge actual behavior or a material risk. Avoid tests that merely duplicate the implementation. Record failed or inconclusive cases rather than weakening assertions to create a pass.

## Pull request content

Use the supplied template to state why the change is needed, what now happens, validation evidence, and remaining limitations. Mark fixtures and replay data clearly. Link the relevant milestone or task.

Do not add success badges, performance claims, benchmark percentages, or completed integration claims before the corresponding evidence exists. Keep the README's status consistent with the actual repository.

## Development commands

The initial repository contains the engineering foundation and documentation check. Application setup/run commands will be added when implemented and tested in a clean environment. Do not publish a speculative quickstart as if it already works.

## Public collaboration

Use issues for project tasks and reproducible bugs. Do not include Tenable credentials, private findings, customer targets, personal contact details, or raw voice recordings. See [SECURITY.md](SECURITY.md) for sensitive reports.

Original contributions use Apache-2.0. Keep third-party licenses and attribution with imported material; see [DEPENDENCIES.md](docs/DEPENDENCIES.md).
