# Chandrasekaran §5.2 independent review

This repository contains an equation-by-equation review of the causal-diamond finite-dimensionality argument in [Chandrasekaran, *An algebraic quantization of gravity from the null cone*, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1). The review derives the trace implication, checks the boost and spectral inequalities, and gives an infinite-dimensional operator model that isolates the cut-to-uncut identification.

Start with the [consolidated v1.6 manuscript](reviews/v1.6-final/) and the [follow-up attempt to bound (5.38)](reviews/gluing-bound/). Open gluing bounds amplitudes between fixed finite-norm states. On the refined complete-cycle cuts, the doubled preparation has squared norm at least proportional to the cut rank and the signed amplitude has magnitude at least proportional to that rank. The follow-up tests two ways to bound the closed amplitude independently, using a positive gluing functional or the exact two-copy ratio, and records what the focusing calculation still needs to control.

The [Zenodo version family](https://doi.org/10.5281/zenodo.24585120) includes the earlier [v1.5-final](https://doi.org/10.5281/zenodo.24585121) preprint.

| Material | What to check |
| --- | --- |
| [v1.6 manuscript and supplement](reviews/v1.6-final/) | Consolidated analysis, editable TeX, pinned Lean and Python reproduction materials, and release checksums |
| [Review](REVIEW.md) | Equation references, derivations, the separation model, and scope of the conclusions |
| [TraceDim.lean](TraceDim.lean) | The three conditional proofs in the supplied source, preserved byte for byte |
| [TraceDimCheck.lean](TraceDimCheck.lean) | Axiom dependencies for those three declarations |
| [Numerical checks](checks/) | 500 finite-matrix checks and sample finite sections of the analytic model |
| [Verification record](evidence/) | Original run outputs, input hashes, and provenance |

## November 27 review materials

The [gluing-bound follow-up](reviews/gluing-bound/) gives the doubled-state norm calculation, sufficient estimates from Appendix E and Appendix D.3, and a classical test of what the clock integral controls. Its [Python check](reviews/gluing-bound/check_gluing_bound.py) verifies the finite-section examples using only the standard library.

The [final integrated v1.5 manuscript](reviews/v1.5-final/) incorporates the signed-cycle clarification. Download the [PDF](reviews/v1.5-final/Finite_closure_v1.5_final.pdf), [standalone TeX](reviews/v1.5-final/Finite_closure_v1.5_final.tex) or [reproduction ZIP](reviews/v1.5-final/Finite_closure_v1.5_final.zip). The [first v1.5 edition](reviews/v1.5/) and the [v1.4 manuscript and Neon review](reviews/v1.4/) are archived separately.

Read the [post-publication clarification and checked inequality](reviews/v1.5-clarification/). On the refined complete-cycle cuts in §5.2, eventual boundedness of the unnormalized signed amplitudes already forces finite dimension. The clarification revises the referee question, distinguishes normalized gluing, and checks the clock-domain, corner-boost and conservation issues against the source.

Read the [v1.2 red-team note](reviews/v1.2/Chandrasekaran_2611.34924_RedTeam_v1.2.pdf) alongside the [subsequent assessment of F5–F7](reviews/v1.2/ADVERSARIAL_REVIEW_V1_2.md). The assessment proposes revisions to the zero-coupling limit, the scope of one-loop finiteness, and the role of the pure-state extension. The supplied note is archived as written.

The [original source ZIP](reviews/v1.2/RedTeam_2611.34924_v1.2.zip) contains editable TeX and supplements. The [review handoff ZIP](reviews/v1.2/REVIEW_V1_2_HANDOFF.zip) contains the subsequent assessment, Python check and run log. After unpacking that handoff, install `mpmath==1.3.0` and run `python3 verify_v1_2_f5.py` in the extracted directory. The [independent review brief](reviews/v1.2/GEMINI_REVIEW_BRIEF.txt) gives the questions for the next reviewer.

Neon's [first report](reviews/v1.2/neon/NEON_FIRST_REVIEW_v1.2.md) records its review of the two PDFs and the Codex assessment. The [follow-up check](reviews/v1.2/neon/NEON_REVIEW_CHECK_v1.2.md) derives an interior-band tail bound for (5.66) and identifies the remaining uniformity question. The [plain-text source packet](reviews/v1.2/neon/NEON_REVIEW_SOURCES_v1.2.txt) contains the 17 files subsequently pasted into Neon. To check the Gaussian estimates numerically with mpmath 1.3.0, run `python3 reviews/v1.2/neon/check_gaussian_band.py`.

The [v1.0 PDF and source archive](reviews/v1.0/) record the first manuscript package. Later reviews refine its assessment and identify a weaker sufficient condition for the signed-cycle argument.

## Reproduce the Lean checks

Run from the repository root with [Elan](https://github.com/leanprover/elan) installed. Lake uses the committed Lean 4.35.0 toolchain and Mathlib lockfile. The first run may download dependencies and the Mathlib build cache.

```sh
lake exe cache get
lake build
lake env lean TraceDimCheck.lean
```

The audit should list only `propext`, `Classical.choice`, and `Quot.sound` for each declaration. The historical “NOT YET COMPILED” comment remains in the byte-preserved source. The [verification log](evidence/lean-verification.log) records the successful later check. The proofs assume the finite partial-sum bound `hN`. Establishing that bound from the gravitational construction is the open question.

## Reproduce the numerical checks

Use Python 3.13 with the recorded package versions. The checks write to a local, ignored `outputs/` directory, leaving the archived evidence available for comparison.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python checks/operator_checks.py
python checks/countermodel.py
diff -u evidence/operator_checks.json outputs/operator_checks.json
diff -u evidence/countermodel_checks.json outputs/countermodel_checks.json
```

The seeded matrix diagnostics enforce the inequalities with floating-point tolerances. Expect slight platform differences in the reported floating-point extrema. The paper's infinite-dimensional arguments and the countermodel's exact derivation are in the review.

The review was conducted by OpenAI Codex at Justin Candler's request, building on the earlier audit prepared by Justin with Claude. The source manuscript is linked by version. The archive records the reviewed inputs by hash and includes the formalization required to reproduce the Lean check.
