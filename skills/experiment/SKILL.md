---
name: experiment
description: Use when an engineering question can be answered by observation, measurement, a prototype, a benchmark, a comparison, or direct verification of the real artifact.
---

# Experiment

Turn an observable uncertainty into the smallest discriminating test.

## Activate

Use for:

- competing technical hypotheses;
- performance or cost claims;
- behavior that can be prototyped;
- claims that a change improved something;
- completion claims requiring real-artifact proof;
- repeated fixes that may share a false premise.

## Process

### 1. State the question

Write one falsifiable question.

If no possible observation could change the decision, this is not an experiment.

### 2. Define the prediction

For each serious hypothesis, state what observation would support it and what would disconfirm it.

Prefer a test that separates multiple hypotheses at once.

### 3. Establish the baseline

Measure the current state first when the task concerns improvement.

Record:

- metric and unit;
- workload or scenario;
- environment;
- success/failure count;
- the system constraint the number is supposed to represent.

### 4. Verify the measurement

Before trusting the number, establish that:

- the intended work actually occurred;
- failures did not masquerade as speed;
- the load generator or harness is not the bottleneck;
- both sides are measured comparably;
- repeated or interleaved runs are stable enough to support the decision.

### 5. Change one meaningful variable

Make or request the smallest change that tests the hypothesis.

Do not pile multiple speculative fixes into one experiment.

### 6. Observe the real surface

Prefer the artifact or behavior the user actually cares about. A proxy is acceptable only when its relationship to the real outcome is established.

### 7. Decide

- Evidence supports the change → keep it.
- Evidence rejects the change → revert or discard it.
- Evidence is inconclusive → change the experiment, not the conclusion.

Record confidence as direct, supported, inferred, speculative, or unknown when necessary.

## Repeated-failure rule

After two or more failed interventions that depend on the same assumption, stop producing variants of the same fix. Hand the common premise to `first-principles`.

## Evidence threshold

A promoted improvement requires a reproducible observation on a relevant surface and an explanation of why the measured number represents the claimed work.

## Stop

Stop when the observation materially resolves the decision.

Do not continue measuring once additional samples would not change the action.
