import sympy as sp
p,s,t,q=sp.symbols('p s t q',positive=True)
# (5.66): Z(l) ~ int^{s*} s_b^{-1/2} s_b^p ds_b ~ s*^{p+1/2}, s* ~ l^2  => exponent of l
expo = 2*(p+sp.Rational(1,2))
# (5.58): log Z = q/(1-q) log l  => solve for q
qsol = sp.solve(sp.Eq(q/(1-q), expo), q)[0]
# (5.69): coefficient at fixed mass
coef = sp.simplify(qsol/(2*(1-qsol)) - sp.Rational(1,2))
print("q(p) =", qsol, "  final coefficient =", coef)
print("p=106/45 -> q =", qsol.subs(p,sp.Rational(106,45)))
# (5.66) normalization: int_0^inf exp(-(s-t)^2/(4t)) (4 pi t)^(-1/2) dt == 1 ?
I = sp.integrate(sp.exp(-(s-t)**2/(4*t))/sp.sqrt(4*sp.pi*t),(t,0,sp.oo))
print("normalization integral =", sp.simplify(I))
# footnote 23 consistency: power-law ensemble Pr(a)=a^k, k=q/(2(1-q)); <a> = k/(k+1) = x^2
k=sp.Rational(257,90); print("x^2 =", k/(k+1), " fn23 q=2x^2/(1+x^2) ->", sp.nsimplify(2*(k/(k+1))/(1+k/(k+1))))
