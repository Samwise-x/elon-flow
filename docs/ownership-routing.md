# Elon-Flow: Canonical Ownership and Routing Contract

Status: initial design contract. This document defines responsibilities and routing; it does not claim the plugin is implemented, installed, or verified.

## Objective

Elon-Flow applies an engineering operating doctrine to improve both an outcome and the mechanism that repeatedly produces it. Optimize for demonstrated system-level value, not activity, local metrics, agent count, or code volume.

## Governing doctrine

The Musk operating philosophy supplied for this project is the authoritative decision framework:

1. **Purpose:** name the highest-value outcome and its measurable system-level objective.
2. **Truth:** distinguish empirical constraints from convention, assumptions, and interpretations.
3. **Question requirements:** challenge each requirement and identify its accountable source where applicable.
4. **Delete:** attempt to eliminate requirements, parts, steps, handoffs, and dependencies.
5. **Simplify and optimize:** improve only what survives deletion.
6. **Find the governing constraint:** identify what currently limits the whole-system objective.
7. **Build, test, learn:** run the smallest discriminating experiment, seek disconfirmation, and update from evidence.
8. **Accelerate:** shorten validated feedback cycles without weakening quality or safety.
9. **Automate:** mechanize a necessary, understood, proven process, never inherited waste.
10. **Improve the production system:** recursively apply this sequence to the mechanism that produces the output.

The five-step engineering algorithm retains its strict internal order: question requirements → delete → simplify/optimize → accelerate → automate. Identifying constraints and conducting experiments supply evidence for that sequence, not a license to skip it.

## Exclusive ownership

| Owner | Responsibility | Explicitly does not own |
| --- | --- | --- |
| Elon-Flow doctrine | Purpose, first principles, requirements, deletion, whole-system constraint, economics, sequencing, acceleration, automation, recursive production-system improvement | Detailed code style, debugging procedure, test-framework preferences |
| pstack-derived mechanisms | Evidence confidence, experiments, measurement integrity, real-artifact verification, reversible autonomy, premise attacks, deterministic levers, structural learning, bounded coordination | Governing philosophy, mandatory fan-out, provider routing |
| Ponytail-derived mechanisms | Minimum complete implementation after necessity has been established: existing code → standard library → native platform → installed dependency → smallest clear implementation | Reopening requirements by default, architectural authority, independent verification policy |
| Matt Pocock-derived mechanisms | Domain vocabulary, deep modules and seams, locality, architecture tradeoffs, reproducible debugging, behavioral test design, progressive disclosure, tracer-bullet decomposition | Governing objective, universal requirement for tickets, human interviews, or architectural ceremony |

These are **sources of extracted mechanisms**, not required runtime dependencies. Elon-Flow must be self-contained and must not import another plugin merely to function.

## Proposed skills and routing

The controller chooses the smallest applicable leaf or combination of leaves. Skills are conditional, not mandatory sequential stages.

| Skill | Activate when | Owns | Completion / exit |
| --- | --- | --- | --- |
| `elon-flow` | User invokes the operating mode or requests a multi-stage engineering outcome | Route, preserve doctrine and ownership, select evidence threshold, coordinate handoffs | Work has a clear next action or verified result, with no redundant skill invocation |
| `first-principles` | Goal, requirements, necessity, economics, or system constraint are unclear or contested | Decomposition, requirement challenge, deletion, governing constraint | Necessity and constraint are evidenced, or the unresolved decision is precisely identified |
| `experiment` | An observable question, optimization claim, competing hypothesis, or completion claim needs proof | Falsifiable prediction, real observation, one-change measurement, keep/revert, evidence confidence | Recorded result supports or rejects the claim; no unverified improvement is promoted |
| `architecture` | Domain terms, module boundaries, interfaces, or structural tradeoffs materially affect the work | Domain glossary, deep-module design, locality, seam selection, ADR threshold | Minimum justified structure and test surface are clear |
| `implement` | Required behavior and relevant design constraints are sufficiently known | Ponytail ladder and smallest complete code change | Behavior is implemented and passed to the appropriate verification surface |
| `debug` | Observed behavior violates expectation or a regression is suspected | Red-capable reproduction, minimization, ranked falsifiable hypotheses, root cause, original-repro rerun | Original failure is demonstrably resolved, or a concrete blocker is recorded |
| `compound` | A validated manual process repeats, a failure recurs, or coordination/context cost dominates | Deterministic lever, structural enforcement, idempotence, reusable evidence trail, production-loop improvement | Repeated work is measurably cheaper or safer and the lever is itself verified |

Routing precedence is **necessity → evidence → architecture when needed → minimal implementation → real verification → compounding when earned**. This is a decision order, not an instruction to invoke every skill. A bug can route directly to `debug`; a measurable uncertainty directly to `experiment`; a small known change directly to `implement`.

## Invariants

- **Reality over assertion:** distinguish direct, supported, inferred, speculative, and unknown claims. Source code showing current behavior does not establish historical author intent.
- **No empirical questions to humans:** investigate observable facts with tools or experiments; ask humans for genuine preference, authorization, or irreducible product decisions.
- **No premature automation:** a deterministic lever must implement an understood, necessary, validated process.
- **No false completion:** tests, compilation, or agent reports do not substitute for verification at the real failure/output surface.
- **No speculative structure:** create a module, abstraction, dependency, agent, workflow, or document only when it reduces demonstrated change cost, risk, or coordination.
- **No mandatory fan-out:** use independent review or parallel workers only when expected information gain justifies their cost; prefer a deterministic method when it suffices.
- **No unauthorized irreversible action:** continue reversible work autonomously; preserve required approvals for destructive, financial, security-sensitive, or external side effects.
- **No repeated textual correction:** when a failure recurs, prefer the highest practical enforceable boundary (architecture, types, static/runtime check, behavior test), and verify against the historical failure.
- **No duplicated authority:** one canonical rule owner; other skills refer to that owner rather than restating competing policy.
- **No infinite ceremony:** every invoked procedure needs a concrete question, exit condition, and stop condition. If the requested outcome is already satisfied, stop.

## Triggered escalation

- Two or more unsuccessful fixes sharing one premise → `first-principles` plus `experiment` to challenge the premise.
- An uncertain design with materially different feasible shapes → `architecture`, optionally independent alternatives.
- A bug without a red-capable reproduction → `debug` first establishes the observation loop, not speculative patching.
- A performance claim → `experiment` must validate the limiter, error rate, real work, repeatability, and system-level effect.
- A recurring manual procedure → `compound` builds a rerunnable lever only after validating the procedure.
- A recurring correction → `compound` promotes it into enforceable structure and replays the old failure.
- A change that repeatedly fights its chosen interfaces → reconsider the architecture rather than accumulating exceptions.

## Documentation and state

Keep the controller short. Conditional procedure details belong in leaf `SKILL.md` files and referenced documents. Do not copy discoverable repository facts into prompts. Use `CONTEXT.md` only for domain vocabulary when the target repository needs it. Record ADRs only for decisions that are difficult to reverse, non-obvious without context, and involve a real tradeoff. Long-running work leaves concise evidence pointers and an auditable current state rather than transcript dumps.

## Exclusions for the first release

No pstack `poteto-mode` clone, model/provider routing, mandatory Arena/Swarm, ten-lane verification plan, obligatory performance gate, automatic PR machinery, or standalone MCP server. No duplicate Ponytail router. No forced Matt grilling, tickets, HTML reports, or interactive approval for reversible execution.

## Acceptance criteria for the next artifact

The skill package must implement these ownership boundaries without contradictory triggers. Every leaf must define activation, permitted actions, evidence threshold, stop condition, and handoff. The controller must avoid loading all leaf content by default. The first release must pass manifest/frontmatter validation and scenario-based routing tests, including a no-op case, an observable uncertainty, a bug, a small implementation, a contested architecture, and a repeated correction.

## Source lineage

Conceptual sources: the user-supplied Musk operating philosophy; `backnotprop/pstack` skills and playbooks; installed Ponytail skills; installed Matt Pocock skills. Extracted ideas are rewritten as an independent operating contract, not copied wholesale. Verify upstream licenses and attribution before distributing source-derived material.
