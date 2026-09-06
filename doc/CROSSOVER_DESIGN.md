# Crossover Design

> - **Lifecycle:** ACTIVE DESIGN AUTHORITY
> - **Owns:** current acoustic direction, driver polarity/topology, NL4 allocation, evidence dependencies, validation gates, and open design decisions
> - **Does not own:** detailed component-bank and inductor construction engineering; installed-driver evidence; measurement procedures
> - **Current decision:** develop an approximately 2.2–2.4 kHz LR4-like acoustic crossover from installed ZMA and common-timing FRD data; no circuit or component value is frozen
> - **Next gate:** export the approved C6 woofer source capture, acquire a protected common-timing tweeter response, then optimise a realizable external network and validate the measured sum and load
> - **Limitations:** no durable woofer FRD export or approved tweeter FRD yet; known local woofer early-tail uncertainty near 2.03 kHz; component values and acoustic polarity remain provisional
> - **As of:** 2026-09-06

This file is the active passive-crossover design authority. The project overview is in [README.md](../README.md), current driver evidence and approved impedance sources are in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md), and detailed prototype-component engineering is in [CROSSOVER_COMPONENT_DEVELOPMENT.md](CROSSOVER_COMPONENT_DEVELOPMENT.md).

All crossover values remain exploratory until the approved C6 woofer capture is
exported, a common-timing tweeter magnitude/phase response is acquired, and the
prototype network is validated acoustically and electrically. Directivity and
distortion remain later validation gates rather than reasons to block the first
reversible external-network iteration.

## 1. Prototype interface and external crossover

The prototype brings the woofer and tweeter out separately through a **Neutrik speakON NL4**.

Pin allocation:

- 1+ : woofer positive;
- 1− : woofer negative;
- 2+ : tweeter positive;
- 2− : tweeter negative.

The robust, keyed four-pole connector keeps the development crossover on the bench, permits easy substitution and polarity reversal, and avoids repeatedly disturbing the cabinet and damping.

The crossover should initially be mounted externally on a board with secure terminals and enough room to swap components. Development-inductor taps must remain accessible so that inductance can be reduced by changing the connected tap rather than cutting off copper. Unused outer winding sections must remain open-circuit, insulated, and mechanically restrained. Do not switch taps with the amplifier energised, and never permit an unused winding section to form a shorted turn.

## 2. Crossover design direction

Design the passive crossover from measured driver responses and impedance in the actual enclosure, not nominal impedances and textbook equations alone.

Current provisional acoustic target:

- crossover region: approximately **2.2–2.4 kHz**, subject to measurement;
- likely target: roughly **fourth-order Linkwitz–Riley acoustic slopes**;
- exact electrical order may differ because the drivers’ natural responses contribute to the final acoustic slopes;
- partial rather than full baffle-step compensation;
- tweeter attenuation required;
- possible woofer impedance equalisation or breakup suppression only if measurements justify it;
- final system impedance and phase must be checked.

Use steeper sixth-order slopes only to solve a measured protection or breakup problem. The normal low-frequency woofer impedance peak does not itself require crossover correction.

## 3. Evidence and model dependencies

Use only the approved installed ZMA sources identified in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md). Phase-bearing FRD data must share a valid electrical timing reference and fixed measurement geometry; use the current method and runbook routed by [MEASUREMENT_WORKFLOW.md](MEASUREMENT_WORKFLOW.md).

The useful present crossover-region loads near 2.30 kHz are approximately:

- woofer: 7.98 ohm at +10.8 degrees;
- tweeter: 3.48 ohm at -5.0 degrees.

These complex loads replace nominal driver impedances in every exploratory
model. The approved C6 installed-woofer source capture is sufficient for initial
prototype modelling once exported with its documented common timing and window;
the corresponding protected tweeter response is still required before acoustic
optimisation. Include measured component capacitance, inductance, DCR,
tolerances, driver spacing, baffle diffraction, and the complete system
impedance/phase in the model. Treat textbook tables and optimiser output as
seeds, particularly if optimisation produces extreme or implausible values.

## 4. Excursion and power philosophy

Do not design for routine operation at rated Xmax:

- normal use well below Xmax;
- loud passages remain below Xmax through most of the operating band;
- brief peaks may approach Xmax;
- Xmech/Xlim remain emergency limits, not operating targets.

Account for $Bl$, suspension and inductance variation, harmonic and intermodulation distortion, and thermal compression. The sealed near-wall alignment is not intended to extract heroic deep bass from one 6.5-inch midwoofer.

Tweeter power ratings must always be read with their specified high-pass condition. Do not apply an unfiltered broadband or low-frequency signal to the bare tweeter.

## 5. Required validation before freezing the crossover

1. Use only current, valid installed ZMA and phase-bearing FRD sources identified in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md).
2. Optimise for acoustic slopes, summed magnitude, directivity, impedance, and component constraints rather than textbook electrical values.
3. Build the crossover externally with measured component values and accessible taps.
4. Measure individual filtered drivers, normal-polarity sum, reverse-polarity null, horizontal off-axis response, distortion, and system impedance/EPDR.
5. Update the model with as-built component values and repeat one controlled change at a time.
6. Move the network inside only after the complete measured assembly is stable and thermally acceptable.

## 6. Open crossover items

- exact crossover frequency and topology;
- exact component values and acoustic polarity;
- final L(W1) development implementation: revised former or separate tapped trim inductor;
- inductor interlock, outer-layer binding, and PCB restraint;
- final system impedance classification and amplifier headroom;
- final crossover mounting position;
- whether DSP remains development-only or is used in the finished system.
