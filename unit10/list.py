Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [38, 21, 53, 62, 19]
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
[38, 21, 53, 62, 19]
>>> person = ['james', 17, 175.3, True]
>>> person
['james', 17, 175.3, True]
>>> a = []
>>> a
[]
>>> b = list()
>>> b
[]
>>> range(10)
range(0, 10)
>>> a = list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b = list(range(5, 12))
>>> b
[5, 6, 7, 8, 9, 10, 11]
>>> c = list(range(-4, 10, 2))
>>> c
[-4, -2, 0, 2, 4, 6, 8]
>>> d = list(range(10, 0, -1))
>>> b
[5, 6, 7, 8, 9, 10, 11]
>>> d
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
