# idotscript

## Syntax

```
function>args
i.
function>
```
### `i.`
`i.` should be between function, but not after the last function or before the first function.
## Functions
### `error`
#### args
none
#### Result
In: `error>`

Out:

```
Traceback (most recent call last):
  File "parser.py", line 18, in <module>
    r(sys.argv[1])
  File "parser.py", line 17, in r
    parse(open(file).read())
  File "parser.py", line 9, in parse
    raise IdotError()
__main__.IdotError
```

### `print`
#### args
stuff to print `,` (comma) seperated
#### Result
In: `print>Hello World!`

Out:

```
Hello World!
```

### `yoda`
#### args
none
#### Result
In: `yoda>`

Out:

```
idot
```