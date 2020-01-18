import example_pkg.hello as hello
import sys

def main():
    s: str = 'hi there'
    if len(sys.argv) > 1:
        s = ' '.join(sys.argv[1:])
    hello(s)
