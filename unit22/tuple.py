Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = (38, 21, 53, 62, 19, 53)
>>> a.index(53)
2
>>> a = (10, 20, 30, 15, 20, 40)
>>> a.count(20)
2
>>> a = (38, 21, 53, 62, 19)
>>> for i in a:
...     print(i, end='')
... 
...     
3821536219
>>> a = tuple(i for i in range(10) if i% 2 == 0)
>>> a
(0, 2, 4, 6, 8)
>>> (i for i in range(10) if i % 2 == 0)
<generator object <genexpr> at 0x000002329EE439F0>
>>> a = (1.2, 2.5, 3.7, 4.6)
>>> a = tuple(map(int, a))
>>> a
(1, 2, 3, 4)
>>> a = (38, 21, 53, 62, 19)
>>> min(a)
19
>>> max(a)
62
>>> sum(a)
193
