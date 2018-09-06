import unittest
import arg

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(arg.fileName(), 'test.py')

if __name__ == '__main__':
    unittest.main()
