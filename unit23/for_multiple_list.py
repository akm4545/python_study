Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [[10, 20], [30, 40], [50, 60]]
>>> for x, y in a:
...     print(x, y)
... 
...     
10 20
30 40
50 60
>>> for i in a:
...     for j in i:
...         print(j, end =' ')
...     print()
... 
...     
10 20 
30 40 
50 60 
