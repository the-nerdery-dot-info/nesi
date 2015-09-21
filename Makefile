EXECUTABLE_NAME := nesi

init:
	@echo "Installing development dependencies"
	pip install flake8
	pip install pylint
	pip install nose

test:
	@echo "Executing all tests"
	nosetests

lint:
	@echo "Checking code for PEP8 compliance and common code smells"
	flake8 $(EXECUTABLE_NAME)
	flake8 **/*.py
	@echo "Checking code more aggressively for code smells"
	pylint -E $(EXECUTABLE_NAME)
	pylint -E **/*.py

deploy-test:
	@echo "Uploading package to PyPi Test Server"
	python setup.py register -r pypitest

deploy:
	@echo "Uploading package to PyPi"
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi

install:
	@echo "Installing development build"
	pip install -e .

.PHONY: init test lint deploy-test deploy install
