# Prepublication audit status

Current status: `PASS_3_NO_SUBSTANTIVE_ISSUE_FOUND` for the proof core, with computational evidence integrated afterward.

## Proof audit

- Lemma 1 no-false-extinction implication corrected to refer to the first transition into the absorbing empty state.
- Lemma 3 uses the same first-transition formulation.
- Theorem 6 uses a truncation-based verification proof: finite Bellman values, integrable stopped supermartingale, optional stopping at `T wedge m`, then monotone convergence.
- Lemma 7 stopped coupling explicitly precedes the Case-B lower bound.
- Lemma 8 uses the safe explicit threshold `n >= 14`.
- Theorem 9 is scoped only to homogeneous fixed-bias BRF.

## Computational audit

`audit/bellman_experiments.py` reports:

- `PASS_BELLMAN_EXPERIMENTS`
- exact-rational Bellman evaluation for fair/dyadic/certificate biases on n=2..20;
- exact match to the predecessor fair-coin reference for n=2..8;
- 90-digit numerical Bellman evaluation for the finite bias search.

The numerical bias search is supporting evidence, not a theorem.

## Build / layout audit

- pdflatex twice: PASS
- theorem numbering preserved: Lemma 1, Lemma 2, Lemma 3, Theorem 4, Lemma 5, Theorem 6, Lemma 7, Lemma 8, Theorem 9, Remark 10
- no LaTeX warnings, overfull boxes, or underfull boxes after final compile
- proof core comparison: all 9 audited Lemma/Theorem proof blocks match the Pass 3 source byte-for-byte
- PDF rendered page-by-page and tables/figures visually inspected
- PDF preflight: openable, unencrypted, text-based

## Claim boundary

Do not claim:

- one persistent bit is the randomized minimum;
- `2^{Theta(n log n)}` is optimal over all two-state randomized broadcast protocols;
- the dyadic or certificate-optimal bias exactly minimizes actual expected runtime;
- a tight oblivious-adversary runtime bound.
