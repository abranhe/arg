import sys


class _Parser:
    def __init__(self, args=sys.argv):
        self.contex = {}

        self._parse_args(args)

    def parse(self):
        return self.context

    def _parse_args(self, args):
        if isinstance(args, list):
            self._parse_list_args(args)
        elif isinstance(args, str):
            self._parse_str_args(args)
        else:
            raise TypeError('args must be list or str')

    def _parse_list_args(self, args):
        return args

    def _parse_str_args(self, args):
        return args

    # -------------------------------------------------------------------------

    def filename(self):
        return sys.argv[0]

    def argv():
        return sys.argv[1:]

    def count():
        return len(sys.argv[1:])

    def get_at(self, index):
        if index < self.count():
            return self.argv()[index]
        else:
            return None
