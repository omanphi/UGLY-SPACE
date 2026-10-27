PYTHON ?= python3
TECTONIC ?= tectonic

.PHONY: all check tables paper paper-latexmk clean

all: check paper

check:
	$(PYTHON) -m unittest discover -s experiments -p 'test_*.py' -v
	$(PYTHON) experiments/toy_model.py --check

tables:
	$(PYTHON) experiments/toy_model.py --write

paper: tables
	mkdir -p build
	$(TECTONIC) --keep-logs --keep-intermediates --outdir build paper/main.tex
	$(PYTHON) scripts/check_build.py build/main.pdf build/main.log build/main.blg

paper-latexmk: tables
	mkdir -p build
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build main.tex
	$(PYTHON) scripts/check_build.py build/main.pdf build/main.log build/main.blg

clean:
	rm -rf build
