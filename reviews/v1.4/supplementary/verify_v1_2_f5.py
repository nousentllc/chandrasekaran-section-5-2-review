"""Independent checks of the series and asymptotics in arXiv:2611.34924v1 (4.33).

Run with Python 3 and mpmath: python3 verify_v1_2_f5.py
"""

import cmath
import math

import mpmath as mp


def partial_amplitude(s: float, count: int) -> complex:
    return sum(cmath.exp(-2j * k / s) / (2 * s * s * k * k) for k in range(1, count + 1))


def exact_amplitude(s: mp.mpf) -> mp.mpc:
    return mp.polylog(2, mp.exp(-2j / s)) / (2 * s * s)


def main() -> None:
    mp.mp.dps = 50
    count = 200_000
    for s_float in (10.0, 100.0):
        s = mp.mpf(s_float)
        partial = partial_amplitude(s_float, count)
        exact = exact_amplitude(s)
        error = abs(mp.mpc(partial.real, partial.imag) - exact)
        tail_bound = 1 / (2 * s * s * count)
        assert error <= tail_bound + mp.mpf("1e-12")
        print(f"s={s_float:g}: partial error={mp.nstr(error, 8)}, tail bound={mp.nstr(tail_bound, 8)}")

    for s_int in (100, 1_000, 10_000):
        s = mp.mpf(s_int)
        amplitude = exact_amplitude(s)
        leading = mp.zeta(2) / (2 * s * s)
        next_term = 1j * (mp.log(2j / s) - 1) / (s**3)
        assert abs(amplitude - leading - next_term) < 1 / (s**4)
        print(
            f"s={s_int}: A={mp.nstr(amplitude, 12)}, "
            f"s²A={mp.nstr(s*s*amplitude, 12)}, "
            f"s²A(no phase)={mp.nstr(mp.zeta(2)/2, 12)}"
        )

    assert math.isclose(float(mp.zeta(2) / 2), math.pi**2 / 12)
    print("As s→∞, A(s)→0 while s²A(s)→ζ(2)/2.")


if __name__ == "__main__":
    main()
