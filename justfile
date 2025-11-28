# List available recipes.
help:
    @just --list --unsorted

# Run unit tests without coverage and API request tests.
test:
    uv run pytest -m 'not api_request' --spec

# Run unit tests without API request tests.
test-cov:
    uv run pytest -m 'not api_request' --spec --cov

# Run all unit tests and coverage.
[confirm('NOTE: The full test suite can take a very long time. Are you sure? [y|N]')]
test-all:
    uv run pytest --spec --cov

# Run linting and formating checks.
lint:
    uv run deptry .
    uv run ruff format --check .
    uv run ruff check .

# Run static typing analysis.
type:
    uv run mypy --install-types --non-interactive

# Run security and safety checks.
safety:
    uvx vulture  --exclude .venv --min-confidence 100 .
    uvx radon mi --show --multi --min B .
    uvx complexipy --quiet .

# Run all checks.
check: lint safety type

# Run checks and tests.
ready: lint safety type test

# Reformat the code using isort and ruff.
[confirm]
reformat:
    uv run ruff format .
    uv run ruff check --select I --fix .

# Extract current production requirements. Save to a file by appending `> requirements.txt`.
reqs:
    uv export --no-dev

# Run the development server.
serve:
    uv run reflex run --loglevel debug --env dev
