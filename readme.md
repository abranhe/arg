<p align="center" id="top">
	<a href="https://pypi.org/project/arg">
		<img src="https://cdn.abranhe.com/projects/arg/logo.svg">
	</a>
	<br>
	<br>
	<a href="https://pypi.org/project/arg">
		<b>𝘼𝙍𝙂</b>
	</a> Parse command line arguments made easier...
</p>

<p align="center">
	<a href="https://github.com/abranhe/arg/actions/workflows/main.yml">
		<img src="https://github.com/abranhe/arg/actions/workflows/main.yml/badge.svg" />
	</a>
	<a href="https://app.travis-ci.com/github/abranhe/arg">
		<img src="https://img.shields.io/travis/com/abranhe/arg.svg?logo=travis" />
	</a>
	<a href="https://pypi.org/project/arg">
		<img src="https://img.shields.io/pypi/v/arg">
	</a>
	<a href="https://github.com/abranhe/arg/blob/master/license">
		<img src="https://img.shields.io/github/license/abranhe/arg.svg" />
	</a>
</p>

## Install

```console
$ pip install arg
```

## Usage

```console
$ python main.py ford -m mustang --year 2017 red
```

> _main.py_

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

## API

### `arg()`

> Return an array with the arguments without the file name

**Return Type**: `list`

### `.v()`

> Return an array with all the arguments. (**arg.v** ~> argv _Argumet Vector_)

**Return Type**: `list`

### `.c()`

> Return an array with all the arguments. (**arg.c** ~> argc _Argument Count_)

**Return Type**: `int`

### `.s()`

> Return an string with all the arguments. (arg.s ~> Arguments to String)

**Return Type**: `str`

### `.fileName()`

> Return an string with the name of the file

**Return Type**: `str`

### `.at(n)`

> Return the value of the argument at value at **n**, otherwise **404**

**Return Type**: `str`

## Related

- [**lupe**](https://github.com/abranhe/lupe): The CLI helper you need 🥭

## License

MIT © [Abraham Hernandez](https://github.com/abranhe)
