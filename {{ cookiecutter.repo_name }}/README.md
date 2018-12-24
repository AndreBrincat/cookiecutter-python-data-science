# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installing the environment

You need to have `conda` installed (from
[Miniconda](https://conda.io/miniconda.html) or
[Anaconda](https://www.anaconda.com/download)).

Create the environment:

```bash
$ conda env create -f environment.yml
```

After packages are installed, you can activate the environment, and install
the "local" package corresponding to the Python module in `src/`

```bash
$ source activate {{cookiecutter.conda_environment}}
$ pip install -e .
```

---

Project based on the [cookiecutter-data-science](https://drivendata.github.io/cookiecutter-data-science/) template.
