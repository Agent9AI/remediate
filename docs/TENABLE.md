# Tenable and Hexa integration plan

## Established prerequisite

The owner confirmed on 2026-10-23 that a Tenable account with Hexa is available for testing. The application adapter has not authenticated, discovered tools, or read a finding yet. Account availability does not establish scanner entitlement, network reachability, scan authorization, or the presence of a rescan MCP tool.

## Day 1 read-only spike

1. Obtain the actual connection and authentication setup through the owner's approved local configuration. Never put credentials in this public repository, issues, screenshots, or chat logs.
2. Authenticate and discover the tools actually advertised by that service.
3. Record relevant tool names and schemas in a sanitized contract snapshot, with their source and retrieval time. Review before trusting descriptions as instructions.
4. Select a permitted tool and retrieve one authorized finding.
5. Normalize source, finding ID, asset identity, component, `observed_at`, `retrieved_at`, severity context, and evidence references.
6. Establish an explicit mapping to a controlled application recipe. Prefer the same deliberately provisioned lab asset where practical.
7. Determine which required security observations are obtainable. Record limitations before choosing the demonstration case.

**Exit evidence:** successful discovery/read records, a normalized finding, a documented lab mapping, and a list of supported versus unavailable verification operations. Store raw sensitive results outside git. Publish only a deliberately sanitized fixture when authorized.

## Time and identity

`observed_at` is when the security observation was made. `retrieved_at` is when Remediate read it. A live retrieval does not refresh the underlying observation.

A sandbox candidate may be separate from the original asset. Show that relationship explicitly. Candidate success does not close or verify the original production finding.

## Verification round trip

A second, authorized Tenable observation for the exact candidate would strengthen the demonstration. First establish permission, scanning capability, reachable lab target, identity continuity, and scan duration. The first release does not require scan-launch or production mutation tools.

If an authorized completed lab scan is available, read it and bind its result to the relevant candidate. If the scan cannot fit the pitch, label it as a previously completed observation. Never present an old or unrelated scan as a fresh candidate result.

If a scanner result is mandatory under the declared verification plan and unavailable, candidate remediation remains pending. Application tests and runtime observations can still be useful evidence with their scope stated.

## Failure behavior

- Expired or missing credentials: actionable connection error without secret disclosure.
- Changed tool contract: re-review the affected grant/adapter contract.
- Rate limits or transient failures: bounded retry, recorded outcome, budget accounting.
- Missing finding or ambiguous asset: no guessed mapping.
- Stale observation: display its age and keep freshness requirements explicit.
- Unavailable live access: retain a labeled import fixture; never mark it as a successful live read.

## What to publish

Publish adapter code, schema contracts, a sanitized example, configuration variable names once implemented, and a reproducible validation procedure. Keep tenant IDs, private hostnames, credentials, customer data, and unredacted findings outside the public repository.
