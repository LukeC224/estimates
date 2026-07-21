# Method

How a takeoff is built and priced. Derived from the H. Douglas Consulting workbook for
2033 E. 7, which is the quality bar.

## Reading the set

```sh
python3 scripts/read_plans.py <file.pdf> --text          # text layer, all pages
python3 scripts/read_plans.py <file.pdf> --render 19,20  # render sheets to PNG
```

Text first, then render. Both, always — a takeoff from the text layer alone will miss
quantities, because keynote legends extract as text while the bubbles that place them do
not.

What each sheet type yields:

| Sheet | Yields |
|---|---|
| Cover / drawing list | Issue date and revision, drawing index, consultants |
| Stats / FSR overlay | Floor areas by level, FSR, allowable vs proposed |
| Site plan | Hardscape and softscape areas, tree protection, utility connections, access |
| Notes and legend | Contractual assumptions, supply splits, abbreviations |
| Assemblies | Wall/floor/roof makeups — drives insulation, membrane, cladding, GWB quantities |
| Window & door schedule | Direct counts and sizes. The highest-value sheet in any set |
| Demolition plans | Demo quantities, what is retained, keynote list |
| Demolition elevations | Existing building face calcs, retention extent |
| Floor plans | Room areas, wall runs, fixture positions, wall type tags |
| Elevations | Cladding areas by material, opening percentages |
| Sections | Ceiling heights, floor-to-floor, assembly continuity |
| Stair details | Riser/tread counts, guard lengths, finishes |
| RCP | Ceiling heights, fixture counts, smoke detectors |
| Section/plan details | Trim, jamb conditions, flashing lengths |

## Quantities

Room by room, element by element. Every quantity records the sheet it came from.

Where a drawing states an area, use the stated figure and cite it. Where you measure or
infer, mark it. The distinction matters when Luke reviews.

**Cross-check against the architect's own area table.** Run it floor by floor with a
difference column and explain each gap. The consultant did exactly this and reconciled with
notes like "concrete wall thickness −95.89 sf", "exclusions +23.91 sf". A takeoff that
matches the architect's areas to the square foot has probably just copied them; a takeoff
that differs and *explains why* has been done.

**Waste factors go in the quantity, not the rate.** The source embeds them in the quantity
formula (`=806*0.85` for net area, `×2.25` for coverage). Note the factor — it is otherwise
invisible in any column, which is a real flaw in the original and worth improving on.

Written measurement rules from the source, worth reusing:
- Basement measured inside face of concrete to centre of inside wall
- Stair tread areas = plan area × 1.5, to allow for risers
- Disposal at $150/hour assuming 5 loads per day

## Pricing a line

```
quantity × unit rate           = material / subtrade cost
quantity ÷ productivity divisor = labour hours
labour hours × blended rate     = labour cost
```

Materials and subtrades roll into one column; in-house labour into another. They stay
separate all the way to the summary, because the client is buying cost-plus and the split
is contractual.

### Four kinds of line

**Self-perform** — rate from the material tables, real productivity-driven hours.

**Subtrade, unit-priced** — the rate is the sub's supply-and-install price. Labour collapses
to a single interface hour for GC coordination. Note the vendor and the date of the price.

**Lump-sum quote** — enter the total (grossed ×1.07 for PST), then back-calculate the unit
rate by dividing by quantity. This keeps the line comparable to others in its division.

**P.C. allowance** — provisional cost where scope is undefined. Unit is literally `P.C.`.
Say what it covers.

### Quote provenance

Attribute and date every quote: *"Zebiak house lift and move price $19,000 (+/- $22,000 to
lift and place; confirm price if shifting more than 12″) @ 2024-04-11."*

A quote without a date is unusable six months later, and drawing sets routinely sit for six
months. In the source workbook the vendor detail sits in the description column of the row
*below* the priced line.

### Exclusions are visible lines

Anything out of scope gets a zero-value line reading `NOT INCLUDED`, `BY OWNER`, `BY OTHERS`
or `N.I.C.`. Never omit silently — the client will assume anything not mentioned was priced.

On 2033 E. 7: 21 NOT INCLUDED, 11 BY OWNER, 9 BY OTHERS, 11 omit.

## The question register

Every ambiguity that moves the number becomes a question tied to the line it affects, with
the assumption you're making stated inline in the meantime.

The consultant embedded assumptions directly in item names — "001 Family Room (hardwood)
152.75sf?" — so the architect confirming the room list also confirms the finish. Copy that.

Never silently resolve an ambiguity that changes cost.

See `qa-checklist.md` for the standing questions.

## Schedule drives general requirements

Div 1 scales with duration, not with area. Job site costs and supervisory spread evenly
across the programme.

The consultant computed periods as `ROUNDUP(months × 1.08 × 2, 0)` — a 1.08 buffer on the
stated duration, then bi-weekly periods. Twelve months became 26 periods. Div 1 then divides
across them.

Standard sequence: demolition → excavation → formwork/concrete → drain tile/paving →
framing + metals → windows/cladding/roofing → landscaping/fencing → plumbing rough-in →
electrical rough-in → insulation → drywall → trim/prime/lay hardwood → cabinet cases → tile
→ finish hardwood → finish paint → slabs/specialties/appliances → final plumbing → final
electrical → cabinet doors → cleanup.

Long-lead items need deposits early and a "measure" milestone: doors, windows, cabinets,
stone slabs, tile. Appliances get ordered first.

**Cross-check labour against the schedule.** Total labour ÷ crew-day cost gives crew-days;
that should be consistent with the stated duration. On 2033 E. 7: $413,056.93 ÷ $7,481.34
= 259.8 crew-days = 51.96 weeks against a 12-month assumption. If your labour total implies
a programme materially different from the one you've assumed, one of the two is wrong.

## Verification

Before issuing, check:

1. Division subtotals sum to the materials and labour totals
2. The markup chain arithmetic (fee on contingency-inclusive subtotal; GST on everything)
3. Internal and client documents reconcile to the same total
4. No unit rates, hours or margin leaked into the client document
5. Every quantity cites a sheet
6. Every allowance is labelled P.C. and described
7. Every exclusion appears as a visible line
8. Labour-implied duration matches the assumed programme
9. $/sq.ft. is in a defensible range against the benchmarks
10. Every open question is listed

The source workbook carries an explicit "all 6 cells must match" cross-check block. Build
the equivalent.
