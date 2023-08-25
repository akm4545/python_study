Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
re.match('[0-9]*', '1234')
<re.Match object; span=(0, 4), match='1234'>
re.match('[0-9]+', '1234')
<re.Match object; span=(0, 4), match='1234'>
re.match('[0-9]+', 'abcd')
re.match('a*b', 'b')
<re.Match object; span=(0, 1), match='b'>
re.match('a+b', 'b')
re.match('a*b', 'aab')
<re.Match object; span=(0, 3), match='aab'>
re.match('a+b', 'aab')
<re.Match object; span=(0, 3), match='aab'>
re.match('abc?d', 'abd')
<re.Match object; span=(0, 3), match='abd'>
re.match('ab[0-9]?c', 'ab3c')
<re.Match object; span=(0, 4), match='ab3c'>
re.match('ab.d', 'abxd')
<re.Match object; span=(0, 4), match='abxd'>
re.match('h{3}', 'hhhello')
<re.Match object; span=(0, 3), match='hhh'>
re.match('(hello){3}', 'hellohellohelloworld')
<re.Match object; span=(0, 15), match='hellohellohello'>
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000')
<re.Match object; span=(0, 13), match='010-1000-1000'>
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100')
re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000')
<re.Match object; span=(0, 11), match='02-100-1000'>
>>> re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000')
>>> re.match('[a-zA-Z0-9]+', 'Hello1234')
<re.Match object; span=(0, 9), match='Hello1234'>
>>> re.match('[A-Z0-9]+', 'hello')
>>> re.match('[가-힣]+', '홍길동')
<re.Match object; span=(0, 3), match='홍길동'>
>>> re.match('[^A-Z]+', 'Hello')
>>> re.match('[^A-Z]+', 'hello')
<re.Match object; span=(0, 5), match='hello'>
>>> re.search('^[A-Z]+', 'Hello')
<re.Match object; span=(0, 1), match='H'>
>>> re.search('[0-9]+$', 'Hello1234')
<re.Match object; span=(5, 9), match='1234'>
>>> re.search('\*+', '1 ** 2')
<re.Match object; span=(2, 4), match='**'>
>>> re.match('[$()a-zA-Z0-9]+', '$(document)')
<re.Match object; span=(0, 11), match='$(document)'>
>>> re.match('\d+', '1234')
<re.Match object; span=(0, 4), match='1234'>
>>> re.match('\D+', 'Hello')
<re.Match object; span=(0, 5), match='Hello'>
>>> re.match('\w+', 'Hello_1234')
<re.Match object; span=(0, 10), match='Hello_1234'>
>>> re.match('\W+', '(:)')
<re.Match object; span=(0, 3), match='(:)'>
>>> e.match('[a-zA-Z0-9 ]+', 'Hello 1234')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    e.match('[a-zA-Z0-9 ]+', 'Hello 1234')
NameError: name 'e' is not defined. Did you mean: 're'?
>>> re.match('[a-zA-Z0-9 ]+', 'Hello 1234')
<re.Match object; span=(0, 10), match='Hello 1234'>
>>> re.match('[a-zA-Z0-9\s]+', 'Hello 1234')
<re.Match object; span=(0, 10), match='Hello 1234'>
>>> p = re.compile('[0-9]+')
>>> p.match('1234')
<re.Match object; span=(0, 4), match='1234'>
>>> p.search('hello')
