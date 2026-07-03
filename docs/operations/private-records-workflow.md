# Private Records Workflow

Status: Draft

Date: 2026-07-03

## Purpose

Define how Cindy Tennis Lab handles real athlete records without committing
private data to the public repository.

This workflow supports:

- Athlete Profile & Safety Baseline
- Match Baseline
- private coach notes
- private parent observations
- future experiment records

## Public Repo Rule

The public repository may store:

- schemas
- public-safe examples
- anonymized templates
- privacy rules
- reflection structure

The public repository must not store:

- real event schedules
- exact locations
- opponent names
- private coach notes
- medical details
- pain details tied to a real minor
- identifiable video links
- raw private video
- sensitive mental or nutrition notes

## Private Paths

Real data should live outside the public repo or under ignored paths:

- `data/private/`
- `profiles/private/`
- `medical/`

These paths are ignored by `.gitignore`.

## Recommended Private Match Record

Use the public template:

- `experiments/templates/match-baseline.example.yaml`

Copy its structure into a private location, then fill real details privately.

Suggested private path pattern:

```text
data/private/cindy/matches/YYYY-MM-DD-match-baseline.yaml
```

Do not commit that file.

## Minimum Match Observation

Keep match observation lightweight:

- serve rhythm
- serve in-rate
- double faults
- return ready position
- first three balls
- reset after lost point
- enjoyment
- safety boundary signals

## Parent Rule

During a junior match, the parent role is presence, safety, encouragement, and
post-match reflection.

Do not turn one match into a verdict.

Do not turn the sideline into a coaching session.

## Review Rule

After the match, review only:

- what went well
- one learning
- one next question

Training changes should wait for a later coach or experiment review.
