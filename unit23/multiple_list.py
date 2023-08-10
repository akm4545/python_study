Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [[10, 20], [30, 40], [50, 60]]
a
[[10, 20], [30, 40], [50, 60]]
a[0][0]
10
a[1][1]
40
a[2][1]
60
a[0][1] = 1000
a[0][1]
1000
a = []
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]
a = []
a.append([])
a[0].append(10)
a[0].append(20)
>>> a.append([])
>>> a[1].append(500)
>>> a[1].append(600)
>>> a[1].append(700)
>>> a
[[10, 20], [500, 600, 700]]
>>> a = ((10, 20), (30, 40), (50, 60))
>>> b = ([10, 20], [30, 40], [50, 60])
>>> c = [(10, 20), (30, 40), (50, 60)]
>>> a[0][0] = 500
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[0][0] = 500
TypeError: 'tuple' object does not support item assignment
>>> a[0] = (500, 600)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[0] = (500, 600)
TypeError: 'tuple' object does not support item assignment
>>> b[0][0] = 500
>>> b[0] = (500, 600)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b[0] = (500, 600)
TypeError: 'tuple' object does not support item assignment
>>> c[0][0] = 500
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c[0][0] = 500
TypeError: 'tuple' object does not support item assignment
>>> c[0] = (500, 600)
>>> a = [[10, 20], [30, 40], [50, 60]]
>>> a
[[10, 20], [30, 40], [50, 60]]
>>> from pprint import pprint
>>> pprint(a, indent=4, width=20)
[   [10, 20],
    [30, 40],
    [50, 60]]
