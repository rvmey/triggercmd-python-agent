# Updating

Bump the version in pyproject.toml
```
python3 -m build
python3 -m twine upload --repository pypi dist/*
```