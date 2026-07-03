# Agent Source Map v0.1

Status: Draft

Date: 2026-07-03

This map connects the Cindy Tennis Lab virtual team to the source classes each
role needs before making durable claims.

The goal is not to collect more material. The goal is to collect the minimum
source set that lets each agent produce traceable claims.

## Source Flow

```text
Source
->
Claim
->
Knowledge Node
->
Experiment
->
Validation
```

## Agent Source Needs

| Agent | Must-Have Source Classes | Seed Sources | Primary Output |
| --- | --- | --- | --- |
| Product Owner Agent | project decisions, roadmap, issue history | Project Charter, RFCs | priorities and scope |
| Chief Architect Agent | RFCs, schemas, architecture docs | RFC-0001, athlete profile schema | system boundaries |
| Research Agent | papers, official systems, books, videos, cases | Source Registry | source notes and claim candidates |
| Knowledge Graph Agent | source notes, extracted claims, ontology docs | Tennis Knowledge Graph v0.1 | node and relation updates |
| Experiment Agent | claims, metrics, athlete profile, own data | Athlete Profile schema, Serve metrics | experiment protocols |
| Coach Agent | skill ontology, drills, official systems, coaching frameworks | Serve Ontology, USTA, World Tennis | practice focus options |
| Content Agent | validated claims, public-safe stories, diagrams | Journal, public research notes | public explanations |
| Physical Performance Agent | growth, load, movement, physical development sources | Athlete Profile schema, World Tennis | load and movement context |
| Rehab & Injury Prevention Agent | safety policies, pain monitoring, injury-prevention sources | USTA Safe Play, Athlete Profile schema | boundary reminders |
| Nutrition Agent | general fueling, growth, hydration, professional guidance | Athlete Profile schema | questions and boundaries |
| Mental Skills Agent | match reflection, confidence, stress, sport psychology sources | Athlete Profile schema, World Tennis Coaching and Sports Science Review | reflection prompts |

## Current Priority Sources

| Source | Tier | Why It Matters | Agent Fit |
| --- | --- | --- | --- |
| The Skills of a Tennis Athlete | T3 | Practice framework and skill taxonomy inspiration | Research, Knowledge Graph, Coach |
| USTA Coaching / Safe Play | T2 | Coaching education, safeguarding, and coach-development standard | Coach, Rehab & Injury Prevention, Product Owner |
| World Tennis / ITF Coaching | T2 | Global coach education, certification, publications, and development context | Coach, Physical Performance, Research |
| Djokovic Serve Case | T4 | High-level serve implementation example | Coach, Knowledge Graph, Content |

## Rules

- T2 official systems define standards and boundaries, not personalized advice.
- T3 practice frameworks can create claim candidates, but need validation.
- T4 professional cases show implementation variants, not junior training models.
- Private or copyrighted materials must not be copied into the public repo.
- Claims become local truth only after experiment or review.
