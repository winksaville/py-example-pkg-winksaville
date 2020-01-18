# Example Package

Created from [this tutorial](https://packaging.python.org/tutorials/packaging-projects/)
and [this](https://python-packaging.readthedocs.io/en/latest/minimal.html)

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Hello method

Added hello method in example_pkg/hello.py which uses the python
markdown package to output html.

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


#### Direct

From the project root (i.e. from the directory where setup.py is located) you can do:
```
$ python3 -c "import example_pkg as ep; ep.hello('**hi**')"
<p><strong>hi</strong></p>
```
Or install using `pip` in normal mode `pip install .` or in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) with `pip install -e .` and then using the python REPL:
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
