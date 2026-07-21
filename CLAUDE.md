# CLAUDE.md

Working notes for this repo. Read before touching the skill or producing an estimate.

## What this repo is

A single Claude Code skill that produces construction estimates from architectural
drawings, for Caisley Developments Ltd. (Vancouver BC). The skill is the product; the
repo exists to hold it, its learned pricing knowledge, and the estimates it has produced.

## Git workflow

Commit and push directly to `main`. No feature branches, no PRs — this is a single-author
repo and the review that matters happens on the estimates themselves, not the diffs.
Push after each meaningful change rather than batching.

## Non-negotiables

These came directly from Luke. Do not quietly change them.

- **Quantity takeoff × unit rate.** Not $/sq ft benchmarks, not comparable-job lump sums.
  Every priced line traces back to a countable or measurable quantity and the sheet it
  came from. If a quantity genuinely can't be taken off the drawings, say so on the line
  and carry it as a stated allowance — don't disguise a guess as a takeoff.
- **Estimate realistically, then flag risk.** Aim at likely final cost. Do not shade
  numbers down to look competitive. Separately, call out the lines with real change-order
  exposure and say why.
- **Ask for the fee before finalizing.** Cost the project first. Then stop and ask what
  fee % applies (range 8–18%, set per job by scope). Never assume 10% because Ogden used
  it.
- **One number per line.** No optimistic/likely/pessimistic ranges. Luke wants the likely
  figure.
- **Trade codes are fixed.** Use the Caisley list in `references/trade-codes.md`. If a
  scope item doesn't fit an existing code, raise it rather than inventing a code silently.

## Two outputs, one source of truth

Every estimate produces two deliverables from a single underlying takeoff:

**Internal working estimate** — comprehensive, modelled on the H. Douglas Consulting
workbook for 2033 E. 7th Ave. CSI MasterFormat divisions, every line traced to a quantity
and unit rate, labour broken out from materials and subtrades, contingency and fee
explicit, open questions and assumptions recorded. This is the working document and the
source of truth.

**Client presentation estimate** — lighter, modelled on the Ogden format. Grouped by trade
with a single figure per trade, plus assumptions, exclusions, and the total. This is what
goes to the client.

The client version is a *rollup of* the internal one, never a separately-derived number.
They must reconcile exactly. If they don't, the internal version is right.

Critically: **the client version must not leak unit rates, labour hours, productivity
factors, or margin.** Those are the internal document's reason for existing. A client
seeing `Drywall — 4,200 SF @ $3.15` can price-shop the line and can back-calculate the
markup. `Drywall — $13,230` is what they get. Aggregate before presenting, and never carry
a rate column into the client deliverable.

## Money model

Verified cell-by-cell against 2033 E. 7 (ESTIMATE DETAILS H24024–H24048). Use this, not the
simpler Ogden version.

```
M  = materials + subtrades           Σ of column H
L  = contractor's labour             Σ of column J
S1 = M + L
C  = S1 × contingency%               5% on 2033 E. 7
S2 = S1 + C
F  = S2 × fee%                       8–18%, asked per job — COMPOUNDS ON CONTINGENCY
S3 = S2 + F
G  = S3 × 5%                         GST, on everything including fee
T  = S3 + G
```

At 5% contingency and 10% fee that is `T = (M+L) × 1.21275`, which reproduces
$2,177,895.65 exactly.

Two things are easy to get wrong here. The **fee applies to the contingency-inclusive
subtotal**, not to bare cost — fee on S2, never on S1. And **GST applies to the fee as
well**, so it sits at the very bottom of the stack.

**PST (7% BC) never appears as a summary line. It is embedded in material unit rates.** The
lumber table computes `retail = supplier_cost × 1.20`, then `rate = retail × 1.07`. So a
material rate carries a 20% handling markup *and* PST before it ever reaches a line item.
Subtrade quotes are grossed the same way: `H = quote × 1.07`.

That answers the question raised when only Ogden was available: PST is real and is being
charged, just at line level rather than in the summary. When seeding a rate from a supplier
quote, apply ×1.20×1.07. When seeding from an existing line rate in a past estimate, it is
already grossed — do not double-apply.

Insurance is cost code 1.5 (a Div 1 line, not a markup). Supervision is code 1.8 as direct
labour, not a markup. Permits sit in Div 0. Overhead and profit are the fee, and only the
fee.

The 10% lien holdback on the CRITPATH billing schedule is a payment mechanism, not a cost.
It never enters an estimate total.

## Reading drawing sets

Plans are large-format vector PDFs (2592×1728 pt sheets). Both layers matter:

- **Text layer** — `page.get_text()` gets keynotes, room names, dimension strings, general
  notes, finish schedules, drawing lists. Cheap and reliable. Start here.
- **Rendered image** — the text layer gives you the keynote *legend* but not which rooms
  the keynote bubbles sit in, and no wall runs or fixture positions. For anything spatial,
  render the sheet with `pymupdf` at sufficient DPI and look at it.

A takeoff done from the text layer alone will miss quantities. Render the sheets.

Typical sheet types in a permit set, and what each yields:

| Sheet | Yields |
|---|---|
| Cover / drawing list | Floor areas, occupancy, zoning, code edition, scope summary |
| General notes | Contractual assumptions, what's GC-supplied vs owner-supplied |
| Demolition plan | DEMO quantities — walls removed, fixtures stripped |
| Demolition RCP | Ceiling/lighting/sprinkler removals and relocations |
| Construction plan | New walls, doors, millwork, plumbing fixture schedule |
| RCP | Ceiling heights, light fixture counts, smoke detectors |
| Electrical plan | Switch/outlet/keypad counts, relocations |
| Finishes plan | Floor and wall finish scope by room |
| Dimension plan | Wall lengths and room areas for quantity math |
| Sprinkler plan | Head relocations — a separate trade (SP) |

## Environment

System Python 3.9 at `/usr/bin/python3`. No Homebrew, no poppler, no ghostscript on this
machine. PDF work goes through `pymupdf`, spreadsheets through `openpyxl` — both
pip-installed already. Don't reach for `pdftoppm` or `mutool`; they aren't there.

## Learning from review

This is the part that matters most. An estimate that gets corrected and doesn't update the
knowledge files has wasted the correction.

When Luke gives feedback, classify it:

- **Bad rate** → update the entry in `references/rate-card.md`. Record the old value, the
  new value, and the job. Rates are evidence, so keep the provenance.
- **Missing scope** → the takeoff didn't catch something the plans implied. This is the
  most valuable kind. Add a lesson describing the *cue in the drawings* that should have
  triggered it, not just the missing line.
- **Wrong quantity** → the measurement or count was off. Note the sheet and what was
  misread.
- **Wrong assumption** → an assumption or exclusion was wrong for how Caisley actually
  works. Fix the default.

Write lessons so they fire at the right moment. `"microtopping over existing cabinetry
implies cabinet prep labour, not just the coating"` is useful. `"be more careful with
finishes"` is not.

## Handling the Ogden overrun

Ogden went from a $506k original estimate to $1.46M invoiced. That is the single richest
piece of evidence in the repo and it should inform estimates, but read it carefully before
citing it — much of the delta was 68 change orders, i.e. scope that did not exist at
estimate time. Do not conclude "multiply everything by 2.9".

Lines where the revised budget diverged hardest from the original are worth attention when
the same trades appear in a new job. HVAC in particular went from $5,600 to $120,580 —
that's an original estimate that missed the scope entirely, not scope creep.

## Style

- Estimates are client-facing. Plain professional language, no hedging filler, no emoji.
- Assumptions and exclusions are not boilerplate — write the ones that actually apply to
  this job, from what the drawings did and didn't tell you.
- When something in the plans is ambiguous enough to move the number, it belongs in the
  open-questions list rather than being silently resolved.
