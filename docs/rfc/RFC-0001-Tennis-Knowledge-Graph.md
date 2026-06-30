# RFC-0001: Tennis Knowledge Graph

Status: Draft

Date: 2026-06-30

## Summary

This RFC defines Tennis Knowledge Graph v0.1.

The goal is to create a small foundation for connecting tennis knowledge,
evidence, metrics, drills, and experiments.

## Why

Cindy Tennis Lab needs a knowledge graph because tennis learning is not one
linear topic.

Technique depends on physics, biomechanics, anatomy, motor learning, decision
making, drills, metrics, and experiments. Without a graph, observations become
scattered notes and cannot compound over time.

## Scope

Tennis Knowledge Graph v0.1 includes these node types:

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

Tennis Knowledge Graph v0.1 does not include:

- Agents
- RAG
- vector databases
- video recognition
- UI
- public content workflows
- complete Serve ontology

Serve is a Skill node. It is not a top-level domain.

## Node Definitions

| Node | Description | Inputs | Outputs | Relationships |
| --- | --- | --- | --- | --- |
| Knowledge | Reusable idea that survived review. | Evidence, observations, experiments | Principles, models, decisions | Connects all nodes |
| Physics | Ball, force, spin, trajectory, energy. | Video, measurement, external references | Physical constraints | Informs Skill and Metrics |
| Biomechanics | Body movement and kinetic chain. | Video, anatomy, coaching notes | Movement model | Informs Skill and Drill |
| Anatomy | Body structures and health constraints. | Health notes, rehab notes, anatomy references | Safety constraints | Informs Biomechanics and Experiment |
| Motor Learning | How skill changes through practice. | Practice notes, feedback, retention data | Learning rules | Informs Drill and Experiment |
| Skill | A tennis capability such as serve. | Knowledge, biomechanics, motor learning | Skill model | Uses Drill and Metrics |
| Drill | A designed practice task. | Skill focus, constraints, metrics | Practice protocol | Tests Skill |
| Metrics | Measurement used for review. | Evidence, scores, counts | Assessment | Evaluates Drill, Skill, Experiment |
| Experiment | Time-boxed test of a hypothesis. | Question, intervention, metrics | Review decision | Promotes Knowledge |

## Definition Of Done

Tennis Knowledge Graph v0.1 is done when:

- RFC-0001 exists in `docs/rfc/`
- YAML schema exists in `knowledge/schema/`
- top-level node types are defined
- each node has description, inputs, outputs, and relationships
- Serve is represented as a Skill, not as a top-level graph domain
