# Question register

Ambiguities go to the architect or client as questions. They are never resolved silently.

Each question records: the drawing it arises from, the line it affects, the assumption being
carried in the meantime, and the answer when it comes.

## Standing questions — ask on every job

Asked first, before any takeoff:

1. **Are the drawings printed correctly at the indicated scale?**
2. **Is this the most current set?** — On 2033 E. 7 the honest answer was *no*, and the
   estimator recorded it on the face of the estimate rather than letting it pass.
3. Anticipated start date?
4. Anticipated duration in months? — this drives Div 1 *and* the blended labour rate
5. Typical door heights, per floor
6. Is the existing structure being demolished, retained, or partly both?
7. Footprint and depth of the existing building
8. Confirm insurance cost against the final total

## Scope-split questions

9. What is supplied by owner vs by contractor? Appliances and plumbing fixtures especially
10. What is by others / N.I.C.? Get this explicitly rather than inferring from silence
11. Who holds the allowances — contractor or client direct?

## Finish confirmation

Run a room-by-room list with the assumed finish embedded in the room name, so confirming the
list confirms the finishes:

> 001 Family Room (hardwood) 152.75 sf?
> 003 Mud Room (tile) 175.5 sf?
> 213 Primary Shower (tile floor & walls)?

Prefix convention: `X` exterior, `P` planter, `V` void. Report interior, exterior and total
separately.

## Per-drawing questions

One slot per sheet. Most stay empty; the ones that fire are short and material. Real examples
from 2033 E. 7:

- A101 Site plan — "extent of hard landscaping to include?"
- A200 Floor plans — "heating system?" → heat pump
- A200 — "Deck: cedar, IPE?" → IPE
- A200 — "Front patio and stairs: concrete?" → concrete

## What a permit set won't tell you

A BP/DP package is strong on envelope, openings, assemblies and areas. It routinely omits
the following, and each becomes an allowance and a question rather than a takeoff:

- **Structural** — sizing, underpinning, shoring, lifting method
- **Mechanical and electrical** — no ducts, capacities, panel or service size, no lighting
  layout. All-electric designs may need a service upgrade nobody has priced
- **Sprinklers** — NFPA 13D residential design is usually delegated
- **Interior doors** — often no schedule at all, even when exterior doors are scheduled
- **Room finishes** — frequently referenced but absent
- **Millwork** — kitchens, vanities, pantry, built-ins shown in plan with no elevations or
  specs. Usually the largest single allowance
- **Appliance and fixture specs** and who supplies them
- **Window manufacturer and frame material**
- **TBD colours and materials** — Hardie, stone, pavers
- **Geotech**, excavation support, dewatering
- **Landscape and irrigation detail**

## Coastal BC, 1985–2000 wood-frame — ask before pricing

Leaky-condo-era stock. Concealed rot is the base case, and it was the largest single driver of
the overrun on VAS2686. See `lessons.md` and the rate card's concealed-condition buffers.

- **Can we cut two or three test openings before the number goes out?** The highest-value
  pre-estimate spend available on this vintage. One day of work reprices the whole framing line.
- Which walls sit below or behind failed water management, and for how long has it been failing?
- Is there a building envelope condition assessment, depreciation report or engineer's report we
  can see? On a strata there almost always is, and it will name the rot.
- Has any previous remediation been done, and where does it stop?
- Who carries the structural engineer's field review of framing once it is opened?
- **Do the drawings say "replace where deteriorated" or "to be reviewed by structural"?** That is
  the architect telling you rot is expected and will not be quantified. Price it as a range.

## Parkade, podium and plaza deck work — ask before pricing

- **How many phases?** A four-phase job is not a one-phase job divided by four — shoring cycles,
  mobilizations, fire watch days and ventilation rental all scale with phase count. Price a
  stated number and flag additional phases as a change.
- **Is any part of the deck post-tensioned?** CSA S448.1 excludes PT slabs and the risk profile
  changes completely.
- **Will the strata's insurer permit torch-applied membrane on an occupied residential
  building?** Carriers have tightened hard after 2019–2025 losses and many now exclude it. If
  the answer is no, the product change is a scope change and gets priced as one.
- Does the building's own ventilation stay running? If it is shut down or intakes are sealed,
  the deck can become a confined space — materially different cost.
- Is a hazmat survey done? **WorkSafeBC OHS s.20.112 puts the duty jointly on the owner *and*
  every responsible employer**, and the BC survey trigger is buildings predating 1990-12-31.
  Bituminous mastics and adhesives test positive roughly half the time and cannot be identified
  visually. Work stops if unidentified material is found mid-job.
- What is under the fill — irrigation, landscape lighting, gas, sprinkler? BC Housing names
  buried services as the *first* unforeseen cost on podium work.
- Is the existing slab sloped to drain, and has anyone surveyed the falls?
- What overburden depth and what point loads? Over 150 mm or with planters, a Protected Membrane
  Roof design is forced and electronic leak detection becomes mandatory.

## Renovation-specific

Renovations carry latent risk that new builds don't. Ask:

- **Has a hazmat survey been done?** A pre-1990 house without an asbestos and lead survey is
  an open-ended liability, not a line item
- What condition is the retained fabric in? "Patch and repair as needed" is unquantifiable
  and belongs in contingency, not in a rate
- Is there a mould note or evidence of water ingress?
- Will the structure be re-verified after demolition exposes it?
- Site access constraints — tree protection zones, lane-only machinery access, hydro-vac
  requirements in root zones. These carry a real productivity premium
- Temporary works: hoarding, weather protection, dust walls, protection of retained finishes

## Answering conventions

- Unanswered questions carry a literal `?` and stay visible in the issued estimate
- An assumption carried pending an answer is stated inline where the number appears
- When an answer arrives, update the affected line and note the date
- Questions that never get answered become exclusions or P.C. allowances at issue — they do
  not quietly disappear
