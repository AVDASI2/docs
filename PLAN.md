# Plan: AVDASI 2 Avionics refresh, 2026-27

Working notes for the refresh. Everything is on branch `zensical-migration`; **nothing is pushed until the whole new site goes live at once**. The rollback tags `v2025-26-mkdocs` and `v2025-26-site` are local until then.

## Phases

1. ~~MkDocs → Zensical, Flight Lab theme~~ (done, 19 Sep)
2. Curriculum review: discussion, PowerPoint uploads, session design
3. Deploy the refreshed curriculum, with Marp slides

## Order of work

The unit requirements spec review comes **before** the curriculum review, because the curriculum depends on it. Claude: nudge Steve about the spec review before starting the curriculum review.

1. Unit requirements spec review (Steve, separate session)
2. Review `reviews/2026-09-19-stepbystep.md` together: all B (must fix) and C (should fix) items, the Friday session fit, and the "How not to break it" page
3. Provisional workshop topics for weeks 2–5 (the table on the intro deck and on Sessions 2026-27)
4. Intro lecture: plan both parts in more depth
5. Mechanisms strand review (Claude supporting)
6. Curriculum review
7. Toolchain options: Mission Planner and macOS, Lua or pymavlink, MATLAB or Python for logs. After the spec and curriculum reviews

## To do

- [x] **Kit list on the site** (19 Sep). The *Kit List Print* sheet from `2025-26/.../lab/AVDASI2 Avionics kits.xlsx` is now on the Kit page (`00-kit.md`). Assumed correct until Tim confirms. Issue and return process still to add
- [ ] **Questions for Tim** from the kit cross-check (review addendum K1–K9): how the servo rail is powered (there's no BEC), the supply voltage and which XT60 goes where, the large servo model, ADC header soldering, and whether the 2025-26 prep jobs are done
- [ ] **Internal MWE requirements.** A short requirements spec for the avionics minimum working example: a deliverable for the avionics stream, separate from the unit-level spec. The intro deck's "What done looks like" slide refers to it
- [ ] **Intro deck** (`slides/w01-intro`), Tue 22 Sep: now split into Part 1 Avionics and Part 2 Mechanisms. Fill the requirements placeholders after the spec review, and resolve the TODOs in the speaker notes (names, fabrication lab room, laptop policy, Mechanisms lead)
- [ ] **Bench test** of guide pages 00–05 on a freshly reset kit before Friday (review, section H)
- [ ] **Marp theme.** `flightlab-marp-template` is committed and tagged `v1.0.0` (19 Sep) but has no remote. Once it's pushed: point `package.json` at `github:<org>/<repo>#v1.0.0`, add a slide build to CI, and stop committing `docs/slides/`
- [ ] Before going live: the home page still says "Material for MkDocs"; decide the licence (CC BY 4.0, as in the control course?) and how to credit past contributors

## Future

- Whole-unit context, and goals for sharing resources and external profile
- Parallel guidelines for the MSc Aerial Robotics Group Project (ARGP; Holybro X650, Cube autopilots). Overlaps with this guide; AVDASI 2 is wind-tunnel only

## Noticed in the teaching schedule

- Company Day is listed as "Friday 10-Oct"; the Friday of week 3 is 9 Oct
- TB2 dates are shown as 2026; they should be 2027
