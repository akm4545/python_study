Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [38, 21, 53, 62, 19]
>>> i = 0
>>> while i < len(a)
SyntaxError: incomplete input
>>> while i < len(a):
...     print(a[i])
...     i += 1
... 
...     
38
21
53
62
19
>>> while i < len(a):
...     print(a[i])
...     i += 1
... 
...     
