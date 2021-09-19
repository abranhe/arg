"""
Parse command-line arguments made easier

Read more on the [documentation](https://github.com/abranhe/lupe)
"""

__version__ = '0.0.2'

from arg.parser import _Parser


def parse(*args):
    __parser = _Parser(*args)

    return __parser.parse()
