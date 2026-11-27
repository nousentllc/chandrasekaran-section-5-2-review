"""Finite Fourier blocks illustrating the two-index absolute sum in the pair-amplitude section."""

import numpy as np


def check_block(m):
    size = 4**m
    index = np.arange(size)
    fourier = np.exp(-2j * np.pi * np.outer(index, index) / size) / np.sqrt(size)
    amplitude = 1 / (m * np.sqrt(size))
    paths = amplitude**2 * fourier
    np.testing.assert_allclose(np.abs(paths).sum(), 2**m / m**2, rtol=1e-12)
    np.testing.assert_allclose(paths.sum(), 1 / (2**m * m**2), atol=1e-13)
    print(f"block {m}, dimension {size}, absolute sum {np.abs(paths).sum():.8f}")


def main():
    for m in range(1, 5):
        check_block(m)


if __name__ == "__main__":
    main()
