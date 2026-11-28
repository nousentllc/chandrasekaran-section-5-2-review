"""Reproduce finite algebra checks from the gluing-bound follow-up."""

from fractions import Fraction as F
from itertools import product
from math import log


def check_open_and_closed_sections():
    weight = F(1, 4)
    delta = F(1, 2)
    # On the full open cut, x_i = 2**(-i), y_i = 3**(-i), i >= 1.
    # The squared norms are 1/3 and 1/8, so their product is 1/24.
    open_norm_product_squared = F(1, 24)
    rank_results = []
    for rank in (4, 16, 64, 256):
        open_sum = (1 - F(1, 6) ** rank) / 5
        assert 0 < open_sum < F(1, 5)
        assert open_sum**2 <= open_norm_product_squared
        closed_sum = -delta * weight * rank / 2
        assert closed_sum == F(-rank, 16)
        rank_results.append(closed_sum)
    return rank_results


def purity(weights):
    total = sum(weights)
    return sum(weight**2 for weight in weights) / total**2


def check_purity_envelope():
    cases = 0
    for floor in (F(1, 8), F(1, 4), F(1, 2), F(3, 4), F(1)):
        allowed = (floor, (1 + floor) / 2, F(1))
        for rank in range(1, 7):
            for weights in product(allowed, repeat=rank):
                ratio = purity(weights)
                assert F(1, rank) <= ratio <= (1 + floor) ** 2 / (4 * floor * rank)
                assert ratio <= 1 / sum(weights)
                cases += 1
        # At floor = p/q, p/(p+q) of the weights are one.
        p, q = floor.numerator, floor.denominator
        weights = (F(1),) * p + (floor,) * q
        assert purity(weights) == (1 + floor) ** 2 / (4 * floor * len(weights))
    return cases


def check_noncommuting_compression():
    # T = diag(1/4, 1/2, 1). Compress onto (3/5, 4/5, 0) and (0, 0, 1).
    floor = F(1, 4)
    a, b = F(3, 5), F(4, 5)
    assert a**2 + b**2 == 1
    commutator_entry = a * b * (floor - F(1, 2))
    assert commutator_entry != 0
    weights = (a**2 * floor + b**2 * F(1, 2), F(1))
    ratio = purity(weights)
    assert F(1, 2) <= ratio <= (1 + floor) ** 2 / (8 * floor)
    return ratio


def check_focusing_envelope():
    # alpha = 1/2 and w = 2**(-2*k) give exp(Xi(1)) = 2**k exactly.
    samples = []
    for k in (2, 4, 8, 16):
        width = F(1, 2 ** (2 * k))
        clock_excess_upper = width * (2**k - 1)
        # The 1/4 in (4.22) gives a velocity-cost lower bound of 4*k*log(2).
        velocity_cost_lower = 4 * k * log(2)
        assert 0 < clock_excess_upper < F(1, 2**k)
        if samples:
            assert clock_excess_upper < samples[-1][0]
            assert velocity_cost_lower > samples[-1][1]
        samples.append((clock_excess_upper, velocity_cost_lower))
    return samples


def main():
    print("Closed amplitudes at ranks 4, 16, 64, 256:",
          ", ".join(map(str, check_open_and_closed_sections())))
    print("Exact replica cases:", check_purity_envelope())
    print("Noncommuting compression ratio:", check_noncommuting_compression())
    for upper, lower in check_focusing_envelope():
        print(f"Clock excess <= {float(upper):.6g}; velocity cost >= {lower:.6g}")


if __name__ == "__main__":
    main()
