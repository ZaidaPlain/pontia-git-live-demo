# Project Jupiter

Example data analysis project.

## Description

The project takes a small sales dataset, cleans it and shows a summary of the results.
It is deliberately simple: the goal is not the analysis itself, but to provide a base for practising
the Git workflow (commits, branches, merges, conflicts, `.gitignore`, etc.).

## Requirements

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/) 3.11 or higher
- [uv](https://docs.astral.sh/uv/) (Python environment and dependency manager)

## Installation

```bash
git clone https://github.com/ZaidaPlain/test-pontia-repository-example.git
cd test-pontia-repository-example
uv sync
```

`uv sync` creates the virtual environment (`.venv`) and installs the dependencies listed in `pyproject.toml`.

## Usage

Clean the data (writes the output files to `data/processed/`):

```bash
uv run python src/cleaning.py
```

Open the exploration notebook:

```bash
uv run jupyter lab notebooks/
```

## Project structure

```
.
├── data/
│   ├── raw/            # Original data
│   └── processed/      # Cleaned data (generated automatically)
├── notebooks/          # Exploration notebooks
├── src/                # Source code
├── .gitignore          # Files Git should not track
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Exact dependency versions
└── README.md
```

## Contributing

1. Create a branch for your change: `git switch -c my-change`
2. Make your changes and commit them: `git add .` and `git commit -m "Describe the change"`
3. Push the branch: `git push -u origin my-change`
4. Open a *pull request* on GitHub for review.

## License

For educational purposes only.
