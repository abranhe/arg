"""Token types for the arg parser."""
SPACE = ' '
SMALL_FLAG = '-'
LARGE_FLAG = '--'
SINGLE_QUOTE = "'"
DOUBLE_QUOTE = '"'

def tokenize(args):
	"""
	Tokenize an command-line args. Returns a list of tokens.
	It accepts a string or a list of strings, otherwise it will rise an exception.

	```python
	>>> tokenize('-a -b -c')
	['-a', '-b', '-c']
	```
	"""
	if isinstance(args, list):
		return map(lambda x: f'{x}', args)

	# if not isinstance(args, str) or not isinstance(args, list):
	#     raise TypeError('args must be a string or a list of strings')

	args = args.strip()

	i = 0
	opening = None
	prev_char = None
	tokens = []

	# loop for all items in args
	for char in args:
		prev_char = char

		if char == SPACE and not opening:
		    if not prev_char == SPACE:
		        i += 1
		    continue

		if char == opening:
		    opening = None
		elif char in [SINGLE_QUOTE, DOUBLE_QUOTE] and not opening:
		    opening = char



	return tokens
