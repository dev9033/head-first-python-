# find help about any module (`dir`)

_example: below will tell what random module contain_

```python
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MA
GICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__al
l__', '__builtins__', '__cached__', '__doc__', '__file__', '__
loader__', '__name__', '__package__', '__spec__', '_accumulate
', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst',
 '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin'
, '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'b
etavariate', 'choice', 'choices', 'expovariate', 'gammavariate
', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'norm
alvariate', 'paretovariate', 'randint', 'random', 'randrange',
 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'unifo
rm', 'vonmisesvariate', 'weibullvariate']
>>>
```

# find help about something specific (`help(<name>)`)

with help() we can find documentation on the particular function
_example: below will tell about random's randint function_

```python
>>> import random
>>> help(random.randint)

Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
/tmp/tmp9g3zpm1e (END)
```

# know what is the type of a particular variable (`type`)

```python
>>> x = 4
>>> y = 5.3
>>> c = 'hey'
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(c)
<class 'str'>
```

# Methods / Functions
* for _ in _:
* range(start,stop,step)
* in
* not in
* len()
* list`[]`
  1. insert
     * append
     * extend
     * insert
   2. remove
      * remove
      * pop
      * clear
      * del
  3. sorted
* join()
* format()
* copy()
* split() `[::2]`
* `\t` tab
* `\n` next line
* dict()
  * setdefault()
* set()
  * union()
  * intersection()
  * difference()
  * sorted()
* type()

<br>

---

---

<ul style="color:red;">
<li>
for sequential search list is slower than set. So always prefer sets when doing sequential searches</li>
<li>If you need to perform frequency count dictionary is best. But if you want to maintain insertion order then list is best</li>
<li>If the data in your structure never changes, put it in a tuple (for better performance)</li>
</ul>

---

---

<br>

# MODULES content

## <ins>sys</ins>

- stdin.readline()
- platform
- version

## <ins>os</ins>

- getenv
- getcwd
- environ

## <ins>datetime</ins>

- datetime
  - isoformat
  - date
    - isoformat
  - today
    - year
    - day
    - minute
    - month

## <ins>time</ins>

- strftime
- sleep

## <ins>html</ins>

- escape
- unescape

## random

- randint
