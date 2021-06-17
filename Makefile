.PHONY: venv

pip:
	pip install --upgrade pip

venv:
	python3.8 -m venv venv

requirements-dev: pip
	pip install -r requirements-dev.txt

build: requirements-dev
	python3.8 setup.py sdist

pypi: build check-readme
	twine upload dist/*

doc: requirements-dev
	cd docs; make clean

# From Scikit-learn
code-analysis:
	flake8 diarypy | grep -v external
	pylint -E diarypy/ -d E1103,E0611,E1101

clean:
	rm -rf ./dist

# All the following assume the requirmenets-dev are installed, but to make the
# output clean the dependency has been removed
test:
	pytest --cov-report=term-missing --cov=diarypy diarypy

check-readme:
	twine check dist/*
