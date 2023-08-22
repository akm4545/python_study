Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lambda x: x + 10
<function <lambda> at 0x000001A890949BC0>
>>> plus_ten = lambda x: x + 10
>>> plus_ten(1)
11
>>> (lambda x: x + 10)(1)
11
>>> (lambda x: y = 10; x + y)(1)
SyntaxError: invalid syntax
>>> y = 10
>>> (lambda x: x + y)(1)
11
>>> def plus_ten(x):
...     return x + 10
... 
>>> list(map(plus_ten, [1, 2, 3]))
[11, 12, 13]
>>> list(map(lambda x: x+ 10, [1, 2, 3]))
[11, 12, 13]
>>> (lambda: 1)()
1
>>> x = 10
>>> (lambda: x)()
10
