# Pytest CI Pipeline

This repository demonstrates **continuous integration** for a Python project.  
It includes:
- A simple math utility library (`math_utils.py`)
- Unit tests with Pytest (parametrized + exception tests)
- Coverage reports
- Linting (flake8)
- GitHub Actions CI pipeline

## Running Tests Locally
```bash
pip install -r requirements-dev.txt
pytest --cov=.
