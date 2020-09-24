# Simple Makefile for this package
#
# My test.pypi.org API token is stored in 1Password in TestPyPi-token
# When making 'upload' set username to __token__ and then get and
# paste the token from 1Password.

# Use a blank pypi_repo to upload to the "non-test" repository

pypi_repo=--repository-url https://test.pypi.org/legacy/
#pypi_repo=

SRCS= \
 Makefile \
 README.md \
 LICENSE \
 setup.py \
 example_pkg/__init__.py \
 example_pkg/command_line.py \
 example_pkg/hello.py \
 tests/__init__.py \
 tests/test_hello.py

.PHONY: build upload clean

build: build/completed_ts

build/completed_ts: ${SRCS}
	python3 setup.py sdist bdist_wheel
	touch build/completed_ts

upload: build/completed_ts
	python3 -m twine upload ${pypi_repo} dist/*

test:
	pytest tests

clean:
	rm -rf build dist example_pkg_winksaville.egg-info __pycache__
	rm -rf .mypy_cache .pytest_cache
