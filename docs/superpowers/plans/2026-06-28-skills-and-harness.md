# Skills And Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add repository-level AI skills and a lightweight validation harness so Cindy Tennis Lab can turn recurring tennis-learning work into repeatable workflows.

**Architecture:** Store human-readable skill instructions under `skills/`, test fixtures and rubrics under `harness/`, and a dependency-free Python validator under `harness/scripts/`. Link the new surfaces from `README.md` and `docs/architecture/repository-structure.md`.

**Tech Stack:** Markdown, YAML-like fixtures, Python standard library, Git.

---

### Task 1: Add Core AI Skills

**Files:**
- Create: `skills/README.md`
- Create: `skills/serve-video-review/SKILL.md`
- Create: `skills/monthly-growth-report/SKILL.md`
- Create: `skills/practice-plan/SKILL.md`
- Create: `skills/match-review/SKILL.md`
- Create: `skills/knowledge-capture/SKILL.md`

- [ ] **Step 1: Define skill index**

Document when each skill should be used and how skills connect to labs, programs, and records.

- [ ] **Step 2: Define five first skills**

Each skill needs frontmatter, trigger guidance, inputs, workflow, output format, and guardrails.

### Task 2: Add Harness Fixtures And Rubric

**Files:**
- Create: `harness/README.md`
- Create: `harness/cases/serve-video-review.yaml`
- Create: `harness/cases/monthly-growth-report.yaml`
- Create: `harness/cases/practice-plan.yaml`
- Create: `harness/rubrics/ai-output-rubric.yaml`

- [ ] **Step 1: Add harness README**

Explain that the harness checks structure and evaluation readiness, not model correctness.

- [ ] **Step 2: Add cases and rubric**

Define three starter cases and one shared rubric for evidence, clarity, safety, and next action quality.

### Task 3: Add Validation Script

**Files:**
- Create: `harness/scripts/validate_harness.py`
- Modify: `README.md`
- Modify: `docs/architecture/repository-structure.md`

- [ ] **Step 1: Add validator**

Use only Python standard library. Validate required skill frontmatter, required skill sections, required harness case fields, and required rubric fields.

- [ ] **Step 2: Link docs**

Add `skills/` and `harness/` to project entry points and repository structure.

- [ ] **Step 3: Verify**

Run `python3 harness/scripts/validate_harness.py`. Expected output: `Harness validation passed.`
