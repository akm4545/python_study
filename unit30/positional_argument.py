Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

    
print_numbers(10, 20, 30)
10
20
30
x = [10, 20, 30]
print_numbers(*x)
10
20
30
print_numbers(*[10, 20, 30])
10
20
30
>>> def print_numbers(*args):
...     for arg in args:
...         print(arg)
... 
...         
>>> print_numbers(10)
10
>>> print_numbers(10, 20, 30, 40)
10
20
30
40
>>> x = [10]
>>> print_numbers(*x)
10
>>> y = [10, 20, 30, 40]
>>> print_numbers(*y)
10
20
30
40
>>> def print_numbers(a, *args)
SyntaxError: incomplete input
>>> def print_numbers(a, *args):
...     print(a)
...     print(args)
... 
...     
>>> print_numbers(1)
1
()
>>> print_numbers(1, 10, 20)
1
(10, 20)
>>> print_numbers(*[10, 20, 30])
10
(20, 30)
