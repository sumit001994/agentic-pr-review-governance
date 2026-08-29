# Agentic PR Review & CI/CD Governance — Validate-Before-Trust AI Architecture

**© 2026 Sumit Saurabh. All rights reserved.**
This repository is provided publicly for portfolio and demonstration purposes only.
No permission is granted to copy, reuse, modify, or redistribute any part of it. See
[LICENSE](./LICENSE).

---

Every pull request tells an AI agent to look closer — but never to act alone.
That's the whole idea behind this project: a real, tool-calling agent reviews code
changes inside a live CI/CD pipeline, investigating before it ever forms an
opinion, and never getting the final word.

Before it sees a single line of a diff, a plain-text filter blacks out anything
that looks like a secret — deliberately not AI, because a filter that needs an LLM
to judge sensitivity would have to expose the secret first. A quick, deterministic
score then tells the agent how carefully to look. From there, it reasons for
itself: pulling more file context, checking a real vulnerability database, running
an actual test, tracing related code — never guessing when it can check instead.

Even its own suggestions don't get trusted blindly. A separate, independent
process re-verifies every claimed fix against the real diff before anything is
ever posted as a one-click suggestion. If the AI is unavailable for any reason, a
fully deterministic fallback takes over — there's always a review, never silence.

The same discipline carries into deployment: a real Kubernetes cluster scales
itself under genuine load, proven end-to-end, not just described. And the one time
someone proposed giving the agent more autonomy — letting it fix things itself —
that idea was turned down before a line of code was written, because the rule
holds even under pressure: propose, never act.

## Repository layout

- [`architecture_skeleton/`](./architecture_skeleton) — real structure and
  signatures, no implementation.
- [`snippets/`](./snippets) — one small, real, simplified example of a single safe
  design idea.
