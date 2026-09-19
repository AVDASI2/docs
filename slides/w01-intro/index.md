---
marp: true
theme: flightlab
paginate: true
header: "AVDASI 2 · Avionics & Mechanisms"
footer: "Dr. Steve Bullock · Week 1"
title: "Week 1: Avionics & Mechanisms introduction"
description: "Full-cohort introduction to the Avionics and Mechanisms strands of AVDASI 2, 2026-27."
author: "Dr. Steve Bullock"
---

<!-- _class: title -->

# Avionics & Mechanisms

## AVDASI 2 · Week 1 introduction

Dr. Steve Bullock
Tuesday 22 September 2026

<!--
Full cohort, 1.40 Pugsley, 12:00–13:00. Everyone is here, not just the avionics
and mechanisms specialists: the first half is for everyone, the second half is
mostly logistics for the specialists but everyone should hear it once.

Timing guide (60 min): who & where 5 · why it matters 10 · requirements 15 ·
integration 15 · workshops & before Friday 10 · questions 5.
-->

---

# Today

1. Who we are, and where things happen
2. What avionics and mechanisms do in *your* aircraft
3. What the requirements specification asks for
4. Integration: where avionics meets every other division
5. The workshops, and what to do before Friday

---

# Who's who

<div class="columns">
<div>

**Teaching**

- **Steve Bullock**: avionics lead
- **George**: teaching and coordination, Thu & Fri
- **Robin Carter**: PhD from 1 Oct, has flown these autopilots on the MSc Aerial Robotics project

</div>
<div>

**Labs and kit**

- **Tim**: avionics kit issue and return, M.003
- **Jasmin**: lab coverage

**Unit coordinators**

- **Jasmin** and **Mark**

</div>
</div>

<!--
TODO(Steve): check names and roles as you want students to see them — first
names only from the Teams thread; add surnames/emails if wanted. Jas/Jasmin
assumed to be the same person. Mechanisms lead?
-->

---

# Where things happen

| Space | Room | What for |
|---|---|---|
| **Stacks Room** | QB F.05, under the QB library | Avionics workshops, Fri 09:00–11:00 |
| **Avionics lab** | M.003 | Kit issue, supervised tool use |
| **The Hangar** | L.080 | Main lab, open access |
| **Fabrication lab** | 0.080 | Fabrication |

<!--
TODO(Steve): check the fabrication lab room number (message said "above it in
0.080"), and when supervised hours in M.003 will run.
-->

---

<!-- _class: section -->

# Why avionics and mechanisms?

## Every division depends on them

---

# The model is only as good as what moves it

- Your wind-tunnel model has **control surfaces**, and something has to move them repeatably
- Your test campaign needs **data**, and something has to measure, time-stamp and log it
- Your aerodynamicists need **the angle you asked for**, not the one you got

Avionics and mechanisms turn a shaped piece of foam and carbon into an **instrumented test article**.

<!--
Pitch this at the whole cohort: aero, structures and design students all
depend on this strand working. The mechanisms team connects the servo to the
surface; the avionics team decides which servo, commands it, and records what
happened.
-->

---

# Flight-grade kit, off-design

- **Cube Orange+** autopilot running **ArduPilot**, the Flight Lab's standard research autopilot
- Flown for volcano monitoring, conservation, humanitarian work and search and rescue
- In AVDASI 2 it's **bolted into a wind tunnel**, with no GPS and restricted movement, and you command surfaces directly

That's deliberately off-design. Much of the avionics work is getting a flight controller to behave usefully on the ground.

---

<!-- _class: section -->

# The requirements specification

## What it asks of avionics and mechanisms

---

# Avionics requirements

<div class="callout">

**Placeholder.** Fill in from the requirements specification: the avionics requirements, with their IDs.

</div>

- requirement: what it means in practice
- requirement: what it means in practice
- requirement: what it means in practice

<!--
TODO(Steve): populate from the requirements spec once uploaded. One slide per
group of related requirements; quote the IDs so students can trace them.
-->

---

# Mechanisms requirements

<div class="callout">

**Placeholder.** Fill in from the requirements specification: the mechanisms requirements, with their IDs.

</div>

- requirement: what it means in practice
- requirement: what it means in practice

<!--
TODO(Steve): populate from the requirements spec. Who teaches the Mechanisms
sessions (Thu 11:00–13:00, 1.59 Design Suite, weeks 3–5)?
-->

---

# What "done" looks like

<div class="callout">

**Placeholder.** The minimum working example, stated against the requirements, plus how it's assessed.

</div>

- The step-by-step guide gets every avionics team to a **minimum working example**
- Your design builds on it; there are many routes to the requirements

<!--
TODO(Steve): the MWE's scope and how avionics feeds the assessment.
-->

---

<!-- _class: section -->

# Integration

## Where avionics meets every other division

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
Draft integration notes. The key message: avionics can't be designed in
isolation, and each interface has an owner on both sides. Encourage companies
to write these down early (an interface control table) and revisit at each
design review.
-->

---

# Interfaces to pin down early

- **Torque and travel**: what the surface needs, and what the servo can give with margin at a stall
- **Power**: what each component draws, at what voltage, from which supply
- **Connectors and cables**: which plug, which route, and who crimps it
- **Data**: what's logged, at what rate, in what units and file format, and who uses it
- **Command**: who moves which surface in the tunnel, and how you stop it

<!--
"Stall" here means the servo stall, not aerodynamic stall — flag the double
meaning. Stalled servos draw amps (guide step 05).
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
TODO(Steve): replace with a single system diagram (the review's B8 bench
wiring figure would serve both the guide and this slide).
-->

---

<!-- _class: section -->

# The workshops

## Avionics specialists: this part's for you

---

# Avionics workshops

| Week | Date | Where | Provisional focus |
|---|---|---|---|
| 1 | **Fri 25 Sep**, 09:00–11:00 | Stacks Room + M.003 | Kit issue; Cube, Mission Planner, telemetry, power |
| 2 | Fri 2 Oct, 09:00–11:00 | Stacks Room | Servos and Lua scripting (run by George) |
| 3 | No session | | Company Day, Fri 9 Oct |
| 4 | Fri 16 Oct, 09:00–11:00 | Stacks Room | Sensors: ADC and I²C |
| 5 | Fri 23 Oct, 09:00–11:00 | Stacks Room | To be confirmed: extra support |

Mechanisms: Thursdays 11:00–13:00, 1.59 Design Suite, weeks 3–5.

<!--
Provisional focus follows the step-by-step guide (review E). Confirm before
Tuesday. Wind-tunnel test plan review is week 7.
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

# Before Friday

- **Install Mission Planner on a Windows laptop.** It's Windows-only; one working laptop per group at minimum
- **Bring** that laptop, charged
- **Read** the guide's index, *Kit* and *Cube* pages

<div class="callout">

avdasi2.github.io/docs → Avionics → Step-by-step guide

</div>

<!--
TODO(Steve): confirm the laptop policy (lab loan laptops? Mac users?) before
saying this. See review B5.
-->

---

# Where to find things

- **The guide**: avdasi2.github.io/docs
- **Unit information, spec and assessment**: SharePoint
- **Questions**: Teams, or ask in the workshops
- **Found an error in the guide?** Raise an issue or a pull request on GitHub; it's open for exactly that

---

<!-- _class: title-inverted -->

# Questions

## See you on Friday, 09:00, Stacks Room
