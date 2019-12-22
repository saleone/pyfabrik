test:
	poetry run pytest tests
build:
	poetry build
clean:
	find . -name '__pycache__' -delete
	find . -name '*.py[co]' -delete
	rm -fr dist
