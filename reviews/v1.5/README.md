# Finite closure in null-cone quantization of gravity

Version 1.5, 27 November 2026. Justin, Nous Enterprises LLC. A technical comment on Venkatesa Chandrasekaran's [arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1).

Read the [manuscript](Chandrasekaran_2611.34924_RedTeam_v1.5.pdf) or edit the [single LuaLaTeX source](Chandrasekaran_2611.34924_RedTeam_v1.5.tex). The paper has 37 physical pages, including a cover, abstract, contents, body pages numbered 1–33, and references. The body includes the proofs, controls, analytical limitations and research contributions.

## What changed

- Sections 3–5 clarify the two gluing routes. The positive identity bound gives a short dimension proof. For the signed insertion, a stronger cycle estimate can make the cut amplitudes tend to minus infinity under the infinite-dimension hypothesis. A proof identifying that limit with a positive gravitational amplitude would suffice. Appendix E's later use of finite dimension and the one-loop regular-family estimate in Appendix D.3 are treated separately.
- Sections 6–7 derive the conditional area law, the convergence needed on the joint AdS cut and the center distribution in the entropy integral. At the reported clock parameter the interior center band carries about 11.91 percent of the total. Uniform sublogarithmic error on that band suffices for coefficient matching. The geometric heat-kernel calculation and the subsequent algebraic conversion have distinct roles.
- Sections 8–9 incorporate the fixed-area pair-amplitude limit, the one-loop contour and renormalization qualifications, and the distinction between the represented algebra and its weak closure. A Fourier-block example tests a stronger reading of joint absolute convergence. Intertwining the data suffices to preserve predictions across representations.
- Section 10 adds a compiled Lean theorem for the ambient finite dimension and the quantitative finrank bound, assuming the partial-trace bound on a complete Hilbert basis. Section 11 states concrete ways the open physical assumptions might be established.

## Reproduce the manuscript

Use LuaLaTeX with standard LaTeX packages and keep the included original logo in the same directory as the source. From this directory on a Unix-like system, using TeX Live 2026:

```sh
export SOURCE_DATE_EPOCH=1795737600 FORCE_SOURCE_DATE=1
lualatex -halt-on-error -interaction=nonstopmode Chandrasekaran_2611.34924_RedTeam_v1.5.tex
lualatex -halt-on-error -interaction=nonstopmode Chandrasekaran_2611.34924_RedTeam_v1.5.tex
lualatex -halt-on-error -interaction=nonstopmode Chandrasekaran_2611.34924_RedTeam_v1.5.tex
```

The authoring build used LuaHBTeX 1.24.0. The final build had resolved citations, cross-references and contents, and no overfull boxes. All pages were rendered for review.

## Reproduce the formal and numerical checks

Run these commands inside the reproduction directory. Lake uses the included lockfile for Lean 4.35.0 and Mathlib revision `56a005855ea17e0b0958f73ec801ae140b0a1679`. For a new setup the initial dependency and cache fetches need internet access. The verification build used locally cached copies at the pinned revisions.

```sh
cd reproduction
lake exe cache get
lake build
lake env lean TraceDimCheck.lean
lake env lean TraceDimBasis.lean
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python run_checks.py
```

The original TraceDim.lean is byte-preserved, including its historical pre-compilation comment. The new theorem lives in TraceDimBasis.lean. The reference directory contains the execution records for all four declarations and the seven Python checks. The original import generates a module-style warning in the tested Lean version. The kernel accepted all four declarations and their reported axiom dependencies are propext, Classical.choice and Quot.sound.

The Python run used Python 3.13.2, NumPy 2.3.5, SymPy 1.13.3 and mpmath 1.3.0. Exact archive comparisons are reported for the recorded examples. Floating-point extrema can vary across platforms. The tests cover the abstract mathematics, finite examples, and stated limits. The four-dimensional gluing rule and the one-loop determinant remainder remain physical proof obligations.

In the extracted package, run `shasum -a 256 -c SHA256SUMS` before rebuilding to verify the distributed files. The public repository retains the [v1.4 edition and Neon review](https://github.com/nousentllc/chandrasekaran-section-5-2-review/tree/d535b0d5bdb59b8f4bd021f9f563aa08db4d1995/reviews/v1.4).
