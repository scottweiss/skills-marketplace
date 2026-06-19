---
name: disciplined-implementation
description: Use for any substantial coding task — implementing a feature, fixing a bug, refactoring, or investigating a codebase. An intentionally strict, project- and harness-agnostic delivery method — orient before coding, ground plans in real signatures, work test-first (RED→GREEN), run the complete verification gate before every commit, verify the real running artifact, review with independent eyes, commit small explicit increments, and report auditable evidence. Waivers are allowed only for steps that are impossible or genuinely inapplicable. Language- and tool-neutral.
---

# Disciplined Implementation

An intentionally strict engineering method distilled from observed Fable 5 behavior. It assumes nothing about language, framework, repository layout, or agent harness. Its core convictions are: **never trust a test you have not watched fail, never ship output you have not seen run, never duplicate a concept you could correctly share, and always leave an auditable trail.**

## Operating contract

- Once this skill is invoked for an in-scope task, its required steps are mandatory. Do not silently scale them down because the task appears easy, the gate is slow, or the deadline is inconvenient.
- Task and repository instructions take precedence. Read them first and surface material conflicts instead of silently choosing.
- Protect existing work: inspect status and diffs before editing, identify out-of-scope files, and never overwrite unrelated changes.
- Prefer the repository's established commands, patterns, generators, and dependency tooling over invented substitutes.
- Never expose secrets, credentials, private data, or sensitive production output in logs, screenshots, fixtures, or reports.
- An investigation may correctly end with evidence and a recommendation rather than a code change.
- A required step may be skipped only through the waiver protocol below.

## Core loop

Orient → ground the plan in real signatures → establish the baseline → write and run a failing test → make it pass → run the complete gate before every commit → verify the real artifact → review with independent eyes → commit one concern with explicit paths → report exactly what landed and why.

## 1 — Confirm scope and acceptance criteria

- Use this skill for substantial feature work, bug fixes, refactors, contract changes, migrations, or investigations where correctness and reconstructable evidence matter.
- Trivial prose-only or mechanical metadata work may explicitly opt out before implementation. Do not claim this skill was applied partially.
- Define acceptance criteria, affected surfaces, explicit non-goals, and required evidence before editing.
- Decompose multi-part work into named, numbered phases that each produce a testable increment. Detail a later phase only after earlier assumptions have been verified in real code.
- Track work as discrete items and keep a living decision/audit log for findings, decisions, waivers, and proof references.

## 2 — Orient before touching code

- Read the task, handoff, specification, repository instructions, design documents, and prescribed build/test commands first.
- Enumerate relevant symbols, files, call sites, and existing patterns before reading deeply. Then read enough surrounding context to understand invariants; read whole files when structure requires it.
- Trace every relevant chain to its atomic source: caller → implementation → interface/type → schema or data. Verify contracts on both sides of every boundary.
- Inspect actual signatures, data shapes, fixtures, feature flags, configuration, and generated-file markers. Use the authoritative generator rather than editing generated output by hand.
- Inspect the working tree and staged diff before the first edit.

## 3 — Ground the plan and baseline in reality

- Reproduce the defect, capture current behavior, or run the narrowest relevant check before changing code.
- Gather the real signatures, types, schemas, and integration points. Do not plan from remembered APIs.
- For expensive or externally visible interfaces, validate a cheap prototype first: a signature, sample payload, migration sketch, or UI wireframe.
- Record material assumptions and unknowns. “Code I did not read” is not “code that does not exist.”
- For multi-system work, finish the current phase and update the plan from landed code before detailing the next phase.

## 4 — Implement test-first

- **Follow TDD literally for behavior changes:** write one failing test, run it, confirm it fails for the intended reason, write the minimum implementation to pass, confirm green, then refactor.
- Write and lock test expectations before the implementation edit. For multi-branch behavior, pin success, error, empty, boundary, loading, degraded, permission, and retry paths as applicable before restructuring code.
- Match fixtures to observed production shapes or authoritative schemas, not invented approximations.
- A test that was never observed failing is not accepted as proof of the behavior it claims to protect.
- When a failing automated test is genuinely impossible or inapplicable, invoke the waiver protocol before implementation and define the strongest available substitute proof.

## 5 — Implement the smallest correct shared unit

- Search for the concept and pattern before adding code.
- Do not create a second implementation of the same responsibility. When semantics, ownership, and lifecycle align, extract the shared unit and migrate existing consumers before proceeding.
- Similar syntax alone is not a reason to abstract. When implementations must remain separate, record the semantic or ownership distinction.
- Keep modules small and single-responsibility. Put stable decision tables in named constants rather than burying them in branching code.
- Scope each change to one concern. Defer “while I am here” cleanup to a separate task and commit.
- Treat contract and schema changes as coordinated migrations: update definitions, consumers, tests, and rollout behavior together. Add a compatibility layer only when an explicit rollout requires it, with an owner and removal condition.

## 6 — Run the complete gate before every commit

- Use targeted checks during the RED→GREEN loop for speed.
- **Before every commit, run the repository's complete prescribed verification gate against the final tree:** type-check or compile, lint with zero errors, formatting or generation checks, build, and the complete relevant test suite.
- The repository defines the exact gate. Discover and run it; do not replace it with a generic subset.
- Report the exact commands, results, and available counts, such as “214 tests passed.” Never substitute “green,” “looks good,” or “should pass” for evidence.
- Diagnose every failure to root cause. Before labeling a failure pre-existing, reproduce it on the clean base revision or cite equivalent independent baseline evidence.
- If the working tree changes while a check runs, rerun the affected check against the final state.
- A failed or unavailable full gate blocks the commit unless an explicit waiver is approved and recorded.

## 7 — Verify the real artifact

- Tests and types prove an abstraction; they do not prove the running output. Exercise the actual artifact before declaring completion: run the service or CLI, render and inspect the UI, open the produced file, or query the real test datastore.
- For UI work, inspect intended states, interaction, accessibility, and relevant viewport behavior against the design; capture concrete deltas.
- For data or migration work, verify shape, cardinality, idempotency, failure behavior, and rollback or recovery.
- Use a safe environment for external or destructive effects. Inability to exercise the artifact requires a waiver and remains residual risk.

## 8 — Review with independent eyes, then publish

- Inspect status and read the final diff line by line. Check for debug code, accidental files, generated drift, unrelated edits, placeholders, sensitive data, and whitespace errors.
- When the harness supports it, dispatch a separate read-only reviewer. Otherwise review from a clean context with a deliberately adversarial mindset.
- Use explicit review verdicts: `APPROVED` or `CHANGES_REQUIRED`, with every finding tracked to disposition. Unresolved material findings block completion.
- Commit one logical concern at a time. Stage explicit paths or patches—never `git add -A`, `git add .`, or broad subtree adds—and inspect the staged diff.
- Write commit messages that explain why the change exists.
- Do not push unless asked. A request to create a pull request authorizes pushing its dedicated branch, not merging or publishing unrelated changes.
- After publishing, verify that the remote commit and pull-request diff contain exactly the intended files.

## 9 — Communicate and preserve the audit trail

- Report exact state after each material step: counts, gate status, commit hash, blocker, and next action—numbers, not adjectives.
- Surface blockers immediately, named by type and by who must resolve them. Do not silently work around decisions, credentials, permissions, or scope questions.
- When the reviewer or operator disagrees, reframe rather than defend: acknowledge the point, sharpen it into a constraint, and propose grounded alternatives.
- Keep findings with IDs, severity, status, and proof references; keep decisions with rationale; keep waivers with authorization and residual risk.
- Flag uncertainty explicitly and distinguish verified facts from inference.

## Waiver protocol

A waiver is an exception record, not a convenience switch.

- Waive a required step only when it is impossible or genuinely inapplicable—not because it is slow, expensive, inconvenient, or likely to pass.
- Declare the waiver before skipping the step whenever possible.
- Record: the required rule, why it cannot apply, evidence for that claim, substitute verification, residual risk, and the approving operator.
- If the waiver undermines an acceptance criterion or production confidence, stop and request a decision rather than declaring completion.
- Include every waiver in the final evidence report. No silent waivers.

## Evidence report

Use an auditable final report:

```text
Outcome:
Scope / non-goals:
Baseline:
RED→GREEN evidence:
Complete gate before each commit:
- <commit or planned commit>: <commands, results, and counts>
Artifact verification:
Independent review verdict:
Waivers:
Residual risk:
Commit / pull request:
```

Do not invent counts. Name every check that was skipped, blocked, unavailable, or waived.

## Limitations

- This method cannot discover a repository's real contracts or verification gate without access to its code, configuration, and instructions.
- Some environments cannot provide services, credentials, devices, production-like data, or destructive test targets; these constraints require explicit waivers rather than simulated certainty.
- A clean-context self-review is weaker than genuinely independent review.
- Strict process reduces avoidable implementation risk; it does not replace security, legal, operational, accessibility, or other domain-specific expertise.

## Red flags / stop

| About to… | Instead… |
|---|---|
| Start coding before reading task and repository instructions | Orient and inspect the working tree first |
| Write behavior code before observing a failing test | Run the failing test, or record an approved waiver first |
| Commit after targeted checks only | Run the complete prescribed gate and cite exact results |
| Call a failure “pre-existing” from memory | Reproduce it on the clean base revision |
| Duplicate an existing responsibility | Search first; share it when semantics, ownership, and lifecycle align |
| Abstract two coincidentally similar snippets | Record the distinction and keep them separate |
| Edit generated output by hand | Find and run the authoritative generator |
| Stage the entire tree | Stage explicit paths or patches and inspect the staged diff |
| Declare completion from tests alone | Exercise the real artifact and inspect its output |
| Skip a rule because it is inconvenient | Follow it or record an approved waiver |
| Push because the work is done | Push only when asked |
| Put secrets or private data in evidence | Redact or replace them with safe fixtures |
