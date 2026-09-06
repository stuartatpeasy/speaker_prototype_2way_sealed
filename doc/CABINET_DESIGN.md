# Cabinet and Mechanical Design

This file is the detailed mechanical source for the prototype enclosure. The high-level project state and documentation index are in [README.md](../README.md); driver and alignment evidence is in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md).

## 1. Prototype mechanical baseline

The enclosure geometry in **`3d_models/Prototype loudspeaker cabinet.dae`** records the design basis of the completed acoustically representative prototype. Further enclosure resizing or structural redesign is not planned before measurement of this build.

The prototype itself remains the dimensional authority for details that depend on actual purchased parts or manufacturing. Countersinks will be fitted to the actual screws, tweeter body and terminal clearance will be adjusted empirically, and the rear-panel centre landing will be fitted to the measured working compression of the actual gasket. Confirmed adjustments should be back-annotated into the CAD model.

This baseline freezes the initial enclosure design, not the damping distribution, finish, crossover, or later production refinements.

## 2. Enclosure alignment and volume

The enclosure is **sealed**, giving a predictable prototype with gradual bass roll-off, no port artefacts or below-tuning unloading, and straightforward integration with near-wall placement, a future subwoofer, or DSP high-pass.

The accepted body is approximately **280 × 430 × 300 mm**, giving about **23.65 L gross** and **21.7 L geometric net volume** before damping. The **20–24 L** range remains an acoustic reference, not permission to resize the accepted prototype. The target is well damped rather than maximally extended.

Published woofer parameters predicted approximately **Qtc 0.63 / Fc 54.7 Hz / F3 62 Hz**. The completed prototype must instead be assessed from its installed impedance and acoustic measurements; see [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md).

Width and depth modes remain clustered near **700 Hz**. Retain the present geometry and use bracing, damping, and measurement rather than resizing solely to separate them.

## 3. Cabinet construction

Locked construction choices:

- main cabinet panels: **18 mm plywood**;
- front baffle: two laminated layers of 18 mm plywood, total **36 mm**;
- final cosmetic finish likely to be veneer over the plywood;
- solid hardwood is not required structurally and is not expected to improve acoustic performance.

The cabinet must be airtight, accurately assembled, well braced, internally damped, and free from large unsupported panel spans.

### 3.1 Fastener schedule

To minimise distinct hardware types:

- **M4 × 30 mm black countersunk Pozi machine screws**: rear panel and tweeter, into M4 inserts;
- **M4 × 10 mm Type E non-flanged threaded inserts**: rear frame, centre-brace landing, and tweeter; selected for manufacturability and their ability to be recessed below the plywood surface;
- **No. 8 × 1 in black countersunk Pozi screws**: woofer, direct into plywood; a pragmatic prototype choice that may be improved later;
- **No. 4 × 3/4 in black countersunk Pozi screws**: speakON connector.

## 4. Front baffle

The current baffle design is considered substantially complete.

### 4.1 Overall geometry

- baffle size: approximately **280 × 430 × 36 mm**;
- woofer and tweeter vertically aligned;
- driver centre-to-centre spacing: **150 mm**;
- both drivers flush-recessed;
- no separate driver gaskets: both drivers use their manufacturer-fitted gaskets;
- woofer rear cut-out: approximately Ø148 mm for 18 mm behind the mounting plane, followed by an approximately 11.5 mm, 45° relief to Ø171 mm; this relief is retained to reduce throat reflection and basket shadowing;
- tweeter rear opening kept close to the required body clearance rather than heavily flared.

### 4.2 Edge treatment

All baffle edges use approximately **25 mm radius roundovers**. The side roundovers are most important; retain 25 mm where practical, prioritising a smooth and consistent profile. A reduction to 20 mm is an acceptable manufacturing fallback.

### 4.3 Driver mounting status

For the selected Ø8.5 mm **Type E non-flanged M4 inserts**, retain about **5 mm of sound plywood beyond the insert OD** to any free or cut edge—roughly **9.25 mm insert-axis-to-edge**—with 6 mm preferred and less than 4 mm high-risk. The modelled **Ø5.5 mm pilot is a deliberate, slightly undersized prototype choice**, not a drafting error; confirm insertion behaviour, holding strength, and resistance to ply splitting or delamination in an offcut of the actual plywood before machining the cabinet.

Tweeter mounting:

- recessed Type E non-flanged M4 inserts will be installed from the enclosure side of the baffle, behind the driver-body region; retention relies on their external thread rather than a flange;
- the front portion uses M4 clearance bores and the insert-sized pilots are confined to the rear portion;
- the rear opening includes local clearance around the two terminal “ears” without unnecessarily enlarging the opening around the rest of the tweeter body;
- exact body, terminal, connector, and wiring clearance will be fitted to the physical tweeter because the available 3D model is not a manufacturing drawing.

Prototype woofer mounting:

- basket, airflow, and edge-clearance constraints prevent suitable local mounting islands or conventional M4 wood inserts;
- the specified No. 8 × 1 in screws will be used directly in the plywood for the prototype;
- the accepted CAD uses approximately Ø3.0 mm pilots, slightly below the representative 3.10 mm thread-root diameter; confirm the actual screws in the complete plywood laminate;
- metal backing plates, captive nuts, or another repeatable fastening system remain possible later production refinements.

The woofer fasteners need only compress the flange gasket evenly. They should not be tightened to general-purpose metal-fastener torque.

### 4.4 Final machining checks

Before cutting a repeat or final baffle:

- measure the actual physical drivers;
- make test rebates in scrap;
- include clearance for veneer, adhesive, finish, and manufacturing tolerance;
- confirm flange depth after gasket compression;
- ensure adequate material remains between the two driver rebates;
- preserve full-thickness material around mounting points;
- verify the rear-installed tweeter inserts and corrected body clearance in a full-depth test piece;
- test the selected woofer fastening method in the complete 36 mm plywood laminate, including repeated removal and refitting, tightening feel, pull-out resistance, and any tendency for the plies to split or delaminate.

## 5. Other cabinet panels

The side, top, bottom, and removable prototype rear panel may remain simple rectangles. Exact cutting dimensions and joinery remain to be finalised.

## 6. Rear panel and prototype access

For the prototype, the rear panel should be:

- removable, flush or slightly recessed rather than proud;
- provided with deliberate peripheral assembly clearance for manufacturing tolerance and finish;
- sealed by **15 × 2 mm self-adhesive closed-cell neoprene sponge strip** around the perimeter only;
- fixed by M4 countersunk machine screws into recessed Type E non-flanged threaded inserts in the internal rear frame;
- sufficiently supported and evenly sealed so it does not become a large radiating panel.

Current rear-panel details:

- the approximately **242 × 392 mm** panel has about **1 mm clearance per edge** within the approximately 244 × 394 mm opening;
- 16 perimeter inserts are centred in approximately 20 mm-wide frame rails, about 10 mm from either rail edge;
- the panel screw holes use approximately **Ø4.5 mm shank clearance**; countersink angle, mouth diameter, and depth will be cut to the actual 90° M4 screw heads during the prototype build rather than copied literally from the current CAD representation;
- the main horizontal brace has no compressible centre gasket: it should meet the panel at a rigid central landing, with deliberate clearance elsewhere;
- the modelled central landing is approximately **40 mm wide**, uses the full brace thickness, and is fitted to the panel position only after the actual neoprene reaches a comfortable, repeatable working compression; the single central M4 screw supplies preload rather than bending the panel into contact or crushing the gasket to a nominal dimension.

The final production version may use a permanently glued rear panel after the crossover and damping are settled.

## 7. Prototype connector

The prototype brings woofer and tweeter connections out separately through a **Neutrik speakON NL4** so the development crossover can remain external. The connector and rear panel must remain airtight. A right-angle plug will enable the cabinet to remain at its design distance from the rear wall.

Pin allocation and development-crossover safety are specified in [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md).

## 8. Bracing

Use single-piece **window braces** fitted to the internal cross-section, with large openings and perimeter glue joints tying opposite panels together.

For the removable-rear prototype, the main brace does not depend on a permanent glue joint to the rear panel. Its small, rigid central landing is mechanically clamped to the panel, while the remainder of the brace edge stays at least approximately 1 mm clear to prevent intermittent contact or buzzing.

Likely initial bracing:

- one main horizontal window brace;
- secondary upper, lower, and rear-panel stiffeners;
- placement chosen to avoid the woofer magnet vent, terminals, and connector;
- generous openings so the enclosure remains one acoustically connected volume.

Selected brace corners are chamfered to ease installation of damping material; elaborate internal coving is not required.

## 9. Internal damping and stuffing

Use open, air-permeable **4 oz polyester/Dacron upholstery wadding**, chosen for clean, stable, and readily adjustable prototype damping.

Provisional use:

- one layer on the side, top, and bottom walls;
- two or more layers on the rear wall behind the woofer;
- optional additional loose fill in the remaining volume;
- keep clear of the woofer basket, cone, surround, pole-piece vent, terminals, and tweeter connections;
- do not compress it flat.

The amount and distribution must be recorded and adjusted using repeatable impedance and acoustic measurements. Treat the geometric 21.7 L volume separately from any damping-induced effective-volume increase.

## 10. Feet and support

Use four approximately **32 × 32 × 16 mm soft silicone-rubber feet**. Their installed rise is approximately **15 mm**, giving a supported cabinet height of about **445 mm**. They suit the intended shelf placement, reduce rattles and surface transmission, and provide repeatable positioning without spikes.

## 11. Open mechanical items

- final cutting list and detailed joinery for the 430 mm-high body;
- exact rear-panel countersink dimensions after trial fitting the actual screws;
- final working compression of the neoprene strip and resulting central-landing fit;
- exact empirical tweeter body, terminal, connector, and wiring clearance;
- any later production replacement for the prototype woofer wood-screw mounting;
- final damping quantity and distribution;
- inductor interlock and PCB restraint interfaces with the cabinet;
- final crossover mounting position;
- final veneer and finish.
