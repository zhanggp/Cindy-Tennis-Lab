# Issue #004: Video Annotation

## Why

Video is a primary evidence source. The project needs a simple annotation model
before building any video recognition or AI review workflow.

## Scope

Define video annotation fields for:

- learner
- date
- source file
- clip time range
- camera angle
- observation
- evidence confidence
- next question

## Non-Scope

This issue does not include computer vision, automatic detection, or UI.

## Definition Of Done

- Annotation template is reviewed against `labs/video-analysis-lab/`.
- Annotation records can link to evidence IDs.
- Limitations and camera-angle quality are represented.
