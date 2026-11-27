# Finite closure in null-cone quantization of gravity

**Version 1.5, final integrated edition · 27 November 2026 · Justin, Nous Enterprises LLC**

[Read the PDF](Finite_closure_v1.5_final.pdf) · [Download the editable LuaLaTeX source](Finite_closure_v1.5_final.tex) · [Download the reproduction package](Finite_closure_v1.5_final.zip)

This 38-page technical comment incorporates the [original v1.5 manuscript](https://github.com/nousentllc/chandrasekaran-section-5-2-review/tree/f438db1ecdabf0cb18860752263208093a58ca4b/reviews/v1.5) and its [signed-cycle clarification](https://github.com/nousentllc/chandrasekaran-section-5-2-review/tree/1f4e23ee1c9271ff360d672286555ef0373c7ce2/reviews/v1.5-clarification). The source under review is [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1).

Section 4.4 proves the rank bound on a cofinal family of complete cuts and gives the corresponding estimate for complex responses. Section 2.1 separates the Gaussian overlap at a finite clock reading from density of the form domain and construction of the full-space clock. Sections 6.3 and 9.2 discuss the corner half-turn and conservation of the quadratic source. Section 10 specifies the scope of the formal and numerical checks. Section 11 states the question about independently bounding the physical amplitudes in (5.38).

## Build the manuscript

The editable TeX can be compiled on its own with LuaLaTeX. It uses the adjacent original logo when present. With the TeX alone, it recovers the same PNG from bytes stored after the manuscript text. No shell escape or bibliography download is required. In a directory containing the source, run the following with TeX Live 2026.

~~~sh
export SOURCE_DATE_EPOCH=1795737600 FORCE_SOURCE_DATE=1
lualatex -halt-on-error Finite_closure_v1.5_final.tex
lualatex -halt-on-error Finite_closure_v1.5_final.tex
lualatex -halt-on-error Finite_closure_v1.5_final.tex
~~~

The final build used LuaHBTeX 1.24.0. All 38 pages were rendered and reviewed. The standalone and packaged builds agreed outside the generated PDF trailer identifier. The finished paper includes the cover, abstract and contents, the numbered body on pages 1–34 and the references on page 35.

## Check the mathematics

From the extracted package, verify the distributed files before compiling them.

~~~sh
shasum -a 256 -c SHA256SUMS
cd reproduction
lake exe cache get
lake build
lake env lean TraceDimCheck.lean
lake env lean TraceDimBasis.lean
lake env lean CycleBound.lean
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python run_checks.py
~~~

The lockfile specifies Lean 4.35.0 and Mathlib revision `56a005855ea17e0b0958f73ec801ae140b0a1679`. The final check used a freshly compiled copy of TraceDim and cached dependencies at the pinned revision. The [Lean record](reproduction/reference/final-lean.log) lists all six declarations and their axiom dependencies. The [Python record](reproduction/reference/v1.5-python.log) matches the final re-execution of all seven checks. Floating-point output can vary with the platform. The physical gluing bound in four dimensions remains an input to the application.
