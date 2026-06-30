# Issue #001: Design Tennis Knowledge Graph v0.1

## Why

Cindy Tennis Lab needs a Tennis Knowledge Graph so knowledge, evidence, drills,
metrics, and experiments can compound over time instead of staying as scattered
notes.

## Scope

Define Tennis Knowledge Graph v0.1 with these node types:

- Knowledge
- Physics
- Biomechanics
- Anatomy
- Motor Learning
- Skill
- Drill
- Metrics
- Experiment

## Non-Scope

This issue does not include:

- Agents
- MCP
- RAG
- vector database
- video recognition
- UI
- complete Serve ontology

## Definition Of Done

- RFC-0001 exists under `docs/rfc/`.
- YAML schema exists under `knowledge/schema/`.
- Each node has description, inputs, outputs, and relationships.
- Serve is represented as a Skill node, not a top-level domain.
- Changes are committed to Git.
