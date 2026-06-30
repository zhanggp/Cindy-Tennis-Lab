# Issue #002: Build Tennis Knowledge Source Registry v0.1

## Goal

Establish Cindy Tennis Lab's knowledge source registration system for papers,
official systems, coaching frameworks, ebooks, professional player cases, video
analysis research, and own training data.

## Why

The project should not advance by memory or scattered links.

It should move through:

```text
Source
↓
Claim
↓
Knowledge Node
↓
Experiment
↓
Validation
↓
Training
```

## Scope

Create:

- `sources/README.md`
- `sources/registry.yaml`
- `sources/private-sources.example.yaml`
- `knowledge/claims/README.md`
- `knowledge/claims/serve.yaml`
- `knowledge/claims/motor-learning.yaml`
- `research/README.md`
- `research/papers/README.md`
- `research/official/README.md`
- `research/coaching-frameworks/README.md`
- `research/video-analysis/README.md`

Update `.gitignore` so these top-level private/raw asset directories are not
committed:

- `private/`
- `raw/`
- `pdfs/`
- `ebooks/`
- `videos/`

## Seed Sources

Add first seed sources:

- The Skills of a Tennis Athlete
- USTA Coaching
- World Tennis / ITF
- Tennis biomechanics paper
- Tennis video analysis paper
- Zhang Zhizhen serve case
- Djokovic serve case
- Mickey training data
- Cindy training data

## Definition Of Done

- Source registry exists and includes the seed sources.
- Private-source example exists.
- Claim extraction files exist.
- Research directories exist.
- Private/raw asset directories are ignored by Git.
- Copyright policy is explicit.
- Practice frameworks are marked as needing validation before becoming
  knowledge.
