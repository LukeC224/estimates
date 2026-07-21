# Lessons

Corrections from reviewed estimates. Read before starting a takeoff.

Each lesson names the **cue in the drawings** that should have triggered it, not just the
thing that was missed — a lesson only helps if it fires at the right moment.

Format:

```
## <short title>
**Job:** <project> · **Date:** <yyyy-mm-dd> · **Type:** bad rate | missing scope | wrong quantity | wrong assumption
**Cue:** what in the drawings should have triggered this
**Lesson:** what to do
```

---

## Reference lessons from prior jobs

These are drawn from the two source projects rather than from a reviewed estimate. They
carry the same weight.

## HVAC scope can be missed entirely, not merely underpriced
**Job:** 1988 Ogden Ave · **Type:** missing scope
**Cue:** A mechanical scope stated only as "HVAC — heating cooling" with no equipment
schedule, no duct layout and no load calculation.
**Lesson:** Ogden carried $5,600 originally against a $120,580 revised budget. That is not
escalation or scope creep — the original number priced something far smaller than the job.
When a drawing set has no mechanical design, do not price mechanical from a plan reading.
Carry a P.C. sized from a comparable completed project and say plainly that no mechanical
design exists.

## A large change-order count means the estimate was priced against an incomplete scope
**Job:** 1988 Ogden Ave · **Type:** wrong assumption
**Cue:** Original estimate $506,371.74; final invoiced $1,459,487.83 across 68 change orders.
**Lesson:** Do not read this as "multiply by 2.9". Most of the delta was scope that did not
exist at estimate time. The correct response is to establish at the outset how completely the
scope is defined, and to say so in the estimate. An estimate against a permit set is not the
same product as an estimate against a construction set, and should not be presented as
though it were.

## Div 8 carries no labour
**Job:** 2033 E. 7 · **Type:** wrong assumption
**Cue:** A window and door schedule with supply pricing.
**Lesson:** Doors and windows are supply-only in Div 8. Installation hours belong in 6.9 and
hardware installation in 6.10. Putting install labour in Div 8 double-counts once the budget
is exported to Sage.

## Every subtrade line still carries GC coordination cost
**Job:** 2033 E. 7 · **Type:** missing scope
**Cue:** Any line where the rate is a sub's supply-and-install price.
**Lesson:** Book one interface hour per subtrade line. It looks trivial per line and is not
in aggregate — Div 16 on 2033 E. 7 was a pure $125,000 P.C. and still carried $5,456.59 of
coordination labour. Zero coordination hours on a subbed division is always wrong.

## The blended labour rate hides a dependency on the schedule
**Job:** 2033 E. 7 · **Type:** wrong assumption
**Cue:** Any change to assumed project duration.
**Lesson:** The blended crew rate is weighted across the calendar years the programme spans,
so changing months-to-complete reprices all labour with no visible edit anywhere. Recompute
the blend whenever the schedule moves, and re-verify the labour total afterwards.

## A permit set is not a construction set
**Job:** 2033 E. 7 · **Type:** wrong assumption
**Cue:** Drawing list with no structural, no MEP, no finish schedule, no millwork elevations.
**Lesson:** Envelope, openings, assemblies and areas can be taken off properly. Interiors,
services and structure cannot, and must be carried as P.C. allowances with the gap stated.
An estimate that prices these as though they were designed is presenting guesses as takeoff.

## Check the project number against the street address
**Job:** 2033 E. 7 · **Type:** wrong assumption
**Cue:** A file or estimate named for a number that does not match the drawing title block.
**Lesson:** "2033 E. 7" is VFA's project number 2033 for a site at **2212 E 7th Ave**. The
estimate workbook is named for the project number. Read the address off the title block, not
off the filename.

## Verify the drawing issue against the estimate date
**Job:** 2033 E. 7 · **Type:** wrong assumption
**Cue:** Any estimate where the drawing set's issue date is unknown or older than the work.
**Lesson:** That estimate is dated 2024-04-17; the permit set is dated 2024-09-06. It was
priced against an earlier issue, and the Q&A sheet says so explicitly. Always date the set,
compare it to today, and record the answer in the estimate. Five months of design development
between issues is normal and moves numbers.

## Renovation framing labour carries a 20% uplift
**Job:** 2033 E. 7 · **Type:** bad rate
**Cue:** Working into or alongside existing structure.
**Lesson:** Add 20% to framing labour on renovations. The separate 20% complex-house uplift
applies only when the job is *not* a renovation — they do not stack.

## Supplier cost is not a unit rate
**Job:** 2033 E. 7 · **Type:** bad rate
**Cue:** Seeding a rate from a supplier quote.
**Lesson:** `rate = supplier_cost × 1.20 × 1.07` — 20% material handling, then 7% PST. A
quote entered raw understates the line by 28.4%. Rates already in the rate card are grossed;
do not apply it twice.

---

## Corrections from reviewed estimates

*(none yet — this section fills as Luke reviews estimates)*
