# Serve Sources

Serve Ontology v0.1 should be built from registered sources, not memory.

The flow is:

```text
Source
->
Claim
->
Serve Node
->
Experiment
->
Validation
```

## Source Coverage

| Source Type | Registry Examples | Tier | Role |
| --- | --- | --- | --- |
| Own data | `mickey_training_data`, `cindy_training_data` | T0 | Highest-value validation data |
| Scientific paper | `tennis_stroke_biomechanics_mediapipe_pose` | T1 | Research direction for pose and biomechanics metrics |
| Official system | `usta_coaching`, `world_tennis_itf` | T2 | Coaching standards, safety, and development context |
| Ebook/framework | `skills_of_a_tennis_athlete` | T3 | Practice framework and skill taxonomy inspiration |
| YouTube coaching | `essential_tennis_youtube`, `top_tennis_training_youtube`, `feel_tennis_youtube`, `intuitive_tennis_youtube` | T3 | Coaching practice claims that need validation |
| Professional case | `djokovic_serve_case`, `zhang_zhizhen_serve_case` | T4 | High-level implementation examples |

## Rules

- Do not commit raw copyrighted source material.
- Do not treat T3 coaching practice as scientific proof.
- Do not treat professional players as standard answers.
- Extract claims first, then decide whether they belong in the Serve model.
- Promote only claims that survive evidence review or experiment.

## Initial Serve Claim Targets

The first extraction pass should look for claims about:

- serve efficiency versus speed
- toss repeatability
- side-on body shape
- upward drive
- relaxed swing
- balanced landing
- recovery into the next ball
- serve metrics

## Related Files

- `sources/registry.yaml`
- `knowledge/claims/serve.yaml`
- `knowledge/schema/tennis-knowledge-graph-v0.1.yaml`
