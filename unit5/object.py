Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(10)
<class 'int'>
>>> divmod(5, 2)
(2, 1)
>>> quotient, remainder = divmod(5, 2)
>>> print(quotient, remainder)
2 1
>>> 0b110
6
>>> 0o10
8
>>> 0xF
15
>>> 3.5 + 2.1
5.6
>>> 4.3 - 2.7
1.5999999999999996
>>> 1.5 * 3.1
4.65
>>> 5.5 / 3.1
1.7741935483870968
>>> 4.2 + 5
9.2
>>> float(5)000
SyntaxError: incomplete input
>>> float(5)
5.0
>>> float(1 + 2)
3.0
>>> float('5.3')
5.3
>>> type(3.5)
<class 'float'>
>>> 1.2 + 1.3j
(1.2+1.3j)
>>> complex(1.2, 1.3)
(1.2+1.3j)
