Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
30 in a
True
100 in a
True
110 in a
False
110 not in a
True
30 not in a
False
43 in (38, 76, 43, 62, 19)
True
1 in range(10)
True
>>> 'P' in 'Hello, Python'
True
>>> a = [0, 10, 20, 30]
>>> b = [9, 8, 7, 6]
>>> a + b
[0, 10, 20, 30, 9, 8, 7, 6]
>>> range(0, 10) + range(10, 20)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    range(0, 10) + range(10, 20)
TypeError: unsupported operand type(s) for +: 'range' and 'range'
>>> list(range(0, 10)) + list(range(10,20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> tuple(range(0, 10)) + tuple(range(10,20))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
>>> 'Hello, ' + 'world!'
'Hello, world!'
>>> 'Hello, ' + 10
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    'Hello, ' + 10
TypeError: can only concatenate str (not "int") to str
>>> 'Hello, ' + str(10)
'Hello, 10'
>>> 'Hello, ' + str(1.5)
'Hello, 1.5'
>>> [0, 10, 20, 30] * 3
[0, 10, 20, 30, 0, 10, 20, 30, 0, 10, 20, 30]
>>> range(0, 5, 2) * 3
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    range(0, 5, 2) * 3
TypeError: unsupported operand type(s) for *: 'range' and 'int'
>>> list(range(0, 5, 2)) * 3
[0, 2, 4, 0, 2, 4, 0, 2, 4]
>>> tuple(range(0, 5, 2)) * 3
(0, 2, 4, 0, 2, 4, 0, 2, 4)
>>> 'Hello, ' * 3
'Hello, Hello, Hello, '
