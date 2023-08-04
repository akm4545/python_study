Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [38, 21, 53, 62, 19]
a[0]
38
a[2]
53
a[4]
19
b = (38, 21, 53, 62, 19)
b[0]
38
r = range(0, 10, 2)
r[2]
4
hello = 'Hello, world!'
hello[7]
'w'
a = [38, 21, 53, 62, 19]
a.__getimte__(1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.__getimte__(1)
AttributeError: 'list' object has no attribute '__getimte__'. Did you mean: '__getitem__'?
a.__getitem__(1)
21
a[-1]
19
a[-5]
38
b = (38, 21, 53, 62, 19)
b[-1]
19
r = range(0, 10, 2)
r[-3]
4
hello = 'Hello, world!'
hello[-4]
'r'
a[5]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[5]
IndexError: list index out of range
len(a)
5
a[len(a)]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[len(a)]
IndexError: list index out of range
a[len(a) - 1]
19
a = [0, 0, 0, 0, 0]
a[0] = 38
a[1] = 21
a[2] = 53
>>> a[3] = 62
>>> a[4] = 19
>>> a
[38, 21, 53, 62, 19]
>>> a[0]
38
>>> a[4]
19
>>> b = (0, 0, 0, 0, 0)
>>> b[0] = 38
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b[0] = 38
TypeError: 'tuple' object does not support item assignment
>>> r = range(0, 10, 2)
>>> r[0] = 3
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    r[0] = 3
TypeError: 'range' object does not support item assignment
>>> hello = 'Hello, world!'
>>> hello[0] = 'A'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    hello[0] = 'A'
TypeError: 'str' object does not support item assignment
>>> del a[2]
>>> a
[38, 21, 62, 19]
>>> del b[2]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    del b[2]
TypeError: 'tuple' object doesn't support item deletion
>>> del hello[2]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    del hello[2]
TypeError: 'str' object doesn't support item deletion
