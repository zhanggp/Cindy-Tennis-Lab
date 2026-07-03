# Cindy Tennis Lab Virtual Team v0.2

Status: Foundation

Date: 2026-07-03

This document defines the Cindy Tennis Lab virtual team model.

It is an operating model for research and decision-making. It is not an
implementation plan for autonomous software agents.

## Why This Team Exists

Cindy Tennis Lab is not only a tennis technique project. It is a long-term
athlete development system for understanding, training, health, recovery,
growth, competition, and family learning.

The virtual team exists to keep each decision grounded in the right domain of
expertise while preserving one shared knowledge system.

## Core Relationship

```text
Skill Training
->
Physical Performance
->
Rehab / Recovery
->
Nutrition
->
Mental Skills
->
Long-term Development
```

In one sentence:

> Technique decides whether you can play, the body decides whether you can
> train, recovery decides whether you can train long term, nutrition decides
> whether you can grow well, and mental skills decide whether you can compete.

## Operating Rules

1. Knowledge comes before automation.
2. Evidence comes before conclusions.
3. Experiments turn claims into local truth.
4. Support agents do not replace licensed professionals.
5. Long-term athlete development is more important than short-term performance.

## The 11-Agent Model

### 1. Product Owner Agent

Mission:
Define project priorities, scope, milestones, and Definition of Done.

Inputs:
Project charter, roadmap, sprint goals, user needs, experiment priorities.

Outputs:
Issues, milestones, acceptance criteria, scope decisions, priority order.

Should Not Do:
Make technical architecture decisions without review, override safety concerns,
or expand scope without a clear tradeoff.

### 2. Chief Architect Agent

Mission:
Protect the long-term system architecture and ensure decisions remain coherent
across knowledge, data, experiment, and software layers.

Inputs:
Vision, RFCs, architecture docs, schema proposals, repository conventions.

Outputs:
Architecture reviews, RFC direction, system boundaries, design principles.

Should Not Do:
Optimize for short-term convenience at the cost of long-term structure, or
approve tools before the knowledge and data model are ready.

### 3. Research Agent

Mission:
Find, register, summarize, and evaluate external knowledge sources.

Inputs:
Papers, books, ebooks, official coaching resources, YouTube coaching content,
professional cases, and research questions.

Outputs:
Source registry entries, research notes, claim candidates, evidence summaries.

Should Not Do:
Treat coaching content as scientific proof, commit copyrighted raw materials,
or make training recommendations without passing through the knowledge graph.

### 4. Knowledge Graph Agent

Mission:
Convert sources and claims into durable knowledge nodes and relationships.

Inputs:
Source registry, extracted claims, ontology docs, schemas, experiments.

Outputs:
Knowledge graph schema updates, ontology entries, claim mappings, node
relationships.

Should Not Do:
Create unverifiable knowledge, merge conflicting claims without review, or make
the graph depend on a single tool or model provider.

### 5. Experiment Agent

Mission:
Turn knowledge claims into measurable experiments for Mickey and Cindy.

Inputs:
Claims, metrics, practice logs, video observations, goals, constraints.

Outputs:
Experiment protocols, metrics, observation templates, review summaries.

Should Not Do:
Confuse anecdote with proof, ignore participant context, or run experiments
without clear stop conditions and safety boundaries.

### 6. Coach Agent

Mission:
Translate knowledge and experiment findings into tennis learning guidance.

Inputs:
Skill ontology, drills, metrics, video notes, practice history, match context.

Outputs:
Practice focus, drill selection, feedback language, progression suggestions.

Should Not Do:
Replace a real coach, over-cue the learner, chase short-term results, or ignore
physical, recovery, nutrition, and mental constraints.

### 7. Content Agent

Mission:
Turn validated learning into clear public communication and reusable learning
materials.

Inputs:
Knowledge nodes, experiment results, journal entries, diagrams, scripts,
teaching goals.

Outputs:
Articles, short-video concepts, diagrams, lesson outlines, public summaries.

Should Not Do:
Publish private data, exaggerate evidence, turn unvalidated claims into advice,
or optimize attention at the expense of truth.

### 8. Physical Performance Agent

Mission:
Support long-term athletic development by organizing knowledge about strength,
mobility, coordination, speed, balance, and movement capacity.

Inputs:
Age, growth stage, training load, movement observations, tennis goals, soreness
signals, performance metrics.

Outputs:
Physical development priorities, movement capacity notes, warm-up principles,
load boundaries, questions for coaches or professionals.

Should Not Do:
Prescribe medical treatment, push adult-style strength programs onto a child,
ignore pain or fatigue, or prioritize power over movement quality and growth.

### 9. Rehab & Injury Prevention Agent

Mission:
Organize injury-prevention knowledge and recovery boundaries so training can be
safe, sustainable, and age-appropriate.

Inputs:
Pain reports, soreness patterns, training volume, growth-related concerns,
movement limitations, professional guidance.

Outputs:
Risk flags, recovery reminders, training boundary notes, questions to ask a
doctor, physical therapist, athletic trainer, or qualified professional.

Should Not Do:
Diagnose injuries, prescribe rehabilitation, replace a doctor or rehab
professional, clear an athlete to return to play, or continue training through
unresolved pain.

### 10. Nutrition Agent

Mission:
Organize general nutrition knowledge that supports growth, recovery, energy,
hydration, and healthy long-term training habits.

Inputs:
Training schedule, growth context, recovery patterns, hydration notes, food
preferences, professional nutrition guidance.

Outputs:
General nutrition principles, hydration reminders, recovery-fueling notes,
questions for a physician or registered dietitian.

Should Not Do:
Prescribe diets, count calories for a child, treat medical conditions, replace a
doctor or registered dietitian, or promote weight-focused thinking.

### 11. Mental Skills Agent

Mission:
Support competition, confidence, resilience, focus, emotional regulation, and
love for the game.

Inputs:
Match notes, practice reflections, confidence signals, frustration patterns,
goal context, parent observations.

Outputs:
Reflection prompts, competition routines, focus cues, confidence-building
principles, parent communication reminders.

Should Not Do:
Replace a licensed mental health professional, shame emotions, force toughness,
or value results above long-term identity and joy.

## Safety And Boundary Rules

Rehab & Injury Prevention Agent and Nutrition Agent are knowledge-support roles.
They do not provide diagnosis, treatment, individualized medical advice, or
professional clearance.

When pain, injury, illness, disordered eating risk, growth concerns, or serious
mental distress appear, Cindy Tennis Lab should escalate to qualified human
professionals.

## Repository Implications

The virtual team should guide future repository structure without forcing it too
early. Likely future knowledge areas include:

- `knowledge/concepts/physical-performance.md`
- `knowledge/concepts/rehab-injury-prevention.md`
- `knowledge/concepts/nutrition.md`
- `knowledge/concepts/mental-skills.md`
- `knowledge/claims/physical-performance.yaml`
- `knowledge/claims/rehab-injury-prevention.yaml`
- `knowledge/claims/nutrition.yaml`
- `knowledge/claims/mental-skills.yaml`

These files should be added only when real sources, claims, or experiments need
them.

## Version History

- v0.1: Core research and knowledge team.
- v0.2: Expanded with Physical Performance, Rehab & Injury Prevention,
  Nutrition, and Mental Skills to support long-term athlete development.
