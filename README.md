# Size Knowledge Accelerates One-Bit Las Vegas Broadcast in Anonymous Dynamic Networks

Author: Ryutaro Yonezu (Independent Researcher)

Status: preprint / not peer reviewed. Paper DOI: `10.5281/zenodo.22662155`.

## Main results

For Bernoulli Reactivation Flooding (BRF) in anonymous, synchronous, port-indistinguishable, 1-interval-connected dynamic networks with idle start and stabilizing termination:

- known-size dyadic BRF uses exactly two persistent protocol states and has causal state-adaptive worst-case expected stabilization time `2^{Theta(n log n)}`;
- for every fixed survival probability `p in (0,1)`, one-frontier exposure is Bellman-optimal for homogeneous BRF;
- over homogeneous fixed-bias BRF, the minimax worst-case expected time is `2^{Theta(n log n)}`.

These are family-specific results. The paper does not prove a lower bound for all two-state randomized broadcast protocols and does not claim that one bit is the randomized minimum.

## Computational evidence

Run:

```bash
python audit/bellman_experiments.py
python audit/make_figures.py
```

The Bellman audit uses exact rational Gaussian elimination for fair, dyadic, and certificate-optimal rational biases on `n=2..20`, plus 90-digit numerical Bellman solves for a one-dimensional bias search. It reproduces the predecessor fair-coin values exactly for `n=2..8`.

Files:

- `paper.tex` - full manuscript source
- `Yonezu_2026_Size_Knowledge_Accelerates_One_Bit_Las_Vegas_Broadcast.pdf` - compiled manuscript
- `audit/bellman_experiments.py` - exact/high-precision computational audit
- `audit/bellman_experiments_output.txt` - frozen audit status
- `audit/make_figures.py` - figure regeneration
- `data/fair_exact_regression.csv` - fair-coin exact regression
- `data/bias_comparison_n2_n20.csv` - finite bias comparison
- `data/bias_landscape_n10.csv` - sampled n=10 landscape
- `figures/` - manuscript figures in PDF and PNG
- `PRIOR_ART_AUDIT.md` - scoped Pass 2 literature boundary
- `PREPUBLICATION_AUDIT.md` - current proof/claim/build status

## Reproduction

```bash
python -m pip install -r requirements.txt
python audit/bellman_experiments.py
python audit/make_figures.py
pdflatex paper.tex
pdflatex paper.tex
```

## Release metadata

- Version: `v1.0.0`
- Publication date: 2026-09-08
- Repository: `yonezaemon1-hub/size-knowledge-accelerates-one-bit-las-vegas-broadcast`
- Paper license: CC BY 4.0
- Code/audit license: MIT
- PDF SHA-256: `0de5feb165268be83c33562b3e2b295584a77feeccf51cb5cd3577919f9089ac`
- Software DOI: `10.5281/zenodo.22661995`
- Paper DOI: `10.5281/zenodo.22662155`
