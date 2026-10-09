---
name: implement
description: Use when required behavior is sufficiently known and the task is to implement the smallest correct change without speculative abstraction or dependency growth.
---

# Implement

Build only what survived requirement challenge.

## Activate

Use when the desired behavior is known well enough that the remaining problem is implementation.

## The ladder

Trace the affected flow first. Then stop at the first rung that fully solves the requirement:

1. Reuse something already present in the codebase.
2. Use the language or standard library.
3. Use a native platform capability.
4. Use an already-installed dependency.
5. Collapse the solution to the smallest clear expression.
6. Only then write the minimum new code.

The ladder shortens implementation, not understanding.

## Rules

- No interface with one hypothetical implementation unless architecture established a real seam.
- No factory for one product.
- No configuration for values that do not vary.
- No compatibility path without an actual consumer or migration need.
- No new dependency for functionality already available cheaply in the project, standard library, or platform.
- Prefer deletion to addition.
- Prefer boring, explicit code to clever compression.
- Minimize files and moving parts only after locating the correct responsibility.
- Do not weaken security, trust-boundary validation, data-loss prevention, accessibility, or explicit user requirements to save code.

## Intentional ceilings

A deliberately simple solution may keep a known ceiling when the ceiling is not currently the governing constraint.

When useful, record:

- the ceiling;
- the observable trigger that would justify upgrading;
- the likely upgrade path.

Do not create vague future-improvement debt with no trigger.

## Verification handoff

Implementation is not completion.

- Behavior claim or measurable outcome → `experiment`.
- Bug fix → return to the original `debug` reproduction.
- Repeated procedure now stable enough to mechanize → `compound`.

## Evidence threshold

The implementation must satisfy the known requirement with no speculative machinery beyond what current evidence requires.

## Stop

Stop when the minimum complete implementation exists and the relevant verification path is ready to run.
