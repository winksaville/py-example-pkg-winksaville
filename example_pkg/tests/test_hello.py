#!/usr/bin/env python3
from __future__ import annotations # Required for typing annotations

import example_pkg.hello as hello

from io import StringIO
from contextlib import redirect_stdout

#def test_hello1(self: TestHello) -> None:
def test_hello1() -> None:
    with redirect_stdout(StringIO()) as capturedOutput:
        hello('wink')
    assert capturedOutput.getvalue().strip() == '<p>wink</p>'

def test_hello2() -> None:
    with redirect_stdout(StringIO()) as capturedOutput:
        hello('*wink saville*')
    assert capturedOutput.getvalue().strip() == '<p><em>wink saville</em></p>'
