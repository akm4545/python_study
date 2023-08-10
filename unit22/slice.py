Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [10, 20, 30]
>>> a[len(a):] = [500]
>>> a
[10, 20, 30, 500]
>>> a = [10, 20, 30]
>>> a[len(a):] = [500, 600]
>>> a
[10, 20, 30, 500, 600]
>>> if not a
SyntaxError: incomplete input
>>> if not a:
...     print('empty')
... else:
...     print('not empty')
... 
...     
not empty
>>> 
>>> seq = []
>>> if seq:
...     print(seq[-1])
... 
...     
