from example_pkg import YoDude

import sys

def main():
    print(f"command_line sys.argv={sys.argv}")
    s: str = 'hi there'
    if len(sys.argv) > 1:
        s = ' '.join(sys.argv[1:])
    yd = YoDude(s)
    yd.hello()
