# Serve Physics

Physics describes what the ball must do.

## Core Variables

| Variable | Meaning | Why It Matters |
| --- | --- | --- |
| Trajectory | Ball path over the net into the service box | Determines margin and target shape |
| Speed | Ball velocity | Useful only when control and recovery remain stable |
| Spin | Ball rotation | Helps margin, shape, and control |
| Launch angle | Initial direction after contact | Affects net clearance and depth |
| Contact height | Height of impact point | Changes available angle into the box |
| Placement | Target zone inside the box | Connects serve to point construction |

## Serve Physics Claims

- A serve needs enough net clearance and box depth before speed matters.
- Serve speed without repeatability is not yet a useful skill metric.
- Spin and trajectory can create safety margin before power is stable.
- Placement should eventually connect to serve-plus-one decisions.

## Inputs

- video
- ball landing location
- first serve count
- second serve count
- target zone
- contact estimate

## Outputs

- ball flight model
- target-zone map
- margin assessment
- metrics for serve review

## Related Nodes

- Skill
- Metrics
- Experiment
