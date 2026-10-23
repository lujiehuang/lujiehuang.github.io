# NextStep

**Turn overwhelm into one clear next action.**

NextStep is a small decision-support skill for moments when everything feels urgent and you do not know what to do first.

It is not therapy, diagnosis, or crisis care. It does one practical thing:

> Reduce cognitive overload by turning a messy list of worries and tasks into one concrete next action.

## What it does

Given a list of things on your mind, NextStep:

1. separates **controllable** from **uncontrollable** items;
2. groups tasks into **now / today / this week / later**;
3. estimates urgency, importance, effort, dependency, and reversibility;
4. identifies the **single best next action**;
5. gives one short backup step for what to do afterward;
6. explicitly parks items that do not require attention yet.

## Output format

The default output is intentionally short:

- **Do now:** one action
- **Why:** one or two reasons
- **Ignore for now:** things that are not actionable yet
- **Then:** the next action after completion

## Example

Input:

> I need to prepare for a PhD meeting, revise a paper, apply for jobs, and I keep worrying that several professors have not replied.

Output:

> **Do now:** Draft the 5-minute introduction for the meeting that happens first.  
> **Why:** It is time-sensitive, high-impact, and fully controllable.  
> **Ignore for now:** Whether professors reply today — that is not currently controllable.  
> **Then:** Answer the three questions requested by the next supervisor.

## Core principle

> Anxiety often grows when too many open loops compete for attention. NextStep does not try to solve everything. It closes one loop at a time.

## Safety boundary

If the user expresses imminent danger, self-harm intent, or inability to stay safe, stop the prioritization workflow and encourage immediate human support / emergency help instead of continuing task optimization.

## Files

- `SKILL.md` — reusable instructions
- `scoring.md` — lightweight prioritization logic
- `examples/` — example inputs and outputs
- `templates/` — minimal response templates

## Author

Lujie Huang  
https://lujiehuang.github.io/
