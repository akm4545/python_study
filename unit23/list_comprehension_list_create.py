Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [[0 for j in range(2)] for i in range(3)]
>>> a
[[0, 0], [0, 0], [0, 0]]
>>> a = [[0] * 2 for i in range(3)]
>>> a
[[0, 0], [0, 0], [0, 0]]
