Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10 == 10 and 10 != 5
True
>>> 10 > 5 or 10 < 3
True
>>> not 10 > 5
False
>>> not 1 is 1.0
True
>>> bool(1)
True
>>> bool(0)
False
>>> bool(1.5)
True
>>> bool('False')
True
>>> True and 'Python'
'Python'
>>> 'Python' and True
True
>>> 'Python' and False
False
>>> 0 and 'Python"
SyntaxError: incomplete input
>>> 0 and 'Python'
0
>>> True or 'Python'
True
>>> 'Python' or True
'Python'
>>> False or 'Python"
SyntaxError: incomplete input
>>> False or 'Python'
'Python'
>>> 0 or False
False
