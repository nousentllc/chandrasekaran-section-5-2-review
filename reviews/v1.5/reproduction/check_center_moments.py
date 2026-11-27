"""Check the conditional moments of Eq. (5.66) and the coefficient in Eq. (5.69)."""

import mpmath as mp
import sympy as sp


def check_moment_formula():
    u, s = sp.symbols("u s", real=True)
    root = sp.sqrt(1 - 4 * u)
    transform = sp.exp(s * (1 - root) / 2) / root
    mean = transform.diff(u).subs(u, 0)
    second = transform.diff(u, 2).subs(u, 0)
    assert transform.subs(u, 0) == 1
    assert sp.simplify(mean - (s + 2)) == 0
    assert sp.simplify(second - mean**2 - (2 * s + 8)) == 0
    assert sp.simplify(second - 2 * s * mean + s**2 - (2 * s + 12)) == 0


def check_quadrature(s):
    # t = x^2 removes the square-root singularity at the origin for s = 0.
    def density(x):
        if x == 0:
            return 1 / mp.sqrt(mp.pi) if s == 0 else 0
        return mp.exp(-((x*x - s) / (2*x))**2) / mp.sqrt(mp.pi)

    grid = [0, mp.sqrt(s + 1), mp.sqrt(s + 1) + 4, mp.inf]
    norm = mp.quad(density, grid)
    mean = mp.quad(lambda x: x*x * density(x), grid)
    offset_moment = mp.quad(lambda x: (x*x - s)**2 * density(x), grid)
    assert abs(norm - 1) < mp.mpf("1e-28")
    assert abs(mean - (s + 2)) < mp.mpf("1e-28")
    assert abs(offset_moment - (2*s + 12)) < mp.mpf("1e-28")


def check_coefficient():
    p = sp.Rational(106, 45)
    q = (p + sp.Rational(1, 2)) / (p + 1)
    alpha = q / (2 * (1 - q))
    assert q == sp.Rational(257, 302)
    assert alpha - sp.Rational(1, 2) == p
    return float(2**(-alpha) - 4**(-alpha))


def main():
    mp.mp.dps = 45
    check_moment_formula()
    for s in (0, 1, 20, 200):
        check_quadrature(s)
    fraction = check_coefficient()
    print(f"Symbolic and numerical moment checks passed. Band fraction: {fraction:.12f}")


if __name__ == "__main__":
    main()
