import sys

class Arguments(object):
	args = sys.argv

	def a(self):
		# slice array instead of .copy()
		# https://stackoverflow.com/a/2612815/7602110
		aa = self.args[:]
		del aa[0]
		return aa

	__call__ = a

	# argv: (argument vector)
	def v(self):
		return self.args

	# argc: (argument count)
	def c(self):
		return len(self.args)

	# args: (argument as string)
	def s(self):
		return ' '.join(self.args)

	# File Name
	def fileName(self):
		return self.args[0]

	# Get Specific Arg
	def at(self, number):
		return self.args[number] if (0 <= (number) < len(self.args)) else '404'

sys.modules[__name__] = Arguments()
