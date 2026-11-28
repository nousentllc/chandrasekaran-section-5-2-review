# Checking the first Neon review of the v1.2 red-team note

27 November 2026. Codex follow-up for Nous. The accompanying first Neon report is the text supplied by the user, verbatim. Neon reported reading the two PDFs and the earlier Codex review before seeing the scripts. It reported analytic checks and no code execution. The separate plain-text packet contains the 17 text files from the two v1.2 archives, including code and recorded outputs. The version examined is [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/pdf/2611.34924v1).

## The finite-dimensionality question in §5.2

Write $`T=C_b^\dagger C_b`$ on the clock-selected space. Under (5.30c), $`T\ge cI`$ for fixed preparation and diamond, with $`c=e^{-s_*}m_{b,\mathscr D}>0`$. If identity gluing supplies a finite upper bound $`N`$ on all positive partial traces, every rank-$`r`$ orthogonal projection satisfies $`cr\le\mathrm{Tr}(PT)\le N`$. Thus $`d_{\mathscr D}\le N/c`$. Conversely a bounded $`T`$ on a finite-dimensional space has finite trace. The converse alone cannot establish circular reasoning. A circular argument would use the dimension conclusion to justify the finite gluing premise on which its derivation depends. An independent derivation of finite identity gluing would make the boost-cycle step unnecessary for the dimension bound.

The manuscript's (5.38) concerns the signed insertion $`X`$ of (5.37a). Finite uniform bounds for identity partial traces constitute an additional premise when using the short argument. The Cauchy–Schwarz estimate in (4.29)–(4.30) applies to fixed Hilbert vectors. Applying it to a closed preparation requires identifying the needed vector or trace and controlling its norm as the cut sum grows. Appendix E's application in (E.17) invokes §5.2. The positive ratio in (D.49) draws on a one-loop count for regular saddles. JT (2.17) illustrates a divergent closure in a different theory. These checks leave the four-dimensional gluing question open.

The three theorems in TraceDim.lean end at finiteness of an orthonormal family's index type, under an explicit bound on all its finite partial sums. The supplied file compiled in the earlier pinned environment, as recorded in lean-verification.log. Specialization to a complete Hilbert basis, the physical gluing map, and the bound for the proposed preparation lie outside that file.

## The proposed integral-tail objection to (5.66)

There are two variables here. The spectral area $`s`$ is bounded by $`S=s_*`$. The Gaussian center $`t=s_b`$ ranges over the entire positive real axis. For $`s\ge0`$ set

```math
K(s,t)=(4\pi t)^{-1/2}\exp[-(s-t)^2/(4t)].
```

Equation (5.66) uses $`\int_0^\infty K(s,t)\,dt=1`$. This follows by expanding the square and using the elementary Gaussian integral $`\int_0^\infty t^{-1/2}e^{-at-b/t}dt=\sqrt{\pi/a}\,e^{-2\sqrt{ab}}`$ for $`a>0`$, $`b\ge0`$. No cutoff on $`t`$ enters the identity.

Here is a conditional estimate for the coefficient comparison. Assume the ensemble construction of §5.3 and its positive limiting mass for $`B=[S/4,S/2]`$ in (5.63) and footnote 24. Denote the unnormalized positive area measure in (5.56) by $`\mu`$, with $`Z=\mu([0,S])`$. The weighted integral in (5.66), restricted to centers $`I=[S/8,3S/4]`$, is $`J_I=\int\mu(ds)\int_I K(s,t)\,dt`$ by (5.25). For $`s\in B`$ both omitted tails are uniformly small:

- For $`0<t<S/8`$, one has $`(s-t)^2/(4t)\ge S/32`$. The lower tail is at most $`\sqrt{S/(8\pi)}e^{-S/32}`$.
- For $`t>3S/4`$, one has $`s\le 2t/3`$, hence $`(s-t)^2/(4t)\ge t/36`$. The upper tail is at most $`3\,\mathrm{erfc}(\sqrt{S/48})`$.

Consequently $`(1-o(1))\mu(B)\le J_I\le Z`$. Since $`\mu(B)/Z`$ tends to a positive constant, $`J_I`$ and $`Z`$ have the same leading logarithmic exponent. This reasoning does not require controlling the tails at every allowed area. If the one-loop trace scales as $`t^p`$ up to positive multiplicative constants uniform across the interior window, its contribution there has order $`S^{p+1/2}`$, as seen by substituting $`t=Su`$. The question worth asking is what gives that uniform saddle estimate as the diamond grows. The bound uses the paper's band-mass premise and makes no independent derivation of it. A missing global tail estimate alone does not establish a failure.

There is a separate overstatement in Neon's report. Equation (5.58) gives $`\log Z=[q/(1-q)+o(1)]\log(\ell/\ell_0)`$. Its remainder may grow as $`o(\log\ell)`$ and need not be $`O(1)`$. Comparing leading exponents still yields $`q/(1-q)=2p+1`$, so the coefficient in (5.69) is $`p`$ in the regime where that comparison applies. Equation (5.67) supplies geometric and heat-kernel input, including the Schwarzschild and spherical-cut assumptions. The algebra explains why that input is recovered.

## Scope of F5–F7

- **Pair amplitude, (4.32)–(4.34).** The displayed series and Neon's expansion give $`A(s)\to0`$ and $`s^2 A(s)\to\pi^2/12`$ at fixed area as $`G_N\to0^+`$. The phase matters for the cubic logarithm. Absolute convergence already follows from the Gaussian variance. One sentence in Neon's verdict divides by $`t^2`$ for $`t=2/s`$. The actual amplitude is $`t^2\mathrm{Li}_2(e^{-it})/8`$. Preservation of this variance by an interacting Hamiltonian would be a question for an extension to that dynamics. The specific externally prepared overlap in (4.33) needs no such preservation.
- **One-loop conservation, (6.13)–(6.16).** Equation (6.15) derives conservation for classical on-shell linearized perturbations. Appendix D.2, immediately after (D.20), explicitly subtracts the vacuum singularity in the shear contraction before coincidence and discusses local curvature terms. The remaining technical question is whether a prescription for the full composite source, including its contact and boundary terms, obeys the corresponding renormalized conservation identity. Fixed smearing is part of the observable. Independence from arbitrary changes of that smearing requires a separate claim. The manuscript retains $`\Lambda`$ as a parameter. Zero-$`\Lambda`$ on-shell vacuum scattering is a narrower setting. The formal match through one loop does not settle regulator-dependent anomalies or the interacting two-loop behavior.
- **Clock and representation, (4.16)–(4.17), (5.1)–(5.2), footnote 20.** A pure extension gives $`\pi_\omega(\mathcal A)''=\mathcal B(\mathcal H_\omega)`$. Appendix C.2 discusses the cutoff quadratic forms and the density argument at fixed area, including (C.11)–(C.17). Appendix C.3 discusses the sector embedding and unrestricted intermediate insertions in (C.21). A precise question is how the clock's spectral projections on the full representation compare across admissible extensions. Intertwining the clock, area, and preparation data would suffice for equality of the associated predictions. Equality of particular numerical observables can also occur under weaker conditions. No pair of extensions with different physical predictions was constructed here.

The checks warrant narrowing the public claims about tails, conservation and representation dependence. The §5.2 issue remains a request for an independent finite-closure argument for this preparation. Neither Neon's report nor this follow-up supplies a refutation.
