import unittest

from arg import tokenizer


class TokenizerTest(unittest.TestCase):
    def test_unquoted_string(self):
        args = tokenizer.tokenize('--foo 99')
        self.assertEqual(args[0], '--foo')
        self.assertEqual(args[1], '99')

    # def test_unquoted_list(self):
    #     args = tokenizer.tokenize(['--foo', '99'])
    #     self.assertEqual(args[0], '--foo')
    #     self.assertEqual(args[1], '99')

    # def test_quoted_string_with_no_spaces(self):
    #     args = tokenizer.tokenize("--foo 'hello'")
    #     self.assertEqual(args[0], '--foo')
    #     self.assertEqual(args[1], "'hello'")

    # def test_single_quoted_string_with_spaces(self):
    #     args = tokenizer.tokenize("--foo 'hello world' --bar='foo bar'")
    #     self.assertEqual(args[0], '--foo')
    #     self.assertEqual(args[1], "'hello world'")
    #     self.assertEqual(args[2], "--bar='foo bar'")

    # def test_invalid_args(self):
    #     with self.assertRaises(TypeError):
    #         tokenizer.tokenize('dfs')


if __name__ == '__main__':
    unittest.main()
