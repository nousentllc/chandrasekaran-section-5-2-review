# Can open gluing bound the closed amplitude in (5.38)?

Follow-up to [*Finite closure in null-cone quantization of gravity*](https://doi.org/10.5281/zenodo.24585121). Equation numbers without a section label refer to [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/html/2611.34924v1). This operator analysis was carried out by OpenAI Codex at Justin Candler’s request.

**Result.** The open gluing law (4.29)–(4.30), even with exact unitarity, does not imply a bound for the closed (5.38) amplitudes. With the positive weight in (5.30c) and the refined-cycle estimate (5.32), (D.25), the ordinary closed amplitudes have magnitude at least proportional to rank. A separate, finite positive gluing functional that agrees on individual basis-state insertions would furnish the bound. An exact lower bound on the two-copy ratio in (D.47) would also furnish it. The first-order realization of Appendix E uses finite dimension to check finiteness in (E.17). Appendix D.3 obtains its positive ratio for a regular one-loop family. The four-dimensional bound remains open.

## 1. Apply the open estimate to the doubled state

Let $H=\mathcal H_{\mathscr D}$, $C=C_b:H\to K$ for the outgoing space $K$, and $T=C^\dagger C$. At fixed preparation and clock cutoff, (5.21d), (5.23b), (5.25) and (5.30c) give $cI\le T\le I$ with $c=e^{-s_*}\min_{[0,s_*]}f_b>0$. This step uses exact cap unitarity on $H$. Fix the boost and the bounded insertion $X$ from (5.37a).

For an arbitrary finite-rank orthogonal projection $P$, with basis $e_i$ of $PH$, let

$$
\Phi_P=\sum_i Ce_i\otimes\overline{e_i},\qquad
W_P=\|\Phi_P\|^2=\mathrm{Tr}(PT),\qquad
Z_P[X]=\langle\Phi_P,X\Phi_P\rangle.
$$

The vector $\Phi_P$ is independent of the basis of $PH$. Indeed, it is the Hilbert–Schmidt vector of $CP$; the normalized version is (D.22), and (5.31) includes both diagonal and off-diagonal terms in its expectation. Orthogonality on the conjugate leg gives $c\,\mathrm{rank}\,P\le W_P\le\mathrm{rank}\,P$. For nested cuts $P\le Q$, it also gives $\|\Phi_Q-\Phi_P\|^2=W_Q-W_P$. If $H$ is infinite-dimensional and the projections exhaust a basis, $\Phi_P$ is unbounded in norm. A change of orthonormal basis leaves the bound intact.

In (4.29) the resolution of the identity is tested between fixed vectors $x,y$ after transporting the external states to the cut. In finite sections,

$$
\left|\langle y,Px\rangle\right|\le\|x\|\|y\|,\qquad
\sum_i|\langle y,e_i\rangle\langle e_i,x\rangle|
\le\|x\|\|y\|.
$$

Applying a norm estimate to the actual external vectors of the doubled expectation gives

$$
|Z_P[X]|\le\|\Phi_P\|\|X\Phi_P\|\le\|X\| W_P.
$$

This is at most a bound proportional to rank. The contraction associated with $C$ is a vector in the ordinary Hilbert tensor product precisely when $C$ is Hilbert–Schmidt, equivalently $\sup_P W_P=\mathrm{Tr}(T)<\infty$. A finite norm for $Ce$ for every unit state $e$, or density of the states generated in (5.20), supplies none of this summability. The shift $-\delta_\eta I/2$ in $X$ tests that very summability.

### The signed insertion does not cancel this growth

Under the infinite-dimensional hypothesis, refine the complete-cycle cuts as in (5.32), (D.25) to give $|r_P|\le\delta_\eta/4$, where $r_P=\langle\Delta_\eta\widehat{\mathcal O}\rangle_P$. With the same preparation and insertion on each cut, (5.38) yields

$$
Z_P[X]=W_P(r_P-\delta_\eta/2),\qquad
\mathrm{Re}\,Z_P[X]\le -\delta_\eta W_P/4,\qquad
|Z_P[X]|\ge \tfrac{\delta_\eta c}{4}\mathrm{rank}\,P.
$$

This also holds for complex responses. An exhaustion by finite unions of cycles reaches arbitrarily high rank when $H$ is infinite-dimensional, and the same holds along any cofinal family. Thus a bound by $B$ along such a family gives $\dim H\le4B/(\delta_\eta c)$ when the hypotheses hold on the family. When the cycle estimates are supplied only under the infinite-dimensional hypothesis, the result is a contradiction of that hypothesis. It takes no passage to a strict sign for the uncut amplitude. Since the expectations are quadratic in $\Phi_P$, the proof does not rely on additivity of signed amplitudes over disjoint cycles.

For an elementary separation, take $H=K=\ell^2(\mathbb N)$, $U=I$ and the area operator equal to a scalar in $[0,s_*]$. Then $T=tI$ for $0<t\le1$, the boost is a scalar phase, and $Z_P[X]=-t\delta_\eta\mathrm{rank}\,P/2$ for any fixed positive test shift $\delta_\eta$. Formula (4.30) holds for all fixed external vectors. The stronger [model with a separate nonzero boost response](../../REVIEW.md#positive-uncut-response-and-uniformly-suppressed-cut-response-can-coexist-without-identification) tests the reference-state issue. The scalar model tests only the implication from open gluing. It supplies neither the physical smooth-background shift nor a model of the nonlinear field equations.

## 2. Try the stronger gluing law in Appendix E

There is a short sufficient condition that avoids assuming a limit of signed amplitudes. Fix $C$ as above. Suppose the path integral independently gives a positive linear functional $F$ on a space of bounded insertions containing $I$ and the finite cut projections, with $F(I)=N<\infty$. Require that this space contains $I-P$ with its ordinary positive operator order, and that finite-rank closure matches $F(P)=\mathrm{Tr}(PT)$ on the cut projections. Agreement on individual basis projections plus linearity suffices. Then

$$
W_P=F(P)\le F(I)=N,\qquad |Z_P[X]|\le\|X\|N.
$$

Positivity alone gives the inequality, even before proving normality of $F$ or identifying its value on an infinite cut. For a complete basis, the same premise gives $\dim H\le N/c$. Conversely, if $T$ has finite ordinary trace, $F(A)=\mathrm{Tr}(T^{1/2}AT^{1/2})$ is such a positive functional on $\mathcal B(H)$. This is an exact criterion for the standard identity closure.

Condition 5 of §E.1 assumes finite compatible closed amplitudes for a class of smeared preparations. If this is taken as an independent axiom, one needs to place the clock-selected preparation in that class and identify its finite-rank matrix-element weights and order with the corresponding positive closure. One possible application is (E.5): a compactly supported $g$ equal to one on the bounded boost spectrum acts as the identity on the clock-selected sector. A finite value in that sector for the same reflected preparation, with the stated finite-rank compatibility, would do the job. Finiteness of an abstract trace on a different representation, or on a different sector, gives no such comparison. In §E.3, (E.15) identifies the trace in the physical Hilbert space, but (E.17) verifies finiteness there using (5.39c). Using that verification upstream would be circular. The conditional argument in this section gives a way to use an independently justified geometric closure.

### A Bessel inequality version using the product preparations of §5.4

Equations (5.71)–(5.74) suggest the following simpler test of the Hilbert-space construction. Let the connected preparation prospectively give a finite-norm vector $\Psi$ in the physical space of the two boundaries, with norm squared $N$. Assume disconnected product preparations have their usual product inner products, as furnished by factorization (E.2) on their closed pairings. For any orthonormal family $e_i$ in $H$, evolve to $f_i=Ue_i$ at the outgoing cap. The product preparations $q_i=f_i\otimes\overline{e_i}$ are orthonormal under these inner products. If gluing one such product onto the connected preparation gives the coefficient from (5.72) with $N_M=C_b=UT^{1/2}$, then

$$
\big|\langle q_i,\Psi\rangle\big|
=\big|\langle Ue_i,C_be_i\rangle\big|
=\langle e_i,T^{1/2}e_i\rangle\ge\sqrt c .
$$

Bessel’s inequality gives $cn\le N$ for a family of $n$ states. This uses only diagonal product overlaps and finite-rank Bessel inequalities. It requires neither an area eigenbasis nor completeness of the product states in the two-boundary space. In particular, the use of Bessel does not require (5.73), whose trace formula presupposes control of the connected norm. This route reduces the missing input to constructing a single geometric preparation of finite norm with the stated overlaps, compared with proving convergence of the entire signed cut net. Equation (5.71) does not give an independent finite-norm construction for that preparation.

## 3. Try the two-copy gluing calculation in Appendix D.3

The exact ratio in (D.47) supplies another test. Write $T_P=PTP|_{PH}$, $n=\mathrm{rank}\,P>0$ and

$$
R_P(2)=\frac{\mathrm{Tr}(T_P^2)}{(\mathrm{Tr}\,T_P)^2}.
$$

If $R_P(2)\ge r>0$ on a cofinal family, (D.47) gives $W_P\le 1/r$, so $B=\|X\|/r$ suffices. The implication uses neither a ratio limit nor a presumed finite partition function. With the stronger hypothesis (5.30c), the inverse-rank behavior is quantitative. For eigenvalues $\lambda_i\in[c,1]$ of $T_P$, put $\mu=n^{-1}\sum_i\lambda_i$. Since $(\lambda_i-c)(1-\lambda_i)\ge0$, we have

$$
\frac1n\le R_P(2)\le
\frac{(1+c)\mu-c}{n\mu^2}\le\frac{(1+c)^2}{4cn}.
$$

The lower bound is Cauchy–Schwarz. The final inequality follows from $((1+c)\mu-2c)^2\ge0$. The upper constant is attained if the fraction of unit eigenvalues is $c/(1+c)$ and the rest are $c$, whenever this fraction is realizable for the given rank. This applies to compressions even when $P$ and $T$ fail to commute. A proposed lower bound $r$ now also gives $n\le (1+c)^2/(4cr)$.

The ratio $R^{\rm reg}_2$ in (D.48)–(D.49) is obtained from the regular one-loop saddles with the mode count in (D.45)–(D.46) and the disk factor in (D.48). A comparison of that number with the exact $R_P(2)$ needs to account for the disk factor and the full clock-selected state space. For instance, an error bound $|R_P(2)-R^{\rm reg}_2|\le\varepsilon<R^{\rm reg}_2$ uniform on a cofinal family would close the argument. A finite number of regular excitations at each fixed area does not give this. Even a direct integral with one-dimensional fibers over a continuous area interval, such as $L^2([0,1],ds)$ with area acting by multiplication, has an infinite-dimensional full space. The integral of fiber dimensions is finite in this example, while the ordinary trace of any bounded strictly positive area weight diverges. The example isolates a requirement on the area sectors. It is independent of the saddle approximation.

## 4. Can clock focusing supply the missing estimate?

A sufficient operator estimate would exhibit a nonnegative excitation operator $Q$ on the full representation with $\mathrm{Tr}(e^{-\beta Q})<\infty$ for some $\beta>0$, and a form bound $\langle e,Qe\rangle\le a\ell(\mathscr D)+b$ for every unit $e\in P_{\mathscr D}H_\omega$, including the domain assertion. Jensen’s inequality for the spectral measure of $Q$ gives $\langle e,e^{-\beta Q}e\rangle\ge e^{-\beta(a\ell(\mathscr D)+b)}$. Summing over a finite orthonormal family then yields

$$
\dim(P_{\mathscr D}H_\omega)
\le e^{\beta(a\ell(\mathscr D)+b)}\mathrm{Tr}(e^{-\beta Q}).
$$

The same premise bounds (5.38) by multiplying the right side by $\|X\|$. It requires no commutation between $Q$ and the clock. Equations (D.40)–(D.46) provide a candidate excitation cost and heat-trace estimate in a regular fixed-data oscillator calculation. A trace over the entire representation and a uniform comparison covering all allowed states are additional steps.

There is a specific obstruction to taking the clock form alone as an upper estimate on local shear in (D.35). In the classical single-generator specialization of (4.22)–(4.27), keep the second polarization constant and write $\Xi(v)=\int_\epsilon^v t|z'(t)|^2\,dt/4$ for one varying polarization $z$. Choose a smooth bump $z$ supported in $(1-w,1)$, with $0<w<1-\epsilon$. Scale the bump so $\Xi(1)=\alpha\log(1/w)$ for any fixed $0<\alpha<1$. It vanishes at both ends and $0\le\Xi(v)\le\Xi(1)$. The change in the focusing contribution to the clock obeys

$$
\int_\epsilon^1(e^{\Xi(v)}-1)\,dv
\le w(e^{\Xi(1)}-1)\longrightarrow 0,
\qquad
\int_{1-w}^1 |z'(v)|^2\,dv\ge 4\alpha\log(1/w)\longrightarrow\infty .
$$

Thus the clock integral by itself does not bound a squared conformal-velocity cost in a fixed neighborhood of the corner. This check uses the dimensionless radial variable $v$. It does not identify that cost with the exact affine, transverse-smeared, vacuum-subtracted operator in (D.28), and it imposes no transverse focusing or fixed-cap expansion constraint from (D.38)–(D.40). Those are possible sources of additional control. The classical example therefore tests a shortcut from (4.27), and leaves the full quantum estimate open.

## Reproduce the finite calculations

From the repository root run the following with Python 3.10 or later. The script uses only the standard library. It checks the exact rational rank and replica inequalities, includes a noncommuting compression, and samples the analytic upper envelope for the corner-localized focusing contribution. It does not simulate gravity or prove the operator and path-integral identifications.

    python3 reviews/gluing-bound/check_gluing_bound.py

The [checked scalar signed-cycle inequality](../v1.5-clarification/CycleBound.lean) and the [released verification record](../v1.5-final/reproduction/reference/final-lean.log) cover the previously formalized part of the argument.
