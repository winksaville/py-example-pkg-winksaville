# import example_pkg.YoDude as YoDude
from contextlib import redirect_stdout
from io import StringIO

from example_pkg import YoDude


def test_hello1() -> None:
    yd = YoDude("Hello, ")
    with redirect_stdout(StringIO()) as capturedOutput:
        yd.hello("Winkster")
    assert capturedOutput.getvalue().strip() == "<p>Hello, Winkster</p>"


def test_hello2() -> None:
    yd = YoDude()
    with redirect_stdout(StringIO()) as capturedOutput:
        yd.hello("  *Wink Saville*  ")
    assert capturedOutput.getvalue().strip() == "<p>YoDude <em>Wink Saville</em></p>"
