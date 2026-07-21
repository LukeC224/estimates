# Rate card

Seeded from the 2033 E. 7 estimate (H. Douglas Consulting, 2024-04-17). Every rate below is
evidence from a real Caisley project, not an industry table.

**Rates are on a 2024 basis.** Escalate before use — see [Escalation](#escalation).

Update this file whenever Luke corrects a rate. Record old value, new value, job and date;
provenance is what makes a rate trustworthy later.

## Labour rates

In-house crew only. Everything else is a subtrade.

| Role | 2024 | 2025 | 2026 |
|---|---|---|---|
| Contractor / site supervisor | $75.00 | $79.65 | $84.59 |
| Foreman / lead carpenter | $70.00 | $74.34 | $78.95 |
| Carpenter | $62.00 | $65.84 | $69.93 |
| Apprentice carpenter (helper) | $55.00 | $58.41 | $62.03 |
| General labourer | $45.00 | $47.79 | $50.75 |

Escalation 6.2%/yr (ICBA 2024 projection). Standard week 7:30–4:00 Mon–Fri.
Crew capacity: 2 contractors, 5 foremen, 14 carpenters, 5 helpers, 3 labourers.

### Blended chargeout — how labour is actually priced

Estimating does **not** use per-role rates. It uses one blended crew rate applied to
everything, back-converted from hours.

Active crew = supervisor + foreman + carpenter + apprentice, averaged:
`(75 + 70 + 62 + 55) / 4 = $65.50` on a 2024 basis. That is then weighted across the
calendar years the schedule spans. On 2033 E. 7 — 4 months in 2024, 8 months in 2025 —
it came to **$68.2073/hr**.

Two separate rates sit outside the blend: **$78.10** for supervisory lines in Div 0/1, and
**$46.90** for labourer lines.

Recompute the blend for each job's schedule. It is not a constant.

> **This is a trap.** The blended rate embeds the project duration. Change months-to-complete
> and every labour line reprices silently, with no visible edit. Whenever the schedule moves,
> recompute the blend and re-verify the labour total.

Billing note carried in the source: labour is *estimated* at the average crew rate, but
*billed* at the individual rates above.

## Productivity divisors

Labour hours = quantity ÷ divisor. These are the observed values.

| Divisor | Work |
|---|---|
| ÷1000 | drywall removal (sq.ft.) |
| ÷128 | vapour retarder (sq.ft.) |
| ÷50 | framing crew (sq.ft.) |
| ÷40 | batter boards (lineal) |
| ÷15 | ICF (sq.ft.) |
| ÷12.5 | Ipe decking (lineal) |
| ÷10 | structural steel & LVL (lineal) |
| ÷8 | Hardie siding (sq.ft.) |
| ÷100 | wood fencing (lineal) |

Fixed-hour lines use 1, 4, 8 or 16 hours flat. **Subtrade lines book 1 "interface" hour** for
GC coordination — never zero, because coordination is real cost.

### Renovation and complexity adjustments

- **Renovation: +20% framing labour.** On 2033 E. 7 that was +$12,450.66.
- **Complex house: +20%** — applies only when the job is *not* a renovation. The two do not
  stack.
- **Form lumber reuse credit**: −$2,607.68 on that job.

## Material markup

Supplier cost is not the rate. The chain is:

```
retail = supplier_cost × 1.20      20% material handling markup
rate   = retail × 1.07             7% BC PST
```

So a supplier quote becomes a line rate at **×1.284**.

Subtrade lump-sum quotes are grossed for PST only: `× 1.07`.

Example: 2×4 at supplier cost → $0.68052/lineal ft after both steps.

> Rates already in this file are grossed. Do not re-apply the markup to them. Apply it only
> when seeding a *new* rate from a raw supplier quote.

## Unit rates — observed

Quantities and rates from real priced lines. `at` = each. `P.C.` = provisional cost
allowance.

### Div 1 — General requirements
| Item | Unit | Rate |
|---|---|---|
| Hazmat inspection | at | $1,750 |
| Surveyor | at | $3,000 |
| Layout from pins | layout | $20 |
| Hot2000 energy modelling | at | $4,000 |
| Site camera (Night Owl) | months | $1,040 |
| Scaffolding | sq.ft. | $2.40 |
| Disposal bins | bins | $1,200 |
| Level 1 first aid kit | at | $57.58 |

### Div 2 — Sitework
| Item | Unit | Rate |
|---|---|---|
| Remove existing drywall | sq.ft. | $7.00 |
| House lift & move | at | $19,000 |
| Trucks & dump fees | loads | $750 |
| Wood fences | lineal | $80 |

House lift is attributed and dated in the source: "Zebiak house lift and move $19,000
(+/- $22,000 to lift and place; confirm price if shifting more than 12″) @ 2024-04-11."

### Div 3 — Concrete
| Item | Unit | Rate |
|---|---|---|
| R30 ICF blocks 3¼″ | sq.ft. | $6.22 |
| ICF bracing rental | lineal | $15 |
| Rebar — footings | yards | $166.65 |
| Rebar — foundation walls | yards | $162.36 |

### Div 5 — Metals
| Item | Unit | Rate |
|---|---|---|
| W10×68 steel | lineal | $68 |
| W12×50 steel | lineal | $50 |
| Custom exterior railings | lineal | $330 |

### Div 6 — Wood and plastics
| Item | Unit | Rate |
|---|---|---|
| Parallam beam pack-out | lineal | $20.39 |
| 1¾″ × 7¼″ LVL | lineal | $11.61 |
| 14″ TJI 360 | lineal | $10.13 |
| TJI hangers | hangers | $5.83 |
| 5/4 × 6 Ipe decking | lineal | $17.12 |

### Div 7 — Thermal and moisture
| Item | Unit | Rate |
|---|---|---|
| R28 batts | sq.ft. | $4.00 |
| Intello Plus membrane | sq.ft. | $1.33 |
| Hardieplank 8¼″ | sq.ft. | $2.31 |
| Colvent 2-ply SBS roofing | sq.ft. | $20.00 |

### Div 8 — Doors and windows
| Item | Unit | Rate |
|---|---|---|
| Westeck windows | sq.ft. | $167.11 |

Back-calculated from a $55,659.39 quote × 1.07 over 356.375 sq.ft. Supply only — install
hours are in 6.9.

### Div 9 — Finishes
| Item | Unit | Rate |
|---|---|---|
| New drywall | sq.ft. | $1.25 |
| Kitchen millwork | lineal | $1,200 |

### Div 10 — Specialties
| Item | Unit | Rate |
|---|---|---|
| Towel rods | P.C. | $125 |

### Div 15 — Mechanical
| Item | Unit | Rate |
|---|---|---|
| Plumbing rough-in | units (fixtures) | $1,580 |
| Radiant heat | sq.ft. | $14.00 |

### Div 16 — Electrical
Carried as a single **P.C. of $125,000** for the whole division, then split into sections by
fixed percentage. Sub-categories carried at `P.C. × 0.05` = $6,250 each.

That is the honest treatment when there is no electrical design in the set — which on a
permit drawing package there usually isn't.

## Benchmarks

From 2033 E. 7 — a major renovation with retention, house lift, new full basement and
2-storey rear addition:

- **House: $588.90/sq.ft.** over 2,877.25 sq.ft. — excludes fee, contingency and GST
- **Hard landscaping: $76.77/sq.ft.**
- Contractor's labour ran **18.97%** of total estimate
- Div 1 general requirements ran **12%** of trade cost over a 12-month programme
- Div 9 finishes was the largest division at **20.7%**; cabinetry alone **8.0%**

Use these to sanity-check a completed estimate. They are not a substitute for takeoff, and
an estimate that only matches a $/sf benchmark hasn't been done.

## Concealed condition buffers

Scope that cannot be quantified from drawings because it is behind, under or inside something.
These are **not** contingency — contingency covers the estimate being wrong. These cover work
that is certainly there and merely unmeasured. They belong on the line, as unit rates against a
provisional quantity with a stated range.

### Coastal BC concealed rot — 1985–2000 wood-frame

**Trigger:** a wood-frame building of roughly 1985–2000 vintage anywhere on the BC coast
(Vancouver, North Shore, Richmond, Surrey, Victoria, Nanaimo), where the work exposes the base
of exterior walls, or any assembly sitting below or behind failed water management.

This is leaky-condo-era construction: face-sealed, no drainage cavity. Where a membrane at the
base of a wall has been failing for thirty years, the framing has been wet that whole time.
**Assume rot is present. Sound framing is the exception, not the expectation.**

Do not price this as a lump-sum allowance. Carry it as:

| Item | Unit | Provisional basis |
|---|---|---|
| Sheathing replacement | sq.ft. | assume **50%** of exposed wall area, range 10–100% |
| Stud / plate replacement | lineal | assume **40%** of exposed wall run, range 0–100% |
| Sill plate and rim joist replacement | lineal | assume **30%** of exposed wall run, range 0–100% |
| Structural engineer field review of opened framing | at | 1 per phase, minimum 2 |

Those percentages are a **starting position for pricing, not a takeoff** — they exist so the
line is the right order of magnitude before anyone opens a wall. Say so on the line.

**Rot never arrives alone.** Every one of these follows from it and each was missed on VAS2686:
- cladding removal and reinstatement over the full opened area
- scaffolding or lifts to reach it
- painting and finishing of the reinstated cladding
- sheathing membrane, flashing and trim reinstatement
- masonry removal and rebuild where brick returns to the wall base

If a rot line exists and those five don't, the estimate is incomplete.

**Buy the answer instead of guessing it.** Two or three test openings at the worst-looking
condition cost a day and reprice the entire line. On any building of this vintage, ask for
them before the number goes out. It is the highest-value pre-estimate spend available.

### Concrete repair on a suspended slab

Never lump sum. Unit rate against a provisional quantity **with a stated range**, plus a
separate per-inch adder for depth found beyond the specified average. Read Jones
Christoffersen's own tenders bound the quantity at 2×–5× their estimate (see `lessons.md`), and
they have full access to the structure. Price topside *and* soffit/underside repairs — the
underside is different access, different equipment, and is the item most often left out.

Scale reference: ACMS (BC) publishes membrane repair at ~$100/m² against concrete repair at
~**$1,500/m²**. Concrete repair is roughly **15× membrane repair per unit area**, which is why
a modest quantity surprise in concrete swamps the membrane line it was meant to protect.

**Two multipliers compound, and both are documented:**

1. **Detection shortfall ≈ 1.46×.** FHWA-RD-01-020 *Reliability of Visual Inspection for Highway
   Bridges* (2001), §5.4.4: a deck with core-validated delamination of **19%** of area was
   surveyed by 22 professional teams, 20 using chain drag. Their **average call was 13%**. Only
   5 of 22 landed within 5 points. Sounding finds roughly two-thirds of what is actually there.
2. **Geometric overcut ≈ 1.8× on small patches.** ACI RAP-7 requires repair limits to extend
   **3–4″ beyond** the marked delamination. A 2 ft × 2 ft patch becomes 4.0 → 7.1 sq.ft. The
   ratio worsens as patches get smaller and more numerous.

Applied to a sounded quantity these give roughly **2.5×** before anyone has found anything
unexpected — which is why RJC's 2×–5× tender range is not conservatism, it is arithmetic.

**Vintage flag:** CSA S413 *Parking Structures* first appeared in **1987**. A parkade built
around 1990 was designed to that first edition and predates every subsequent tightening of
cover, drainage, expansion joints and protection systems. Major rehabilitation is normally
needed at 20–30 years; a 1990 structure in 2026 is 36 years old and past its first cycle.

**Documented BC outcomes** (court records, so the numbers are on the record):

| Case | Original | Final | Delta |
|---|---|---|---|
| Strata Plan LMS 1383, Vancouver | $270,000 | $447,601 | **+65.8%** — scope grew from P1 slab alone to P1 + P2 + delamination repair |
| Wight v. VR 123, Maple St., Vancouver, 2024 | $1,700,000 | $2,100,000 | **+23.5%** |
| Enefer v. LMS 1564, Odyssey Towers | $6,150,000 | ~$7,000,000 | **+13.8%** — the court found the levy was voted **before the drawings were complete** |

Every documented BC case exceeded the industry's own 10% recommendation.

## Escalation

Rates above are 2024. Compound at **6.2%/yr** from mid-2024 unless a better figure is known.

| To | Factor |
|---|---|
| 2025 | ×1.062 |
| 2026 | ×1.128 |
| 2027 | ×1.198 |

Material prices move faster and less predictably than labour, particularly lumber and steel.
Where a material line is large enough to matter, get a current quote rather than escalating
a two-year-old rate — and when you do, remember the quote needs ×1.20×1.07 to become a rate.

## Units of measure

House convention is long words, never abbreviations. Match it:

`sq.ft.` · `lineal` · `lineal ft.` · `at` (each) · `units` · `sheets` · `hours` · `yards` ·
`cubic yards` · `months` · `days` · `sides` · `treads` · `doors` · `boxes` · `squares` ·
`loads` · `trees` · `footings` · `P.C.` · `allowance`

## Corrections log

Append here whenever a rate changes. Newest first.

| Date | Item | Old | New | Job | Note |
|---|---|---|---|---|---|
| 2026-07-21 | Concealed rot, base of exterior wall | $14,000 lump-sum P.C. | unit rates, ~50% sheathing / 40% studs assumed — see [Concealed condition buffers](#concealed-condition-buffers) | VAS2686 parkade | Structural rot was the **largest single driver** of a 42% overrun. The drawings said "replace where deteriorated" and were answered with a token. |
| 2026-07-21 | Concrete repair, suspended slab | $32,000 lump-sum P.C. | unit rate × provisional qty, range 2–5×, plus per-inch depth adder | VAS2686 parkade | Overrun confirmed legitimate by Luke. Structure of the line was the error, not the rate. |
| 2026-07-21 | Contingency, small podium deck | 10% | 15–20% | VAS2686 parkade | CHOA 600-008 / BC Housing MM17: 10% is the published floor and scales **up** as the job gets smaller. |
| 2026-07-21 | Escalation basis | ICBA 6.2%/yr projection | StatCan BCPI 18-10-0289-01, Vancouver CMA, trade-specific series | VAS2686 parkade | Measurement beats projection. 2024Q1→2026Q1: resid. composite +5.1%, Div.9 thermal/moisture +6.5%, concrete −2% over 2025. |
| 2026-07-21 | Programme, occupied-site remediation | 5 months | price the strata's access windows, not the trade sequence | VAS2686 parkade | Programme overrun confirmed legitimate by Luke. Div 1 and the blended rate both move with it. |
