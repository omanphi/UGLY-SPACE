# UGLY-SPACE

### On the Systematic Underexploration of Mathematically Unattractive Solution Spaces

> **AI-GENERATED ACADEMIC SATIRE.** This is an AI-generated work of academic
> satire, produced at the direction of a human. It is not intended to
> misrepresent fictional claims as established mathematical results.
> It is not peer reviewed. No human authors or institutional affiliations
> have been invented.

## Abstract

We introduce and formalize **UGLY-SPACE**, the class of mathematical problems
that only admit solutions that are aesthetically unacceptable. An aesthetic
validator rejects otherwise correct solutions whose ugliness exceeds a
prescribed threshold. We conjecture that many longstanding open problems belong
to UGLY-SPACE, explaining their historical resistance to human solutions. We
interpret recent AI-generated results on $k$-SAT and integer multiplication as
incursions into this space ([1][eth], [2][multiplication]), driven by search
unconstrained by human aesthetic preferences. We discuss implications for
mathematical discovery and the future employment of mathematicians.

## Illustrative bounds

**Exact counting for $k$-SAT.** [OpenAI, Theorem 1.1][eth] reports a deterministic
algorithm counting satisfying assignments of a $k$-CNF with $n$ variables and
$m$ clauses, for fixed $k\geq2$, in polynomial space and time

$$
(n+m)^{O_k(1)}\,2^{O_k\!\left(n\log\log n/\sqrt{\log n}\right)}.
$$

**Integer multiplication.** [OpenAI, Theorem 1][multiplication] reports exact
deterministic multiplication of two $n$-bit integers on a fixed finite-tape
Turing machine in time

$$
O\!\left(n(\lg n)^{1-\kappa}\right),\qquad \kappa=2^{-182}.
$$

Ignoring hidden constants, the formal saving factor reaches two only when
$\log_2\log_2 n=2^{182}$. An asymptotic improvement has been obtained;
arranging a demonstration is left to experimental colleagues.

[eth]: https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf
[multiplication]: https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf

## Mathematical model

For independent sampling with replacement, a verifier, and candidate weights
proportional to `q₀(c) exp(−λ A(c))`:

- A sensitivity identity shows exactly when penalizing ugliness increases
  expected discovery time. It can also decrease it.
- In a deliberately adversarial family with `n` pretty invalid candidates
  and one valid candidate of ugliness `n`, the mean discovery times are
  `1 + n exp(λn)` versus `n + 1`. For fixed `λ > 0`, their ratio is
  exponential in `n`.
- A bounded aesthetic range `Δ` caps the slowdown at `exp(λΔ)`, exposing
  the assumption responsible for the separation.

The **Fundamental Theorem of Mathematical Ugliness** establishes the
separation between the specified sampling policies. The discussion develops
the Aesthetic Regularization Hypothesis, the Grothendieck–GPU Tradeoff, and
the Optimist's and Pessimist's Conjectures, then considers the future
employment of mathematicians.

## Read and build

The source is [paper/main.tex](paper/main.tex). Install Python 3.10+, GNU Make,
and [Tectonic 0.17.0](https://github.com/tectonic-typesetting/tectonic/releases/tag/tectonic%400.17.0)
on your `PATH`. Tectonic downloads its TeX support files on the first build,
so that build requires network access. No Python dependencies are needed.

```sh
make check       # Independent enumeration checks and generated-table freshness
make paper       # Regenerate the example table and compile build/main.pdf
make all         # Both checks and PDF build
```

For an explicitly located compiler:

```sh
make all TECTONIC=/path/to/tectonic
```

With an existing TeX Live installation, `make paper-latexmk` instead uses
`latexmk`, `pdflatex`, and BibTeX. On Debian/Ubuntu the packages are `latexmk`,
`texlive-latex-recommended`, `texlive-fonts-recommended`, and `lmodern`.
`make clean` removes only the generated `build/` directory.

The [GitHub Actions workflow](.github/workflows/paper.yml) checks the numerical
example, builds the PDF and bibliography, rejects unresolved citations and
references, and uploads an artifact named `ugly-space-paper`. It does not
create releases or deploy anything. After a workflow run, download the PDF
from that run's **Artifacts** section.

## Reproduce the toy model

```sh
python3 experiments/toy_model.py
python3 experiments/toy_model.py --n 1 4 8 16 --penalty 0.5
make tables      # Refresh the tracked CSV and LaTeX table
```

The script evaluates exact-distribution formulas numerically; it does not
simulate a real research community or report measured AI performance.
[experiments/results.csv](experiments/results.csv) and
[paper/generated/toy-table.tex](paper/generated/toy-table.tex) are deterministic
outputs for `n = 1, 4, 8, 16` and `λ = 0.5`. The displayed budget is `B = n + 1`.
The paper's proofs, rather than floating-point calculations, establish the
asymptotic claims. See [experiments/README.md](experiments/README.md) for the
model and verification details.

## Repository contents

| Path | Purpose |
| --- | --- |
| `paper/main.tex` | Paper, disclosure, definitions, proofs, conjectures, limitations |
| `paper/references.bib` | Real background references with DOI links |
| `paper/generated/toy-table.tex` | Reproducible numerical illustration |
| `experiments/toy_model.py` | Dependency-free numerical reproduction |
| `experiments/test_toy_model.py` | Enumeration, boundary, and counterexample checks |
| `scripts/check_build.py` | PDF and LaTeX diagnostic checks |
| `.github/workflows/paper.yml` | Checks and PDF artifact build |
| `CONTRIBUTING.md` | Standards for extending the satire honestly |

## Provenance and references

The concept and requested scope come from the human-supplied
[shared conversation, “Formalizing UGLY SPACE”](https://chatgpt.com/share/6ae08455-8f40-83eb-aded-16982d6dec5b).
The manuscript, proofs, code, and repository text were generated by OpenAI
Codex at the user's direction. This disclosure is not a claim of human
review, formal proof-assistant verification, or endorsement by any cited author.

The bibliography cites the connection
between statistical mechanics and optimization in
[Kirkpatrick, Gelatt, and Vecchi (1983)](https://doi.org/10.1126/science.220.4598.671),
and a substantial formally verified proof in
[Hales et al. (2017)](https://doi.org/10.1017/fmp.2017.1), together with
[OpenAI's October mathematics release](https://openai.com/index/sharing-ai-progress-in-mathematics/)
and the two preprints discussed above. The aesthetic interpretation belongs
to this paper; no UGLY-SPACE conjecture is attributed to the cited authors.

The repository's original material is offered under the [MIT License](LICENSE),
to the extent applicable rights exist. Referenced publications retain their
own rights. Please preserve the AI-generation and satire disclosures in
redistributions.
