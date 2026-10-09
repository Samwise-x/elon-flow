---
name: architecture
description: Adjudicate ownership, domain boundaries and irreversible design decisions using actual repository evidence.
---

# Architecture

Read the code and domain vocabulary first. Prefer clear ownership and locality. For a proposed seam, ask whether it reduces future change cost or improves testability and locality. If yes, retain the seam; otherwise prefer simplicity. Document irreversible decisions in an ADR. Do not impose patterns unsupported by the artifact.
