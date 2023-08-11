Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'Hello, world!'.replace('world', 'Python')
'Hello, Python!'
s = 'Hello, world!'
s = s.replace('world!', 'Python')
s
'Hello, Python'
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)
'1ppl2'
'apple pear grape pineapple orange'.split()
['apple', 'pear', 'grape', 'pineapple', 'orange']
'apple, pear, grape, pineapple, orange'.split(', ')
['apple', 'pear', 'grape', 'pineapple', 'orange']
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
'apple pear grape pineapple orange'
'0'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
'apple0pear0grape0pineapple0orange'
'python'.upper()
'PYTHON'
'PYTHON'.lower()
'python'
'   Python   '.lstrip()
'Python   '
'   Python   '.rstrip()
'   Python'
'   Python   '.strip()
'Python'
', python.'.strip(',.')
' python'
import string
', python.'.strip(string.punctuation)
' python'
sring.punctuation
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sring.punctuation
NameError: name 'sring' is not defined. Did you mean: 'string'?
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> ', python.'.strip(string.punctuation + ' ')
'python'
>>> ', python.'.strip(string.punctuation).strip()
'python'
>>> 'python'.ljust(10)
'python    '
>>> 'python'.rjust(10)
'    python'
>>> 'python'.center(10)
'  python  '
>>> 'python'.center(11)
'   python  '
>>> 'python'.rjust(10).upper()
'    PYTHON'
>>> '35'.zfill(4)
'0035'
>>> '3.5'.zfill(6)
'0003.5'
>>> 'hello'.zfill(10)
'00000hello'
>>> 'apple pineapple'.find('pl')
2
>>> 'apple pineapple'.find('xy')
-1
>>> 'apple pineapple'.rfind('pl')
12
>>> 'apple pineapple'.rfind('xy')
-1
>>> 'apple pineapple'.index('pl')
2
>>> 'apple pineapple'.rindex('pl')
12
>>> 'apple pineapple'.count('pl')
2
