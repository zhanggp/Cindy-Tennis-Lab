# Issue #003: Experiment Schema v0.1

Status: Done

## Why

Cindy Tennis Lab needs a consistent experiment model so training ideas can be
tested, reviewed, and promoted into knowledge.

## Scope

Define an experiment schema with:

- question
- hypothesis
- intervention
- evidence plan
- primary metric
- supporting metrics
- stop conditions
- review decision

Create:

- `data/schemas/experiment.schema.yaml`
- `experiments/templates/serve-claim-experiment.example.yaml`

## Non-Scope

This issue does not run the first experiment.

This issue does not create a training plan.

This issue does not commit real athlete data.

## Definition Of Done

- Experiment schema exists in `data/schemas/`.
- Cindy health guardrails are represented.
- Experiment records can link to evidence and metrics.
- A public-safe serve claim experiment example exists.
