Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {1, 2, 3, 4,}
>>> a
{1, 2, 3, 4}
>>> b = a
>>> a is b
True
>>> b.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> b
{1, 2, 3, 4, 5}
>>> a = {1, 2, 3, 4}
>>> b = a.copy()
>>> a is b
False
>>> a == b
True
>>> b.add(5)
>>> a
{1, 2, 3, 4}
>>> b
{1, 2, 3, 4, 5}
