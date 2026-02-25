# Finite
Generates a random password. The password is unique can can never be generated again. 

## Setup

```
git clone https://github.com/richardayikwei/finite
cd finite
uv sync --dev
```

## Running the server

```
uv run uvicorn app.main:app --reload
```

## Testing

```
uv run pytest
```

## Commit Messages and Bumping versions numbers

Committing changes

```
git add .
uv run cz commit
```

Bumping version numbers

```
uv run cz bump
```

## Linting & Formatting

```
uv run ruff check .
```
or

```
uv run ruff check . --fix
```

## Documentation

```
uv run pyment -e -o numpydoc app/
```