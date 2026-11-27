"""Numerical illustrations of the analytic bounds on the kernel in Eq. (5.66)."""

from mpmath import mp


def check_band(max_area, area_fraction):
    area = max_area * area_fraction
    lower = mp.mpf(max_area) / 8
    upper = 3 * mp.mpf(max_area) / 4

    def kernel(center):
        return mp.exp(-(area - center) ** 2 / (4 * center)) / mp.sqrt(4 * mp.pi * center)

    left = mp.quad(kernel, [0, lower])
    middle = mp.quad(kernel, [lower, area, upper])
    right = mp.quad(kernel, [upper, 2 * max_area, mp.inf])
    assert left <= mp.sqrt(max_area / (8 * mp.pi)) * mp.exp(-mp.mpf(max_area) / 32)
    assert right <= 3 * mp.erfc(mp.sqrt(mp.mpf(max_area) / 48))
    assert abs(left + middle + right - 1) < mp.mpf("1e-32")


def main():
    mp.dps = 45
    for max_area in (64, 256, 1024):
        for numerator in (2, 3, 4):
            check_band(max_area, mp.mpf(numerator) / 8)
        print(f"S = {max_area}: normalization and both tail bounds passed at three areas")


if __name__ == "__main__":
    main()
