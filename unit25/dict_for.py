Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> for i in x:
...     print(i, end=' ')
... 
...     
a b c d 
>>> for key, value in x.items():
...     print(key, value)
... 
...     
a 10
b 20
c 30
d 40
>>> for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
...     print(key, value)
... 
...     
a 10
b 20
c 30
d 40
>>> for key in x.keys():
...     print(key, end=' ')
... 
...     
a b c d 
>>> for value in x.values():
...     print(value, end=' ')
... 
...     
10 20 30 40 
