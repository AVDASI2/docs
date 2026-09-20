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
4. Intro lecture: plan the avionics content in more depth (25 minutes)
5. Curriculum review
6. Toolchain options: Mission Planner and macOS, Lua or pymavlink, MATLAB or Python for logs. After the spec and curriculum reviews

## Moving to avdasi2.github.io

The site moves from `AVDASI2/docs` (served at `avdasi2.github.io/docs`) to the
org Pages repository `AVDASI2/avdasi2.github.io`, so it is served at the root.
Its Jekyll landing page is replaced: that page's content is now on the Zensical
home page. Old `/docs` links redirect to the new root.

Old `/docs` links redirect to the new root: see `migration/README.md`.

Steps, all of which need Steve's GitHub access:

1. Push this branch to `AVDASI2/docs` first, so the work and the snapshot tags
   (`v2025-26-mkdocs`, `v2025-26-site`) are backed up
2. Clone `AVDASI2/avdasi2.github.io`, and replace its contents with this
   repository's, on a branch
3. Check the build, merge, and set Settings > Pages > Source to **GitHub Actions**
4. Confirm <https://avdasi2.github.io> serves the new site
5. In `AVDASI2/docs`: publish the redirect from `migration/docs-redirect/` on
   `gh-pages` (see `migration/README.md`), remove the CI workflow, add a note to
   the README pointing at the new home, and archive the repository. Keep the
   repository: it holds the snapshot tags
6. Move any open issues to the new repository first, if there are any

## Publishing model

Two sites from one source, as in CADE30008: the in-progress site is everything
in `docs/` and is local only; the live site is only what `publish.yaml` lists.
See the README. `publish.yaml` currently lists everything that was already
public on the old site, so the gate only holds back new or reworked pages.

## Scheduling

[STATUS.md](STATUS.md) is the scheduling summary that `steve-todo` reads: chunks,
hard dates and who we're waiting on, with the detail left here. Rewrite it when
this plan changes. Its format is being agreed with the steve-todo session.

## To do

- [x] **Kit list on the site** (19 Sep). The *Kit List Print* sheet from `2025-26/.../lab/AVDASI2 Avionics kits.xlsx` is now on the Kit page (`00-kit.md`). Assumed correct until Tim confirms. Issue and return process still to add
- [ ] **Verify the kit assumptions with Tim** (review addendum K1–K9). Asked, no reply yet; we are proceeding on the assumption that the kits are ready and include BECs. Still to confirm: the supply voltage and which XT60 goes where, the large servo model, ADC header soldering, and whether the 2025-26 prep jobs are done
- [ ] **Internal MWE requirements.** A short requirements spec for the avionics minimum working example: a deliverable for the avionics stream, separate from the unit-level spec. The intro deck's "What done looks like" slide refers to it
- [ ] **Intro deck** (`slides/intro`): 25 minutes of avionics, then 25 on Mechanisms. **Hard stop 12:50**: FDAC control lecture 1 follows at 13:00 in the same room, and the rig is set up during the hour. Fill the requirements placeholders after the spec review
- [ ] **Servos, shared with Mechanisms.** Servo content serves both strands, so write it once. Mechanisms is otherwise taught separately: Steve on theory and design tools (Linkage app, cardboard prototyping) with the intro and Mech 2; Mark Graham and Vince Maes on implementation (2D to 3D, bearings) with Mech 4; Mech 3 proposed as joint
- [ ] **Confirm the Friday workshop slot.** Every Friday 09:00-11:00 workshop collides with AENGM0073 (QB 1.18 LT), where Steve is named as a lecturer. Steve is asking BK what his share is; until then the workshop times are provisional
- [ ] **Bench test** of guide pages 00–05 on a freshly reset kit before Friday (review, section H)
- [x] **Marp theme** (20 Sep). Published as `BristolFlightLab/marp-template`; `package.json` pins `#v1.0.0`, CI builds the decks, and `docs/slides/` is no longer committed. The CI slide build is untested until the first push; if it fails, commit `docs/slides/` again as a fallback
- [ ] Before going live: decide the licence (CC BY 4.0, as in the control course?) and how to credit past contributors
- [ ] Consider an AGENTS.md, as CADE30008 has, once the conventions settle
- [ ] Run the [annual update](teaching/annual-update.md) each year; it starts with notes written while teaching is fresh

## Future

- Whole-unit context, and goals for sharing resources and external profile
- Parallel guidelines for the MSc Aerial Robotics Group Project (ARGP; Holybro X650, Cube autopilots). Overlaps with this guide; AVDASI 2 is wind-tunnel only

## Noticed in the teaching schedule

- Company Day is listed as "Friday 10-Oct"; the Friday of week 3 is 9 Oct
- TB2 dates are shown as 2026; they should be 2027
