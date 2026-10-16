# TIC 26986661.01 — a temperate 2.1 Earth-radius planet candidate on a 4.0-day orbit

Discovered by **Advait Paliwal** (independent researcher, advaitpaliwal@gmail.com) on 2026-10-10 in TESS full-frame-image photometry.

| | |
|---|---|
| Host | TIC 26986661 = LP 371-15 = 2MASS J10021661+2134318, M dwarf, 67.4 pc, T = 13.3 |
| Period | 3.9962274 (+0.0000155/−0.0000167) d |
| Mid-transit | 2460263.6065 (+0.0023/−0.0031) BJD_TDB |
| Depth / duration | 3971 ± 390 ppm / 1.44 h |
| Radius | 2.06 ± 0.12 R⊕ |
| Equilibrium temperature | 513 ± 24 K |
| TESS data | sectors 21, 45, 46, 48, 72 + 2026 special pointing (FFI only) |
| False-positive probability | 0.0155 ± 0.0012 (TRICERATOPS + MOLUSC Gaia limits, no neighbours removed, fitted depth; Revision 1); NFPP 0 |

Status: **planet candidate**. Not a TOI or CTOI as of 2026-10-10. High-resolution imaging is needed to exclude an unresolved bound companion.

## Revision 1 (2026-10-16)

The research note was revised in response to the journal editor. The corrected numbers are:

- **False-positive probability:** FPP = 0.0155 ± 0.0012 (ten runs, range 0.0136–0.0171), NFPP = 0. TRICERATOPS was rerun at the fitted depth of 3971 ppm (was the 3112 ppm search depth) on the masked wotan light curve of all six sectors folded on the fitted ephemeris, with all 34 neighbours kept (`revision1/fpp/summary.json`). Most of the FPP (0.013) is a planet orbiting an unresolved bound companion; eclipsing binaries at twice the period sum to 0.0024.
- **Difference images:** six sectors (adds the 2026 pointing); every Gaia source within 120″ is disfavoured, summed Δχ² 101–144, and every source is disfavoured in every sector (7.8–39.1).
- **MOLUSC:** Gaia RUWE and contrast tests only (no imaging); 50,000 companions generated, 54.6% kept.
- **Prior listing:** the same signal (P = 3.996223 d) appeared two days before this search found it in a public candidate list by Eumemic, commit [297b388b](https://github.com/eumemic/exoplanets/commit/297b388b96213cfb43786339bba532b04f979cf6) (2026-10-08). This record reports an independent detection and vetting; the source files are in `revision1/sources/`.
- **Figure 1** now has three panels: folded six sectors, unfolded Sector 72 with the trend, and four single transits (`revision1/figure1_combined_TIC26986661.png`).

Every change, with its source, is listed in [`revision1/CHANGES.md`](revision1/CHANGES.md). The revised note text is with the journal and is not included here.

Data: TESS (NASA, via MAST: TESS-SPOC doi:10.17909/t9-wpz1-8s54, QLP doi:10.17909/t9-r086-e880) and ESA Gaia. Licences: code MIT; text, figures and data CC BY 4.0.
