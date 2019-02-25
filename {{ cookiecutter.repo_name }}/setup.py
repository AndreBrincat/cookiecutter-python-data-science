from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.python_module_name }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}'
)
