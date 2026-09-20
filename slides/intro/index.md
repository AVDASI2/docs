---
marp: true
theme: flightlab
paginate: true
header: "AVDASI 2 · Avionics"
footer: "Dr. Steve Bullock · Introduction"
title: "Avionics: introduction"
description: "Introduction to the Avionics strand of AVDASI 2, 2026-27."
author: "Dr. Steve Bullock"
---

<!-- _class: title -->

# Avionics

## AVDASI 2 · Introduction

Dr. Steve Bullock

<!--
Full cohort, 1.40 Pugsley, 12:00-13:00, avionics then Mechanisms.

HARD STOP 12:50. FDAC control lecture 1 is 13:00-15:00 in this room, and the
TSRs set the Quanser rig up during this hour. So it's 25 minutes each, not 30:
avionics 12:00-12:25, Mechanisms 12:25-12:50. There is no slack for
overrunning, and questions have to come out of the 25.

Timing guide (25 min): opening and who's who 3 · why avionics 4 ·
requirements 6 · integration 6 · workshops and getting ready 4 · questions 2.

If time is short, cut "The system on the bench and in the tunnel" (it's in the
guide) and "Where to find things" (it's on the last slide anyway).
-->

---

# Today

1. Who we are, and where things happen
2. What avionics does in *your* aircraft
3. What the requirements ask for
4. Integration: where avionics meets every other division
5. The workshops, and how to get ready

---

# Who's who, and where

<div class="columns">
<div>

**Teaching**

- **Steve Bullock**: avionics lead
- **George**: teaching and coordination, Thu & Fri
- **Tim**: avionics kit issue and return
- **Robin Carter**: PhD from 1 Oct, has flown these autopilots on the MSc Aerial Robotics project

</div>
<div>

**Spaces**

- **Stacks Room**, QB F.05: workshops
- **Avionics lab**, M.003: kit issue, supervised tool use
- **The Hangar**, L.080: main lab, open access

</div>
</div>

<!--
TODO(Steve): check names and roles as you want students to see them. Jasmin
coordinates lab coverage; add if useful.
-->

---

# The model is only as good as what moves it

- Your wind-tunnel model has **control surfaces**, and something has to move them repeatably
- Your test campaign needs **data**, and something has to measure, time-stamp and log it
- Your aerodynamicists need **the angle you asked for**, not the one you got

Avionics turns a shaped piece of foam and carbon into an **instrumented test article**.

<!--
Pitch this at the whole cohort: aero, structures and design students all
depend on this strand working.
-->

---

# Flight-grade kit, off-design

- **Cube Orange+** autopilot running **ArduPilot**, the Flight Lab's standard research autopilot
- Flown for volcano monitoring, conservation, humanitarian work and search and rescue
- In AVDASI 2 it's **bolted into a wind tunnel**, with no GPS and restricted movement, and you command surfaces directly

That's deliberately off-design. Much of the avionics work is getting a flight controller to behave usefully on the ground.

---

# Avionics requirements

<div class="callout">

**Placeholder.** Fill in from the requirements specification: the avionics requirements, with their IDs.

</div>

- requirement: what it means in practice
- requirement: what it means in practice
- requirement: what it means in practice

<!--
TODO(Steve): populate from the requirements spec once uploaded. Quote the IDs
so students can trace them.
-->

---

# What "done" looks like

<div class="callout">

**Placeholder.** The avionics minimum working example (MWE), stated as the stream's own internal requirements, plus how it's assessed.

</div>

- The step-by-step guide gets every avionics team to a **minimum working example**
- The MWE has its own short requirements: a deliverable for the avionics stream, separate from the unit specification
- Your design builds on it; there are many routes to the requirements

<!--
TODO(Steve): the MWE's internal requirements (see PLAN.md) and how avionics
feeds the assessment.
-->

---

# Avionics is an integration job

| With | You need to agree |
|---|---|
| **Aerodynamics** | Surface sizes and deflections, and so hinge moments, and so servo torque |
| **Mechanisms** | Linkages, travel, backlash, end stops |
| **Structures** | Mounting, access, cable routes, mass |
| **Test** | Power, comms, what's logged, how it's handed over |

Every row is an **interface**. Interfaces agreed late are the ones that fail.

<!--
Encourage companies to write these down early, as an interface control table,
and revisit them at each design review.
-->

---

# Interfaces to pin down early

- **Torque and travel**: what the surface needs, and what the servo can give with margin at a stall
- **Power**: what each component draws, at what voltage, from which supply
- **Connectors and cables**: which plug, which route, and who crimps it
- **Data**: what's logged, at what rate, in what units and file format, and who uses it
- **Command**: who moves which surface in the tunnel, and how you stop it

<!--
"Stall" here means the servo stall, not aerodynamic stall - flag the double
meaning. Stalled servos draw amps.
-->

---

# The system on the bench and in the tunnel

<div class="columns">
<div>

**Power**

- Bench supply → power module → Cube
- Bench supply → BEC → servo rail → servos
- *Not* laptop USB for anything that moves

</div>
<div>

**Signals**

- Cube → servo signal pins → surfaces
- Sensors → ADC / I²C → Cube → log
- Cube ↔ Wi-Fi telemetry ↔ laptop running Mission Planner

</div>
</div>

<!--
TODO(Steve): replace with a single system diagram. The photo taken during
Thursday's bench test is meant to serve this and review item B8. Working
assumption: kits are ready and include BECs; the supply voltage is still to
confirm with Tim.
-->

---

# Avionics workshops

| Date | Where | Provisional focus |
|---|---|---|
| **Fri 25 Sep**, 09:00–11:00 | Stacks Room + M.003 | Kit issue; Cube, Mission Planner, telemetry, power |
| Fri 2 Oct, 09:00–11:00 | Stacks Room | Servos and Lua scripting (run by George) |
| Fri 16 Oct, 09:00–11:00 | Stacks Room | Sensors: ADC and I²C |
| Fri 23 Oct, 09:00–11:00 | Stacks Room | To be confirmed: extra support |

No session on Fri 9 Oct: Company Day. The schedule on SharePoint is the one to trust.

<!--
Every Friday 09:00-11:00 workshop sits on top of AENGM0073 in QB 1.18 LT, where
Steve is named as a lecturer alongside BK. Steve is asking BK what his share
actually is; until that comes back, treat these times as provisional and don't
promise more than the schedule does.
-->

---

# Friday: kit day

1. **09:00** A short taught intro in the Stacks Room: the kit, and the requirements in more depth
2. **From 09:30** Groups go up to **M.003** one at a time to collect a kit from Tim
3. **While you wait** Read the guide's first pages (*Kit*, *Cube*), with no hardware yet
4. **Kit in hand** Work through the guide to the Friday checkpoint
5. **To finish** How not to break each component

**Friday checkpoint:** Cube on Plane firmware, buzzer quiet, connected over Wi-Fi, running on bench power.

---

# Getting ready

- **Install Mission Planner on a Windows laptop.** It's Windows-only, and there are no laptops to borrow: each group needs one of its own
- **Bring** that laptop, charged
- **Read** the guide's index, *Kit* and *Cube* pages

<div class="callout">

Everything you need is on the **Getting ready** page: avdasi2.github.io → Avionics

</div>

<!--
Laptop policy, settled 20 Sep: no lab loan laptops. One Windows laptop per
group, a student's own, installed before Friday. Say this explicitly here -
it's the most likely thing to stall a group on the day.
-->

---

<!-- _class: title-inverted -->

# Questions

## See you on Friday, 09:00, Stacks Room
