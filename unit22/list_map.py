Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])

    
a
... [1, 2, 3, 4]
... a = [1.2, 2.5, 3.7, 4.6]
... a = list(map(int, a))
... a
... [1, 2, 3, 4]
SyntaxError: multiple statements found while compiling a single statement
>>> a = list(map(str, range(10)))
>>> a
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> a = input().split()
10 20
\
>>> a
['10', '20']
>>> a = map(int, input().split())
a
>>> a
<map object at 0x0000023DA26379A0>
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list(a)
ValueError: invalid literal for int() with base 10: 'a'
>>> a = map(int, input().split())
10 20
>>> list(a)
[10, 20]
>>> a, b = [10, 20]
>>> a
10
b
>>> 
>>> bn
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    bn
NameError: name 'bn' is not defined. Did you mean: 'b'?
>>> b
20
