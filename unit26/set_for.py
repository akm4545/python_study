Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {1, 2, 3, 4}
>>> for i in a:
...     print(i)
... 
...     
1
2
3
4
>>> for i in {1, 2, 3, 4}L
SyntaxError: incomplete input
>>> for i in {1, 2, 3, 4}:
...     print(i)
... 
...     
1
2
3
4
