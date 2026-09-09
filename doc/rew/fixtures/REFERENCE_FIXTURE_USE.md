# Amplifier-Output Reference Fixture — Use

Lifecycle: **CURRENT PROCEDURE**
Release: **approved for controlled powered-amplifier bench use**
Owns: pre-use inspection, connection, startup, stop rules, and interface
applicability.
Specification:
[`REFERENCE_FIXTURE_SPECIFICATION.md`](REFERENCE_FIXTURE_SPECIFICATION.md)
Qualification:
[`../qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md`](../qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md)
Last reviewed: 2026-09-09

## 1. Applicability And Boundaries

The fixture is the complete path from one SU-V570 speaker-output pair through
the red/black input cable, insulated attenuator/clamp, short TRS tail, and plug
to an interface input. It references amplifier-terminal voltage; it does not
carry loudspeaker current and is not a speaker load, mains-isolation device,
protective-earth connection, or substitute for appliance-safety testing.

The passive fixture and its cables passed the dated electrical qualification.
Its original interface release was for UMC202HD Input 2 central TRS in `LINE`
mode. Its use with UMC22 `INST 2` is separately risk-accepted and qualified by
[`../qualification/UMC22_FRD_QUALIFICATION.md`](../qualification/UMC22_FRD_QUALIFICATION.md).
Interface contact maps, phantom behaviour, gains, input limits, and calibration
do not transfer between interfaces.

Use this fixture only on the same amplifier channel and speaker bank as the
driver under test. Do not change between amplifier-terminal and driver-terminal
reference planes without documenting the change.

## 2. Pre-Use Inspection

With every item unpowered and disconnected from USB:

1. Inspect the bare-wire red/black termination. Both conductors must be fully
   captured, secure, insulated, and free of stray strands that could bridge
   binding posts.
2. Inspect the approximately `6 cm` multilayer heat-shrink body for cuts,
   abrasion, softening, discoloration, crushing, looseness, or exposed internal
   structure.
3. Gently check both cable exits and the TRS plug clamp. A moderate pull must
   transfer into strain relief, not a solder joint.
4. Confirm the red lead is marked/identified positive and black negative.
5. Confirm the TRS plug and selected input are the intended interface path.
6. Inspect any temporary breakout terminal block for restraint, insulation,
   stray strands, and separated tip/ring/sleeve nodes. Use it only for a
   specified check; remove it for normal measurement.

If the fixture, adaptor, breakout, or playback cable has been altered or
damaged, do not rely on the old release. Repeat the affected resistance and
functional qualification, not every historical test indiscriminately.

## 3. Switched-Off Connection

1. Stop REW Generator, Check Levels, and Measure; stop other application audio.
2. Switch the SU-V570 off and turn its volume fully down. Disconnect interface
   USB and turn phantom off. Set interface output and input gains fully down and
   Direct Monitor off.
3. Connect the selected interface output through its already mapped playback
   cable to SU-V570 `AUX` left. Keep `POWER AMP DIRECT` off, tone `DEFEAT`, and
   loudness off unless a revised procedure explicitly says otherwise.
4. Connect the driver separately to the chosen speaker-output pair.
5. At the same pair, connect fixture red/`In+` to positive and black/`In-` to
   negative. The fixture cable must not carry driver current.
6. Insert the fixture output only into the qualified interface input:
   UMC202HD Input 2 central TRS in `LINE`, or UMC22 `INST 2` under its own
   procedure. Leave the input's unrelated contacts and sockets unused.
7. Connect the measurement microphone before enabling phantom. Leave unused
   output and headphone sockets empty as required by the interface procedure.

For a first gross reference-level check only, a passed breakout may be inserted
between fixture and input. Restrain and insulate it before power. Do not reuse
the `100 kohm` phantom-isolation adaptor as an audio breakout.

## 4. Startup And Level Check

1. Connect USB with the amplifier still off. Enable phantom only after the
   microphone connection is secure. Confirm normal indication, no clip LED,
   silence, and no instability, heating, or smell.
2. Power the SU-V570 at minimum volume with every generator stopped. Observe for
   approximately one minute on a newly assembled route. Stop for transient or
   sustained hum/buzz, clipping, instability, heat, smell, or smoke.
3. Set the interface output to the qualified position. With a true-RMS meter
   at the electrical reference plane and the authorised low-level tone, raise
   amplifier volume slowly to the active procedure's stated voltage target and
   frequency, then stop the tone immediately. The completed raw-driver and
   Seed A packages used different reference planes and levels; do not inherit
   `1.00 V RMS at 1 kHz` as a universal setting.
4. If the runbook requests a gross fixture check, stop the tone before moving
   the meter, connect at the restrained breakout, and confirm the protected
   reference is broadly one tenth of the amplifier-output voltage (for example,
   `80-120 mV RMS` for `1.00 V RMS`).
   Stop, restore the meter to the driver, remove the breakout, and connect the
   fixture directly to the input before measurement.
5. With signal stopped, verify useful reference-channel headroom and no
   clipping, dropout, material noise, or movement-sensitive pickup. Exact
   attenuation and noise are measurement-quality checks, not reasons to repeat
   completed high-voltage qualification.

The true-RMS meter establishes driver voltage. REW's electrical reference
normalises amplifier gain/response but does not independently prove absolute
driver voltage.

## 5. Global Stop Rules

Stop immediately and de-energise safely for:

- an unexpected low-resistance path or open intended path;
- a wrong connector/contact, reversed polarity, loose strand, or altered
  reference channel/bank;
- unstable DC, current-limit operation, clipping, reference dropout, or
  unexplained noise;
- excessive component or cable heating;
- insulation damage, exposed conductor, smell, smoke, visible spark, or
  perceptible tingle; or
- any amplifier, PC, loudspeaker, or personal-safety concern.

Do not touch, reconnect, or move meter leads while a signal is present. Do not
use anticipated loudness or amplifier volume position as protection. Do not use
the heat-shrink fixture for permanent installation, crushing, abrasion,
unattended operation, or after visible/tactile damage.

If a stop condition is a physical/electrical failure, keep the fixture
unapproved until the cause is understood and every affected gate passes again.
If it is only a measurement-quality failure, preserve the result and follow the
active interface procedure before deciding whether more hardware testing is
justified.
