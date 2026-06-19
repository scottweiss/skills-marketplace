---
name: disciplined-implementation
description: Use for substantial code changes or risky investigations. A portable, risk-calibrated delivery method — read repository instructions, map impact, ground plans in real signatures, establish a baseline, define proof before implementation, prefer RED→GREEN for behavior changes, run repository-prescribed verification, exercise the real artifact, review the diff independently, publish only when authorized, and report exact evidence and residual risk. Language- and tool-neutral.
---

# Disciplined Implementation

A portable method for reliable engineering changes. **Rigor scales with risk; evidence does not disappear.**

## Operating contract

- This skill supplements the task and repository instructions; it does not replace them. Surface material conflicts instead of silently choosing.
- Protect existing work: inspect status and diffs before editing, and never overwrite unrelated changes.
- Prefer the repository's established commands, patterns, generators, and dependency tooling over invented substitutes.
- Never expose secrets, credentials, private data, or sensitive production output in logs, screenshots, fixtures, or reports.
- An investigation may correctly end with evidence and a recommendation rather than a code change.
- When a step is impossible or inapplicable, state why, use the strongest feasible substitute, and report the residual risk.

## Core loop

Scope → orient → establish a baseline → define proof → observe failure when applicable → implement the smallest slice → run targeted checks → run the full gate → exercise the real artifact → review independently → publish and report.

## 1 — Calibrate rigor and scope

- Define the acceptance criteria, affected surfaces, explicit non-goals, and required evidence before editing.
- Scale ceremony to risk, not to line count:

| Risk | Typical indicators | Expected evidence |
|---|---|---|
| Low | Documentation, metadata, or a local mechanical change with no runtime behavior | Focused validation, diff review, and any cheap repository-prescribed checks |
| Medium | Contained behavior change, bug fix, or refactor | RED→GREEN when feasible, targeted checks, full gate, and real-artifact verification |
| High | Public contract, schema/data migration, security, permissions, concurrency, broad refactor, or irreversible effect | Baseline, branch/error coverage, phase gates, migration and rollback reasoning, real-artifact verification, and independent review |

- Decompose multi-part work into named slices that each produce a reviewable, testable increment. Detail later slices only after earlier assumptions are confirmed.
- Keep task tracking and a decision log for multi-phase or high-risk work. For small work, the final evidence report is sufficient.

## 2 — Orient before touching code

- Read the task, repository instructions, relevant design documents, and the prescribed build/test commands first.
- Enumerate relevant symbols, files, call sites, and existing patterns before reading deeply. Then read enough surrounding context to understand behavior; whole-file reading is appropriate when structure or invariants require it.
- Trace each relevant chain to its source: caller → implementation → interface/type → schema or data. Verify contracts on both sides of every boundary.
- Inspect actual signatures, data shapes, fixtures, feature flags, configuration, and generated-file markers. Use the generator rather than manually editing generated output.
- Check the working tree for user changes and identify files that are out of scope.

## 3 — Ground the plan and establish a baseline

- Reproduce the defect, capture current behavior, or run the narrowest relevant check before changing code whenever practical.
- Ground the plan in real signatures, types, schemas, and integration points; do not plan from remembered APIs.
- For expensive or externally visible interfaces, validate a cheap prototype first: a function signature, sample payload, migration sketch, or UI wireframe.
- Record material assumptions and unknowns. Do not present unread code or unavailable environments as verified facts.

## 4 — Define proof, then implement the smallest slice

- For behavior changes and bug fixes, prefer test-first: write the expectation, run it, confirm it fails for the intended reason, implement the minimum change, confirm it passes, then refactor.
- When an automated failing test is not suitable—such as documentation, mechanical metadata, exploratory work, an inaccessible external dependency, or an untestable legacy seam—define the strongest alternative proof before editing and report the exception.
- Pin success, error, empty, boundary, loading, degraded, permission, and retry paths in proportion to risk.
- Match fixtures to observed production shapes or authoritative schemas, not invented approximations.
- Search for existing behavior before adding a pattern. Share an abstraction only when semantics, ownership, and lifecycle align; similar syntax alone is not a reason to extract.
- Keep each change focused. Separate unrelated cleanup and avoid speculative compatibility code.

## 5 — Use a verification ladder

- Run fast, targeted checks after each slice.
- Run the repository-prescribed full gate before final handoff and at completed phase boundaries. Before intermediate commits, run at least the affected checks; follow stricter repository rules when they exist.
- The full gate is whatever the project defines—tests, type-checking, lint, build, generation checks, formatting, integration tests—not a generic checklist imposed on every repository.
- Report the exact command, result, and available counts. Never replace evidence with “looks good” or “green.”
- Diagnose failures to root cause. Before calling a failure pre-existing, reproduce it on the clean base revision or cite independent baseline evidence.
- If the working tree changes while a check is running, rerun the affected check against the final state.
- Treat contract changes as coordinated migrations: update definitions, consumers, tests, and rollout/compatibility behavior together. Use a compatibility layer only when the rollout requires it, with an explicit removal plan.

## 6 — Verify the real artifact

- Exercise the actual output before declaring completion: run the service or CLI, render and inspect the UI, open the generated file, or query the real test datastore.
- For UI work, check intended states, interaction, accessibility, and relevant viewport behavior against the design.
- For data or migration work, verify shape, cardinality, idempotency, failure behavior, and rollback or recovery.
- Use a safe environment for external or destructive effects. Clearly identify anything that could not be exercised and why.

## 7 — Review independently, then publish

- Inspect status and read the final diff line by line. Check for debug code, accidental files, generated drift, unrelated edits, and whitespace errors.
- Use a separate read-only reviewer or a clean-context review when available. Otherwise perform a deliberate adversarial pass against the acceptance criteria and highest-risk inputs.
- Track findings with severity and disposition; unresolved material findings block completion.
- Commit one logical concern at a time. Stage explicit paths or patches rather than broad adds, and preserve unrelated user changes.
- Publish only when authorized. A request to create a pull request authorizes pushing a dedicated branch; it does not authorize unrelated changes or merging.
- After publishing, verify that the remote commit and pull-request diff contain exactly the intended files.

## Evidence report

Use an auditable final report:

```text
Outcome:
Scope:
Evidence:
- <command or inspection>: <result and count, when available>
Artifact verification:
Review:
Deviations / residual risk:
Commit / pull request:
```

Do not invent counts. Use exact numbers when the tool exposes them, and name checks that were skipped, blocked, or unavailable.

## Red flags / stop

| About to… | Instead… |
|---|---|
| Edit before reading task and repository instructions | Orient and inspect the working tree first |
| Claim TDD without observing the test fail | Run the failing test, or document why another proof is stronger |
| Call a failure “pre-existing” from memory | Reproduce it on the clean base revision |
| Skip the full gate without explanation | Run it, or report the constraint and residual risk |
| Extract merely because two snippets look alike | Confirm shared semantics, ownership, and lifecycle |
| Edit generated output by hand | Find and run the authoritative generator |
| Stage the entire tree | Stage explicit paths or patches and inspect the staged diff |
| Declare completion from tests alone | Exercise the real artifact and inspect its output |
| Publish without authorization | Keep changes local; a pull-request request is explicit authorization |
| Put secrets or private data in evidence | Redact or replace with safe fixtures |
