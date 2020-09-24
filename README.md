# Example Package

Created from [this tutorial](https://packaging.python.org/tutorials/packaging-projects/)
and [this](https://python-packaging.readthedocs.io/en/latest/minimal.html)

This is uploaded to test.pypi.org as [example-pkg-winksaville](https://test.pypi.org/project/example-pkg-winksaville/)
as it is only an example package and not useful.

## Build and upload

Only uploaded to `pypi_repo=--repository-url https://test.pypi.org/legacy/`
```
make build
make upload
```

## Tests

Run `make test` or `pytest`
```
(py-38) wink@3900x:~/prgs/python/projects/example-pkg-winksaville (master)
$ make test
pytest tests
============================ test session starts =============================
platform linux -- Python 3.8.5, pytest-6.0.2, py-1.9.0, pluggy-0.13.1
rootdir: /home/wink/prgs/python/projects/example-pkg-winksaville
collected 2 items                                                            

tests/test_hello.py ..                                                 [100%]

============================= 2 passed in 0.02s ==============================
(py-38) wink@3900x:~/prgs/python/projects/example-pkg-winksaville (master)
$ pytest
============================ test session starts =============================
platform linux -- Python 3.8.5, pytest-6.0.2, py-1.9.0, pluggy-0.13.1
rootdir: /home/wink/prgs/python/projects/example-pkg-winksaville
collected 2 items                                                            

tests/test_hello.py ..                                                 [100%]

============================= 2 passed in 0.02s ==============================
```

## Install

Install using `pip` in normal mode `pip install .` or in
[editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)
with `pip install -e .`:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ pip install .
```

## Hello method

`hello(s: str) -> None` method is the main interface provided by
this package.

Example, from the project root (i.e. from the directory where
setup.py is located) you can do:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ python3 -c "import example_pkg as ep; ep.hello('**hi**')"
<p><strong>hi</strong></p>
```
Or from the repl
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ python3
Python 3.8.1 | packaged by conda-forge | (default, Jan  5 2020, 20:58:18) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import example_pkg
>>> example_pkg.hello('*yo dude*')
<p><em>yo dude</em></p>
>>> 
```
## Command line operation

[Install](#install) and then `hello` is a command which prints 'hi there' or the
concatenation of the arguments:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ hello
<p>hi there</p>
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ hello '**yo dude**'
<p><strong>yo dude</strong></p>
```

This works by adding [entry_points](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point)
to setuptools.setup and then the command_line.py file in the package.