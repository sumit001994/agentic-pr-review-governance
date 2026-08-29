# Agentic PR Review & CI/CD Governance — Validate-Before-Trust AI Architecture

**© 2026 Sumit Saurabh. All rights reserved.**
This repository is provided publicly for portfolio and demonstration purposes only.
No permission is granted to copy, reuse, modify, or redistribute any part of it. See
[LICENSE](./LICENSE).

---

An original CI/CD architecture built around one real question: can an AI agent be
trusted to review real code changes in a real pipeline — without ever becoming a
single point of failure, and without ever being the thing that decides what's
"safe enough" to act on?

This is not a demo of "ask an LLM to review a diff." It's a real multi-tool,
reasoning agent wired into a real GitHub Actions pipeline, governed end to end by one
non-negotiable rule: **the AI can propose, investigate, and recommend — it never
gets to act unilaterally, and nothing it claims is trusted until something separate
and deterministic has independently verified it.**

## What it does

- Runs automatically on every pull request: a redaction filter blacks out anything
  that looks like a secret **before** the diff ever reaches the model — deliberately
  plain pattern-matching, not AI, because a guardrail that itself needs an LLM to
  decide what's sensitive would have to expose the secret to make that judgment.
- A deterministic, point-based risk score (low/medium/high) is computed on the
  redacted diff **before** the agent starts reasoning, and is fed back to the agent
  as an instruction: look harder, or a light pass is fine.
- A real **LangGraph tool-calling agent** — not a single prompt — reasons, chooses
  whether to call any of four read-only tools (more file context, a real dependency
  vulnerability check, an actual test run, related-code lookup), observes the real
  result, and loops until confident. None of the four tools can write to the
  repository.
- Any fix the agent proposes is **independently re-verified**: a separate,
  deterministic component re-derives the real added line numbers straight from the
  diff's own hunk headers and only promotes a fix to a real, one-click GitHub
  suggestion if the AI's claimed file and line genuinely match. A wrong guess still
  shows up as plain text — it just doesn't get the one-click treatment.
- If the AI is unavailable for any reason — no key, a network failure, a service
  outage — a separate, fully deterministic local reviewer runs instead. Different
  depth, same guarantee: there is always a real review, never silence.
- On merge to `main`, a completely separate, non-AI pipeline builds a container
  image, scans it for known vulnerabilities, and pushes it to a registry.
  Deployment to the running Kubernetes cluster from there is a deliberate manual
  step, not yet an automated trigger — a real, named gap, worth being upfront about
  rather than implying more automation than actually exists.

## What makes this genuinely agentic, not "an LLM call with a system prompt"

- **`get_file_context`** — reads more of a file when the diff cuts off mid-method.
- **`check_dependency_vulnerabilities`** — checks a real CVE database against a
  specific library version that changed.
- **`run_targeted_test`** — actually runs one relevant test and reports the real
  result, including when nothing was actually verified (see below).
- **`get_related_code_context`** — finds other real files that reference the
  changed class.

The agent chooses which of these to call, observes the real result, and can call
more before forming a final opinion — genuine reason → act → observe → reason again,
not a single round-trip.

## Real gaps found and fixed — not just claimed working on day one

- **A secret-exposure gap**: the diff was always redacted before the AI saw it, but
  one tool's own raw output (reading a real file straight off disk) was only
  redacted afterward, for the human-facing report — meaning a secret in some
  unrelated file the agent inspected would already have reached the AI provider
  unredacted. Fixed by moving redaction to every tool's actual return boundary,
  uniformly across all four tools, not just the one first suspected — backed by a
  regression test with a real fixture secret.
- **A redaction side-effect gap**: the same secret-detection pattern, when it
  matched partway through a camelCase-prefixed variable name, replaced the entire
  match — including half the identifier — leaving syntactically invalid code
  behind. Found live, during interview-prep rehearsal, by actually running the
  system rather than assuming it worked. Fixed with regex capturing groups so only
  the secret value is replaced, never the surrounding variable name or syntax —
  backed by a regression test proving the exact broken case now produces valid code.
- **A silent-false-pass gap**: a tool asked to run a guessed, nonexistent test name
  reported `passed: true` because zero tests technically failing is technically
  true — indistinguishable from a real pass. Fixed to report an explicit "nothing
  was actually verified" result instead. This exact guardrail has since fired live,
  correctly, on unscripted runs.

## A real governance moment — a guardrail held under pressure

A reviewer proposed letting the agent automatically edit files and re-run tests in
a loop to fix what it found, and apply low-risk changes on its own. That was
declined before writing a line of code — not because the idea was badly explained,
but because it broke an already-built, already-tested rule: the agent can flag
problems, it never gets to fix them itself. What was built instead gave the human
better evidence — not the agent more power.

## What was actually proven, not just claimed

- The autoscaler was proven with real generated load: CPU watched crossing a real
  configured threshold, replica count watched rising in real time, confirmed via
  the cluster's own event log — and the scale-down afterward was verified too, not
  just the scale-up half most demos stop at.
- The credential path for the LLM call now tries real Workload Identity Federation
  first (a short-lived, auto-issued credential, proactively refreshed before a
  long multi-tool reasoning turn could ever get caught mid-call), falling back to a
  static key only where there's genuinely no CI identity to federate with — a
  local developer machine.
- A real GitHub Actions run went fully green end to end, including a real review
  comment genuinely posted by the pipeline's own bot on a real pull request.

## Repository layout

- [`architecture_skeleton/`](./architecture_skeleton) — the real module structure,
  class names, type hints, and function signatures. No implementation bodies.
- [`snippets/`](./snippets) — one small, real, standalone, simplified example
  illustrating a single safe design decision from the real system.
