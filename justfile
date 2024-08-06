# TODO setup venv
# TODO setup devel (add mypy, test etc, run mypy install)
val:
	mypy forecastbox --ignore-missing-imports
	mypy tests --ignore-missing-imports
	pytest tests

# TODO build
