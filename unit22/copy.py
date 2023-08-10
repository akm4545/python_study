Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [0, 0, 0, 0, 0]
>>> b = a
>>> a is b
True
>>> b[2] = 99
>>> a
[0, 0, 99, 0, 0]
>>> b
[0, 0, 99, 0, 0]
>>> a = [0, 0, 0, 0, 0]
>>> b = a.copy()
>>> a is b
False
>>> a == b
True
>>> b[2] = 99
>>> a
[0, 0, 0, 0, 0]
b
>>> 
>>> 
>>> b
[0, 0, 99, 0, 0]
