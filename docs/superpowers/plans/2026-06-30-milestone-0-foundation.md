# Milestone 0 Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish Milestone 0 as the foundation gate for Cindy Tennis Lab before any Agent implementation begins.

**Architecture:** Treat the current v0.1 foundation as the starting point, then add a stricter Milestone 0 readiness layer around Vision, Architecture, Knowledge Graph Schema, Data Strategy, Experiment Protocol, and Repository Convention. Keep the work Git-native: Markdown for decisions and conventions, YAML for schemas and taxonomies, and existing harness validation for repository sanity checks.

**Tech Stack:** Markdown, YAML, Git, Python standard library harness validation.

---

## Scope Check

Milestone 0 is a foundation milestone, not an Agent milestone. It intentionally produces documents, schemas, conventions, and readiness gates. It does not create Agent prompts, Agent code, automation services, dashboards, databases, or UI.

The six modules are connected enough to implement in one milestone plan because they define a single operating foundation:

- Vision defines why the lab exists.
- Architecture defines how the system is organized.
- Knowledge Graph Schema defines how concepts connect.
- Data Strategy defines how evidence becomes reusable records.
- Experiment Protocol defines how learning claims are tested.
- Repository Convention defines how future work stays coherent.

## File Structure

Create or modify these files:

- Create: `docs/milestones/2026-06-30-foundation.md`
  - Milestone charter, duration, module checklist, completion criteria, and Agent gate.
- Modify: `README.md`
  - Add Milestone 0 as the current entry point before Agent work.
- Modify: `ROADMAP.md`
  - Add Milestone 0 as the foundation gate between v0.1/v0.2 and future Agent implementation.
- Create: `docs/decisions/2026-06-30-milestone-0-foundation-gate.md`
  - Record the decision that Agents wait until the six foundation modules are complete.
- Modify: `docs/architecture/system-overview.md`
  - Add the foundation readiness layer and the six-layer learning data architecture.
- Modify: `docs/architecture/repository-structure.md`
  - Add `docs/milestones/`, schema/taxonomy expectations, and repository convention references.
- Modify: `docs/architecture/workflow.md`
  - Add milestone-driven workflow before issue execution.
- Create: `knowledge/schema/knowledge-graph-schema.yaml`
  - Define graph node types, edge types, ID rules, and promotion rules.
- Modify: `knowledge/schema/tennis-knowledge-schema.yaml`
  - Link existing knowledge items to graph concepts without breaking the current schema.
- Create: `knowledge/taxonomy/evidence-taxonomy.yaml`
  - Define evidence types and privacy levels.
- Create: `knowledge/taxonomy/metric-taxonomy.yaml`
  - Define metric families and scales.
- Create: `knowledge/taxonomy/stroke-taxonomy.yaml`
  - Define stroke and movement categories.
- Create: `knowledge/schema/tennis-data-system-schema.yaml`
  - Define evidence, observation, assessment, experiment, knowledge item, and program focus records.
- Create: `docs/architecture/data-strategy.md`
  - Explain source of truth, data lifecycle, storage policy, privacy policy, and migration strategy.
- Create: `docs/architecture/experiment-protocol.md`
  - Define how learning experiments are proposed, run, reviewed, and promoted.
- Create: `experiments/README.md`
  - Add shared experiment rules for learner-specific experiment folders.
- Modify: `experiments/cindy/README.md`
  - Align Cindy experiments with the shared protocol.
- Modify: `experiments/mickey/README.md`
  - Align Mickey experiments with the shared protocol.
- Create: `docs/architecture/repository-convention.md`
  - Define naming, language, file placement, commits, evidence references, and review cadence.

## Task 1: Create Milestone Charter And Gate

**Files:**
- Create: `docs/milestones/2026-06-30-foundation.md`
- Modify: `README.md`
- Modify: `ROADMAP.md`
- Create: `docs/decisions/2026-06-30-milestone-0-foundation-gate.md`

- [ ] **Step 1: Create milestone directory**

Run:

```bash
mkdir -p docs/milestones
```

Expected: `docs/milestones/` exists.

- [ ] **Step 2: Create milestone charter**

Create `docs/milestones/2026-06-30-foundation.md` with this structure and content:

```markdown
# Milestone 0: Foundation

Date: 2026-06-30

Duration: 1-2 weeks

Status: Active

## Purpose

Milestone 0 exists to make Cindy Tennis Lab ready for long-term iteration before
any Agent implementation begins.

The goal is not to write Agent code. The goal is to make the foundation clear
enough that future Agents can work inside a stable learning system.

## Modules

| Module | Status | Output |
| --- | --- | --- |
| Vision | Complete | Mission, vision, manifesto, why, and principles are linked from `README.md`. |
| Architecture | Complete | System overview, repository structure, and workflow exist under `docs/architecture/`. |
| Knowledge Graph Schema | In progress | Graph node and edge schema under `knowledge/schema/`. |
| Data Strategy | In progress | Evidence-to-knowledge strategy under `docs/architecture/`. |
| Experiment Protocol | In progress | Experiment lifecycle and review rules under `docs/architecture/`. |
| Repository Convention | In progress | Naming, placement, commit, and review conventions under `docs/architecture/`. |

## Completion Criteria

Milestone 0 is complete when:

- the six modules above have durable repository files
- every module is linked from `README.md`
- schema and taxonomy files have stable IDs and allowed values
- experiment work has an explicit protocol
- repository conventions make file placement and naming decisions clear
- `python3 harness/scripts/validate_harness.py` passes
- `git diff --check` passes

## Agent Gate

Agent work starts only after Milestone 0 is complete.

Before that point, AI assistance should focus on foundation design, schemas,
records, experiments, and documentation.

## Non-Goals

Milestone 0 does not build:

- Agent code
- dashboards
- databases
- automation services
- video processing pipelines
- public-facing websites
```

- [ ] **Step 3: Link milestone from README**

Modify `README.md` in the "Start here" list by adding:

```markdown
- [docs/milestones/2026-06-30-foundation.md](docs/milestones/2026-06-30-foundation.md)
```

Place it before `VISION.md` so the active milestone is the first navigation step.

- [ ] **Step 4: Add Milestone 0 to roadmap**

Modify `ROADMAP.md` by adding this section before `## v0.1 Foundation`:

```markdown
## Milestone 0: Foundation Gate

Milestone 0 turns the first foundation work into an explicit readiness gate
before Agent implementation.

Required modules:

- Vision
- Architecture
- Knowledge Graph Schema
- Data Strategy
- Experiment Protocol
- Repository Convention

Agent work begins only after these modules are complete and linked.
```

- [ ] **Step 5: Record the foundation gate decision**

Create `docs/decisions/2026-06-30-milestone-0-foundation-gate.md`:

```markdown
# Decision: Milestone 0 Foundation Gate

Date: 2026-06-30

## Decision

Cindy Tennis Lab will establish Milestone 0 as a foundation gate before building
Agents.

## Context

The repository already has mission, architecture, skills, and an initial data
system design. The next risk is moving into Agent implementation before the
knowledge graph, data strategy, experiment protocol, and repository conventions
are stable enough.

## Consequences

Agent work is deferred until Milestone 0 is complete.

The near-term work should produce durable documentation and schemas:

- Vision
- Architecture
- Knowledge Graph Schema
- Data Strategy
- Experiment Protocol
- Repository Convention

Future Agent plans should cite this decision and the milestone charter.
```

- [ ] **Step 6: Verify Task 1**

Run:

```bash
git diff --check
```

Expected: no output.

- [ ] **Step 7: Commit Task 1**

Run:

```bash
git add README.md ROADMAP.md docs/milestones/2026-06-30-foundation.md docs/decisions/2026-06-30-milestone-0-foundation-gate.md
git commit -m "docs: establish milestone 0 foundation gate"
```

Expected: commit succeeds.

## Task 2: Refresh Architecture Around Milestone 0

**Files:**
- Modify: `docs/architecture/system-overview.md`
- Modify: `docs/architecture/repository-structure.md`
- Modify: `docs/architecture/workflow.md`

- [ ] **Step 1: Update system overview with foundation readiness**

Modify `docs/architecture/system-overview.md` after `## System Layers` by adding:

```markdown
### Milestone 0 Readiness

Milestone 0 is the readiness layer before Agent implementation.

It requires six modules to be explicit and linked:

- Vision
- Architecture
- Knowledge Graph Schema
- Data Strategy
- Experiment Protocol
- Repository Convention

Agent work should not begin until these modules have durable repository files
and clear review rules.
```

- [ ] **Step 2: Add learning data architecture to system overview**

Modify `docs/architecture/system-overview.md` before `## Feedback Loop` by adding:

```markdown
### Learning Data System

The long-term data system has six layers:

1. Evidence: source material such as videos, frame sheets, coach feedback,
   match notes, practice notes, and health notes.
2. Observation: claims extracted from evidence with confidence and limitations.
3. Assessment: scores, measurements, and review metrics.
4. Experiment: time-bound learning tests with hypotheses and review dates.
5. Knowledge: reusable concepts promoted only after review.
6. Program: learner-specific pathways that change based on evidence.
```

- [ ] **Step 3: Update repository structure for milestones and taxonomy**

Modify the folder map in `docs/architecture/repository-structure.md` so it includes:

```text
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── milestones/
│   └── superpowers/
├── knowledge/
│   ├── schema/
│   ├── taxonomy/
│   ├── ontology/
│   └── concepts/
```

- [ ] **Step 4: Add milestones section to repository structure**

Add this section after `## Docs`:

```markdown
## Milestones

`docs/milestones/` stores active milestone charters and completion criteria.

A milestone answers: what must be true before the project moves to the next
stage?
```

- [ ] **Step 5: Expand knowledge section**

Modify the `## Knowledge` section in `docs/architecture/repository-structure.md`
so it includes:

```markdown
`knowledge/schema/` defines data structures. `knowledge/taxonomy/` defines
allowed values. `knowledge/ontology/` defines tennis domains such as serve,
footwork, and match play. `knowledge/concepts/` stores cross-cutting ideas such
as biomechanics, tactics, mental game, and injury prevention.
```

- [ ] **Step 6: Update workflow with milestone gate**

Modify `docs/architecture/workflow.md` before `## Issue Flow` by adding:

```markdown
## Milestone Flow

1. Choose the active milestone.
2. Define the milestone completion criteria.
3. Create or update the milestone charter.
4. Complete the required modules.
5. Run repository validation.
6. Record the milestone decision.
7. Move to issue-level execution only after the milestone gate is satisfied.
```

- [ ] **Step 7: Verify Task 2**

Run:

```bash
git diff --check
```

Expected: no output.

- [ ] **Step 8: Commit Task 2**

Run:

```bash
git add docs/architecture/system-overview.md docs/architecture/repository-structure.md docs/architecture/workflow.md
git commit -m "docs: align architecture with milestone 0"
```

Expected: commit succeeds.

## Task 3: Define Knowledge Graph Schema

**Files:**
- Create: `knowledge/schema/knowledge-graph-schema.yaml`
- Modify: `knowledge/schema/tennis-knowledge-schema.yaml`
- Create: `knowledge/taxonomy/stroke-taxonomy.yaml`

- [ ] **Step 1: Create taxonomy directory**

Run:

```bash
mkdir -p knowledge/taxonomy
```

Expected: `knowledge/taxonomy/` exists.

- [ ] **Step 2: Create knowledge graph schema**

Create `knowledge/schema/knowledge-graph-schema.yaml`:

```yaml
schema:
  name: knowledge-graph-schema
  version: 0.1.0
  purpose: >
    Define how Cindy Tennis Lab connects learners, evidence, observations,
    assessments, experiments, knowledge items, and program decisions.

id_rules:
  format: namespace:learner_or_domain:date_or_scope:slug
  examples:
    - evidence:cindy:2026-05:match-video-0004
    - observation:cindy:2026-05:serve-recovery-slow
    - assessment:cindy:2026-05:stroke-baseline
    - experiment:cindy:2026-06:fixed-serve-routine
    - knowledge:serve:fixed-routine-before-power
  rules:
    - Use lowercase English slugs.
    - Keep Chinese in titles and notes, not IDs.
    - Never reuse an ID for a different meaning.

node_types:
  learner:
    required_fields:
      - id
      - name
      - profile
      - long_term_goal
  evidence:
    required_fields:
      - id
      - learner_id
      - date
      - type
      - title
      - path_or_reference
      - privacy_level
  observation:
    required_fields:
      - id
      - learner_id
      - date
      - category
      - statement
      - evidence_ids
      - confidence
      - limitations
  assessment:
    required_fields:
      - id
      - learner_id
      - date
      - metric
      - value
      - scale
      - evidence_ids
  experiment:
    required_fields:
      - id
      - learner_id
      - start_date
      - end_date
      - question
      - hypothesis
      - primary_metric
      - review_status
  knowledge_item:
    required_fields:
      - id
      - title
      - category
      - evidence_ids
      - observation_ids
      - promotion_reason
  program_focus:
    required_fields:
      - id
      - learner_id
      - time_window
      - focus
      - source_ids

edge_types:
  derived_from:
    from:
      - observation
      - assessment
    to:
      - evidence
  supports:
    from:
      - evidence
      - observation
      - assessment
    to:
      - hypothesis
      - knowledge_item
      - program_focus
  tests:
    from:
      - experiment
    to:
      - hypothesis
      - observation
  promotes_to:
    from:
      - observation
      - experiment
    to:
      - knowledge_item
  informs:
    from:
      - knowledge_item
      - assessment
      - experiment
    to:
      - program_focus

promotion_rules:
  observation_to_knowledge:
    allowed_when:
      - repeated_across_evidence
      - confirmed_by_coach
      - validated_by_experiment
      - required_as_safety_guardrail
    required_fields:
      - promotion_reason
      - evidence_ids
      - last_reviewed
```

- [ ] **Step 3: Link graph schema from existing tennis schema**

Modify `knowledge/schema/tennis-knowledge-schema.yaml` under `schema:` by adding:

```yaml
  related_schemas:
    - knowledge-graph-schema
```

Then add these optional fields under `knowledge_item.fields`:

```yaml
    evidence_ids:
      type: array
      items:
        type: string
      description: Evidence ids supporting this item.
    observation_ids:
      type: array
      items:
        type: string
      description: Observation ids promoted into this item.
    experiment_ids:
      type: array
      items:
        type: string
      description: Experiment ids that tested this item.
    promotion_reason:
      type: string
      description: Why this item is stable enough to become reusable knowledge.
    last_reviewed:
      type: string
      format: date
      description: Last date this item was reviewed.
```

- [ ] **Step 4: Create stroke taxonomy**

Create `knowledge/taxonomy/stroke-taxonomy.yaml`:

```yaml
taxonomy:
  name: stroke-taxonomy
  version: 0.1.0

stroke_groups:
  serve:
    items:
      - first_serve
      - second_serve
      - serve_plus_one
  return:
    items:
      - first_serve_return
      - second_serve_return
      - return_plus_one
  baseline:
    items:
      - forehand_neutral
      - forehand_open
      - backhand_neutral
      - backhand_open
  net:
    items:
      - forehand_volley
      - backhand_volley
      - overhead
  movement:
    items:
      - split_step
      - first_step
      - recovery_step
      - outside_foot_brake
      - ready_position

development_notes:
  cindy:
    current_stage: age_9_to_10_action_models
    principle: Stabilize movement quality before chasing speed.
```

- [ ] **Step 5: Verify Task 3**

Run:

```bash
python3 harness/scripts/validate_harness.py
git diff --check
```

Expected:

```text
Harness validation passed.
```

`git diff --check` produces no output.

- [ ] **Step 6: Commit Task 3**

Run:

```bash
git add knowledge/schema/knowledge-graph-schema.yaml knowledge/schema/tennis-knowledge-schema.yaml knowledge/taxonomy/stroke-taxonomy.yaml
git commit -m "docs: define knowledge graph schema"
```

Expected: commit succeeds.

## Task 4: Define Data Strategy

**Files:**
- Create: `knowledge/schema/tennis-data-system-schema.yaml`
- Create: `knowledge/taxonomy/evidence-taxonomy.yaml`
- Create: `knowledge/taxonomy/metric-taxonomy.yaml`
- Create: `docs/architecture/data-strategy.md`

- [ ] **Step 1: Create data system schema**

Create `knowledge/schema/tennis-data-system-schema.yaml`:

```yaml
schema:
  name: tennis-data-system-schema
  version: 0.1.0
  purpose: >
    Define Git-native records for evidence, observations, assessments,
    experiments, knowledge items, and program decisions.

record_types:
  evidence_item:
    required_fields:
      - id
      - learner_id
      - date
      - type
      - title
      - path_or_reference
      - source_context
      - privacy_level
      - notes
  observation:
    required_fields:
      - id
      - learner_id
      - date
      - category
      - statement
      - evidence_ids
      - confidence
      - limitations
      - hypothesis
      - suggested_next_action
      - review_status
  assessment_metric:
    required_fields:
      - id
      - learner_id
      - date
      - cycle
      - metric
      - value
      - scale
      - context
      - evidence_ids
      - reviewer
      - notes
  experiment:
    required_fields:
      - id
      - learner_id
      - start_date
      - end_date
      - question
      - hypothesis
      - intervention
      - primary_metric
      - supporting_metrics
      - stop_conditions
      - evidence_plan
      - review_result
      - next_decision
  program_focus:
    required_fields:
      - id
      - learner_id
      - time_window
      - focus
      - evidence_ids
      - decision
      - next_review_date

storage_policy:
  source_of_truth:
    - Markdown for narrative records.
    - YAML for structured indexes and schemas.
    - CSV for tabular tracking.
  large_files:
    policy: Index large videos by path or external reference instead of copying them into Git by default.
  privacy:
    policy: Store the minimum personal detail needed for learning and review.
```

- [ ] **Step 2: Create evidence taxonomy**

Create `knowledge/taxonomy/evidence-taxonomy.yaml`:

```yaml
taxonomy:
  name: evidence-taxonomy
  version: 0.1.0

evidence_types:
  - video
  - frame_sheet
  - match_note
  - practice_note
  - coach_feedback
  - analysis_doc
  - health_note
  - report
  - photo
  - other

privacy_levels:
  - public_safe
  - family_private
  - medical_sensitive
  - child_sensitive

confidence_levels:
  - low
  - medium
  - high

review_statuses:
  - captured
  - reviewed
  - needs_evidence
  - promoted
  - retired
```

- [ ] **Step 3: Create metric taxonomy**

Create `knowledge/taxonomy/metric-taxonomy.yaml`:

```yaml
taxonomy:
  name: metric-taxonomy
  version: 0.1.0

metric_families:
  stroke:
    scale: 1-5
    metrics:
      - technical_stability
      - ball_quality_placement
      - tactical_execution
      - match_transfer
  health:
    scale: mixed
    metrics:
      - foot_pain_0_10
      - pain_limited_yes_no
      - sleep_consistency
      - nutrition_support
      - rehab_completion
  serve:
    scale: mixed
    metrics:
      - toss_score_0_100
      - side_on_score_0_100
      - trophy_score_0_100
      - leg_drive_score_0_100
      - contact_score_0_100
      - follow_through_score_0_100
      - first_serve_in_0_20
      - second_serve_in_0_20
  practice_load:
    scale: mixed
    metrics:
      - weekly_tennis_hours
      - weekly_rehab_sessions
      - high_impact_exposure
```

- [ ] **Step 4: Create data strategy document**

Create `docs/architecture/data-strategy.md`:

```markdown
# Data Strategy

Cindy Tennis Lab uses Git-native data first.

## Source Of Truth

Markdown, YAML, and CSV files are the source of truth during Milestone 0 and the
early knowledge-capture phase.

## Data Lifecycle

1. Evidence is captured or indexed.
2. Observations are extracted from evidence.
3. Assessments measure selected signals.
4. Experiments test one hypothesis at a time.
5. Knowledge is promoted only after review.
6. Program decisions are updated from evidence, assessments, and experiments.

## Storage Policy

Large videos are indexed by path or external reference. They are not copied into
Git by default.

Small documents, schemas, taxonomies, reports, and indexes belong in Git.

## Privacy Policy

Child, medical, school, and family-sensitive records should use conservative
metadata and avoid unnecessary personal detail.

## Initial Migration

The first migration target is Cindy's 2026-05 baseline:

- parent-workspace analysis documents
- DJI match videos
- close-up training videos
- derived frame sheets
- stroke tracking CSV

The migration should create evidence indexes, observations, assessments, and a
monthly summary without duplicating large videos.

## Future Export

When Git-native files stabilize, they may be imported into SQLite, dashboards,
search indexes, vector retrieval, or graph views.
```

- [ ] **Step 5: Verify Task 4**

Run:

```bash
python3 harness/scripts/validate_harness.py
git diff --check
```

Expected:

```text
Harness validation passed.
```

`git diff --check` produces no output.

- [ ] **Step 6: Commit Task 4**

Run:

```bash
git add knowledge/schema/tennis-data-system-schema.yaml knowledge/taxonomy/evidence-taxonomy.yaml knowledge/taxonomy/metric-taxonomy.yaml docs/architecture/data-strategy.md
git commit -m "docs: define data strategy"
```

Expected: commit succeeds.

## Task 5: Define Experiment Protocol

**Files:**
- Create: `docs/architecture/experiment-protocol.md`
- Create: `experiments/README.md`
- Modify: `experiments/cindy/README.md`
- Modify: `experiments/mickey/README.md`

- [ ] **Step 1: Create experiment protocol document**

Create `docs/architecture/experiment-protocol.md`:

```markdown
# Experiment Protocol

Experiments turn learning ideas into testable cycles.

## Principle

One experiment should test one hypothesis with one primary metric.

## Experiment Lifecycle

1. Question: what are we trying to understand?
2. Hypothesis: what do we think is happening?
3. Intervention: what will change for the cycle?
4. Evidence plan: what will be recorded?
5. Primary metric: how will we judge progress?
6. Stop conditions: what makes the experiment unsafe or unhelpful?
7. Review: what happened?
8. Decision: continue, revise, promote, or retire.

## Required Fields

- id
- learner_id
- start_date
- end_date
- question
- hypothesis
- intervention
- primary_metric
- supporting_metrics
- stop_conditions
- evidence_plan
- review_result
- next_decision

## Cindy Health Guardrails

Pain above 3/10 limits high-impact conclusions.

Pain above 5/10, limping, morning heel pain, or refusal to run should stop
high-impact tennis experiments and trigger health-first review.

## Promotion Rule

An experiment can promote a pattern into knowledge only when the result is
supported by evidence and the review decision says `promote`.
```

- [ ] **Step 2: Create experiments root README**

Create `experiments/README.md`:

```markdown
# Experiments

Experiments are learner-specific tests.

Use experiments when the lab needs to test a hypothesis before promoting it to
program guidance or reusable knowledge.

Start with:

- [docs/architecture/experiment-protocol.md](../docs/architecture/experiment-protocol.md)
- [cindy/README.md](cindy/README.md)
- [mickey/README.md](mickey/README.md)
```

- [ ] **Step 3: Update Cindy experiment README**

Modify `experiments/cindy/README.md` by adding this section:

```markdown
## Protocol

Cindy experiments must follow the shared experiment protocol.

Health signals are part of the experiment data. Pain, sleep, recovery, and
training load should be recorded when they affect the result.

No Cindy experiment should chase performance at the expense of long-term health
or love for tennis.
```

- [ ] **Step 4: Update Mickey experiment README**

Modify `experiments/mickey/README.md` by adding this section:

```markdown
## Protocol

Mickey experiments must follow the shared experiment protocol.

Adult learning experiments should separate feel, video evidence, match outcome,
and practice consistency.
```

- [ ] **Step 5: Verify Task 5**

Run:

```bash
git diff --check
```

Expected: no output.

- [ ] **Step 6: Commit Task 5**

Run:

```bash
git add docs/architecture/experiment-protocol.md experiments/README.md experiments/cindy/README.md experiments/mickey/README.md
git commit -m "docs: define experiment protocol"
```

Expected: commit succeeds.

## Task 6: Define Repository Convention

**Files:**
- Create: `docs/architecture/repository-convention.md`
- Modify: `README.md`
- Modify: `docs/architecture/repository-structure.md`
- Modify: `docs/architecture/workflow.md`

- [ ] **Step 1: Create repository convention document**

Create `docs/architecture/repository-convention.md`:

```markdown
# Repository Convention

Cindy Tennis Lab grows through small, reviewable repository changes.

## Naming

Use lowercase English slugs for IDs and file names.

Chinese is welcome in titles, notes, reports, and learner-facing documents.

## File Placement

- Foundation ideas go in `foundation/`.
- Architecture, workflow, milestones, and decisions go in `docs/`.
- Stable reusable tennis knowledge goes in `knowledge/`.
- Learner pathways go in `programs/`.
- Applied research goes in `labs/`.
- Real learner evidence and reports go in `records/`.
- Hypothesis tests go in `experiments/`.
- Chronological reflection goes in `journal/`.

## Commits

Use one goal, one output, one commit.

Prefer commit messages such as:

- `docs: establish milestone 0 foundation gate`
- `docs: define data strategy`
- `docs: define experiment protocol`
- `docs: migrate cindy 2026-05 baseline`

## Evidence References

Use stable evidence IDs when a conclusion depends on source material.

Do not cite memory when a file, video, frame sheet, note, or report exists.

## Promotion

Records and observations can be messy.

Knowledge should be promoted only when evidence, coach feedback, experiment
results, or safety guardrails support it.
```

- [ ] **Step 2: Link convention from README**

Add this entry to the README "Start here" list:

```markdown
- [docs/architecture/repository-convention.md](docs/architecture/repository-convention.md)
```

- [ ] **Step 3: Link convention from repository structure**

Add this sentence under `## Docs` in `docs/architecture/repository-structure.md`:

```markdown
`docs/architecture/repository-convention.md` defines naming, file placement,
commit, evidence reference, and promotion rules.
```

- [ ] **Step 4: Link convention from workflow**

Add this sentence after the opening paragraph in `docs/architecture/workflow.md`:

```markdown
Repository work should follow
`docs/architecture/repository-convention.md`.
```

- [ ] **Step 5: Verify Task 6**

Run:

```bash
git diff --check
```

Expected: no output.

- [ ] **Step 6: Commit Task 6**

Run:

```bash
git add docs/architecture/repository-convention.md README.md docs/architecture/repository-structure.md docs/architecture/workflow.md
git commit -m "docs: define repository convention"
```

Expected: commit succeeds.

## Task 7: Final Milestone 0 Readiness Review

**Files:**
- Modify: `docs/milestones/2026-06-30-foundation.md`

- [ ] **Step 1: Update milestone module statuses**

Modify the module table in `docs/milestones/2026-06-30-foundation.md` so every
module status is `Complete` after Tasks 1-6 are committed:

```markdown
| Module | Status | Output |
| --- | --- | --- |
| Vision | Complete | Mission, vision, manifesto, why, and principles are linked from `README.md`. |
| Architecture | Complete | System overview, repository structure, and workflow exist under `docs/architecture/`. |
| Knowledge Graph Schema | Complete | Graph node and edge schema under `knowledge/schema/`. |
| Data Strategy | Complete | Evidence-to-knowledge strategy under `docs/architecture/`. |
| Experiment Protocol | Complete | Experiment lifecycle and review rules under `docs/architecture/`. |
| Repository Convention | Complete | Naming, placement, commit, and review conventions under `docs/architecture/`. |
```

- [ ] **Step 2: Add completion note**

Add this section before `## Non-Goals`:

```markdown
## Completion Review

Milestone 0 is complete when the module table above is complete and repository
validation passes.

The next milestone may begin planning Agent work only by referencing:

- this milestone charter
- the knowledge graph schema
- the data strategy
- the experiment protocol
- the repository convention
```

- [ ] **Step 3: Run final validation**

Run:

```bash
python3 harness/scripts/validate_harness.py
git diff --check
git status --short
```

Expected:

```text
Harness validation passed.
```

`git diff --check` produces no output.

`git status --short` shows only `docs/milestones/2026-06-30-foundation.md` as modified before the final commit.

- [ ] **Step 4: Commit final milestone review**

Run:

```bash
git add docs/milestones/2026-06-30-foundation.md
git commit -m "docs: complete milestone 0 foundation review"
```

Expected: commit succeeds.

## Plan Self-Review

Spec coverage:

- Vision is covered by Task 1 through milestone charter links and completion criteria.
- Architecture is covered by Task 2.
- Knowledge Graph Schema is covered by Task 3.
- Data Strategy is covered by Task 4.
- Experiment Protocol is covered by Task 5.
- Repository Convention is covered by Task 6.
- The Agent gate is covered by Tasks 1 and 7.

Validation coverage:

- `git diff --check` is run after every task.
- `python3 harness/scripts/validate_harness.py` is run after schema/data tasks and final review.
- Every task ends with a focused commit.

Execution rule:

- Do not start Agent implementation during this plan.
- After this plan is complete, create a separate plan for the first Agent milestone.
