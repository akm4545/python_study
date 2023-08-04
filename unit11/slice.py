Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[0:4]
[0, 10, 20, 30]
a[0:10]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[1:1]
[]
a[1:2]
[10]
a[4:7]
[40, 50, 60]
a[4:-1]
[40, 50, 60, 70, 80]
a[2:8:3]
[20, 50]
a[2:9:3]
[20, 50, 80]
a[:7]
[0, 10, 20, 30, 40, 50, 60]
a[7:]
[70, 80, 90]
a[:]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[:7:2]
[0, 20, 40, 60]
a[7::2]
[70, 90]
a[::2]
[0, 20, 40, 60, 80]
a[::]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[5:1:-1]
[50, 40, 30, 20]
a[::-1]
[90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
a[0:len(a)]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[:len(a)]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
b[4:7]
(40, 50, 60)
b[4:]
(40, 50, 60, 70, 80, 90)
b[:7:2]
(0, 20, 40, 60)
r = range(10)
r
range(0, 10)
r[4:7]
range(4, 7)
r[4:]
range(4, 10)
r[:7:2]
range(0, 7, 2)
list(r[:7:2])
[0, 2, 4, 6]
hello = 'Hello, world!'
hello[2:9]
'llo, wo'
hello[2:]
'llo, world!'
hello[:9:2]
'Hlo o'
range(10)[slice(4, 7, 2)]
range(4, 7, 2)
range(10).__getitem__(slice(4,7,2))
range(4, 7, 2)
s = slice(4, 7)
a[s]
[40, 50, 60]
r = range(10)
r[s]
range(4, 7)
hello = 'Hello, world!'
hello[s]
'o, '
a[2:5] = ['a', 'b', 'c']
a
[0, 10, 'a', 'b', 'c', 50, 60, 70, 80, 90]
a[2:5] = ['a']
a
[0, 10, 'a', 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e']
a
[0, 10, 'a', 'b', 'c', 'd', 'e', 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e']
a
[0, 10, 'a', 'b', 'c', 'd', 'e', 50, 60, 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:8:2] = ['a', 'b', 'c']
a


a
[0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:8:2] = ['a', 'b']
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a[2:8:2] = ['a', 'b']
ValueError: attempt to assign sequence of size 2 to extended slice of size 3
b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
b[2:5] = ('a', 'b', 'c')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b[2:5] = ('a', 'b', 'c')
TypeError: 'tuple' object does not support item assignment
>>> r = range(10)
>>> r[2:5] = range(0, 3)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    r[2:5] = range(0, 3)
TypeError: 'range' object does not support item assignment
>>> hello = 'Hello, world!'
>>> hello[7:13] = 'Python'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    hello[7:13] = 'Python'
TypeError: 'str' object does not support item assignment
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> del a[2:5]
>>> a
[0, 10, 50, 60, 70, 80, 90]
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> del a[2:8:2]
>>> a
[0, 10, 30, 50, 70, 80, 90]
>>> b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
>>> del b[2:5]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    del b[2:5]
TypeError: 'tuple' object does not support item deletion
>>> r = range(10)
>>> del r[2:5]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    del r[2:5]
TypeError: 'range' object does not support item deletion
>>> hello = 'Hello, world!'
>>> del hello[2:9]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    del hello[2:9]
TypeError: 'str' object does not support item deletion
