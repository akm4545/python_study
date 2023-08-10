Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [i for i in range(10)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b = list(i for i in range(10))
>>> b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> c = [i + 5 for i in rnage(10)]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c = [i + 5 for i in rnage(10)]
NameError: name 'rnage' is not defined. Did you mean: 'range'?
>>> c = [i + 5 for i in range(10)]
>>> c
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> d = [i * 2 for i in range(10)]
>>> d
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> a = [i for i in range(10) if i % 2 == 0]
>>> a
[0, 2, 4, 6, 8]
>>> b = [i + 5 for i in range(10) if 1 % 2 == 1]
>>> b
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> a = [i * j for j in range(2, 10) for i in range(1, 10]
...      
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> a
...      
[0, 2, 4, 6, 8]
>>> a = [i * j for j in range(2, 10) for i in range(1, 10)]
...      
>>> a
...      
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
