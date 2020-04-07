.PHONY: black
black:
	python -m black betfund_logger
	python -m black tests

.PHONY: tests
tests:
	python -m pytest --cov=betfund_logger --cov-report term-missing .

.PHONY: lint
lint:
	python -m pylint betfund_logger