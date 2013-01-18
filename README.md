# loops

Loop context inspired by Mako.


### Installation and usage

To install, just run `python setup.py install` from terminal.


Say we are iterating over some iterable.
Now we would like to do something special despending on the position of the current item.
Usually we can write like this:

```
last_index = len(list(iterable))
for i, x in enumerate(iterable, from=1):
    if i == 1: print('The first item')
    if i == last_index: print('The last item')
```

It works fine but always makes me wondering: is there any simpler way to do this?

The code using `loops` looks like:

```
for l, x in loops.loop(iterable):
    if l.isfirst(): pass
    if l.islast(): pass
    if l.iseven(): pass
    if l.index % 3 == 0: pass
```

which is more readable than the approch shown above.


Sometimes we want to get multiple items per loop.
Maybe because of the ill-formed data, bad design etc. whatever.
With `loops` now we can just write:

```
for l, (a, b) in loops.loop(iterable, n=2):
    print(l.count) # the loop counter: 0, 1, 2 ...
    print(l.index) # the index of the first loop variable: 0, 2, 4, ...
    print('a=%s, b=%s' % (a, b))
```


And how do we check whether the iterator is empty?

```
for l, x in loops.loop(iterable):
    pass

if l.isempty():
    print('empty')
```

### Troubleshooting
