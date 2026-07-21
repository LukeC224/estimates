---
name: construction-estimate
description: Produce a construction cost estimate from architectural drawings, permit sets, or scope documents. Use when given plans, a spec, or build-out material and asked to estimate, price, budget, or cost a project. Also use when reviewing or correcting a previously produced estimate. Vancouver BC residential and renovation work for Caisley Developments.
---

# Construction estimate

Turn a drawing set into a priced estimate: quantity takeoff, unit rates, CSI divisions,
contingency, fee, GST. Produce a detailed internal workbook and a lighter client document.

Read `references/method.md` before starting a takeoff. Read `references/lessons.md` too —
it holds corrections from past estimates and exists to stop repeat mistakes.

## Before anything else: date the drawings

Find the issue date and revision on the title block, and compare it to today. Then ask
whether this is the current set. On 2033 E. 7 the estimate was priced from a set five months
older than the permit issue, and the estimator recorded "CONFIRM THAT THESE ARE THE MOST
CURRENT SET OF DRAWINGS — **NO**" on the face of the estimate.

Do the same. If the set can't be confirmed current, say so in the estimate rather than
letting it pass silently.

Also check the project number against the street address. On VFA drawings, `2033 // 2212
East 7th` means project 2033 at 2212 E 7th Ave — the leading number is not the address.

## Procedure

### 1. Read the set

Extract the text layer of every sheet first (`page.get_text()` via pymupdf) — cheap, and it
carries keynotes, schedules, general notes, dimension strings, room names.

Then **render the sheets and look at them**. The text layer gives you a keynote legend but
not which rooms the bubbles sit in, no wall runs, no fixture positions. A takeoff built from
text alone will miss quantities. `scripts/read_plans.py` handles both.

Identify what kind of set this is. A permit/DP set gives you envelope, openings, assemblies
and areas, but typically has no structural, no MEP, no finish schedule and no millwork — so
those scopes become allowances and RFIs, not takeoff. Say which kind of set you had.

### 2. Take off quantities

Room by room, element by element. Every quantity records the sheet it came from.

Where the drawings state an area, use the stated figure and cite it. Where you measure or
infer, mark it as such. Cross-check your own totals against the architect's area table and
reconcile the difference — the consultant on 2033 E. 7 ran a floor-by-floor comparison with
a difference column and notes explaining each gap ("concrete wall thickness −95.89 sf").

Waste factors belong in the quantity, not the rate. Note the factor used.

### 3. Ask the questions

Build a question register as you go, one entry per ambiguity, each tied to the line it
affects. State the assumption you're making in the meantime — inline, where it will be read.
`references/qa-checklist.md` has the standing questions plus the pattern.

An ambiguity that moves the number is a question, never a silent decision.

### 4. Price it

Each line: `quantity × unit rate`. Rates come from `references/rate-card.md`.

Labour is separate from materials and is **productivity-driven**: hours = quantity ÷ a
units-per-hour divisor, then hours × the blended crew rate. It is not crew-hours × trade
rate. Subtrade lines still book one interface hour for GC coordination.

Mark every line as self-perform, subtrade, quote, or P.C. allowance. Provisional Costs are
legitimate and expected where scope is undefined — label them "P.C." and say what they
cover. Do not disguise an allowance as a takeoff.

Anything genuinely out of scope gets carried as a visible zero line reading NOT INCLUDED /
BY OWNER / BY OTHERS. Silence reads as inclusion, and the client will assume it was priced.

### 5. Stop and ask for the fee

Cost the project first. Then ask. The range is 8–18% and it is set per job by scope. Do not
default to 10% because the examples used it.

Ask for contingency at the same time. 5% was used on 2033 E. 7; a renovation touching
century-old fabric with no hazmat survey deserves more.

### 6. Apply the money model

See CLAUDE.md. Briefly: fee applies to the contingency-inclusive subtotal, GST applies to
everything including fee, and PST is already inside the material rates.

### 7. Write both deliverables

**Internal** — CSI divisions, every line with quantity, unit, rate, material and labour
split, source sheet, and its self-perform/subtrade/quote/P.C. marking. Plus the question
register, assumptions, exclusions, and the risk lines.

**Client** — trade-level rollup. One figure per division or trade group. Assumptions,
exclusions, open questions, total. **No unit rates, no labour hours, no productivity
factors, no margin.** A client who can see `Drywall — 11,087 sf @ $1.25` can price-shop the
line and back-calculate your markup.

Both must reconcile to the same total. Cross-check them explicitly; the consultant's
workbook carries an "all 6 cells must match" block for exactly this reason.

### 8. Flag the risk

Separately from the number, name the lines with real change-order exposure and say why.
Ground this in the drawings and in `references/lessons.md`, not in generic caution.

## Learning from review

When Luke corrects an estimate, classify the correction and write it down. An uncorrected
knowledge file makes the same mistake next time.

- **Bad rate** → update `references/rate-card.md`. Keep old value, new value, job, date.
  Rates are evidence; provenance matters.
- **Missing scope** → the most valuable kind. Add to `references/lessons.md`, describing the
  *cue in the drawings* that should have triggered the line — not just the missing item.
- **Wrong quantity** → note the sheet and what was misread.
- **Wrong assumption** → fix the default in `references/qa-checklist.md`.

Write lessons so they fire at the right moment. "Microtopping over existing cabinetry
implies cabinet prep labour, not just the coating" is useful. "Be careful with finishes" is
not.

## Scripts

```sh
read_plans.py plans.pdf --index              # sheet numbers and titles from the title block
read_plans.py plans.pdf --text 19,20         # text layer
read_plans.py plans.pdf --render 19,20       # PNG, then Read them
build_workbook.py takeoff.json -o est.xlsx   # writes est-internal.xlsx and est-client.xlsx
```

`build_workbook.py` emits **two separate files**, not two tabs. The detail must never
travel in the same workbook as the client summary — a second tab is one click away from
exposing every rate and the margin. It prints both totals so you can confirm they
reconcile.

Both scripts need pymupdf and openpyxl. There is no poppler or ghostscript on this machine;
do not reach for `pdftoppm`.

## Reference files

- `references/method.md` — takeoff and pricing procedure in detail
- `references/cost-codes.md` — the CSI division and cost code taxonomy
- `references/rate-card.md` — unit rates, labour rates, productivity divisors
- `references/qa-checklist.md` — standing questions to put to the architect/client
- `references/lessons.md` — accumulated corrections
