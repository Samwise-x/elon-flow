---
name: first-principles
description: Use when an engineering goal, requirement, inherited assumption, cost structure, dependency, or governing constraint must be challenged before implementation.
---

# First principles

Determine what should exist before optimizing how to build it.

## Activate

Use this skill when one or more are true:

- the requirement may be inherited rather than necessary;
- a constraint is asserted without evidence;
- a supplier, dependency, process, or architecture is treated as fixed;
- the system-level objective is unclear;
- several fixes have failed under the same assumption;
- work is being optimized before the governing constraint is known.

## Process

### 1. Define the outcome

State the highest-value system outcome and the metric or observable condition that represents it.

Reject local proxies that can improve while the real outcome stays flat or worsens.

### 2. Decompose reality

Separate:

- physical or technical facts;
- economic facts;
- policy or authorization constraints;
- current implementation choices;
- conventions;
- hypotheses.

Mark uncertainty instead of filling it with confidence.

### 3. Challenge requirements

For every material requirement, ask:

- What outcome does this protect?
- What evidence makes it necessary?
- Who or what can defend it?
- What happens if it is removed?

Requirements with no surviving justification become deletion candidates.

### 4. Delete

Attempt to remove whole requirements, steps, handoffs, abstractions, dependencies, or components before improving them.

Deletion is a test, not vandalism. Preserve safety, trust boundaries, explicit user requirements, and real external constraints.

### 5. Find the governing constraint

Identify what presently limits the system-level objective.

Prefer evidence that distinguishes the current bottleneck from merely visible or expensive components.

### 6. Hand off

- Observable uncertainty → `experiment`.
- Structural question → `architecture`.
- Known surviving requirement ready for code → `implement`.

## Evidence threshold

A requirement survives only when supported by an explicit external constraint, observed system behavior, an irreversible product decision, or a demonstrated system-level tradeoff.

## Stop

Stop when necessity, deletion decisions, and the governing constraint are clear enough that the next action no longer depends on inherited assumptions.

Do not continue decomposing once the implementation question is actually known.
