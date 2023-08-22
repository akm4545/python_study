Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(a, b):
...     return a + b
... 
>>> x = add(10, 20)
>>> x
30
>>> print(add(10, 20))
30
>>> def not_ten(a):
...     if a == 10:
...         return
...     print(a, '입니다.', sep='')
... 
...     
>>> not_ten(5)
5입니다.
>>> not_ten(10)
