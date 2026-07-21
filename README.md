# Estimates

A Claude Code skill that turns architectural drawings and build-out documentation into a
priced construction estimate — and gets better at it every time Luke corrects it.

Built for **Caisley Developments Ltd.**, Vancouver BC.

## What it does

Give it a permit plan set, architecture spec, or scope document. It:

1. Reads the drawings (including the graphical sheets, not just the text layer).
2. Extracts a **quantity takeoff** — counts and measurements traced to specific sheets.
3. Prices each quantity against a **rate card** built from Caisley's past jobs.
4. Rolls up **by trade code**, using the standard Caisley division structure.
5. Asks for the **project fee %** (8–18%, set per job once the cost is known), applies it,
   then applies 5% GST.
6. Emits a **client-ready PDF** and a **budget spreadsheet** matching the house format.
7. Flags the lines most likely to blow up, with reasons drawn from prior overruns.

## What makes it different from a generic estimator

It learns. Every estimate gets reviewed, Luke says what was wrong, and those corrections
are written back into the rate card and the lessons file. The next estimate starts from
the corrected numbers. See [Feedback loop](#feedback-loop).

## Ground rules baked in

| | |
|---|---|
| Region | Vancouver, BC — VBBL, City of Vancouver permitting |
| Currency | CAD |
| Method | Quantity takeoff × unit rate (not $/sq ft benchmarks) |
| Structure | By trade/division, Caisley trade codes |
| Fee | 8–18% on cost, decided per job, **prompted before finalizing** |
| Tax | 5% GST on (cost + fee) |
| Output | Single likely number — no three-point ranges |
| Deliverables | Client-ready PDF + budget spreadsheet |

## Usage

```
> estimate the plans at ~/Downloads/X8Richards_250910_Permit Plan Draft.pdf
```

The skill will work through takeoff → pricing → review, stop to ask for the fee, then
write the deliverables to `estimates/<job-name>/`.

To correct it afterwards, just say so in plain language:

```
> tile install is way low — that scope is closer to $30k, and you missed the
> waterproofing membrane entirely
```

It updates the rate card, records the lesson, and reprices.

## Repo layout

```
.claude/skills/construction-estimate/   the skill itself
  SKILL.md                              main instructions
  references/
    trade-codes.md                      the Caisley division structure
    rate-card.md                        unit rates, learned and maintained
    method.md                           takeoff and pricing procedure
    lessons.md                          accumulated corrections from review
  scripts/
    read_plans.py                       PDF text + page rendering
    build_workbook.py                   spreadsheet generation
estimates/<job>/                        one directory per estimate produced
reference/                              past jobs used as evidence
```

## Reference material

Two source documents anchor the whole system:

- **1988 Ogden Ave interior renovation** — a complete budget-vs-invoice spreadsheet.
  Defines the trade code list, the grouping, and the fee/tax model. Also the cautionary
  tale: original estimate $506k, final $1.46M.
- **X8 Richards (1111 Richards St)** — an 11-sheet Vancouver permit plan draft for a
  1,712 sq ft two-level condo renovation. The first live test case.

## Setup

Requires Python 3 with two libraries:

```sh
pip3 install pymupdf openpyxl
```

`pymupdf` reads and renders the drawing sheets; `openpyxl` reads past budget
spreadsheets and writes new ones.

## Feedback loop

The skill is only as good as its rate card, and the rate card only improves if
corrections get written down. After each estimate:

1. Luke reviews and says what was wrong — a rate, a missed scope item, a wrong quantity.
2. The skill classifies the correction: bad rate, missing line, wrong takeoff, or wrong
   assumption.
3. Rate corrections update `rate-card.md`. Everything else becomes an entry in
   `lessons.md` with the job it came from.
4. Lessons are consulted at takeoff time, so the same mistake shouldn't recur.
