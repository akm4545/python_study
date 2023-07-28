Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = -5
>>> a is -5
True
>>> a = -6
>>> a is -6
False
>>> True and Treu
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    True and Treu
NameError: name 'Treu' is not defined
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> not True
False
>>> not False
True
>>> not True and False or not False
True
>>> ((not True) and False) or (not False)
True
