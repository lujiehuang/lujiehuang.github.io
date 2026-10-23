# Lightweight Prioritization Logic

This skill is intentionally not a rigid numerical optimizer, but the following score can be used when several tasks compete.

## Suggested score

```text
priority =
  3 × urgency
+ 3 × importance
+ 2 × controllability
+ 1 × unlocks_other_tasks
- 2 × dependency_on_others
- 1 × effort
```

Use a 0–2 scale for each factor.

The score is only a tie-breaker. Do not present fake precision to users.

## Override rules

A task can override the score if:

- it has a hard deadline within hours;
- delaying it causes irreversible harm;
- it is a safety / health matter;
- it unlocks several other tasks.

## Anti-anxiety rule

If an item is **important but not actionable**, explicitly remove it from the "do now" list.

Examples:
- waiting for a professor to reply;
- waiting for a journal decision;
- waiting for an interview result;
- worrying about an event months away with no action available today.

The skill should name these as "waiting" rather than treating them as tasks.
