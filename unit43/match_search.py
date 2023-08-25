Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.match('Hello', 'Hello, world!')
<re.Match object; span=(0, 5), match='Hello'>
>>> re.match('Python', 'Hello, world!')
>>> re.search('^Hello', 'Hello, world!')
<re.Match object; span=(0, 5), match='Hello'>
>>> re.search('world!$', 'Hello, world!')
<re.Match object; span=(7, 13), match='world!'>
>>> re.match('hello|world', 'hello')
<re.Match object; span=(0, 5), match='hello'>
