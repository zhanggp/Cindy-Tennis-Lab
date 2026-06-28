# Repository Structure

Cindy Tennis Lab is organized as a long-term learning system.

The structure separates stable philosophy, reusable tennis knowledge,
learner-specific programs, applied labs, real records, experiments, and journals.

```text
Cindy-Tennis-Lab/
├── foundation/
├── docs/
├── knowledge/
├── skills/
├── harness/
├── programs/
├── labs/
├── records/
├── experiments/
└── journal/
```

## Foundation

`foundation/` stores principles that should change slowly.

It answers: why do we learn this way, how should AI support learning, and what
should parents protect over the long term?

## Docs

`docs/` stores system architecture, repository workflow, and decision records.

It answers: how does the lab work as an engineering system?

## Knowledge

`knowledge/` stores reusable tennis knowledge.

`knowledge/schema/` defines structure. `knowledge/ontology/` defines tennis
domains such as serve, footwork, and match play. `knowledge/concepts/` stores
cross-cutting ideas such as biomechanics, tactics, mental game, and injury
prevention.

## Skills

`skills/` stores repeatable AI workflows.

Each skill defines when to use it, what inputs it expects, how to reason through
the task, what output format to produce, and what guardrails protect the
learner.

## Harness

`harness/` stores test cases, rubrics, and validation scripts for skills.

The harness does not prove that AI advice is correct. It checks whether a skill
has enough structure to be evaluated consistently.

## Programs

`programs/` stores learner-specific long-term paths.

- `programs/cindy-ncaa-pathway/`: Cindy's junior development and NCAA pathway.
- `programs/mickey-2.5-to-4.0/`: Mickey's adult learner path from 2.5 to 4.0.

## Labs

`labs/` stores applied R&D.

The first labs are serve development, video analysis, and animation course
design. Labs can be messy while ideas are being tested, then stable outputs can
move into `knowledge/` or `programs/`.

## Records

`records/` stores real learner evidence: monthly videos, reports, practice
notes, match notes, and growth archives.

This area should preserve what actually happened, not what we wish had happened.

## Experiments

`experiments/` stores early learner-specific explorations.

When an experiment becomes durable, move its pattern into `programs/`, `labs/`,
or `knowledge/`.

## Journal

`journal/` stores chronological reflection.

The journal is the memory of the project: one day, one note, one learning step.
