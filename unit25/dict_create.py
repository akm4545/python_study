Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> keys = ['a', 'b', 'c', 'd']
>>> x = dict.fromkeys(keys)
>>> x
{'a': None, 'b': None, 'c': None, 'd': None}
>>> y = dict.fromkeys(keys, 100)
>>> y
{'a': 100, 'b': 100, 'c': 100, 'd': 100}
>>> x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> x['z']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x['z']
KeyError: 'z'
>>> from collections import defaultdict
>>> y = defaultdict(int)
>>> y['z']
0
>>> z = defaultdict(lambda: 'python')
>>> z['a']
'python'
>>> z[0]
'python'
