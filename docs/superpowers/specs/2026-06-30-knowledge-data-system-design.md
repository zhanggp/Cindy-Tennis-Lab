# Cindy Tennis Lab Knowledge And Data System Design

Date: 2026-06-30

Status: Draft for user review

## 1. Purpose

Cindy Tennis Lab has finished its foundation layer: mission, repository
structure, first tennis knowledge schema, AI skills, and a lightweight harness.
The next step is to turn scattered evidence and analysis into a long-term
learning data system.

This design defines a Git-native knowledge and data architecture for Cindy
Tennis Lab v0.2. It should support years of iteration without forcing the
project into a heavy app or database too early.

The core purpose is:

- preserve real evidence before interpretation
- connect video, coaching feedback, training notes, health signals, and match
  outcomes
- make progress measurable across months and years
- protect uncertainty and avoid turning one observation into a permanent rule
- let future tools, databases, dashboards, or AI workflows build on stable
  source files

## 2. Existing Context

The Git history shows three completed foundation steps:

- `5aaf7c4`: initialized foundation v0.1 with vision, manifesto, why, roadmap,
  first principles, system overview, journal, and initial knowledge schema
- `83e5657`: organized repository structure into foundation, docs, knowledge,
  programs, labs, records, experiments, and journal
- `0129f81`: added AI skills and a validation harness for repeatable workflows

The repository already has the right conceptual containers, but the real Cindy
evidence still lives partly outside `Cindy-Tennis-Lab/`, especially the 2026-05
Chinese analysis documents and the stroke tracking CSV template in the parent
workspace.

Current gap:

- `knowledge/schema/tennis-knowledge-schema.yaml` defines a reusable knowledge
  item, but not the full data lifecycle.
- `records/cindy/` exists, but does not yet contain structured monthly evidence.
- Skills imply useful fields, such as serve scores, practice focus, match
  patterns, risks, and next actions, but those fields are not yet unified.
- Existing 2026-05 analysis has strong content but needs stable IDs, evidence
  references, and migration into a durable record layer.

## 3. Design Principles

### Git Native First

Markdown, YAML, and CSV remain the source of truth for v0.2. This keeps every
decision reviewable in Git and avoids premature database complexity.

### Evidence Before Knowledge

Raw or derived evidence is not the same as knowledge. A video clip, coach note,
or one match observation should first become an evidence record or observation.
Only repeated or high-confidence patterns should be promoted into `knowledge/`.

### Separate Fact, Interpretation, And Hypothesis

Every durable record should distinguish:

- what happened
- what was observed
- what may explain it
- what action will test the hypothesis
- when it should be reviewed again

### Learner Health Comes First

For Cindy, tennis development data must include health and recovery signals.
Pain, sleep, nutrition, workload, and emotional response are not side notes;
they are part of the training system.

### One Main Focus Per Cycle

Monthly and 4-8 week cycles should choose one primary development focus. The
data system can hold many signals, but training decisions should stay small
enough to act on.

### Future Exportability

Every entity should have stable IDs and simple fields so the same data can later
feed SQLite, dashboards, search indexes, vector retrieval, or a knowledge graph.

## 4. Recommended Architecture

The long-term system should have six layers.

### Layer 1: Evidence

Evidence is the most concrete layer. It answers: what source material exists?

Examples:

- original videos
- derived frame sheets
- match score notes
- practice notes
- coach feedback
- medical or rehab notes
- monthly reports
- parent reflections

Evidence records should live under `records/<learner>/evidence/` or be indexed
there when the file itself is too large or stored outside Git.

### Layer 2: Observation

Observation records answer: what did we see in the evidence?

An observation should not pretend to be a universal conclusion. It should
include source references, confidence, and limitations. For example:

- "发球后第一拍准备慢 appears in 2026-05 match footage."
- "Split-step instability may be connected to foot pain, but needs direct pain
  reporting to verify."

Observation records should live under `records/<learner>/observations/`.

### Layer 3: Assessment

Assessment records answer: how are we measuring the current state?

Examples:

- stroke tracking scores
- serve monthly review data
- pain 0-10 logs
- sleep and nutrition checks
- practice workload summaries
- match transfer ratings

Assessment records should live under `records/<learner>/assessments/`, with CSV
or YAML preferred for structured metrics.

### Layer 4: Experiment

Experiment records answer: what are we testing next?

Examples:

- "For 8 weeks, use fixed serve routine and track first-serve routine
  consistency."
- "Add 2-second recovery rule after each feed and track ready-position return."

Experiment records should live under `experiments/<learner>/` while active.
Validated patterns may later move into `programs/`, `labs/`, or `knowledge/`.

### Layer 5: Knowledge

Knowledge records answer: what reusable learning has survived review?

Examples:

- serve phase ontology
- footwork principles
- injury-prevention concepts
- tactics patterns
- AI workflow rules

This layer remains in `knowledge/`. It should be more stable than records and
experiments.

### Layer 6: Program

Program records answer: how does the learner path change because of evidence?

For Cindy, this connects the monthly data to the NCAA pathway:

- age-stage roadmap
- monthly focus
- yearly development story
- coach and parent communication
- long-term health and academic balance

This layer remains in `programs/cindy-ncaa-pathway/`.

## 5. Proposed Repository Shape

Add these folders over time:

```text
records/
  cindy/
    evidence/
      2026/
        2026-05/
          index.yaml
          documents/
          videos/
          frames/
    observations/
      2026/
        2026-05-observations.yaml
    assessments/
      stroke-tracking.csv
      serve-monthly.csv
      health-load-log.csv
    monthly/
      2026-05.md
    reports/
      2026-05-growth-report.md

knowledge/
  schema/
    tennis-knowledge-schema.yaml
    tennis-data-system-schema.yaml
  taxonomy/
    stroke-taxonomy.yaml
    evidence-taxonomy.yaml
    metric-taxonomy.yaml

docs/
  decisions/
    2026-06-30-knowledge-data-system-v0.2.md
```

Do not move large original videos into Git by default. Instead, store stable
metadata and relative or external file references.

## 6. Core Entity Model

### Learner

Represents a person using the system.

Required fields:

- `id`
- `name`
- `profile`
- `long_term_goal`
- `active_program`

Existing learners:

- `cindy`
- `mickey`
- `shared`

### Evidence Item

Represents a source artifact.

Required fields:

- `id`
- `learner_id`
- `date`
- `type`
- `title`
- `path_or_reference`
- `source_context`
- `privacy_level`
- `derived_from`
- `notes`

Allowed evidence types:

- `video`
- `frame_sheet`
- `match_note`
- `practice_note`
- `coach_feedback`
- `analysis_doc`
- `health_note`
- `report`
- `photo`
- `other`

### Observation

Represents one claim extracted from evidence.

Required fields:

- `id`
- `learner_id`
- `date`
- `category`
- `statement`
- `evidence_ids`
- `confidence`
- `limitations`
- `hypothesis`
- `suggested_next_action`
- `review_status`

Observation categories should reuse the current knowledge schema categories:

- `technique`
- `tactics`
- `footwork`
- `serve`
- `return`
- `rally`
- `match_play`
- `physical`
- `mental`
- `learning_habit`
- `parent_companionship`
- `ai_workflow`

### Assessment Metric

Represents a score or measurement.

Required fields:

- `id`
- `learner_id`
- `date`
- `cycle`
- `metric`
- `value`
- `scale`
- `context`
- `evidence_ids`
- `reviewer`
- `notes`

Initial Cindy metric families:

- stroke technical stability, 1-5
- foot pain, 0-10
- pain limitation, yes/no
- ball quality and placement, 1-5
- tactical execution, 1-5
- match transfer, 1-5
- serve phase scores, 0-100
- first serve in count, 0-20
- second serve in count, 0-20
- ready-position recovery count, 0-n
- weekly practice load
- sleep consistency
- nutrition support
- rehab completion

### Experiment

Represents one testable learning cycle.

Required fields:

- `id`
- `learner_id`
- `start_date`
- `end_date`
- `question`
- `hypothesis`
- `intervention`
- `primary_metric`
- `supporting_metrics`
- `stop_conditions`
- `evidence_plan`
- `review_result`
- `next_decision`

### Knowledge Item

The existing `knowledge_item` schema remains valid, but should be expanded to
link back to observations and experiments:

- `evidence_ids`
- `observation_ids`
- `experiment_ids`
- `promotion_reason`
- `last_reviewed`

## 7. ID Naming

Use stable, readable IDs:

```text
evidence:cindy:2026-05:match-video-0004
evidence:cindy:2026-05:coach-feedback-rehab-reset
observation:cindy:2026-05:serve-recovery-slow
assessment:cindy:2026-05:stroke-baseline
experiment:cindy:2026-06:fixed-serve-routine
knowledge:serve:fixed-routine-before-power
```

Rules:

- lowercase English slugs
- learner ID included for learner-specific records
- month included for time-bound records
- keep Chinese in titles and notes, not in IDs
- never reuse an ID for a different meaning

## 8. Data Flow

### Capture Flow

1. Add or reference evidence.
2. Register it in an evidence index.
3. Extract observations with evidence IDs.
4. Add assessment scores if measurable.
5. Choose one experiment or next action.
6. Review after the planned cycle.
7. Promote durable patterns to knowledge only after review.

### Monthly Flow

1. Create or update monthly evidence index.
2. Update stroke and serve assessments.
3. Add health and load summary.
4. Write monthly report using the `monthly-growth-report` skill.
5. Decide next month's primary focus.
6. Link the month back to the Cindy NCAA pathway.

### Promotion Flow

Observation becomes knowledge only when one of these is true:

- repeated across multiple evidence sources
- confirmed by coach feedback
- validated in an experiment cycle
- required as a safety guardrail

## 9. Initial 2026-05 Migration

The first real migration should use existing parent-workspace files as the
baseline:

- `docs/xinqi-match-video-analysis-2026-05.md`
- `docs/xinqi-closeup-training-video-analysis-2026-05.md`
- `docs/xinqi-serve-action-analysis-2026-05.md`
- `docs/xinqi-coach-feedback-rehab-training-reset-2026-05-10.md`
- `docs/xinqi-stroke-long-term-tracking-2026-05.md`
- `docs/xinqi-stroke-tracking-template.csv`
- `202605/` DJI match videos
- `analysis/` derived frame sheets
- root-level close-up training videos

Recommended migration output:

- `records/cindy/evidence/2026/2026-05/index.yaml`
- `records/cindy/observations/2026/2026-05-observations.yaml`
- `records/cindy/assessments/stroke-tracking.csv`
- `records/cindy/monthly/2026-05.md`
- `docs/decisions/2026-06-30-cindy-2026-05-baseline-migration.md`

The migration should not duplicate large video files. It should index them and
preserve their current paths.

## 10. Error Handling And Guardrails

### Missing Evidence

If a score or conclusion lacks evidence, mark it as `needs_evidence` instead of
inventing a reference.

### Unclear Video

If the camera angle is insufficient, record the limitation and request a future
clip angle. Do not overstate fine technical conclusions from distant video.

### Health Signals

Pain above 3/10 should mark related high-impact training assessments as
limited. Pain above 5/10 or warning signs such as limping should trigger a
health-first note and avoid technical conclusions for that session.

### Privacy

Use conservative metadata for personal, medical, school, and child-related
records. Avoid storing unnecessary sensitive details.

### AI Output

AI-generated analysis should be treated as interpretation unless linked to
evidence and reviewed. The system should preserve uncertainty, not launder AI
text into truth.

## 11. Validation

v0.2 should extend the existing harness mindset with simple validators.

Initial validation checks:

- every evidence item has an ID, learner, type, title, and reference
- every observation links to at least one evidence ID
- every assessment metric declares scale and context
- every experiment has a question, hypothesis, primary metric, and review date
- every promoted knowledge item links back to evidence, observation, or
  experiment IDs
- no duplicate IDs across structured files

This can be implemented later with a dependency-free script similar to
`harness/scripts/validate_harness.py`.

## 12. What v0.2 Should Not Do Yet

Do not build a full app yet.

Do not require a database yet.

Do not move large videos into Git by default.

Do not turn every note into a rigid form.

Do not promote every observation into reusable knowledge.

Do not optimize for rankings or winning at the expense of health, joy, and
long-term learning.

## 13. Roadmap

### Phase 1: Design And Schema

- write this design
- add `tennis-data-system-schema.yaml`
- add taxonomy files
- update repository structure docs

### Phase 2: Cindy 2026-05 Baseline Migration

- index existing May evidence
- migrate stroke tracking CSV into `records/cindy/assessments/`
- create observations from existing analysis
- create a monthly baseline summary

### Phase 3: Review Workflows

- update skills so their outputs include structured IDs
- add validation cases for evidence, observations, assessments, and experiments
- add a monthly review checklist

### Phase 4: Reporting And Querying

- generate monthly summaries from structured records
- compare month-over-month trends
- produce coach-facing and parent-facing views

### Phase 5: Optional Database Or App

Only after the Git-native model stabilizes:

- import YAML/CSV into SQLite
- build a dashboard
- add search or vector retrieval
- create a knowledge graph view

## 14. Success Criteria

The v0.2 system is successful if:

- a new video or coach note can be added without confusion
- a monthly report can cite evidence IDs rather than vague memory
- Cindy's serve, movement, pain, and match transfer can be tracked over time
- the repository can answer "what changed since last month?"
- future AI workflows can use structured data without losing nuance
- the family, coach, and AI can share one calmer language for progress

## 15. Open Questions For Review

1. Should real evidence be copied into `Cindy-Tennis-Lab/records/` when small,
   or always referenced from the parent workspace?
2. Should Cindy's Chinese analysis documents remain Chinese-first, or should
   the repository gradually add English summaries for long-term portability?
3. Should health/load data stay as CSV for easy editing, or move to YAML for
   richer context?
4. Which 2026-06 or 2026-07 training cycle should become the first formal
   experiment after the 2026-05 baseline migration?
