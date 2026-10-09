# Routing and ownership

## Exclusive ownership

| Area | Owner |
| --- | --- |
| Purpose, first principles, requirement challenge, deletion, governing constraint, acceleration, automation order | `first-principles` under the Elon-Flow doctrine |
| Observable uncertainty, measurement, disconfirmation, evidence confidence, completion proof | `experiment` |
| Domain vocabulary, module depth, interface and seam placement, architectural locality | `architecture` |
| Minimum complete implementation | `implement` |
| Reproduction, minimization, falsifiable diagnosis, root-cause correction | `debug` |
| Deterministic leverage, recurring-failure enforcement, reusable execution machinery | `compound` |

## Combination rules

Use more than one leaf only when the second leaf answers a different question.

Examples:

- Requirement may be unnecessary, then its surviving implementation is uncertain → `first-principles` then `implement`.
- Two architectural shapes are plausible and observable behavior can discriminate → `architecture` plus `experiment`.
- Bug reproduction identifies a recurring process flaw → `debug` then `compound`.
- Performance work needs a baseline and a code change → `experiment` defines the measurement; `implement` makes the smallest justified change; `experiment` verifies it.

## Escalation rules

- Two or more failed fixes sharing one premise → challenge the premise before another fix.
- Repeated manual procedure with stable steps → consider a deterministic lever.
- Repeated human correction → encode the lesson at the highest practical enforcement layer.
- Repeated architectural exceptions, casts, special cases, or locks → reconsider the chosen structure.
- Repeated coordination around one shared resource → try to separate ownership before adding synchronization.

## Non-routes

Do not invoke a leaf merely because its vocabulary appears in conversation. Route by the decision that must be made next.
