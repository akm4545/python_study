Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
{1, 2, 3, 4, 5, 6}
set.union(a, b)
{1, 2, 3, 4, 5, 6}
a & b
{3, 4}
set.intersection(a, b)
{3, 4}
a - b
{1, 2}
set.difference(a, b)
{1, 2}
a ^ b
{1, 2, 5, 6}
set.symmetric_difference(a, b)
{1, 2, 5, 6}
a = {1, 2, 3, 4}
a |= {5}
a
{1, 2, 3, 4, 5}
a = {1, 2, 3, 4}
a.update({5})
a
{1, 2, 3, 4, 5}
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
a
{1, 2, 3, 4}
a.intersercion_update({0, 1, 2, 3, 4})
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.intersercion_update({0, 1, 2, 3, 4})
AttributeError: 'set' object has no attribute 'intersercion_update'. Did you mean: 'intersection_update'?
a.intersection_update({0, 1, 2, 3, 4})
a
{1, 2, 3, 4}
a = {1, 2, 3, 4}
a -= {3}
a
{1, 2, 4}
a = {1, 2, 3, 4}
a.defference_update({3})
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.defference_update({3})
AttributeError: 'set' object has no attribute 'defference_update'. Did you mean: 'difference_update'?
>>> a.difference_update({3})
>>> a
{1, 2, 4}
>>> a = {1, 2, 3, 4}
>>> a ^= {3, 4, 5, 6}
>>> a
{1, 2, 5, 6}
>>> a = {1, 2, 3, 4}
>>> a.symmetric_difference_update({3, 4, 5, 6})
>>> a
{1, 2, 5, 6}
>>> a = {1, 2, 3, 4}
>>> a <= {1, 2, 3, 4}
True
>>> a.issubset({1, 2, 3, 4})
True
>>> a = {1, 2, 3, 4}
>>> a < {1, 2, 3, 4, 5}
True
>>> a = {1, 2, 3, 4}
>>> a >= {1, 2, 3, 4}
True
>>> a.issuperset({1, 2, 3, 4})
True
>>> a = {1, 2, 3, 4}
>>> a > {1, 2, 3}
True
>>> a = {1, 2, 3, 4}
>>> a == {1, 2, 3, 4}
True
>>> a == {4, 2, 1, 3}
True
>>> a != {1, 2, 3}
True
>>> a.isdisjoint({5, 6, 7, 8})
True
>>> a.isdisjoint({3, 4, 5, 6})
False
