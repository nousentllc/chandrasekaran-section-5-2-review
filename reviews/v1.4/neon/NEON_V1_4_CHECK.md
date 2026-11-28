# Review of Neon's response to Claude's v1.4

27 November 2026. Neon compared the revised note with the manuscript and the earlier Codex assessment. The accompanying response preserves the user's pasted text verbatim, including its citation placeholder. Neon reports an analytic review. The Lean and Python executions are recorded separately in the [v1.4 verification record](../README.md). Equation numbers below refer to [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/pdf/2611.34924v1).

## What v1.4 resolved

- **F5.** The fixed-area limits in (4.32)–(4.34) are now stated precisely. The unscaled amplitude tends to zero and the rescaled amplitude tends to $\pi^2/12$. The phase produces a crossover at $k\sim s$ in a convergent free-field sum.
- **F6.** The revised note recognizes the one-loop agreement and limits its UV implications. The qualification on one-loop scattering at $\Lambda=0$ concerns ultraviolet divergences. Section 6 allows nonzero $\Lambda$. The manuscript specifies state and contour boundary conditions in (6.16) and (D.1). The open issue concerns renormalization of the full composite source and its boundary terms.
- **F7.** The revision distinguishes the represented algebra from its bicommutant in (4.17). Neon's statement that invariance *requires* unitary equivalence needs qualification. A unitary intertwining the representations and the clock, area, and preparation data suffices to preserve the resulting predictions. Equality of a particular rank, spectrum, or entropy can hold under weaker conditions. Footnote 20 leaves equivalence open.

## How much of (5.66) comes from the interior band?

Assume the finite thermal ensemble in §5.3, the support $0\le s\le S=s_*$, and the limiting distribution (5.63). Let $s$ be drawn with thermal weights $e^{-s}/Z$ including multiplicity, as in (5.56). Write $t=s_b$ for the continuous Gaussian center. Conditional on $s$, (5.25) and (5.66) give the normalized density

$$
K(s,t)=(4\pi t)^{-1/2}\exp[-(s-t)^2/(4t)],\qquad t>0.
$$

The marginal probability of $t\in I$ is exactly the contribution to the (5.66) integral from centers in $I$, divided by $Z$. This makes it possible to calculate that fraction without identifying the center $t$ with an eigenvalue $s$.

For $u<1/4$, integrating $e^{ut}K(s,t)$ gives

$$
M_s(u)=(1-4u)^{-1/2}\exp\left[\frac{s}{2}\left(1-\sqrt{1-4u}\right)\right].
$$

For example, write the exponent inside the integral as $s/2-(1/4-u)t-s^2/(4t)$ and use the Gaussian integral from the [earlier tail calculation](../../v1.2/neon/NEON_REVIEW_CHECK_v1.2.md). Differentiating at zero gives $\mathbb E[t\mid s]=s+2$, $\mathrm{Var}(t\mid s)=2s+8$, and $\mathbb E[(t-s)^2\mid s]=2s+12$. Hence, for every fixed $\varepsilon>0$,

$$
\Pr(|t/S-s/S|>\varepsilon)\le\frac{2S+12}{\varepsilon^2 S^2}\longrightarrow0.
$$

Equation (5.63) gives the continuous limiting distribution function $F(a)=a^\alpha$ for $0\le a\le1$, with $\alpha=q/[2(1-q)]>0$. Moving a band endpoint by $\varepsilon$ changes its limiting probability by an amount tending to zero with $\varepsilon$. The probability bound therefore transfers the same limiting distribution from $s/S$ to $t/S$. In particular, the fraction of the full integral from centers $S/4<t<S/2$ tends to

$$
c_0=2^{-\alpha}-4^{-\alpha}>0.
$$

At the reported $q=257/302$ this fraction is approximately $0.119074$. The other centers can supply most of the normalization. A band with limiting mass $c_0>0$ nevertheless determines the same growth exponent as the full positive integral. This argument assumes (5.63) and addresses a later entropy calculation. It cannot supply the existence of the finite ensemble in §5.2.

## What estimate suffices for F2?

On $I_S=[S/4,S/2]$ write $L_S(t)=\log\mathrm{Tr}(C_b^\dagger C_b)=p\log t+R_S(t)$. A uniform $O(1)$ bound on $R_S$ gives two-sided constant multiples of $S^{p+1/2}$ for the band integral by (5.66). It does not on its own give a limiting proportionality constant. An even weaker sufficient bound for the **leading logarithmic coefficient** is $\sup_{t\in I_S}|R_S(t)|=o(\log S)$. Indeed, the integral of $t^{p-1/2}$ on $I_S$ is a fixed positive constant times $S^{p+1/2}$, and the exponential of the remainder changes it by at most factors $S^{\pm o(1)}$. Since the band fraction tends to $c_0$, this gives

$$
\log Z=(p+1/2)\log S+o(\log S).
$$

Pointwise control for individual saddles does not by itself justify this integrated estimate. A uniform estimate or a direct estimate of the band integral would suffice. The Gaussian kernel alone gives no bound on the determinant remainder. We have not derived that remainder from the gravitational theory.

With $S\propto\ell^2$, comparison to (5.58) then gives $q/(1-q)=2p+1$. Equation (5.69) returns $q/[2(1-q)]-1/2=p$. The model's $0<q<1$ entails $p>-1/2$ on this branch. The value $106/45$ enters through (5.67c), and the ensemble conversion preserves it. The consistency of that conversion and the physical assumptions behind (5.67) remain part of the result.

## The §5.2 question for the author

What independently bounds the positive identity-cut partial traces for this four-dimensional doubled preparation, or proves that they converge to its finite uncut norm? Given (5.30c), $C_b^\dagger C_b\ge cI$ with $c>0$, a common upper bound $N$ immediately bounds the dimension by $N/c$. The manuscript's (5.38) uses a specific signed insertion. The open-vector bound (4.30) needs an additional identification to control the identity closure. Appendix E's application in (E.17) uses the §5.2 conclusion. Granting finite identity gluing makes the boost-cycle argument redundant for the dimension bound. Circularity would require using finite dimension to establish the premise on which that bound relies. The dimension of the physical four-dimensional space remains open.

The accompanying check differentiates the moment formula symbolically and independently integrates the kernel and its moments numerically, including the endpoint $s=0$. It also checks the coefficient arithmetic. The concentration and band-limit arguments above are analytic.
