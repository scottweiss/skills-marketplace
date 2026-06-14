---
name: disciplined-implementation
description: Use for any substantial coding task — implementing a feature, fixing a bug, refactoring, or investigating a codebase. A rigorous, project- and harness-agnostic delivery method — orient before coding, ground plans in real signatures, work test-first (RED→GREEN), run the full verification gate before every commit, verify the real running artifact, review with independent eyes, commit small explicit increments, and report auditable state. Language- and tool-neutral.
---

# Disciplined Implementation

A portable engineering method distilled from observing a highly effective coding agent. It assumes nothing about your language, framework, repo layout, or agent harness. The core convictions: **never trust an abstraction you haven't watched fail, never ship output you haven't seen run, never duplicate what you could share, and always leave an auditable trail.**

## Core loop
Orient → ground the plan in real signatures → write a failing test → make it pass → run the full gate and cite the numbers → verify the real artifact → review with independent eyes → commit one concern with explicit paths → report what landed and why.

---

## 1 — Orient before touching code
- Read the task/handoff/spec and any existing design docs first; never start blind.
- **Enumerate before you read in depth.** Search for the symbol or pattern to build a map of call sites, then read only the narrow ranges you need — don't read large files whole.
- **Trace each relevant chain to its atomic source** (caller → implementation → definition → data/schema). At an interface boundary, verify the contract on BOTH sides and flag any divergence.
- Track the work as discrete items in whatever task tool your harness provides; keep their status current.

## 2 — Ground the plan in reality (multi-part work)
- Before planning across multiple subsystems, gather the real signatures, types, and integration points — **don't plan from memory of APIs.** If your harness supports parallel subagents, fan the research out.
- Decompose into named, numbered phases, each shipping something testable on its own. Write a phase's detailed plan only once the previous phase has landed, so it references real code, not guesses.
- Prototype the interface cheaply (a signature, a wireframe, a sample payload) and get agreement before building behind it.

## 3 — Implement test-first
- **Follow TDD literally:** write one failing test, RUN IT and watch it fail for the right reason, then write the minimal code to pass, then confirm green. If you didn't see it fail, you don't know it tests anything.
- Write/lock the test expectations BEFORE the implementation edit. For multi-branch logic (success / error / loading / degraded), pin each branch with a concrete test before refactoring, so regressions can't slip through silently.
- Match test fixtures to real data shapes (inspect the actual schema/response), not invented ones.
- **Extract before you duplicate.** Before implementing a pattern, search whether it already exists elsewhere. If it does, extract it into one shared module/component/constant and migrate both consumers FIRST — then proceed. Do this on first sight, not after a reviewer flags it.
- Keep modules small and single-responsibility; put decision tables in module-level constants, not inline conditionals. Scope each change to one concern; defer "while I'm here" cleanups to their own task.

## 4 — Verify with the full gate
- **Run your project's complete verification gate before EVERY commit** — type-check/compile, lint (zero errors, not just zero *new* errors), build, and the test suite — and cite the numeric results ("214 tests pass"), never just "green".
- During a task, stay fast with targeted test runs; run the full suite at phase boundaries. Long suites can run in the background while you do other work.
- **Diagnose every gate failure to root cause before fixing.** If you suspect a failure is "pre-existing," verify it against the clean/base tree before trusting that claim.
- Treat contract/schema changes as one atomic change: update the definition and every consumer (both sides, plus tests) together — no compatibility shims.

## 5 — Verify the real artifact (not just the abstraction)
- Tests and types prove the abstraction; they don't prove the running thing. **Exercise the ACTUAL output before declaring done:** hit the running service, render the UI and look at it, open the produced file, query the real datastore to confirm shapes and cardinality.
- For UI work, capture the rendered result and compare it to the intended design, listing concrete deltas.

## 6 — Review with independent eyes, then ship
- **Don't review your own work in the same mindset.** If your harness supports subagents, dispatch a separate read-only reviewer against the change; otherwise review from a clean context with a deliberately critical eye.
- Green tests are necessary, not sufficient — **read the diff line by line.** Ask for adversarial inputs against risky redesigns.
- Use explicit review verdicts (APPROVED / CHANGES_REQUIRED + the specific fix), each finding a checklist item.
- **Commit one logical concern per commit, staging explicit file paths** — never `git add -A` / `git add .` / broad subtree adds; they sweep unintended files. Write a message that explains WHY. Don't push unless asked.
- Prefer writing a test against current behavior over stashing changes to compare — stashing risks losing uncommitted work.
- Keep a **living decision/audit log** (findings with IDs + severity + status, decisions with rationale, proof references) and update it as you go, so any future contributor can reconstruct the state.

## Communicate throughout
- Report exact, auditable state after each step: counts, gate status, commit hash, next action — **numbers, not adjectives.**
- Surface blockers immediately, named by type and by who must resolve them (a decision, a credential, a permission, a scope question). Don't silently work around them.
- When the reviewer/operator disagrees, reframe rather than defend: acknowledge the point, sharpen it into a constraint, propose grounded alternatives.
- Flag uncertainty explicitly; "code I didn't read" is not "code that doesn't exist."

## Red flags / stop
| About to… | Instead… |
|---|---|
| Implement a pattern that already exists elsewhere | Search first; extract a shared unit and migrate both, then proceed |
| Commit after only a partial check | Run the full gate, confirm zero lint errors, cite counts |
| `git add -A` / `git add .` / a broad subtree add | Stage explicit file paths |
| Mark work done from green tests alone | Exercise the real running artifact and look at the output |
| Trust your own (or a subagent's) change because tests pass | Read the diff line-by-line; review with independent eyes |
| Write code before a failing test | Write and run the failing test first |
| Plan from memory of an API's shape | Gather the real signatures first |
| Say "pre-existing failure" | Verify against the clean/base tree first |
| Push because it's "done" | Don't — push only when asked |
