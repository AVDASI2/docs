# Status — AVDASI 2 Avionics

**Updated:** 20 Sep 2026 · **Repo:** `~/Documents/GitHub/docs` · **Branch:** `zensical-migration`, nothing pushed

A scheduling summary for `steve-todo`, in chunks rather than tasks. The detail
lives in [PLAN.md](PLAN.md) and [reviews/](reviews/); this file says what state
each chunk is in, what it's waiting on, and what can't move. Rewritten, not
appended to. Keep it under a screen.

*Hard dates* and *Waiting on other people* are rewritten whenever they change;
the rest is refreshed weekly or at a review. The Updated stamp above moves
either way.

## One line

The site is rebuilt and ready; the guide isn't, and Friday's workshop is what makes that urgent.

## Hard dates

| Date | What | Must be true beforehand | State |
|---|---|---|---|
| Tue 22 Sep, 12:00–12:50 | Avionics intro, 25 min, then Mechanisms 25 min | Requirements slides filled | Deck drafted and timed to 25 min; blocked on Steve's requirements spec review, expected today. **Hard stop 12:50**: FDAC control lecture 1 follows at 13:00 in the same room and the rig goes in during the hour |
| Thu 24 Sep | Bench test, one kit | A kit available, reset as a student would find it | Not confirmed. Decides review item B1 (can a servo move without arming after a firmware reset), and the wiring photo taken there serves B8 and the deck's system-diagram placeholder |
| Fri 25 Sep, 09:00–11:00 | Workshop 1, kit issue, Steve and George jointly | Guide's must-fix items done; SSIDs pre-renamed during kit prep | Proceeding on the assumption that kits are ready and include BECs; Tim asked, no reply. Workshop time provisional: it collides with AENGM0073, and Steve is asking BK what his share is |
| Fri 2 Oct, 09:00–11:00 | Workshop 2, George alone | George has draft curriculum and resources, with reading time; B1 answer | Blocked on Steve for the materials. Same AENGM0073 clash |

## Waiting on other people

| Who | What | Lead time |
|---|---|---|
| Steve → George | Draft curriculum and resources for workshop 2 to review | Well before Fri 2 Oct; George is confirmed and booked, and is blocked until this arrives |
| Steve | Requirements spec review, then curriculum review | Blocks the deck's two requirements placeholders for Tuesday, and the workshop plan after that |
| Tim | Kit verification K1–K9: BEC model and servo rail power, PSU voltage and XT60s, large servo model, ADC headers, prep jobs done | Asked, no reply. We are proceeding on assumption; correct the pages if it turns out wrong |
| Tim | Pre-rename telemetry SSIDs to kit numbers | Happens during kit prep, can't be done on the day |
| BK | What Steve's actual share of AENGM0073 is | Decides whether every Friday workshop slot stands |

## Chunks

| Chunk | State | Detail |
|---|---|---|
| Site rebuild: Zensical, theme, move to the root domain | Done, unpushed | PLAN.md |
| Publishing: draft and live split, ports, redirect for old links | Done, unpushed | README.md |
| Step-by-step guide review | Reviewed; B5 closed, K1 assumed; the rest awaiting Steve's decisions | reviews/2026-09-19-stepbystep.md |
| Guide must-fix items before Friday | Not started. A batch of independent decisions, splittable if you need finer scheduling | Review sections B and K |
| Intro deck | Drafted and cut to 25 min; blocked on the requirements spec for two placeholder slides | slides/intro/ |
| Kit pages | Done | docs/avionics/kit-list.md |
| Servos content, shared with Mechanisms | Not started. One piece of work serving both strands, so write it once | PLAN.md |
| Internal MWE requirements | Not started | PLAN.md |
| Push and go live | Blocked on the guide fixes; everything else is ready and Steve has approved pushing | PLAN.md |
| Annual update process | Done | teaching/annual-update.md |

## Parked, deliberately

- Workshop topics for weeks 2–5: provisional until the curriculum review.
- Toolchain decisions: after the requirements and curriculum reviews.
- Licence and contributor credit: before going public, not before Friday.
- Mechanisms as a whole: taught separately, and not in this repo. The exception
  is servos, above.

## Structural moves

Files that moved, so references elsewhere don't rot:

| When | Was | Now |
|---|---|---|
| 20 Sep | `slides/w01-intro/` | `slides/intro/` |
| 20 Sep | `docs/avionics/sessions/w01-intro.md` | `docs/avionics/intro.md` |
| 20 Sep | `docs/avionics/sessions/index.md` | Deleted; the schedule is canonical on SharePoint |
| 20 Sep | Kit list inside `stepbystep/00-kit.md` | `docs/avionics/kit-list.md` |
| 20 Sep | `docs/slides/` committed | Built by CI, no longer committed |
| 19 Sep | Site at `avdasi2.github.io/docs` | Root of `avdasi2.github.io` |
