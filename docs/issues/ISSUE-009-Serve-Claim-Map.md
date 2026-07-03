# Issue #009: Map Serve Claims To Knowledge Node v0.1

## Goal

Map reviewed serve claims to the Serve skill node, related knowledge graph
nodes, observable metrics, and next experiment questions.

## Why

The project priority is:

```text
Source
->
Claim
->
Knowledge Node
->
Experiment
```

Serve already has source notes, claims, review decisions, ontology, and metrics.
The missing link is a compact map that shows how each serve claim connects to
the Serve node and what should happen next.

## Scope

Create:

- `knowledge/skills/serve/claim-map.yaml`

Update:

- `knowledge/skills/serve/README.md`
- `docs/projects/Sprint-1.md`
- `journal/2026/Week27.md`

## Non-Scope

This issue does not include:

- adding new serve claims
- writing a training plan
- writing match advice
- adding private athlete data
- using YouTube or ebooks as scientific evidence
- treating professional players as standard answers

## Definition Of Done

- Every serve claim has a node mapping.
- Every metric reference exists in `knowledge/skills/serve/metrics.yaml`.
- Claims that need validation remain experiment candidates.
- The output preserves the boundary between knowledge structure and training.
