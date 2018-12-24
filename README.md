# Cookiecutter Python Data Science

A more simplified, minimal project structure for data science in Python, based
on [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/).

- Uses `conda` environments instead of `virtualenv` environments.
- Python 3 support only

## Requirements

- `conda` (from [Miniconda](https://conda.io/miniconda.html) or
  [Anaconda](https://www.anaconda.com/download))
- [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html)
  package

## Starting a new project

```bash
$ cookiecutter gh:mganjoo/cookiecutter-python-data-science
```

Customize the Conda `environment.yml` file, and install environment
and local packages using instructions in project `README.md`.
