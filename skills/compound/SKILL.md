---
name: compound
description: Use when validated work repeats, the same correction recurs, coordination cost dominates, or a manual process is ready to become deterministic and cheaper to execute.
---

# Compound

Improve the mechanism that produces the work.

## Activate

Use when the same manual sequence repeats, multiple actors repeatedly coordinate around the same operation, the same mistake recurs, a proven workflow is expensive to rediscover, a long-running process lacks durable state, or a deterministic check could replace repeated interpretation.

Do not activate merely because automation is possible.

## Process

### 1. Prove the process deserves to exist

Confirm that the underlying requirement survived deletion and that the process has already worked manually or experimentally.

If the process is still changing rapidly, keep learning before automating.

### 2. Identify the repeated cost

Name the dominant tax: repeated discovery, hand editing, human coordination, shared-state contention, context reload, inconsistent verification, or a recurring error class.

### 3. Build the smallest lever

Prefer the lightest deterministic mechanism that removes the tax: script, query, codemod, generator, state machine, validator, static rule, runtime guard, reproducible harness, or durable evidence state.

A deterministic mechanism that can do the work reliably outranks repeated agent fan-out.

### 4. Encode recurring corrections structurally

For repeated failures, choose the highest practical enforcement layer:

1. architecture or ownership;
2. type or schema constraint;
3. static or runtime check;
4. behavioral test;
5. prose only when the failure cannot be encoded elsewhere.

Replay at least one historical failure against the new enforcement when possible.

### 5. Remove coordination before adding coordination

When the cost comes from multiple writers or actors, first try to split ownership or mutable state. Add locks, queues, polling, or orchestration only when shared coordination is a real invariant.

### 6. Make retries converge

Automated operations should be idempotent or explicitly reconciled so crashes and retries do not create divergent truth.

### 7. Measure the leverage

Use `experiment` when claiming the lever improved throughput, cost, reliability, or latency.

Compare the cost of the new mechanism against the repeated work it replaces.

### 8. Recurse

Once the lever is stable, run Elon-Flow on the lever itself.

Delete unnecessary steps, simplify it, find its new constraint, and improve the production system again.

## Evidence threshold

Automation requires a validated manual or experimental process plus a measurable recurring cost worth removing.

## Stop

Stop when the recurring work is demonstrably cheaper, safer, faster, or more reproducible and the lever itself has a verification path.
