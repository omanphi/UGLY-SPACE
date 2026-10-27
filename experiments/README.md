# Reproducing the illustration

**AI-generated academic satire.** The numbers here are formula evaluations
for a constructed sampling model, not measurements of humans or AI.

For each positive integer `n`, there are `n` invalid, aesthetically free
candidates and one valid candidate with aesthetic cost `n`. The unpenalized
policy `M` is uniform. Policy `H` reweights candidates by `exp(−λ A)` and
samples independently with replacement. Verification costs one unit;
candidate generation and scoring are assumed free. The candidate sets and
verifier are identical for both policies.

The single-draw success probabilities are `1/(n+1)` and
`1/(1+n exp(λn))`. Thus mean discovery time is the reciprocal of the
respective probability, and success within budget `B` is `1−(1−r)^B`.
The displayed budget is always `n+1`.

Run from the repository root with Python 3.10+:

```sh
python3 experiments/toy_model.py
python3 experiments/toy_model.py --n 2 6 12 --penalty 0.25
python3 experiments/toy_model.py --write
python3 experiments/toy_model.py --check
python3 -m unittest discover -s experiments -p 'test_*.py' -v
```

`--write` regenerates the canonical CSV and the table consumed by the paper,
using `n = 1, 4, 8, 16` and `λ = 0.5`. `--check` detects stale outputs.
These modes reject custom parameters so a local experiment cannot silently
change the paper's declared parameters. The CSV uses nine significant digits;
the paper rounds means and ratios to two decimal places and probabilities
to six decimal places. There is no random seed because there is no sampling
experiment.

The implementation uses log-domain arithmetic for the penalized mean and
`log1p`/`expm1` for small success probabilities. At extreme parameters,
floating-point means and ratios may overflow to infinity, or probabilities
may underflow to zero; these are numerical limits, not infinite discovery
time in the finite-penalty mathematical model. The returned `log_mean_h`
retains the logarithmic mean when `λn` is representable. Use the proofs for
asymptotic conclusions.

Checks independently normalize explicit candidate weights in small cases,
including the reversed construction with a pretty valid candidate. Further
checks exercise the budget bounds, the sensitivity identity on a nonuniform
instance with multiple valid candidates, all nonempty valid subsets of one
bounded-range instance, shift invariance, zero penalty, and probability
boundaries. These are numerical sanity checks, not formal verification.
