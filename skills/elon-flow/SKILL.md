---
name: elon-flow
description: Use when the user explicitly asks for Elon-Flow, first-principles engineering, or wants a nontrivial engineering problem routed through the Elon-Flow operating doctrine.
---

# Elon-Flow

Elon-Flow improves both the work and the mechanism that repeatedly produces the work.

## Controller contract

Route before acting. Use the smallest applicable leaf skill or combination of leaves. Do not invoke every leaf as a ritual.

The governing order is:

1. **Purpose.** Name the system-level outcome that matters.
2. **Truth.** Separate observable constraints from assumptions, conventions, and guesses.
3. **Question.** Challenge requirements and trace important constraints to an accountable source or observed necessity.
4. **Delete.** Try to remove requirements, parts, handoffs, dependencies, and process steps.
5. **Simplify.** Improve only what survives deletion.
6. **Constrain.** Identify the factor currently limiting the whole-system objective.
7. **Learn.** Run the smallest experiment that can disconfirm the current belief.
8. **Accelerate.** Shorten a validated feedback loop.
9. **Automate.** Mechanize only an understood, necessary, proven process.
10. **Compound.** Improve the system that produces the result, then run the doctrine on that system again.

The five-step engineering algorithm keeps its strict internal order:

**question requirements → delete → simplify/optimize → accelerate → automate**

Never automate inherited waste.

## Routing

Use [references/routing.md](references/routing.md) when more than one leaf appears relevant.

- Unclear necessity, inherited requirement, economic assumption, or governing constraint → `first-principles`.
- Observable uncertainty, competing hypothesis, benchmark, optimization claim, or completion claim → `experiment`.
- Domain vocabulary, module shape, interface, seam, or architectural tradeoff → `architecture`.
- Known required behavior that is ready to build → `implement`.
- Broken, failing, regressed, or unexpectedly slow behavior → `debug`.
- Repeated manual work, repeated correction, repeated coordination cost, or a validated process ready for mechanization → `compound`.

A direct leaf route is valid. A bug does not need a ceremonial first-principles pass before `debug`. A tiny known change can route directly to `implement`.

## Global invariants

- Reality outranks precedent, authority, and agent confidence.
- Observable questions are investigated, not delegated back to the human.
- Reversible work proceeds without unnecessary coordination.
- Irreversible, destructive, financial, security-sensitive, or external side effects keep their required authorization gates.
- Tests, compilation, and agent self-report are not substitutes for verification at the real output surface.
- One rule has one owner. Leaf skills point to owners rather than restating competing doctrine.
- Parallel agents are optional instruments. Prefer a deterministic method when it can answer the question.
- Every invoked procedure needs a concrete question, evidence threshold, and exit condition.
- Stop when the requested outcome is already satisfied.

## Evidence language

Use the confidence labels defined in [references/doctrine.md](references/doctrine.md) when a conclusion depends on incomplete evidence.

## Completion

A run is complete when the requested outcome is verified or when the remaining blocker is precise, evidenced, and outside the available authority or capability.

Do not manufacture extra work after that point.
