# UMC202HD Desktop Dropout Diagnosis

Date range: 2026-09-03 to 2026-10-09

Last revised: 2026-10-09

Lifecycle: **CLOSED HARDWARE-FAULT HISTORY — AUDIT ONLY**

Status: **DESKTOP PLAYBACK DROPOUT CLOSED ON 2026-10-09 AFTER OPTICAL SATA
CONNECTIONS WERE RESEATED; MOTHERBOARD-END BLU-RAY DATA PLUG IS THE LEADING
PHYSICAL CAUSE**

## 1. Scope And Current Conclusion

This file is the single authority for the recurring UMC202HD output-stream
dropout discovered during the first full-dual woofer checkout. The passive
reference fixture, SU-V570, analogue playback lead, loudspeaker, and REW are not
the distinguishing cause. The same UMC202HD plays continuously on a Windows 11
laptop; substituting the UMC22's known-good cable did not change the desktop
fault. Before the optical SATA connections were reseated, the desktop dropped
out under both the Behringer driver and Microsoft's USB Audio 2.0 class driver.

After the loose Blu-ray SATA data plug and other optical-drive connections were
reseated, ordinary UMC202HD playback had **zero audible dropouts over about
`360 s`**, with both optical drives still enumerated. A `206 s` WPR retest
within that playback period contains no long `storahci.sys` DPCs, unlike the
earlier glitch trace. This strongly supports an optical SATA connection
problem as the practical cause of the observed desktop fault. The visibly
displaced motherboard-end Blu-ray data plug is the leading physical culprit.
Reseating several optical connections together prevents a controlled
assignment to that one plug. A further user-reported `300 s` playback run at
`24 bit`, `192 kHz` had zero audible dropouts. Together with the earlier
`24 bit`, `48 kHz` retest and the disappearance of the long SATA DPCs, this
closes the operational fault. No UMC202HD full-dual FRD has yet been accepted;
that separate measurement qualification belongs to the current checkout route.

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
| Depower two unused Seagate disks | `21/308 s`; `45/924 s` | powered disk activity and retained `storport.sys` lead rejected as useful causes; SATA data cables remained attached |
| Existing Windows High performance plan | `14/308 s` | generic CPU/power-plan change rejected |
| Disable Realtek PCIe GbE controller | user reports no appreciable difference; no counted run supplied | this adapter is unlikely to be the distinguishing cause; result is qualitative |
| Reseat optical SATA data and power connections; restore Blu-ray enumeration | `0` audible dropouts during about `360 s` at `24 bit`, `48 kHz`; long `storahci.sys` DPCs absent in `206 s` WPR interval | practical hardware fault cleared; motherboard-end Blu-ray data plug is leading physical cause |
| Repeat playback at `24 bit`, `192 kHz` after repair | user-reported `0/300 s` audible dropouts | high-rate operation remains clean; no WPR trace was reported for this run |

The user recalled an apparent bit-rate dependence during the fault. The earlier
five equal-length rate runs did not establish a reliable monotonic trend; the
clean `192 kHz` run is therefore a strong high-rate check of the repair rather
than evidence for a quantified bit-rate law.

The five-rate total was `85/1540 s = 0.0552 s^-1`. With the legacy disks
removed it was `66/1232 s = 0.0536 s^-1`. The difference is immaterial beside
run-to-run variation. The disks remain disconnected for independent idle-power
and ambient-noise benefits.

## 4. Host-Latency And Trace Findings

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
audible dropout was captured in those runs.

On 2026-10-09 the user supplied a Windows Performance Analyzer screenshot from
a Windows Performance Recorder trace captured with the `Audio glitches`
additional profile while several interruptions were audible. One
`Microsoft.Windows.Audio.KernelStreamingEndpoint` `Glitch` event in
`audiodg.exe` is logged at `36.331462 s` in the trace. The selected
`storahci.sys` DPC/ISR window includes a `10.2708 ms` fragment; that long
fragment ends at `36.331263 s`, about `0.199 ms` before the logged glitch.
A second supplied screenshot shows a `Glitch` at `62.551527 s` after a
`storahci.sys` burst whose longest fragment runs for `9.7179 ms` and ends at
`62.550771 s`, about `0.756 ms` before the glitch. This is the end of that
fragment, not the end of the whole DPC. These repeated, close
time relationships make the SATA driver path a stronger trigger candidate
than the session-wide LatencyMon maxima alone. They do not yet prove that the
driver or a particular disk is the root cause. The full-run screenshot shows
regular `storahci.sys` spikes, including spikes without a logged glitch; an
exact recurrence interval has not been extracted. The plotted peaks of about
`12.5` are multi-CPU graph values, not individual DPC durations. The earlier
depowering test excludes powered activity by the two unused Seagate disks as
a useful cause; it does not exclude their connected data cables, or the active
SATA controller/driver path.

In a subsequent full-trace WPA screenshot, the user added `Disk Usage` for
disks `0` and `1`. At the displayed resolution, neither disk's activity has a
visible recurring pattern matching the `storahci.sys` spikes or the logged
audio glitches. This weakens an explanation based on a periodic burst of
ordinary disk I/O, including WPR trace writes, but does not prove that no
individual I/O or controller work occurred at those times. The screenshot
does not identify the device or operation behind the long DPC/ISR fragments.

A closer WPA view with symbols loaded identifies the long call before the
`36.331462 s` glitch as a **Regular DPC** in
`storahci.sys!AhciPortBusChangeDpcRoutine` on logical CPU `0`. It enters at
`36.3200952 s` and exits at `36.3313278 s`: `11.2326 ms` elapsed, of which
`11.1694 ms` is exclusive execution. WPA splits that one DPC into five
fragments; the longest fragment runs for `10.2708 ms`. The DPC finishes
`0.1342 ms` before the logged glitch. The graph's roughly `12.5` peak is not
the duration of this individual DPC. Microsoft's published StorAHCI sample
uses this routine to process a SATA-port bus-change notification, including
port reset and a targeted rescan; it can be reached from an interrupt or a
retry callback. This is a strong clue that the observed activity is in the
bus-change path rather than an ordinary read/write completion, consistent
with the lack of a matching Disk Usage burst. The sample does not establish
the exact path, trigger, affected SATA port, or implementation of this
machine's installed binary, and the screenshot alone does not prove that
this DPC delayed the audio thread. Reference:
[Microsoft StorAHCI sample implementation](https://github.com/microsoft/Windows-driver-samples/blob/main/storage/miniports/storahci/src/util.c).

The closer view of the second glitch identifies another **Regular DPC** in
`storahci.sys!AhciPortBusChangeDpcRoutine` on logical CPU `0`. It enters at
`62.5395155 s` and exits at `62.5510783 s`: `11.5628 ms` elapsed and
`11.2773 ms` exclusive execution across five fragments, the longest
`9.7179 ms`. It ends `0.4482 ms` before the `62.5515265 s` glitch event.
A `USBXHCI.SYS!Interrupter_WdfEvtInterruptDpc` on the same CPU starts at
`62.5510798 s`, only `0.0015 ms` after that SATA DPC ends, and runs for
`0.3595 ms`; its exit is `0.0872 ms` before the glitch. Other smaller DPC/ISR
activity is present, including NVIDIA activity, but neither its aggregate
duration nor the graph height identifies it as the main pre-glitch stall.
This ordering makes delayed USB service by the SATA DPC plausible: DPCs on
one logical CPU cannot execute simultaneously, so the USB DPC can run only
after the long SATA DPC completes. The trace view does not show when that USB
DPC became ready, the audio thread's scheduling, or the SATA port/device
behind the bus-change call, so the complete causal chain remains unproved.

A user-identified spike without an accompanying audible glitch has the same
**Regular DPC** function on logical CPU `0`. It enters at `32.9972944 s` and
exits at `33.0084938 s`: `11.1994 ms` elapsed and `11.1722 ms` exclusive
execution across four fragments, the longest `10.8518 ms`. The screenshot's
Generic Events pane does not display the kernel-streaming glitch series in
this interval, so the absence of a glitch is based on the user's report and
the earlier full-trace view, rather than this detail pane alone. A grouped
`USBXHCI.SYS` row begins at `33.0084941 s`, immediately after the SATA DPC,
but its CPU is not shown on that aggregate row. This control observation
shows that a roughly `11 ms` bus-change DPC is not by itself sufficient to
produce a glitch. The remaining distinction could be the audio/USB service
deadline relative to the DPC, thread scheduling, buffering, or another event;
these possibilities are not yet separated by the screenshots.

The same WPR trace exposes `CPU Usage (Precise)` in WPA, with process/thread
grouping and `Ready (µs)` columns. The initial screenshot is still zoomed to
the non-glitch control interval and shows only aggregate process rows; it does
not yet establish the timing of any `audiodg.exe` thread around a glitch.

In the subsequent view around the `62.5515265 s` glitch, the expanded
`audiodg.exe` thread `14820` has a stack through
`CAudioPump::OutputPumpWorkRoutine` and one context-switch record in the
roughly `20.9 ms` displayed interval. Its `Ready (µs)` Sum and Max are both
`104.4 µs`; `Waits (µs)` is `19,591.7 µs`, and its recorded CPU usage is
`0.5539 ms`. The many expanded stack rows repeat that one record and must
not be counted as separate audio wake-ups. This does not support the narrow
hypothesis that the user-mode audio-pump thread was runnable but denied CPU
time for the whole roughly `11 ms` SATA DPC. A wait can be normal between
audio periods, and the record does not show when the kernel/USB work that
could wake this thread became ready. Thus a delayed notification or USB
service remains possible; the screenshot does not establish the cause of the
glitch.

On 2026-10-09, read-only Windows device enumeration identified one active
Intel `PCI\VEN_8086&DEV_8C82` **Standard SATA AHCI Controller**, using the
Windows `storahci.sys` path. Its present children are a
`Crucial_CT512MX100SSD1` SATA SSD and an `ATAPI iHAS124 E` optical drive.
`Get-Disk` identifies the Crucial as disk `0`, both boot and system; disk `1`
is a separate `CT2000P310SSD8` NVMe SSD. These identities replace any guess
from the `Disk Usage` graph about which disk uses AHCI. Device enumeration
does not identify which SATA port caused the bus-change DPC.

The Windows System log contains records during the 2026-10-08 18:50-19:30
local window around the WPR capture, but no storage events in that window.
A search of storage-related System warning/error providers from 2026-09-05
onwards also found none. This is limited to the System log and does not rule
out short, unlogged SATA bus-change activity. An older, separate burst of
disk and NTFS warnings/errors on 2026-09-04 concerned the two now-disconnected
Seagate disks; it is not contemporaneous with the October audio trace and
does not identify the source of these DPCs. Windows reports both currently
connected disks online and healthy, a coarse status that likewise does not
exclude transient controller or link activity.

The user reported a **second, physically installed Blu-ray drive** that was
absent from Device Manager and Explorer before a physical connection check.
On 2026-10-09,
`pnputil /enum-devices /class CDROM` listed only the started iHAS124;
`pnputil /enum-devices /disconnected /class CDROM` found no non-present
optical device, and a search of the current SCSI-enumeration registry branch
found only the iHAS124 model. A targeted check of the System log around the
October WPR capture found no optical-drive, SATA, or device-arrival/removal
events. This is an **unexplained hardware/enumeration anomaly**, not evidence
that the Blu-ray drive is on the same Intel AHCI controller, intermittently
connected, or responsible for the long DPCs. A fully disconnected or unpowered
drive could simply remain invisible; an intermittent SATA link or power feed
could plausibly trigger bus-change work, but the affected port has not been
identified. The user confirms that the Blu-ray drive **was previously visible**
in this Windows installation and that the Seagate disks were depowered using
separate leads; their depowering does not readily explain its disappearance.
The last known working date remains unknown.

Later on 2026-10-09, the user found the Blu-ray drive's SATA data plug **very
slightly withdrawn at the motherboard socket** and reinserted it. They also
reseated both optical drives' power plugs (on a shared harness) and both
drives' SATA data cables at both ends. After restart, Windows shows both
optical drives in Device Manager and Explorer; a fresh `pnputil /connected
/class CDROM /relations` check identifies the Blu-ray drive as
`PIONEER BD-RW BDR-S09`, started, with the **same Intel AHCI controller** as
the started iHAS124. The physical finding and restored enumeration make the
Blu-ray data connection a credible source of the earlier bus-change DPCs,
and the post-reseating retest below supports that connection group as the
practical fault path. Because several optical connections were reseated
together, the result does not isolate the one visibly loose plug.
The user reports that the iHAS124 had been working normally and the Blu-ray
power plug had appeared firmly seated; these observations increase confidence
in the displaced motherboard-end Blu-ray data plug as the primary cause, but
do not independently prove it.
The user notes that the two unused Seagate HDDs still have SATA data cables
attached at both ends but have no power cables connected. Their unpowered
state was unchanged across the audio retest; they are not currently
enumerated as active disks.

The user reports **zero audible dropouts during about `360 s` of ordinary
UMC202HD playback**, including a `206.016 s` WPR `Audio glitches` trace from
2026-10-09 (`GRAVITAS.10-09-2026.12-33-50.etl`). Both optical drives remained
visible afterwards. The Windows `xperf -a dpcisr -dpc -summary` report for the
new ETL contains `280` `storahci.sys` DPCs, **all at or below `32 µs`**. The
same command on the earlier `88.228 s` glitch ETL
(`GRAVITAS.10-08-2026.19-11-10.etl`) contains `176` `storahci.sys` DPCs,
including **`19` in the `8,192-16,384 µs` duration bucket**. These are
module-level DPC histograms rather than function-level counts; the earlier
WPA symbolised views identify the long calls as
`AhciPortBusChangeDpcRoutine`. The user has not yet reported the new trace's
ETW `Glitch` event count, so zero **audible** dropouts should not be silently
converted into zero logged events. Each `xperf` report emitted one invalid
event warning; the gross disappearance of the long-DPC bucket remains clear.

**Mechanism — strong inference, not directly captured electrical evidence:**
a marginal SATA data contact at the Blu-ray port could intermittently disturb
the link or leave it repeatedly failing negotiation. The AHCI controller can
report changes in physical-link readiness or connection state, even when no
ordinary disk I/O is visible. The published Microsoft StorAHCI sample handles
a port bus change by resetting that port and requesting a targeted rescan;
this matches the symbolised `AhciPortBusChangeDpcRoutine` calls, but the exact
installed-driver path, interrupt reason, port register values, and retry cause
were not captured. The roughly `11 ms` DPCs occupy logical CPU `0`; one trace
shows a USB xHCI DPC starting immediately afterwards and an audio glitch
event following it. Delayed USB/audio service could miss a time-critical
transfer deadline; an audible mute can then outlast the initiating DPC while
the stream recovers. The trace does **not** prove packet loss, the recovery
sequence, or that every bus-change DPC caused a glitch. A similar DPC occurred
without a glitch, consistent with timing relative to the audio buffer or USB
schedule mattering. Sources: [AHCI 1.3.1, section 7.3](https://www.intel.com/content/dam/www/public/us/en/documents/technical-specifications/serial-ata-ahci-spec-rev1-3-1.pdf),
[Microsoft StorAHCI sample](https://github.com/microsoft/Windows-driver-samples/blob/main/storage/miniports/storahci/src/util.c),
[Microsoft USB isochronous transfer documentation](https://learn.microsoft.com/en-us/windows-hardware/drivers/usbcon/transfer-data-to-isochronous-endpoints).

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

## 6. Excluded Causes And Causal Limits

Closed as useful causes for this symptom:

- passive reference fixture, SU-V570, woofer, and playback lead;
- REW versus ordinary media playback;
- ASIO versus Java/WASAPI;
- sample-rate mismatch or higher aggregate USB payload;
- the two tested rear motherboard ports and two tested USB cables;
- the concurrently connected UMC22, StarTech interface, and Wi-Fi dongle;
- powered activity by the two unused Seagate disks; their attached data cables
  were not separately isolated;
- generic Windows Balanced versus High performance power policy;
- the Realtek PCIe GbE controller as a likely distinguishing cause, based on a
  qualitative disable-and-retest report without a supplied count or duration;
- a defective UMC202HD that fails identically on another host.

The motherboard-end Blu-ray SATA data plug is the leading physical explanation:
its visibly displaced state, restored drive enumeration, absence of the long
`storahci.sys` DPCs, and disappearance of audible dropouts align. Since several
optical connectors were reseated together, the exact decisive contact and
underlying electrical sequence remain unproved. Long-term stability also
depends on ordinary future use, but the fault is operationally **closed** after
clean `48 kHz` and `192 kHz` playback runs and disappearance of the long SATA
DPCs. The earlier Windows USB-audio, xHCI, firmware, and driver-revision
hypotheses require no further work on the present evidence.

Do not resume rate, buffer, cable, rear-port, peripheral, disk, or broad power-
plan permutations. Do not replace system USB-audio files manually or flash the
BIOS on the current evidence.

## 7. Closure And Historical Re-entry

The hardware fault needs no further diagnostic test or live Linux boot. The
separately qualified UMC22 route remains available for speaker measurements.
The [UMC202HD checkout route](procedures/UMC202HD_FRD_CHECKOUT.md) owns any
future REW measurement gates; the clean media-playback tests do not by
themselves qualify an acoustic response.

If dropouts recur, first check whether both optical drives remain enumerated,
then compare a short WPR `Audio glitches` trace with the retained before/after
ETLs for the long `storahci.sys!AhciPortBusChangeDpcRoutine` calls. Do not
disable the AHCI controller or change BIOS SATA mode: the boot/system disk
depends on it. Keep raw traces local because they may contain private host
details; record only decision-relevant results here.

## 8. Related Records

- [Current UMC22 installed-woofer procedure](procedures/UMC22_INSTALLED_WOOFER_FRD.md)
- [UMC202HD FRD checkout route](procedures/UMC202HD_FRD_CHECKOUT.md)
- [Current passive-fixture use](fixtures/REFERENCE_FIXTURE_USE.md)
- [Completed fixture qualification and release](qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md)
