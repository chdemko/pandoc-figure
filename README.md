Installation
============

[![Python package](https://img.shields.io/github/actions/workflow/status/chdemko/pandoc-figure/python-package.yml?logo=github&branch=develop)](https://github.com/chdemko/pandoc-figure/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-figure/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-figure?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-figure.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-figure/)
[![Code Climate](https://img.shields.io/codeclimate/maintainability/chdemko/pandoc-figure?logo=codeclimate&barnch=develop)](https://codeclimate.com/github/chdemko/pandoc-figure/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-figure/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-figure/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-figure/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-figure)
[![Codacy](https://img.shields.io/codacy/grade/36051716c52147bca7a7f4c1ca6bc998.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-figure/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-figure.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-figure/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-figure.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-figure/)
[![License](https://img.shields.io/pypi/l/pandoc-figure.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-figure/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-figure?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-figure)
[![Development Status](https://img.shields.io/pypi/status/pandoc-figure.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-figure/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-figure.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-figure/)
[![Pandoc version](https://img.shields.io/badge/pandoc-3.0%20..%203.6-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-figure.svg?logo=github)](https://github.com/chdemko/pandoc-figure/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-figure/develop?logo=github)](https://github.com/chdemko/pandoc-figure/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-figure.svg?logo=github)](http://pandoc-figure.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-figure.svg?logo=github)](http://pandoc-figure.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-figure.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-figure)
[![Docs](https://img.shields.io/readthedocs/pandoc-figure.svg?logo=read-the-docs&logoColor=white)](http://pandoc-figure.readthedocs.io/en/latest/)

*pandoc-figure* is a [pandoc] filter for adding complex figures.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-figure* requires [python], a programming language that comes
pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-figure* using the bash command

~~~shell-session
$ pipx install pandoc-figure
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-figure
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI]. It can be installed
using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org/
[on Windows]: https://www.python.org/downloads/windows/
[PyPI]: https://pypi.python.org/pypi


Getting Help
------------

If you have any difficulties with *pandoc-figure*, please feel welcome to
[file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-figure/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

