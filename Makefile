test:
	poetry run pytest tests

build:
	poetry run poetry build

publish:
	poetry run poetry publish

check:
	poetry run mypy pyfabrik --ignore-missing-imports
	poetry run mypy tests --ignore-missing-imports
	poetry run black --check pyfabrik
	poetry run black --check tests

format:
	poetry run black pyfabrik
	poetry run black tests

fmt: format

clean:
	find . -name '__pycache__' -exec rm -rv {} \;
	find . -name '*.py[co]' -exec rm -rv {} \;
	rm -fr dist
	rm -fr pyfabrik.egg-info
