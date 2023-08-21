Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> y = x
>>> x is y
True
>>> y['a'] = 99
>>> x
{'a': 99, 'b': 0, 'c': 0, 'd': 0}
>>> y
{'a': 99, 'b': 0, 'c': 0, 'd': 0}
>>> x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> y = x.copy()
>>> x is y
False
>>> x == y
True
>>> y['a'] = 99
>>> x
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> y
{'a': 99, 'b': 0, 'c': 0, 'd': 0}
>>> x = {'a': {'python': 2.7}, 'b': {'python': '3.6'}}
>>> y = x.copy()
>>> y['a']['python'] = '2.7.15'
>>> x
{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}
>>> y
{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}
>>> x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
>>> import copy
>>> y = copy.deepcopy(x)
>>> y['a']['python'] = '2.7.15'
>>> x
{'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
>>> y
{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}
