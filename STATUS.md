# Status — AVDASI 2 Avionics

**Updated:** 20 Sep 2026 · **Repo:** `~/Documents/GitHub/docs` · **Branch:** `zensical-migration`, nothing pushed

A scheduling summary for `steve-todo`, in chunks rather than tasks. The detail
lives in [PLAN.md](PLAN.md) and [reviews/](reviews/); this file says what state
each chunk is in, what it's waiting on, and what can't move. Rewritten, not
appended to. Keep it under a screen.

## One line

The site is rebuilt and ready; the guide isn't, and Friday's workshop is what makes that urgent.

## Hard dates

| Date | What | Must be true beforehand | State |
|---|---|---|---|
| Tue 22 Sep | Avionics intro, 25 min | Requirements slides filled; laptop policy decided | Deck drafted, placeholders open |
| Thu 24 Sep | Bench test, one kit | Tim confirms a kit is available | Not confirmed |
| Fri 25 Sep | Workshop 1, kit issue | Guide's must-fix items done; kit list confirmed; SSIDs pre-renamed | At risk, depends on Tim |
| Fri 2 Oct | Workshop 2, George alone | Written handover from workshop 1; B1 arming answer | Not started |

## Waiting on other people

| Who | What | Lead time |
|---|---|---|
| Tim | Kit questions K1–K9: servo rail power (no BEC), PSU voltage, large servo model, ADC headers, prep jobs done | Before Fri 25 Sep, and kit prep happens first |
| Tim | Pre-rename the telemetry SSIDs to kit numbers | During kit prep, can't be done on the day |
| George | Workshop 1 attendance, bench test, workshop 2 cover | Needs to be in the room on 25 Sep |
| Steve | Requirements spec review, then curriculum review | Blocks the deck's placeholders and the workshop plan |

## Chunks

| Chunk | State | Detail |
|---|---|---|
| Site rebuild: Zensical, theme, move to the root domain | Done, unpushed | PLAN.md |
| Publishing: draft and live split, redirect for old links | Done, unpushed | README.md |
| Step-by-step guide review | Reviewed, fixes not applied | reviews/2026-09-19-stepbystep.md |
| Guide must-fix items before Friday | Not started, needs Steve's decisions | Review sections B and K |
| Intro deck | Drafted, placeholders open | slides/intro/ |
| Kit pages | Done | docs/avionics/kit-list.md |
| Internal MWE requirements | Not started | PLAN.md |
| Push and go live | Blocked on the above | PLAN.md, "Moving to avdasi2.github.io" |
| Annual update process | Done | teaching/annual-update.md |

## Parked, deliberately

- Mechanisms: taught separately this year, and out of this repo entirely.
- Workshop topics for weeks 2–5: provisional until the curriculum review.
- Toolchain decisions: after the requirements and curriculum reviews.
- Licence and contributor credit: before going public, not before Friday.
