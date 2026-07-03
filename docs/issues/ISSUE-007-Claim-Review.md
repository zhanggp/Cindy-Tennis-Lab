# Issue #007: Review Current Claim Seeds v0.1

## Goal

Review the current claim seeds and decide which claims can become operating
knowledge, which claims need experiments, and which should remain research
directions.

## Why

Cindy Tennis Lab should not let source collection become knowledge by default.

The project needs a review gate between:

```text
Source
->
Claim
->
Knowledge
```

## Scope

Review claims from:

- `knowledge/claims/adult-learning.yaml`
- `knowledge/claims/coaching-standards.yaml`
- `knowledge/claims/motor-learning.yaml`
- `knowledge/claims/serve.yaml`
- `knowledge/claims/video-analysis.yaml`

## Non-Scope

This issue does not include:

- adding new source categories
- expanding the virtual team
- writing training plans
- writing nutrition plans
- writing rehab advice
- building Agent, RAG, or video automation

## Definition Of Done

- Claim Review v0.1 exists under `knowledge/claims/reviews/`.
- Every current claim has a review decision.
- Claims are classified as `promote_to_knowledge`, `needs_experiment`,
  `research_direction`, or `defer`.
- Review output preserves the boundary between claims and training advice.
