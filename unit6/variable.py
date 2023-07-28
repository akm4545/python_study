Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 10
>>> x
10
>>> y = "Hello, world!"
>>> y
'Hello, world!'
>>> type(x)
<class 'int'>
>>> type(y)
<class 'str'>
>>> x, y, z = 10, 20, 30
>>> x
10
>>> y
20
>>> z
30
>>> x = y = z = 10
>>> x
10
>>> y
10
>>> z
10
>>> x, y = 10, 20
>>> x, y = y, x
>>> x
20
>>> y
10
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x = None
>>> print(x)
None
>>> x
