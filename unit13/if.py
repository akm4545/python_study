Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 10
if x == 10:
    print('10입니다.')

    
10입니다.
if x == 10:
print('10입니다.')
SyntaxError: expected an indented block after 'if' statement on line 1
if x = 10:
...     
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> if x == 10
SyntaxError: incomplete input
>>> x = 10
>>> if x == 10:
...     pass
... 
>>> if x == 10:
...     pass #TODO: x가 10일 때 처리가 필요
... 
...     
>>> x = 10
>>> if x == 10:
...     print('x에 들어있는 숫자는')
...         print('10입니다.')
...         
SyntaxError: unexpected indent
>>> if x == 10:
...     print('x에 들어있는 숫자는')
...     print('10입니다.')
... 
...     
x에 들어있는 숫자는
10입니다.
>>> if x == 10:
...     print('x에 들어있는 숫자는')
... print('10입니다.')
SyntaxError: invalid syntax
>>> if x == 10:
...     print('x에 들어있는 숫자는')
... print('10입니다.')
SyntaxError: invalid syntax
>>> print('10입니다.')
10입니다.
>>> if x == 10:
...     print('x에 들어있는 숫자는')
... print('10입니다.')
SyntaxError: invalid syntax
