Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = {'a': 10, 'b': 20, 'c': 30, 'd':40}
x.setdefault('e')
x
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}
x.setdefault('f', 100)
100
x
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100}
x.update(a=90)
x
{'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100}
x.update(g=50)
x
{'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100, 'g': 50}
x.update(a=900, h=60)
x
{'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100, 'g': 50, 'h': 60}
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
y
{1: 'ONE', 2: 'two', 3: 'THREE'}
y.update([[2, 'TWO'], [4, 'FOUR']])
y
{1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}
y.update(zip([1, 2], ['one', 'two']))
y
{1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdetault('a', 90)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x.setdetault('a', 90)
AttributeError: 'dict' object has no attribute 'setdetault'. Did you mean: 'setdefault'?
>>> x.setdefault('a', 90)
10
>>> x
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.pop('a')
10
>>> x
{'b': 20, 'c': 30, 'd': 40}
>>> x.pop('z', 0)
0
>>> del x['a']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    del x['a']
KeyError: 'a'
>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> del x['a']
>>> x
{'b': 20, 'c': 30, 'd': 40}
>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.popitem()
('d', 40)
>>> x
{'a': 10, 'b': 20, 'c': 30}
>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.clear()
>>> x
{}
>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.get('a')
10
>>> x.get('z', 0)
0
>>> x.items()
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
>>> x.keys()
dict_keys(['a', 'b', 'c', 'd'])
>>> x.values()
dict_values([10, 20, 30, 40])
