Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Person:
...     def greeting(self):
...         print('Hello')
... 
...         
>>> james = Persion()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    james = Persion()
NameError: name 'Persion' is not defined. Did you mean: 'Person'?
>>> james = Person()
>>> james.greeting()
Hello
