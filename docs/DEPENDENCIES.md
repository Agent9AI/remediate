# Dependencies, licenses, and cost policy

Status: selected candidates from the engineering plan. No application dependency lockfile, downloaded model, or runtime integration exists yet. Validate and pin exact versions/digests at implementation; retain original licenses and notices.

| Area | Selected direction | Primary reference / validation needed |
| --- | --- | --- |
| Application/service | TypeScript, Vite, Node.js | Choose supported versions and commit a lockfile when scaffolding exists. |
| Persistence | SQLite and local artifacts | Select a maintained binding and verify license/platform support. |
| Isolation | Rootless Podman and OCI images | https://podman.io/ ; validate the actual host/VM boundary. |
| Assertions | Playwright Test | https://playwright.dev/docs/trace-viewer ; pin browser/test versions and preserve assertions. |
| Evidence envelope | in-toto Statement v1 | https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md ; define and version our own predicate. |
| Recognition | Moonshine Voice English Small Streaming | https://moonshine-voice.readthedocs.io/en/latest/models/available-models/ ; exact English model is the selected MIT-licensed candidate. Do not generalize its terms to other checkpoints. |
| Synthesis | `gradium/phonon-31m-en` through `phonon-tts` | https://huggingface.co/gradium/phonon-31m-en ; selected Apache-2.0 English checkpoint. The 40m family has different non-commercial terms. |
| Browser synthesis | Phonon WASM runtime | https://github.com/gradium-ai/xn-ptts/blob/main/ptts-wasm/js/README.md ; verify browser workers, interruption, cache, and threading requirements. |
| Voice assets | One stock voice | https://huggingface.co/gradium/phonon-voices ; retain asset notice and validate pronunciation. |
| TTS contingency | Kokoro 82M | https://huggingface.co/hexgrad/Kokoro-82M ; audition only if primary synthesis fails. |
| Hosted ASR contingency | Cloudflare Workers AI | https://developers.cloudflare.com/workers-ai/platform/pricing/ ; verify current pricing and data handling when enabling. |

Do not bundle model weights in git. Document acquisition, hashes, expected download size, memory needs, and processing location after measurement. Model weights size is not total runtime memory or total download size.

## Cost policy

- Prefer a default with existing Tenable access, one reasoning provider credential, local containers, and local speech.
- No dependency on temporary promotional credits for ongoing usability.
- Account for local hardware and optional hosted services honestly.
- Record model usage, retries, and pricing date; distinguish estimated application budgets from invoiced costs.
- Keep optional providers out of the required setup path.

## License inventory at implementation

For each reused module, package, model, image, and voice asset, record source URL, exact version/digest, license, required attribution, redistribution terms, and purpose. The repository's Apache-2.0 license covers original contributions only. Do not relicense third-party content by omission.
