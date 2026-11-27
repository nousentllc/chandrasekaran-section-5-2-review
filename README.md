# Chandrasekaran §5.2 independent review

This repository contains an equation-by-equation review of the causal-diamond finite-dimensionality argument in [Chandrasekaran, *An algebraic quantization of gravity from the null cone*, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1). The review derives the trace implication, checks the boost and spectral inequalities, and gives an infinite-dimensional operator model that isolates the cut-to-uncut identification.

Start with [the technical review](REVIEW.md). If the preparation operator in (5.30c) has a uniform positive lower bound and the identity gluing in (5.38) gives a finite ordinary trace, finite dimension follows directly. The review identifies the independent justification required for that gluing, and the approximation control required to transfer the linearized graviton calculation to the strict sign in (5.37b).

| Material | What to check |
| --- | --- |
| [Review](REVIEW.md) | Equation references, derivations, the separation model, and scope of the conclusions |
| [TraceDim.lean](TraceDim.lean) | The three conditional proofs in the supplied source, preserved byte for byte |
| [TraceDimCheck.lean](TraceDimCheck.lean) | Axiom dependencies for those three declarations |
| [Numerical checks](checks/) | 500 finite-matrix checks and sample finite sections of the analytic model |
| [Verification record](evidence/) | Original run outputs, input hashes, and provenance |

## Reproduce the Lean checks

Run from the repository root with [Elan](https://github.com/leanprover/elan) installed. Lake uses the committed Lean 4.35.0 toolchain and Mathlib lockfile. The first run may download dependencies and the Mathlib build cache.

```sh
lake exe cache get
lake build
lake env lean TraceDimCheck.lean
```

The audit should list only `propext`, `Classical.choice`, and `Quot.sound` for each declaration. The historical “NOT YET COMPILED” comment remains in the byte-preserved source. The [verification log](evidence/lean-verification.log) records the successful later check. The proofs assume the finite partial-sum bound `hN`. Establishing that bound from the gravitational construction is the open question.

## Reproduce the numerical checks

Use Python 3.13 with the recorded package versions. The checks write to a local, ignored `outputs/` directory, leaving the archived evidence available for comparison.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python checks/operator_checks.py
python checks/countermodel.py
diff -u evidence/operator_checks.json outputs/operator_checks.json
diff -u evidence/countermodel_checks.json outputs/countermodel_checks.json
```

The seeded matrix diagnostics enforce the inequalities with floating-point tolerances. Expect slight platform differences in the reported floating-point extrema. The paper's infinite-dimensional arguments and the countermodel's exact derivation are in the review.

The review was conducted by OpenAI Codex at Justin Candler's request, building on the earlier audit prepared by Justin with Claude. The source manuscript is linked by version. The archive records the reviewed inputs by hash and includes the formalization required to reproduce the Lean check.
