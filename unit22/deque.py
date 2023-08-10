Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import deque
>>> a = deque([10, 20, 30])
>>> a
deque([10, 20, 30])
>>> a.append(500)
>>> a
deque([10, 20, 30, 500])
>>> a.popleft()
10
>>> a
deque([20, 30, 500])
