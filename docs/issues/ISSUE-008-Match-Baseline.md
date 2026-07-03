# Issue #008: Add Match Baseline Template v0.1

## Goal

Create a privacy-safe template for observing a junior match baseline.

## Why

Junior match contexts need a safe way to capture what to observe without
committing real schedule, location, opponent, coach, or health details.

## Scope

Create:

- `data/schemas/match-baseline.schema.yaml`
- `experiments/templates/match-baseline.example.yaml`
- `records/cindy/matches/README.md`

## Non-Scope

This issue does not include:

- recording Cindy's real match schedule
- recording match location or opponent names
- writing a training plan
- writing nutrition advice
- writing rehab advice
- judging long-term development from one match

## Definition Of Done

- Match baseline schema exists.
- Public example contains placeholder data only.
- Privacy rules clearly block real minor-event details from the public repo.
- The template observes serve, return, first three balls, mental reset, joy, and
  safety boundary signals.
