# Harness

The harness provides lightweight evaluation structure for Cindy Tennis Lab
skills.

It does not prove that an AI answer is technically correct. It checks whether
skills and cases are structured enough to review consistently.

## Contents

- `cases/`: example tasks for skills.
- `rubrics/`: shared evaluation criteria.
- `scripts/validate_harness.py`: dependency-free structure validator.

## Run

```bash
python3 harness/scripts/validate_harness.py
```

Expected output:

```text
Harness validation passed.
```

## Evaluation Principle

Good AI output should be evidence-aware, concise, safe, learner-centered, and
clear about one next action.
