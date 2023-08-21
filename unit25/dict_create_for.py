Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> keys = ['a', 'b', 'c', 'd']
>>> x = {key: value for key, value in dict.fromkeys(keys).items()}
>>> x
{'a': None, 'b': None, 'c': None, 'd': None}
>>> {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}
{10: 0, 20: 0, 30: 0, 40: 0}
>>> {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}
{10: 'a', 20: 'b', 30: 'c', 40: 'd'}
