.PHONY: start req

UNIT_TEST=pytest tests

start:
	echo "start"

req:
	pip freeze > requirements.txt