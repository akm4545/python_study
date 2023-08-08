Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if x > 0:
...     if x < 20:
...         print('20보다 작은 양수입니다.')
... 
...         
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    if x > 0:
NameError: name 'x' is not defined
>>> 
>>> if x > 0 and x < 20:
...     print('20보다 작은 양수입니다.')
... 
...     
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    if x > 0 and x < 20:
NameError: name 'x' is not defined
>>> if 0 < x < 20:
...     print('20보다 작은 양수입니다.')
... 
...     
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    if 0 < x < 20:
NameError: name 'x' is not defined
