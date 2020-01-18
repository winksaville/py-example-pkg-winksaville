#!/usr/bin/env python3
from __future__ import annotations # Required for typing annotations

import example_pkg.hello as hello

import sys
import unittest
from io import StringIO
from unittest.mock import patch

class TestHello(unittest.TestCase):
    def test_hello1(self: TestHello) -> None:
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            hello('wink')
        self.assertEqual(capturedOutput.getvalue().strip(), '<p>wink</p>')

    def test_hello2(self: TestHello) -> None:
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            hello('wink saville')
        self.assertEqual(capturedOutput.getvalue().strip(), '<p>wink saville</p>')

# Works from command line or REPL
def tsts(verbosity=1):
    print(f'test_hello.py.tsts(verbosity={verbosity})')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHello)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

# Works for command line but not via REPL where it prints  'run 0 tests in 0.000secs'
def tests(verbosity=1):
    print(f'test_hello.py.tests(verbosity={verbosity})')
    unittest.main(verbosity=verbosity)

if __name__ == '__main__':
    print('test_hello.py.__main__')
    tsts()
    #tests()
