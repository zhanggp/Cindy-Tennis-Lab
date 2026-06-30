# Issue #006: Build Serve Ontology v0.1

## Goal

Define Serve as the first real Skill node in Cindy Tennis Lab's Tennis
Knowledge Graph.

## Why

Serve is the first concrete domain where the project can connect:

- sources
- claims
- physics
- biomechanics
- anatomy
- motor learning
- drills
- metrics
- experiments

Serve should be modeled before it becomes a training plan, video analysis
workflow, or Agent feature.

## Scope

Fill the Serve skill directory:

- `knowledge/skills/serve/README.md`
- `knowledge/skills/serve/overview.md`
- `knowledge/skills/serve/physics.md`
- `knowledge/skills/serve/biomechanics.md`
- `knowledge/skills/serve/anatomy.md`
- `knowledge/skills/serve/motor-learning.md`
- `knowledge/skills/serve/common-errors.md`
- `knowledge/skills/serve/drills.md`
- `knowledge/skills/serve/metrics.yaml`
- `knowledge/skills/serve/sources.md`

## Non-Scope

This issue does not include:

- a daily training plan
- injury diagnosis
- video recognition
- automatic scoring
- Agent implementation

## Definition Of Done

- Serve is clearly modeled as a Skill node.
- Serve links to Physics, Biomechanics, Anatomy, Motor Learning, Drill, Metrics,
  and Experiment.
- Serve source coverage is documented.
- Serve metrics are valid YAML.
- Existing harness validation still passes.
