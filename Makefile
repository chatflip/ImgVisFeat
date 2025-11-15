.PHONY: help format lint test builddocs cleandocs

.DEFAULT_GOAL := help

help:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  format - Run formatting checks and fixes"
	@echo "  lint - Run linting checks"
	@echo "  test - Run tests"
	@echo "  builddocs - Build the documentation"
	@echo "  cleandocs - Clean the documentation build artifacts"

format:
	uv run ruff check --fix
	uv run ruff format

lint:
	uv run ruff check
	uv run ty check

test:
	uv run pytest

builddocs:
	uv run sphinx-build docs _build

cleandocs:
	rm -rf _build
