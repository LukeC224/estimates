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

## Concealed rot is the base case on 1985–2000 coastal BC wood-frame, not a contingency
**Job:** Strata VAS2686 parkade (1066/1068 Maple / 1988/1998 Ogden) · **Date:** 2026-07-21 · **Type:** missing scope
**Cue:** A building of 1985–2000 vintage anywhere on the BC coast — Vancouver, the North
Shore, Victoria, Nanaimo, Surrey — that is wood-frame above or alongside the work, **plus**
any drawing note in the form "replace where deteriorated", "to be reviewed by structural",
"extent to be confirmed on site". Detail 01/A-6.0 on this job carried both: *"STUDS TO BE
REVIEWED BY STRUCTURAL AND REPLACED WHERE DETERIORATED"* and *"REPLACE PLYWOOD WHERE
DETERIORATED"*.
**Lesson:** That note is the architect telling you they know there is rot and are not going to
quantify it. **Structural rot was the single largest driver of the overrun on this job.** It
was carried at a $14,000 P.C. against a $608,624 estimate — a token.

This is the leaky-condo era. Buildings put up in BC between roughly 1985 and 2000 have face-
sealed assemblies with no drainage cavity, and where a membrane at the base of a wall has been
failing for thirty years the water has been sitting in the framing that whole time. Finding
sound studs is the exception.

Do not price this from the drawings, because the drawings cannot show it. Either:
1. **Get test openings before the number goes out.** Two or three openings at the worst-looking
   base-of-wall condition costs a day and reprices the whole line. This is the single highest-
   value pre-estimate spend on any building of this vintage; ask for it every time.
2. **Or carry rot as a unit-rate provisional item** — $/lineal foot of wall opened, $/stud
   replaced, $/sq.ft of sheathing — with a stated quantity range, not a lump sum. See the
   concrete-repair lesson below; the same reasoning applies and for the same reason.

A lump-sum allowance against concealed rot is a guess wearing the costume of a takeoff.

## Concealed-condition scope is priced as unit rate × provisional quantity, never lump sum
**Job:** Strata VAS2686 parkade · **Date:** 2026-07-21 · **Type:** wrong assumption
**Cue:** Any line where the quantity cannot be known until something is demolished, excavated
or opened — concrete repair under a topping, rot behind cladding, fill depth, buried services.
**Lesson:** Read Jones Christoffersen's tender for the Front Street Parkade rehabilitation
(City of New Westminster, RFP NWRFP-25-02, Addendum 2, 2025-08-14) prices *every* concrete
repair item as a unit rate against an estimated quantity **with a stated range**, and adds a
separate per-inch adder for depth found beyond the specified average:

| Item | Estimated | Range | Upper ÷ est. |
|---|---|---|---|
| Top surface repairs, 4″ avg | 750 sq.ft | 0–1,500 | 2.0× |
| Soffit repairs, 3″ avg | 100 sq.ft | 0–500 | 5.0× |
| Through-slab repairs, 4″ avg | 300 sq.ft | 0–1,000 | 3.3× |
| Aggregate | 3,000 sq.ft | 0–7,000 | **2.33×** |

A sealed BC engineer with full access to the structure and pre-tender testing **will not bound
the quantity tighter than 2×–5× their own estimate.** Caisley, pricing off a permit set with no
access at all, has no business being more confident than that.

Two consequences. First, exposure is **two-dimensional** — area found *and* depth found — and
both need pricing. Second, the structure of the line matters more than the rate in it: a unit
rate with a range converts an argument into an administrative process. On this job the
recommendation to convert the concrete line to a unit rate was actually written into the risk
sheet and then not carried through into the line itself when it wasn't taken up. **Price the
line the way the risk sheet describes it, not the way the request was worded.**

## Small podium projects need a bigger contingency %, not the same one
**Job:** Strata VAS2686 parkade · **Date:** 2026-07-21 · **Type:** wrong assumption
**Cue:** Any podium, plaza or parkade deck waterproofing replacement — especially a small one.
**Lesson:** CHOA Bulletin 600-008 *Replacing Podium Waterproofing* (2016) and BC Housing
*Maintenance Matters* No. 17 (2018), both prepared by Morrison Hershfield, state:

> "It is recommended that at least 10% of the total project costs be set aside in case these
> unexpected issues arise. A larger provisional fund may be needed depending on the project
> size (**the smaller the project, the larger the proportional fund**)."

10% is the published **floor**, and it scales *up* as the job gets smaller, because fixed
discovery costs spread over less area. VAS2686 was 3,400 sq.ft serving four units — about as
small as podium remediation gets — and was carried at exactly 10%. On a deck this size the
starting recommendation should be 15–20%, and the reason should be quoted to the client from
these two documents rather than asserted.

The same bulletin says the cost is *"predominately driven by the amount of material and level
of complexity of the new landscaping design"* — so on any deck job, the landscape package is
the thing to chase down before pricing, not the membrane.

## Escalation is a small share of any large overrun — check it before blaming it
**Job:** Strata VAS2686 parkade · **Date:** 2026-07-21 · **Type:** bad rate
**Cue:** Reviewing any estimate that overran, or pricing from a drawing set more than a year old.
**Lesson:** StatCan Building Construction Price Index, table 18-10-0289-01, Vancouver CMA,
2024 Q1 → 2026 Q1: residential composite **+5.1%**, non-residential composite +6.8%,
Div. 9 thermal & moisture +6.5% residential / +7.4% non-residential. Concrete **fell** over
2025 (index 109.0 → 107.0).

On a 42% overrun, the most generous applicable index explained 17.5% of the gap. The rate
card's flat 6.2%/yr from ICBA is close enough on a two-year horizon, but it is a projection and
StatCan is measurement — prefer the index, and prefer the trade-specific series over the
composite. Escalation is almost never the explanation for a large miss; scope and quantity are.

## Read the detail sheets as images, not just as text
**Job:** Strata VAS2686 parkade · **Date:** 2026-07-21 · **Type:** missing scope
**Cue:** Any detail sheet. The text layer of a details sheet extracts as a flat list of
annotations with no indication of what each one is pointing at.
**Lesson:** Three scope items on A-6.0 were invisible in the text layer and obvious once the
sheet was rendered and looked at: **brick** at the wall base (detail 02 — no Div 4 was carried
at all), **elastomeric paint** on the concrete cap (detail 06 — no Div 9 was carried at all),
and most importantly that detail 01 rebuilds the base of the exterior wall assembly, which
cannot be done without **stripping and reinstating the cladding** — the reason the drawings
call for removing a hedge to erect scaffolding.

Related and worth its own habit: **when the drawings price enabling work, find the work it
enables.** A-1.0 said a section of hedge #9 comes out "to enable installation of scaffolding".
The hedge removal was priced. The scaffolding was not.

## Five scope items that a topside podium takeoff misses every time
**Job:** Strata VAS2686 parkade · **Date:** 2026-07-21 · **Type:** missing scope
**Cue:** Any parkade, podium, plaza or terrace deck waterproofing job.
**Lesson:** All five were absent from the VAS2686 takeoff. Check each explicitly.

1. **Electronic leak detection grid — RCABC makes it mandatory, not optional.** *"Moisture
   monitoring sensor grids (conductance scanning grid) are mandatory and shall be installed on
   the top surface of all waterproofing membrane systems designed with inaccessible overburdens
   and wearing courses."* Only pavers-on-pedestals and ballast under 100 mm are exempt — so
   concrete topping, pavers on pea gravel and lawn all trigger it. An integrity scan is
   separately mandatory over 150 mm overburden and 200 sq.ft. Installed **before** overburden,
   by one of three recognised providers (Detec, ILD, SMT), so it prices like a sole source.
   Contractor's cost. RoofStar **Observer fees and prepaid guarantee-term maintenance are the
   owner's** — exclude them by name.
2. **Expansion joints.** Absent entirely from VAS2686. On a split-slab deck the joint has to tie
   watertight into the buried membrane — Emseal/Migutan class, side flashing sheets, elastomeric
   nosing, blockout, upturns. RJC carries these as separate lump sums.
3. **Soffit and underside repairs.** A topside takeoff naturally prices only what it can see from
   above. RJC carries soffit repairs, joist soffit repairs and through-slab repairs as separate
   unit-price lines — different access, different equipment — plus protection of everything
   hanging below the slab and air-quality obligations for the occupied space underneath.
4. **Fire watch, priced properly.** BC Fire Code 5.2.3.3: continuous watch during hot work,
   **plus 60 minutes after, plus a final inspection 4 hours after completion.** That last one is
   a return trip — realistically 2.5–3 paid hours per torching day, not one. CRCA now treats
   flameless base and cap at all perimeters, penetrations and flashings **extending 915 mm into
   the field** as the standard of care, torch only in the open field; count the linear metres
   rather than taking a percentage. CRCA prohibits torching onto plywood or OSB, which collides
   directly with any sheathing-replacement line.
5. **Shoring for construction loading.** RJC carries a **$40,000 cash allowance**. WorkSafeBC OHS
   s.20.18 requires P.Eng-certified plans to CSA S269.1-16 and s.20.26 requires an engineering
   certificate on site immediately before *each* intended loading event. An older deck may be
   good for only ~2.4 kPa — a mini-ex, a ready-mix truck or a stacked pallet of pavers exceeds
   that locally.

Also routinely missed and individually real: buried services in the fill (BC Housing's
*first*-named unforeseen cost), crane and material handling on a podium, engineered lightweight
growing medium rather than topsoil (it changes the structural load), plant establishment and
warranty periods, guardrail specialty engineering with Schedules S-B/S-C, silica containment for
shot blasting, and a pre-construction condition survey inside 5 days — miss that window and
every defect found at completion is yours.

## An occupied-site remediation programme will run long, and Div 1 goes with it
**Job:** Strata VAS2686 parkade · **Date:** 2026-07-21 · **Type:** wrong assumption
**Cue:** Occupied units, a live parkade, mandatory arborist supervision, phased night seals —
i.e. any job where the sequence is constrained by people rather than by trades.
**Lesson:** Programme overrun was a legitimate and material part of this overrun. Five months
was assumed from the phasing shown on A-6.0 detail 04; the job ran longer. Because Div 1 scales
with duration and the blended labour rate embeds it, a programme miss reprices two things at
once and neither is visible as an edit. On a constrained occupied site, price the duration the
*strata's* access requirements imply, not the one the trade sequence implies, and confirm the
work windows in writing before the number goes out.
