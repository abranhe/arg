<p align="center" id="top">
	<a href="https://pypi.org/project/arg"><img src="https://cdn.abraham.gq/projects/arg/logo.svg"></a>
	<br>
	<br>
	<br>
	<a href="https://pypi.org/project/arg"><b>𝘼𝙍𝙂</b></a>
	: Parse command line arguments made easier...
</p>

<p align="center">
	<!-- Travis CI -->
	<a href="https://travis-ci.org/abranhe/arg"><img src="https://img.shields.io/travis/abranhe/arg.svg?logo=travis" /></a>
	<!-- LICENSE -->
	<a href="https://github.com/abranhe/arg/blob/master/LICENSE"><img src="https://img.shields.io/github/license/abranhe/arg.svg" /></a>
	<!-- @abranhe -->
	<a href="https://github.com/abranhe"><img src="https://abranhe.com/badge.svg"></a>
	<!-- Cash me -->
	<a href="https://cash.me/$abranhe"><img src="https://cdn.abranhe.com/badges/cash-me.svg"></a>
	<!-- Patreon -->
	<a href="https://www.patreon.com/abranhe"><img src="https://cdn.abranhe.com/badges/patreon.svg" /></a>
	<!-- Paypal -->
	<a href="https://paypal.me/abranhe/10"><img src="https://cdn.abranhe.com/badges/paypal.svg" /></a>
</p>


# Install

```
pip install arg
```

# Usage

```
$ python test.py ford -m mustang --year 2017 red
```

> *test.py*

```py
import arg

# argv without file name
print(arg())
# => ['ford', '-m', 'mustang', '--year', '2017', 'red']

# argv
print(arg.v())
# => ['test.py', 'ford', '-m', 'mustang', '--year', '2017', 'red']

# argc
print(arg.c())
# => 7

# args as string
print(arg.s())
# => test.py ford -m mustang --year 2017 red

# file name
print(arg.fileName())
# => test.py

# argument at n
print(arg.at(2))
# => -m

```

# API

### `arg()`

> Return an array with the arguments without the file name

**Return Type**: `list`

### `.v()`

> Return an array with all the arguments. (**arg.v** ~> argv *Argumet Vector*)

**Return Type**: `list`

### `.c()`

> Return an array with all the arguments. (**arg.c** ~> argc *Argument Count*)

**Return Type**: `int`

### `.s()`

> Return an string with all the arguments. (arg.s ~> Arguments to String)

**Return Type**: `str`

### `.fileName()`

> Return an string with the name of the file

**Return Type**: `str`

### `.at(n)`

> Return the value of the argument at value at **n**

**Return Type**: `str`

# Related

- [**lupe**](https://github.com/abranhe/lupe): A better CLI Helper.

# Team

|[![Carlos Abraham Logo](https://avatars3.githubusercontent.com/u/21347264?s=50&v=4)](https://abranhe.com)|
| :-: |
| [Carlos Abraham](https://github.com/abranhe) |

# License

[MIT](https://github.com/abranhe/arg/blob/master/LICENSE) License © [Carlos Abraham](https://github.com/abranhe/)
