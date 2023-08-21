Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
fruits
{'orange', 'cherry', 'pineapple', 'grape', 'strawberry'}
fruits = {'orange', 'orange', 'cherry'}
fruits
{'cherry', 'orange'}
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits[0])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(fruits[0])
TypeError: 'set' object is not subscriptable
fruits['strawberry']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    fruits['strawberry']
TypeError: 'set' object is not subscriptable
'orange' in fruits
True
'peach' in fruits
False
'peach' not in fruits
True
'orange' not in fruits
False
a = set('apple')
a
{'a', 'l', 'p', 'e'}
b = set(range(5))
>>> b
{0, 1, 2, 3, 4}
>>> c = set()
>>> c
set()
>>> c = {}
>>> type(c)
<class 'dict'>
>>> c = set()
>>> type(c)
<class 'set'>
\
>>> set('안녕하세요')
{'안', '녕', '하', '요', '세'}
>>> a = {{1, 2}, {3, 4}}
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a = {{1, 2}, {3, 4}}
TypeError: unhashable type: 'set'
>>> a = frozenset(range(10))
>>> a
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
>>> a |= 10
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a |= 10
TypeError: unsupported operand type(s) for |=: 'frozenset' and 'int'
>>> a.update({10})
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.update({10})
AttributeError: 'frozenset' object has no attribute 'update'
>>> frozeset({frozenset({1, 2}) ,{frozenset({3, 4})}})
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    frozeset({frozenset({1, 2}) ,{frozenset({3, 4})}})
NameError: name 'frozeset' is not defined. Did you mean: 'frozenset'?
>>> frozenset({frozenset({1, 2}), frozenset({3, 4})})
frozenset({frozenset({3, 4}), frozenset({1, 2})})
