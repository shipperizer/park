.PHONY: test run install

PIP?=pip
FLAKE8?=flake8
PYTEST?=py.test
PYTHON?=python

test: lint
	$(PYTEST) --cov park --cov-config .coveragerc test_re.py

run:
	$(PYTHON) park.py

lint:
	$(FLAKE8) --config=.flake8rc park.py

install:
	$(PIP) install -r requirements.txt
