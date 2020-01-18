# Example Package

Created from [this tutorial](https://packaging.python.org/tutorials/packaging-projects/)
and [this](https://python-packaging.readthedocs.io/en/latest/minimal.html)

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Install

Install using `pip` in normal mode `pip install .` or in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) with `pip install -e .`:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ pip install .
```

## Hello method

Is the main interface provided by this package, it takes a sring
as a parameter and prints it.

Example, from the project root (i.e. from the directory where setup.py is located) you can do:
```
$ python3 -c "import example_pkg as ep; ep.hello('**hi**')"
<p><strong>hi</strong></p>
```
Or from the repl if it's installed:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ pip install .
...

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

Install then `hello` is an executable which prints 'hi there' or the
concatenation of the arguments:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ hello
<p>hi there</p>
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ hello yo dude
<p>yo dude</p>
```
### Test

#### Unit tests

Use discover:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ python -m unittest discover
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```

Execute test_hello.py
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ python example_pkg/tests/test_hello.py 
test_hello.py.__main__
test_hello.py.tsts(verbosity=1)
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```

Using REPL:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ python
Python 3.8.1 | packaged by conda-forge | (default, Jan  5 2020, 20:58:18) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import example_pkg.tests as t
>>> t.tsts()
test_hello.py.tsts(verbosity=1)
..
----------------------------------------------------------------------
Ran 2 tests in 0.009s

OK
>>>
```
