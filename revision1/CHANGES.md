Changes made in Revision 1 of the research note. The revised note text is with the journal and is not in this repository; the figure, new runs, scripts and source files it cites are in this folder. Paths in this file are the author's working paths.

# AAS82149 R1 (TIC 26986661): changes from submission4/rnaas4.md

Paths are relative to `~/Scratch/planet-hunt/`. 

Files in `revision-82149/final/`: `rnaas_rev1.md` (body 768 words, abstract 143, caption 65), `Paliwal_TIC26986661_RNAAS_rev1.docx` (built with `tools/mkdocx.py`, python-docx 1.1.2, the same way as AAS82088 R1), `figure1_combined_TIC26986661.png` (copy of `prerev/26986661/fig/figure1_combined_TIC26986661.png`), `response.txt` (confidential author reply).

## Header
| Change | Source |
|---|---|
| Postal address removed; now "Independent researcher" | — |

## Eumemic credit (new)
| Change | Source |
|---|---|
| Abstract: "independent detection and vetting"; "The signal was listed earlier in a public candidate catalogue by Eumemic." | — |
| Search section: "The same signal (P = 3.996223 d) was posted two days before my search found it, in a public list of TESS candidates by Eumemic (2026)…" | `revision-82149/_sources/candidates_2026-10-08d_at_297b388b.csv` (row 26986661, P 3.996223; `.url` sidecar); commit time 2026-10-08T12:04:24Z in `revision-82149/_sources/eumemic_commit_297b388b.json`; our find 2026-10-10 08:10Z per `submission/SUBMITTED.md` Eumemic section |
| Reference added: Eumemic 2026, commit 297b388b96213cfb43786339bba532b04f979cf6 | same JSON (`sha`, `html_url`) |

## Q1: sectors in the difference analysis
| Number | Old | New | Source |
|---|---|---|---|
| Sectors with difference images | 5 (S21–72) | 6 (adds S1751) | `prerev/26986661/loc/all6/diff120_s*.json` |
| S1751 transits in stamp; max \|Δχ²\| | — | 1; 3.3 | `diff120_s1751.json` (`n_events`); `prerev/26986661/loc/dchi2_sum_s1751.csv` |
| Transits in S21–72 stamps | — | 29 (6+6+6+5+6) | `diff120_s{21,45,46,48,72}.json` `n_events` |
| Per-sector Δχ², S21–72, all 8 sources | not given | 7.8–39.1 (every source positive in every sector) | `prerev/26986661/loc/dchi2_sum_6sectors_persector.csv` |
| Summed Δχ² | "at least 101" | 101–144 (101.3–144.0) | `prerev/26986661/loc/dchi2_sum_6sectors.csv` |
| Sources: G, separation | not given | G 17.5–21.0 (17.548–20.958), 84–120″ (83.9–119.7) | same CSV |
| Free-centroid offsets | 1.0–8.8″ | unchanged, now stated as S21–72 | `hunt7/localize/26986661/gate_c.json` |

## Q2: χ² definitions
| Change | Source |
|---|---|
| Δχ² defined: χ² over 15×15 TESScut stamp, per-pixel noise = 1.4826×MAD of 120 random-phase difference images; PRF with free amplitude and offset; Δχ² = χ²(source) − χ²(target) | `prerev/26986661/loc/run/diff120.py` lines 37–51 |
| Box depth defined: median out-of-transit flux minus mean in-transit flux | `deep/26986661/sectors/results.json` (`method`) |

## Q3: neighbours / FPP (rerun)
| Number | Old | New | Source |
|---|---|---|---|
| Neighbours removed | none (not stated) | none, stated; 34 retained (35 stars incl. target) | `hunt7/fpp/26986661/run_fpp.py` (no `remove_star`); `revision-82149/fpp/summary.json` `n_stars` |
| TRICERATOPS tdepth | 3112 ppm (search LC box) | 3971.4 ppm (fitted) | `hunt7/fpp/26986661/out/res_26986661_0.json`; `deep/26986661/fit/all6/result.json` |
| Input light curve | unmasked SG search LC, 5 sectors, search ephemeris | masked wotan biweight 0.5 d LC, 6 sectors, fitted P/T0 | `revision-82149/fpp/prep_masked.py` → `lc_masked_6s.npz`; `revision-82149/fpp/run_fpp.py` |
| Frozen settings | — | same target pickle, Gaia background file, MOLUSC file, filt TESS, N 10⁶, exptime 30 min, nsamples 20, seeds 1000–1009, 10-min bins ±0.25 d, dur 0.04928 d | `revision-82149/fpp/run_fpp.py` |
| FPP | 0.0175 ± 0.0017 (0.0149–0.0205) | 0.0155 ± 0.0012 (0.0136–0.0171), 10/10 runs ≤ 0.035, 3/10 ≤ 0.015 | `revision-82149/fpp/summary.json` |
| NFPP | 0 | 0 (only the target has rows in every probs table) | `summary.json` `NFPP_max`, `ids_in_probs` |
| Bound-companion planet share | 0.016 | 0.013 (STP 0.0131) | `summary.json` `scenario_mean` |
| EB at 2P | 0.0013 | 0.0024 (EBx2P 0.0013 + SEBx2P 0.0009 + PEBx2P 0.0002) | same |
| Note | The masked light curve's own box depth at the fitted ephemeris is 3440 ppm; TRICERATOPS was given the fitted 3971 ppm as tdepth | `res_masked_*.json` `box_depth_ppm` |

## Q4: detrending
| Change | Source |
|---|---|
| Search: lightkurve Savitzky–Golay flatten, ≈0.75 d window, no mask, 30-min bins; SDE 23.4 | `hunt7/run1.py` lines 33–36; `hunt7/res/26986661.json` (`SDE` 23.37) |
| Fit: wotan biweight 0.5 d; points within ±1.77 h (3 × 0.04928 d / 2) masked, trend interpolated | `deep/26986661/fit/all6/prep.py` lines 18–23 |
| Fit: 1330 points within 2.9 h (0.12 d) of transit | `deep/26986661/fit/all6/fitdata.npz` (70+196+203+172+585+104) |
| wotan reference added (Hippke et al. 2019, AJ 158, 143) | — |

## Q5: unfolded light curve
| Change | Source |
|---|---|
| Figure 1 now three panels (folded 6 sectors; unfolded S72 200 s with trend; 4 S72 transits) | `prerev/26986661/fig/figure1_combined_TIC26986661.png`, `fig_stats.json` |
| "A single transit has a median S/N of 2.5" | `fig_stats.json` `median_snr` 2.454 |

## Q6: MOLUSC
| Change | Source |
|---|---|
| RUWE + Gaia contrast tests; 50,000 generated, 27,305 kept (54.6%); kept set replaced the default bound-companion prior | `hunt7/fpp/26986661/molusc.log`; `prerev/26986661/methods_molusc_counts.json` |
| "and imaging" removed from the MOLUSC sentence (no imaging exists) | ExoFOP JSON `revision-82149/_sources/exofop_26986661.json` (`imaging` 0, `tois` [], `ctois` []) |

## Cut to stay under 1000 words (content unchanged, not contradicted)
- "the SPOC pipeline lists no threshold-crossing event"; T14/T12 = 17.4 and the b 95% limit; injection recovery; 134 comparison folds; momentum-dump test; the S1751 single-transit depth 2913 ± 1249 ppm; the "equal-mass grazing binary" sentence. All remain in the repo results.

## Unchanged numbers (rechecked against files)
P, T0, Rp/R★, b, depth, T14, Rp, a, S, Teq from `deep/26986661/fit/all6/result.json`; SPOC/QLP/TARS box depths 3201 ± 281, 2669 ± 363, 3098 ± 381 ppm and odd/even 0.49σ, 0.8σ, 0.84σ from `deep/26986661/sectors/results.json` `combined`.
