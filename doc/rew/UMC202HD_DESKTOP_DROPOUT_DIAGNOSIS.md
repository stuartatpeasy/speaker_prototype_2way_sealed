# UMC202HD Desktop Dropout Diagnosis

Date range: 2026-09-03 to 2026-09-04

Last revised: 2026-09-06

Status: **UMC202HD HARDWARE STRONGLY EXONERATED; DESKTOP UAC2/HOST PATH
UNRESOLVED; LIVE LINUX IS THE NEXT DISCRIMINATOR**

## 1. Scope And Current Conclusion

This file is the single authority for the recurring UMC202HD output-stream
dropout discovered during the first full-dual woofer checkout. The passive
reference fixture, SU-V570, analogue playback lead, loudspeaker, and REW are not
the distinguishing cause. The same UMC202HD plays continuously on a Windows 11
laptop; substituting the UMC22's known-good cable did not change the desktop
fault. The desktop drops out under both the Behringer driver and Microsoft's
USB Audio 2.0 class driver.

The current desktop binding is Microsoft `usbaudio2.sys`, driver
`10.0.26100.9168`; the Behringer `5.72.0` package is uninstalled. Do not
reinstall it merely to resume acoustic work: its observed dropout rate was much
worse. The separately qualified UMC22 installed-woofer route now carries the
first FRD work, so this diagnosis is no longer on that critical path.

## 2. Observed Symptom

- The first REW/ASIO tone at `1.00 V RMS` across the woofer muted for roughly
  `100-300 ms` every `1-3 s` while otherwise clean.
- UMC202HD clip indicators remained dark. Input `SIG` indicators followed the
  audible tone and extinguished during each mute.
- The true-RMS reading fell during interruptions, confirming loss of the source
  stream rather than an acoustic-only effect.
- The same interruption occurred in ordinary local Windows music with REW
  closed.

The earlier periodic DMM dip seen while Output 2 drove the clamp/attenuator is
therefore explained by the same source-stream fault. It is not evidence of an
active or unstable passive attenuator.

## 3. Evidence Matrix

Unless stated otherwise, tests used the same UMC202HD, local playback path,
SU-V570 `AUX` left input, speaker bank `B` left, and woofer. Qualitative early
rates are kept distinct from later counted runs.

| Test or change | Result | Consequence |
| --- | --- | --- |
| REW ASIO, initial `48 kHz`/`512` driver state against REW `88.2 kHz` | frequent dropout | exposed a real rate mismatch but not its cause |
| Matched REW/driver `88.2 kHz`, `1024` samples | unchanged frequent dropout | rate mismatch rejected as sufficient cause |
| Matched `48 kHz` REW tone | unchanged | high sample rate rejected |
| REW Java/WASAPI exclusive output, `48 kHz`, `32k` buffer | unchanged | native ASIO rejected as distinguishing cause |
| Local Windows music, REW closed | dropout reproduced | REW rejected as distinguishing cause |
| Second rear motherboard port, USB 2 to USB 3 | unchanged | tested external port/type rejected |
| Plain Windows restart | unchanged | stale session state rejected |
| UMC22 disconnected | unchanged | second interface rejected |
| UMC22's known-good USB cable substituted | unchanged | both tested cables unlikely |
| Same UMC202HD on Windows 11 laptop | no dropout | interface hardware strongly exonerated; desktop-specific path implicated |
| Behringer `5.72.0` removed; Microsoft UAC2 driver bound | `10/180 s`, then `12/300 s` | vendor binding aggravated but did not solely cause fault |
| Matched UMC22/Microsoft UAC1 control | `0/300 s` | common analogue path and general host latency not sufficient |
| UMC202HD `48-192 kHz`, five equal `308 s` runs | `21, 11, 18, 16, 19` | no useful sample-rate or payload correlation |
| Remove UMC22, StarTech interface, and Wi-Fi dongle | `16/308 s` | practical nonessential USB group rejected |
| Depower two unused Seagate disks | `21/308 s`; `45/924 s` | disks and retained `storport.sys` lead rejected as cause |
| Existing Windows High performance plan | `14/308 s` | generic CPU/power-plan change rejected |

The five-rate total was `85/1540 s = 0.0552 s^-1`. With the legacy disks
removed it was `66/1232 s = 0.0536 s^-1`. The difference is immaterial beside
run-to-run variation. The disks remain disconnected for independent idle-power
and ambient-noise benefits.

## 4. LatencyMon Findings

The raw LatencyMon reports are intentionally ignored by
`rew/*LatencyMon*.txt` because they expose private, project-irrelevant host
details. Decision-relevant results are retained here.

| Playback path | Audible result | Maximum interrupt/DPC observations |
| --- | --- | --- |
| UMC202HD, Microsoft UAC2 | `12/300 s` | about `12.1 ms`; longest DPC `storport.sys`; greatest cumulative DPC time `dxgkrnl.sys` |
| UMC22, Microsoft UAC1 | `0/300 s` | essentially the same about `12.1 ms` pattern |
| UMC202HD, legacy disks absent | `66/1232 s` | about `12.1-12.4 ms`; same named drivers |
| UMC202HD, High performance plan | `14/308 s` | about `11.3 ms` interrupt latency; same broad pattern |

The host latency excursions are credible possible triggers, but they are not
sufficient causes because the matched UMC22 run remained clean. LatencyMon also
reported inconsistent WMI and registry CPU speeds, so its calculated per-driver
execution duration requires caution. No event-level time correlation to an
audible dropout was captured.

## 5. Interface And Host Comparison

### 5.1 Desktop

- Windows 11 build family `26200`.
- Z97-generation desktop platform with 2014-era firmware.
- UMC202HD current Microsoft USB Audio 2.0 driver `10.0.26100.9168`.
- Current endpoint offers `24 bit` at `44.1`, `48`, `88.2`, `96`, `176.4`, and
  `192 kHz`.
- The former Behringer package was version `5.72.0.19646`, control-panel
  version `5.72.0`, dated `2024-12-04`.

### 5.2 Known-Good Laptop

- Windows 11 Enterprise build family `26200`.
- Microsoft `usbaudio2.sys 10.0.26100.8875`.
- Modern Intel USB 3.1/3.2 xHCI controllers.
- A separately enumerated Intel Smart Sound USB-audio device exists, but the
  broad device-name query does not prove it participates in the UMC202HD path.

The broad Windows generation is common, but the UAC2 patch level and USB host-
controller generation both differ. The comparison cannot isolate those two
variables.

## 6. Closed And Open Explanations

Closed as useful causes for this symptom:

- passive reference fixture, SU-V570, woofer, and playback lead;
- REW versus ordinary media playback;
- ASIO versus Java/WASAPI;
- sample-rate mismatch or higher aggregate USB payload;
- the two tested rear motherboard ports and two tested USB cables;
- the concurrently connected UMC22, StarTech interface, and Wi-Fi dongle;
- the two unused Seagate disks;
- generic Windows Balanced versus High performance power policy; and
- a defective UMC202HD that fails identically on another host.

Still open:

- installed Windows USB Audio 2.0 stack behaviour on this desktop;
- UAC2 driver revision interaction;
- Z97-generation xHCI/controller or firmware interaction; and
- a host latency event which UAC1 tolerates but this UAC2 path does not.

Do not resume rate, buffer, cable, rear-port, peripheral, disk, or broad power-
plan permutations. Do not replace system USB-audio files manually or flash the
BIOS on the current evidence.

## 7. Next Diagnostic

The next high-information test is a live Linux boot on the same desktop. It
changes the complete operating-system/audio stack while retaining the desktop
USB controller, UMC202HD, cable, and analogue playback path. WSL audio is not a
substitute because Windows still owns its USB/audio stack.

Use a non-installing live environment, leave the Windows disks untouched, and
play one locally available track for at least the established `5:08` interval.
Prefer `48 kHz` if readily selectable, but do not turn the test into another
rate study. Record the distribution name/version, audio server if readily
visible, USB port/cable, duration, and dropout count.

- Clean Linux playback would implicate installed Windows stack behaviour.
- Repeated Linux dropouts would implicate controller/firmware interaction or a
  lower-level UMC202HD compatibility issue.

This test is deferred while the UMC22 route advances the loudspeaker work.

## 8. Related Records

- [Current UMC22 installed-woofer procedure](procedures/UMC22_INSTALLED_WOOFER_FRD.md)
- [Suspended UMC202HD FRD route](procedures/UMC202HD_FRD_SUSPENDED.md)
- [Current passive-fixture use](fixtures/REFERENCE_FIXTURE_USE.md)
- [Completed fixture qualification and release](qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md)
