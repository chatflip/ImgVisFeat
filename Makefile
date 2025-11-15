.PHONY: help install format lint test servedocs cleandocs

.DEFAULT_GOAL := help

help:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  install - Install all dependencies (all groups)"
	@echo "  format - Run formatting checks and fixes"
	@echo "  lint - Run linting checks"
	@echo "  test - Run tests"
	@echo "  servedocs - Serve documentation with live reload"
	@echo "  cleandocs - Clean documentation build artifacts"

install:
	uv sync --all-groups

format:
	uv run ruff check --fix
	uv run ruff format

lint:
	uv run ruff check
	uv run ty check

test:
	uv run pytest

servedocs:
	uv run mkdocs serve

cleandocs:
	rm -rf site/

