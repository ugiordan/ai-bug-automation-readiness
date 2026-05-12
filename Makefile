.PHONY: setup test lint format coverage

setup:
	pip install -r requirements.txt -r requirements-dev.txt

test:
	python -m pytest tests/ -v

lint:
	ruff check .
	mypy assess/

format:
	ruff format .
	ruff check --fix .

coverage:
	python -m pytest --cov=assess --cov-report=term-missing tests/
