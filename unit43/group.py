Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m = re.match('([0-9]+) ([0-9]+)', '10 295')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    m = re.match('([0-9]+) ([0-9]+)', '10 295')
NameError: name 're' is not defined
>>> import re
>>> m = re.match('([0-9]+) ([0-9]+)', '10 295')
>>> m.group(1)
'10'
>>> m.group(2)
'295'
>>> m.group()
'10 295'
>>> m.group(0)
'10 295'
>>> m.groups()
('10', '295')
>>> m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
>>> m.group('func')
'print'
>>> m.group('arg')
'1234'
>>> re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')
['1', '2', '4', '7', '8']
>>> re.match('[a-z]+(.[a-z]+)*$', 'hello.world')
<re.Match object; span=(0, 11), match='hello.world'>
>>> re.match('[a-z]+(.[a-z]+)*$', 'hello.1234')
>>> re.match('[a-z]+(.[a-z]+)*$', 'hello')
<re.Match object; span=(0, 5), match='hello'>
