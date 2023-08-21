Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {1, 2, 3, 4}
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> a.remove(3)
>>> a
{1, 2, 4, 5}
>>> a.discard(2)
>>> a
{1, 4, 5}
>>> a.discard(3)
>>> a
{1, 4, 5}
>>> a = {1, 2, 3, 4}
>>> a.pop()
1
>>> a
{2, 3, 4}
>>> a.clear()
>>> a
set()
>>> a = {1, 2, 3, 4}
>>> len(a)
4
