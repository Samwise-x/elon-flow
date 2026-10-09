---
name: debug
description: Use when software is broken, failing, regressed, flaky, or unexpectedly slow and the task requires a reproducible root-cause diagnosis before fixing it.
---

# Debug

Build a feedback loop before building a theory.

## Activate

Use for defects, regressions, flaky behavior, unexplained failures, and performance bugs.

## Process

### 1. Build a red-capable loop

Create the smallest unattended command or procedure that can observe the user's actual failure.

Useful forms include a focused behavior test, HTTP or CLI repro script, browser automation, captured-request replay, throwaway harness, differential old-versus-new run, seeded stress loop, or automated bisection.

The loop must be capable of failing for this bug, not merely capable of running.

### 2. Tighten it

Make the loop specific to the reported symptom, deterministic enough to support diagnosis, fast enough to run repeatedly, and agent-runnable where possible.

For a flaky failure, raise the reproduction rate rather than pretending randomness is evidence.

### 3. Reproduce and minimize

Observe the failure. Then remove inputs, steps, callers, state, and configuration one at a time, rerunning after each removal.

A minimal repro contains only load-bearing elements.

### 4. Rank falsifiable hypotheses

Generate multiple plausible mechanisms before editing.

For each hypothesis, state a prediction that distinguishes it from the others.

Do not patch the first plausible story.

### 5. Instrument only to discriminate

Prefer direct state inspection or debugger probes. Add targeted instrumentation only where it separates hypotheses.

For performance failures, establish a baseline and profiler or measurement path before changing code.

### 6. Confirm the mechanism

Do not edit until runtime evidence identifies the surviving mechanism strongly enough to justify the change.

If two or more attempted fixes fail under one shared premise, hand that premise to `first-principles`.

### 7. Fix minimally

Use `implement` for the smallest root-cause correction.

Add a regression test when a correct behavior seam exists. Do not create a shallow test seam merely to satisfy ceremony.

### 8. Re-run the original loop

The original unminimized scenario must now pass.

A unit test passing is not proof that the user's original failure disappeared.

## Performance branch

When the failure is slowness, use `experiment` for baseline integrity, measurement validation, and before/after proof.

## Evidence threshold

No root-cause claim without a reproducible symptom and an observation that distinguishes the chosen mechanism from serious alternatives.

## Stop

Stop when the original failure is gone and the correction is verified, or when no usable observation loop can be built with the available access. In the latter case, record exactly what evidence is missing.
