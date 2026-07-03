# Claims

Claims are the smallest useful units extracted from sources.

Cindy Tennis Lab does not collect sources for their own sake. It extracts
claims, links them to source IDs, maps them to knowledge graph nodes, and tests
them through experiments or own data.

## Claim Schema

```yaml
claim_id:
statement:
source_id:
source_tier:
domain:
skill:
evidence_type:
confidence:
validation_needed:
applicable_age:
related_nodes:
notes:
```

## Rules

- A claim is not automatically true.
- A private source can contribute claims, but not raw copyrighted text.
- T3 practice frameworks need validation before becoming knowledge.
- T0 own data is highest value, but still needs careful interpretation.
- Knowledge is promoted only after review.

## Reviews

Claim review results live under `knowledge/claims/reviews/`.

Review decisions decide whether a claim should be promoted to knowledge, tested
through an experiment, kept as a research direction, or deferred.
