# What finite signed gluing would imply

**Clarification to *Finite closure in null-cone quantization of gravity*, v1.5 · 27 November 2026**

The concluding referee question in v1.5 imposed more than the dimension argument needs. On the refined complete-cycle cuts of §5.2, an eventual bound on the magnitude of the **unnormalized** signed amplitudes already forces finite dimension. Convergence to any finite number gives such a bound. The paper's calculation of a positive uncut response has a role in its sign comparison, but the mathematical inference below uses only information on the cut side and the bound. This observation clarifies what an independent physical gluing theorem would have to deliver. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Manuscript v1.5 and reproduction materials](../v1.5/)

## Signed amplitudes on a complete-cycle exhaustion

Fix one diamond, preparation $`C_b`$, bounded observable, boost and shift $`\delta=\delta_\eta>0`$. On $`H=\mathcal H_D`$ write $`T=C_b^\dagger C_b`$, with $`cI\le T\le I`$ and a fixed $`c>0`$ from (5.21d), (5.23)–(5.25) and (5.30c). For a nonempty finite union of complete basis cycles with projection $`P`$, put $`W_P=\mathrm{Tr}(PT)`$ and $`r_P=\langle\Delta_\eta O\rangle_P`$. Then $`W_P\ge c\,\mathrm{rank}\,P`$. Equation (5.38) gives

```math
Z_P[X]=W_P(r_P-\delta/2).
```

Under the infinite-dimension hypothesis, the paper constructs the cycles using a basis adapted to a narrow spectral interval. For a given positive target, (5.32) and (D.25) let us narrow that interval and increase the fixed cycle length until $`|r_P|\le\delta/4`$ for **every** nonempty finite union. The paper uses a half-gap target. The quarter-gap is a permissible refinement, not a property of every choice of cycles. Order these unions by inclusion so that their projections exhaust the whole basis, including in the nonseparable case.

For real responses, (5.38) immediately yields

```math
-\frac{3\delta}{4}W_P\ \le\ Z_P[X]\ \le\ -\frac{\delta}{4}W_P.
```

The same ordered bounds hold for $`\mathrm{Re}\,Z_P[X]`$ for complex $`r_P`$. More directly, the reverse and forward triangle inequalities give

```math
\frac{\delta c}{4}\mathrm{rank}\,P
\ \le\ \frac{\delta}{4}W_P
\ \le\ |Z_P[X]|
\ \le\ \frac{3\delta}{4}W_P .
```

The earlier one-sided estimate already gives the needed lower bound on the magnitude in the real case. The two-sided estimate makes the relationship with the identity weights explicit.

**Consequences.** If $`|Z_P[X]|\le B`$ eventually on this directed family, every cut in that tail has rank at most $`4B/(c\delta)`$. Every finite set of basis vectors is contained in a complete-cycle cut in the tail: include the cut marking the beginning of the tail and add the finitely many required cycles. This proves $`\dim H\le4B/(c\delta)`$. If $`Z_P[X]\to L`$ is finite, apply the argument with $`B=|L|+\varepsilon`$ for every $`\varepsilon>0`$, giving $`\dim H\le4|L|/(c\delta)`$. In infinite dimension the lower bound instead forces $`|Z_P[X]|\to\infty`$ and $`\mathrm{Re}\,Z_P[X]\to-\infty`$.

Conversely, an eventual bound on $`W_P`$ gives bounded rank by the same floor. On an exhaustion by finite unions of complete cycles the basis must then be finite. The full cut is a terminal element, so with the insertion and preparation fixed the signed net is eventually constant. This proves the equivalence on any such exhaustion satisfying the stated estimates. Bounded weights in a generic signed sum do not ensure convergence, and the cycle construction under the infinite-dimensional hypothesis gives no unconditional existence claim for quarter-gap cycles on a given finite-dimensional diamond.

**Scope of the simplification.** Once the quarter-gap bound holds, the sign of the uncut amplitude and the response transfer in (5.36b), (5.37b) and (D.36) are unnecessary for this boundedness argument. The number used for the shift need only be fixed and positive in the abstract estimate. Changing that shift changes $`X`$, so a physical bound proved for one insertion cannot automatically be applied to another. The chosen boost and the cut estimate still have a role in proving the comparison with $`W_P`$.

A separate proposal to match **normalized** expectations to an independently established positive response remains logically distinct. A normalized limit can exist when the unnormalized amplitudes diverge. For example, on $`\ell^2`$ take $`T=I`$, $`O=0`$ and a positive shift. The normalized expectation of $`X`$ is constantly $`-\delta/2`$, while $`Z_P[X]=-(\delta/2)\mathrm{rank}\,P`$. This tests the normalization distinction alone. Likewise, the ordinary signed argument requires neither a prescription for multiplying infinities nor a proposed extended-real gluing law.

**Revised referee question.** For the fixed four-dimensional preparation and insertion in (5.37a), what estimate or gluing principle, independent of the dimension conclusion (5.39c), makes the unnormalized $`Z_P[X]`$ eventually bounded on the refined complete-cycle exhaustion of (5.32) and (D.25)? If the justification is (4.29)–(4.30), which fixed finite-norm external vectors give that bound after the corner is closed? If the proposed justification concerns normalized expectations, which result identifies their limit and establishes the needed response gap?

## Two questions about the clock

1. **How are clock spectral projections constructed in the chosen representation?** Equations (4.26)–(4.27) give a form on the fixed-area Fock space $`\mathcal K_{\mathcal A}`$. Equations (4.14)–(4.17) give area spectral projections, an isometric embedding of that Fock space and a dense span of its translates by insertions. Equations (5.1)–(5.3) use the clock spectral projections on all of $`\mathcal H_\omega`$ and their commutation with area spectral projections. (C.21) uses the full clock projector, and (E.16) gives covariance under specific frame changes. We did not locate a construction establishing the compatibility of the clock projections on the area-changing preparations. A construction via represented bounded resolvents, or a measurable family of operators on area fibers, could address the question. Agreement between different admissible choices of $`\omega`$ is a further issue explicitly deferred in footnote 20. Actual dependence of the area spectrum or diamond rank on $`\omega`$ has not been demonstrated. This sharpens the existing discussion in v1.5 §§2 and 9.

2. **Which quantum estimate establishes density or nonzero Gaussian overlap?** In (C.13), $`M=\overline{\mathrm{dom}\,Q}`$ is the closure of the form domain. Monotone convergence gives the resolvent on $`M`$, followed by $`P_M`$. Equation (C.14) identifies the limiting deficit for a unit vector as $`\|(I-P_M)\psi\|^2`$. In (C.17) the deduction that $`M=\mathcal K_{\mathcal A}`$ requires control for a family of nearby coherent displacements. Footnote 18 describes the passage from the classical tail bound to the noncommuting matrix element in (5.16) as heuristic. Even if $`M`$ is proper, the positive self-adjoint operator $`u_M`$ on $`M`$ has a finite-reading projection $`1_{[0,\ell]}(u_M)P_M`$ on the fixed-area space, understood with the natural inclusion of $`M`$. Only the component in $`M^\perp`$ is automatically excluded from every finite reading. As $`\ell\to\infty`$, the squared Gaussian projection norm tends to $`\|P_M\Omega_{\mathcal A}\|^2`$. Nonzero overlap gives a nonzero projection at some finite cutoff, whereas the limit one in (5.19) requires the Gaussian itself to belong to $`M`$. Density on all of $`\mathcal K_{\mathcal A}`$, nonzero Gaussian overlap, and the full-space clock in question 1 are three different claims.

## Two qualifications already substantially covered by v1.5

- **Corner half-turn.** Given a self-adjoint nonnegative area generator, spectral calculus defines $`e^{-\widehat{\mathcal A}/(8G_N\hbar)}`$. On the reducing, bounded-area diamond subspace the boost exponential is entire in the rapidity. At $`i\pi`$, (5.22) gives the exponent in (5.23a). Unitarity then yields (5.23b). A KMS or Bisognano–Wichmann theorem is unnecessary for these operator statements. The physical question under F3 is what identifies the Lorentzian half-cap preparation with that continued operator. The classical corner charge in (3.63)–(3.64), the JT half-turn in §2, the real-rapidity gluing in (D.13) and the geometric half-turn in §5.3 give the proposal a rationale. The KMS statement in (5.49) concerns the AdS boundary.
- **Conservation at coincidence.** Polarizing (6.15) on two on-shell linearized solutions gives a conserved bilinear quadratic source. For a finite collection of solution variations in (6.9), contraction against their spacetime-independent covariance preserves that identity. The same holds for a distributionally convergent limit of these conserved tensors. The step requiring care is identifying such a limit with the full composite source defined by the smearing, coincidence and local subtraction in (6.14), including any contact or boundary terms. Appendix D.2 explicitly treats a shear subtraction following (D.20). This is the regulator question already raised in v1.5 §9.2. We found no example of a violation of conservation in the prescribed theory.

## Checks and provenance

Claude proposed the signed-amplitude refinement. Gemini raised the four source questions, and Claude supplied a second reading. This clarification was prepared after checking those suggestions against the cited equations and the released v1.5 source. Agreement between these readings does not supply the physical gluing estimate.

The accompanying Lean file checks the real two-sided scalar inequality and the rank estimate for one cut. Its real response can stand for the real part of a complex response. The exhaustion proof and complex modulus inequality are given above. The v1.5 basis theorem and Gaussian-center check were separately rerun. The latter returns $`2^{-257/90}-4^{-257/90}=0.119074070334`$ to the digits shown under the manuscript's limiting-distribution hypothesis.

To check the new inequalities after installing the pinned dependencies as described in v1.5, run the following from the repository root. [Lean source](CycleBound.lean) · [v1.5 reproduction instructions](../v1.5/README.md)

~~~
cd reviews/v1.5/reproduction
lake env lean ../../v1.5-clarification/CycleBound.lean
~~~
