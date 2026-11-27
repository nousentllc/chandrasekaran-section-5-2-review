import TraceDim

open scoped InnerProductSpace

/-- The bound on positive partial sums for a complete Hilbert basis controls
the ambient dimension. The gluing bound is an explicit hypothesis. -/
theorem dimension_of_basis_trace_bound
    {𝕜 E ι : Type*} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
    (T : E →L[𝕜] E) {c N : ℝ} (hc : 0 < c)
    (hlow : ∀ x : E, c * ‖x‖ ^ 2 ≤ RCLike.re ⟪x, T x⟫_𝕜)
    (b : HilbertBasis ι 𝕜 E)
    (hN : ∀ F : Finset ι, ∑ i ∈ F, RCLike.re ⟪b i, T (b i)⟫_𝕜 ≤ N) :
    FiniteDimensional 𝕜 E ∧ (Module.finrank 𝕜 E : ℝ) ≤ N / c := by
  classical
  let : Finite ι := finite_of_trace_bound T hc hlow b b.orthonormal hN
  let := Fintype.ofFinite ι
  let basis := b.toOrthonormalBasis.toBasis
  refine ⟨basis.finiteDimensional_of_finite, ?_⟩
  rw [Module.finrank_eq_card_basis basis]
  simpa using card_le_of_trace_bound T hc hlow b b.orthonormal hN Finset.univ

#print axioms dimension_of_basis_trace_bound
