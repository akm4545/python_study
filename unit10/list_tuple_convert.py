Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1, 2 3]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a = [1, 2, 3]
>>> tuple(a)
(1, 2, 3)
>>> b = (4, 5, 6)
>>> list(b)
[4, 5, 6]
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> tuple('Hello')
('H', 'e', 'l', 'l', 'o')
>>> a, b, c = [1, 2, 3]
>>> print(a, b, c)
1 2 3
>>> d, e, f = (4, 5, 6)
>>> print(d, e, f)
4 5 6
>>> x = [1, 2, 3]
>>> a, b, c = x
>>> print(a, b, c)
1 2 3
>>> y = (4, 5, 6)
>>> d, e, f = y
>>> print(d, e, f)
4 5 6
>>> input().split()
10 20
['10', '20']
>>> x = input().split()
10 20
>>> a, b = x
>>> print(a, b)
10 20
>>> 
>>> a = [1, 2, 3] #리스트 패킹
>>> b = (1, 2, 3) #튜플 패킹
>>> c = 1, 2, 3 #튜플 패킹
