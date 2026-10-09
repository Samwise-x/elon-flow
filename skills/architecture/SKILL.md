---
name: architecture
description: Use when domain vocabulary, module shape, interface design, seam placement, ownership, or testability materially affects an engineering decision.
---

# Architecture

Create the minimum structure that concentrates complexity instead of spreading it.

## Activate

Use when:

- a change crosses an important module or interface boundary;
- the same domain concept is named inconsistently;
- callers must know too much internal detail;
- state ownership is split;
- testing requires reaching through internals;
- an abstraction is proposed before real variation exists;
- implementation repeatedly fights the chosen shape.

## Domain language

Use one canonical term for each domain concept.

If the target repository maintains a `CONTEXT.md`, treat it as a glossary only. Do not turn it into a specification, design document, or implementation cache.

When the code and the stated domain model disagree, surface the contradiction before designing around it.

## Deep-module test

Prefer a small interface that hides substantial policy or behavior.

Apply the deletion test:

- If deleting the module makes complexity disappear, the module may be pass-through.
- If deleting it spreads complexity across many callers, it is likely earning its place.

A seam is justified by real variation, policy, ownership, or test leverage. One hypothetical implementation is not evidence that an interface is needed.

## Ownership

Each mutable fact should have one authoritative writer.

When concurrent actors would write the same state, try to separate state or ownership before adding serialization.

Validate external data at trust boundaries, then work with internal domain types rather than repeatedly revalidating the same representation.

## Test surface

The public interface should also be the natural behavior test surface.

If verification requires reaching deeply into internals, reconsider the module shape before creating more test-only seams.

## Design alternatives

Explore more than one architecture only when materially different shapes could plausibly win. Compare them on:

- system-level outcome;
- interface size;
- locality of change;
- number of owners;
- testability;
- migration cost;
- coordination cost.

Do not fan out alternatives for an obvious local change.

## ADR threshold

Record an architectural decision only when all are true:

1. reversing it later would be meaningfully costly;
2. a future maintainer would reasonably ask why it exists;
3. the decision involved a real tradeoff among viable alternatives.

## Evidence threshold

A new seam, module, abstraction, or shared mechanism must pay for itself through demonstrated locality, leverage, ownership clarity, or required variation.

## Stop

Stop when the minimum justified structure and its public test surface are clear.

Hand implementation to `implement`, or unresolved observable tradeoffs to `experiment`.
