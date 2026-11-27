/-
  TraceDim.lean — verified core for the §5.2 audit of arXiv:2611.34924v1.

  STATUS: written against current Mathlib, NOT YET COMPILED. The sandbox could not
  install the Lean toolchain. To check it:
    lake new tracedim math && cd tracedim
    # put this file in Tracedim/TraceDim.lean
    lake exe cache get && lake build

  SCOPE. This file proves only pure mathematics:
    (1) If c‖x‖² ≤ Re⟪x, T x⟫ for all x, then for any finite orthonormal family F,
        c·|F| ≤ Σ_{i∈F} Re⟪eᵢ, T eᵢ⟫.
    (2) If those partial sums are bounded by N and c > 0, then every finite
        subfamily has |F| ≤ N/c, and so the orthonormal family is finite.

  INTERPRETATION (not formalized). Take T = C_b† C_b and c = e^{-s*} m_{b,D}
  from Eq. (5.30c). The hypothesis `hN` is what the paper's gluing premise
  (Sec. 4.4 via Eq. 4.29, applied with the insertion X = 1) would supply. This file
  does not claim the paper asserts `hN`. That question is open and is the
  subject of the inquiry to the author.
-/
import Mathlib

open scoped InnerProductSpace

variable {𝕜 : Type*} [RCLike 𝕜] {E : Type*} [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]

/-- Lower operator bound ⇒ partial traces over orthonormal families grow at least
linearly in the number of vectors. -/
theorem card_mul_le_sum {ι : Type*} (T : E →L[𝕜] E) (c : ℝ)
    (hlow : ∀ x : E, c * ‖x‖ ^ 2 ≤ RCLike.re ⟪x, T x⟫_𝕜)
    (e : ι → E) (he : Orthonormal 𝕜 e) (F : Finset ι) :
    c * F.card ≤ ∑ i ∈ F, RCLike.re ⟪e i, T (e i)⟫_𝕜 := by
  calc c * (F.card : ℝ) = ∑ i ∈ F, c * ‖e i‖ ^ 2 := by
        simp [he.1, Finset.sum_const, nsmul_eq_mul, mul_comm]
    _ ≤ ∑ i ∈ F, RCLike.re ⟪e i, T (e i)⟫_𝕜 :=
        Finset.sum_le_sum fun i _ => hlow (e i)

/-- Bounded partial traces + positive lower bound ⇒ |F| ≤ N / c. -/
theorem card_le_of_trace_bound {ι : Type*} (T : E →L[𝕜] E) {c N : ℝ} (hc : 0 < c)
    (hlow : ∀ x : E, c * ‖x‖ ^ 2 ≤ RCLike.re ⟪x, T x⟫_𝕜)
    (e : ι → E) (he : Orthonormal 𝕜 e)
    (hN : ∀ F : Finset ι, ∑ i ∈ F, RCLike.re ⟪e i, T (e i)⟫_𝕜 ≤ N)
    (F : Finset ι) : (F.card : ℝ) ≤ N / c := by
  rw [le_div_iff₀ hc, mul_comm]
  exact (card_mul_le_sum T c hlow e he F).trans (hN F)

/-- Hence the orthonormal family (e.g. a Hilbert basis of H_D) is finite. -/
theorem finite_of_trace_bound {ι : Type*} (T : E →L[𝕜] E) {c N : ℝ} (hc : 0 < c)
    (hlow : ∀ x : E, c * ‖x‖ ^ 2 ≤ RCLike.re ⟪x, T x⟫_𝕜)
    (e : ι → E) (he : Orthonormal 𝕜 e)
    (hN : ∀ F : Finset ι, ∑ i ∈ F, RCLike.re ⟪e i, T (e i)⟫_𝕜 ≤ N) :
    Finite ι := by
  by_contra h
  rw [not_finite_iff_infinite] at h
  obtain ⟨F, hF⟩ := Infinite.exists_subset_card_eq ι (⌊N / c⌋₊ + 1)
  have hle := card_le_of_trace_bound T hc hlow e he hN F
  rw [hF] at hle
  push_cast at hle
  linarith [Nat.lt_floor_add_one (N / c)]
