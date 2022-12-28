# Python HY_Features

**Description**:  This python package provides base abstract classes for [HY_Features](https://docs.opengeospatial.org/is/14-111r6/14-111r6.html).

Other things to include:

  - **Technology stack**: Indicate the technological nature of the software, including primary programming language(s) and whether the software is intended as standalone or as a module in a framework or other ecosystem.
  - **Status**:  Initial development consider pre-alpha. For more details on implementation, see the [CHANGELOG](CHANGELOG.md).
  - **Related Work**
  - This project is based loosely on the work done on the [ngen modeling framework](https://github.com/noaa-owp/ngen) and [hygeo](https://github.com/dblodgett-usgs/hygeo), bringing similar data structures and abstractions to a python library to support various workflows.


## Dependencies
Unit testing done with [pytest](https://github.com/pytest-dev/pytest).  See [requirements.txt](requirements.txt) for other specific python dependencies.

## Installation
Package can be installed from source using pip:
`pip install -e "git+https://github.com/noaa-owp/hypy@master#egg=hypy&subdirectory=python"`

`TODO` see [INSTALL](INSTALL.md).

## Usage

`TODO`

## How to test the software

Install `pytest` and other python dependencies (`pip install -r python/requirements.txt`)
Or create a virtual environment:
```
mkdir venv
virtualenv ./venv
source ./venv/bin/activate
pip install -r python/requirements.txt
```
Then use `pytest` to run the tests:

`pytest --log-cli-level 0 python/hypy/test/`

Also, the following check commands can be run locally to perform code analysis.  PRs have these or similar checks run automatically (see the Github Actions [config file](.github/workflows/python-package.yml)).

```
flake8 ./python --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 ./python --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## Known issues

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

See [CONTRIBUTING](CONTRIBUTING.md), or open an issue to start a conversation!


----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)


----
