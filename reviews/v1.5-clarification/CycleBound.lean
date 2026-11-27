import Mathlib

namespace CycleBound

/-- Scalar estimate for one complete-cycle cut. Here W is its identity weight
and r is the real part of its normalized boost response. -/
theorem two_sided {W δ r : ℝ} (hW : 0 ≤ W) (hr : |r| ≤ δ / 4) :
    -(3 * δ / 4) * W ≤ W * (r - δ / 2) ∧
      W * (r - δ / 2) ≤ -(δ / 4) * W := by
  obtain ⟨hlo, hhi⟩ := abs_le.mp hr
  constructor
  · nlinarith [mul_nonneg hW (sub_nonneg.mpr hlo)]
  · nlinarith [mul_nonneg hW (sub_nonneg.mpr hhi)]

/-- An upper bound B on the magnitude of the negative real part controls
the rank parameter n. Identifying the physical weight and proving the
uniform bound for a family of cuts are separate assumptions. -/
theorem rank_of_cut_bound {c δ W r n B : ℝ} (hc : 0 < c) (hδ : 0 < δ)
    (hW : 0 ≤ W) (hr : |r| ≤ δ / 4) (hfloor : c * n ≤ W)
    (hbound : -(W * (r - δ / 2)) ≤ B) : n ≤ 4 * B / (c * δ) := by
  have hcut := (two_sided hW hr).2
  apply (le_div_iff₀ (mul_pos hc hδ)).2
  nlinarith [mul_nonneg hδ.le (sub_nonneg.mpr hfloor)]

end CycleBound

#print axioms CycleBound.two_sided
#print axioms CycleBound.rank_of_cut_bound
