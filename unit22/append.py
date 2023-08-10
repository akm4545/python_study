Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [10, 20, 30]
>>> a.append(500)
>>> a
[10, 20, 30, 500]
>>> len(a)
4
>>> a = []
>>> a.append(10
...          a
...          
SyntaxError: incomplete input
>>> a = []
...          
>>> a.append(10)
...          
>>> a
...          
[10]
>>> a = [10, 20, 30]
...          
>>> a.append([500, 600])
...          
>>> a
...          
[10, 20, 30, [500, 600]]
>>> len(a)
...          
4
