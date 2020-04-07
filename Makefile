.PHONY: black
black:
	black betfund_logger
	black tests

.PHONY: tests
tests:
	pytest --cov=betfund_logger --cov-report term-missing .

.PHONY: lint
lint:
	pylint betfund_logger