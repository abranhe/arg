import unittest
from arg import arg


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(arg.filename(), 'test.py')


if __name__ == '__main__':
    unittest.main()
