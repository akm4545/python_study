Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add_sub(a, b):
...     return a + b, a - b
... 
>>> x, y = add_sub(10, 20)
>>> x
30
>>> t
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> y
-10
>>> x = add_sub(10, 20)
>>> x
(30, -10)
