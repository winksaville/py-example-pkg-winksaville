# Example Package

Created from [this tutorial](https://packaging.python.org/tutorials/packaging-projects/)

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Hello method

Added hello method to __init__.py

### Test

From the project root (i.e. from the directory where setup.py is located) you can do:
```
$ python3 -c "import example_pkg as ep; ep.hello('hi')"
hi
```
Or install using `pip` in normal mode `pip install .` or in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) with `pip install -e .` and then using the python REPL:
```
(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ pip install -e .
Obtaining file:///home/wink/prgs/python/packaging_tutorial
Installing collected packages: example-pkg-winksaville
  Found existing installation: example-pkg-winksaville 0.0.2
    Uninstalling example-pkg-winksaville-0.0.2:
      Successfully uninstalled example-pkg-winksaville-0.0.2
  Running setup.py develop for example-pkg-winksaville
Successfully installed example-pkg-winksaville

(testpypi) wink@wink-desktop:~/prgs/python/packaging_tutorial (master)
$ python3
Python 3.8.1 | packaged by conda-forge | (default, Jan  5 2020, 20:58:18) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import example_pkg
>>> example_pkg.hello('yo dude')
yo dude
>>> 
```
