Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hello = 'Hello, world!'
>>> hello
'Hello, world!'
>>> hello = '안녕하세요'
>>> hello
'안녕하세요'
>>> hello = "Hello, world!"
>>> hello
'Hello, world!'
>>> hello = '''Hello, Python!'''
>>> hello
'Hello, Python!'
>>> python = """Python Programming"""
>>> python
'Python Programming'
>>> hello = '''Hello, world!
... 안녕하세요.
... Python입니다.'''
>>> print(hello)
Hello, world!
안녕하세요.
Python입니다.
>>> s = "Python isn't difficult"
>>> s
"Python isn't difficult"
>>> s = 'He said "Python is easy"'
>>> s
'He said "Python is easy"'
>>> s = 'Python isn't difficult'
SyntaxError: unterminated string literal (detected at line 1)
>>> s = "He said "Python is easy""
SyntaxError: invalid syntax
