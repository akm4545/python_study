Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [10, 20, 30]
>>> a.insert(2, 500)
>>> a
[10, 20, 500, 30]
>>> len(a)
4
>>> a = [10, 20, 30]
>>> a.insert(0, 500)
>>> a
[500, 10, 20, 30]
>>> a = [10, 20, 30]
>>> a.insert(len(a), 500)
>>> a
[10, 20, 30, 500]
>>> a = [10, 20, 30]
>>> a.insert(1, [500, 600])
>>> a
[10, [500, 600], 20, 30]
>>> a= [10, 20, 30]
>>> KeyboardInterrupt
>>> a = [10, 20, 30]
>>> a[1:1] = [500, 600]
>>> a
[10, 500, 600, 20, 30]
