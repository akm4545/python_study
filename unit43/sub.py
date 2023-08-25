Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.sub('apple|orange', 'fruit', 'apple box orange tree')
'fruit box fruit tree'
>>> re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')
'n n Fizz n Buzz Fizz n n'
>>> re.sub('[0-9]+', lambda m: str(int(m.group()) * 10), '1 2 Fizz 4 Buzz Fizz 7 8')
'10 20 Fizz 40 Buzz Fizz 70 80'
>>> re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234')
'1234 hello 1234 hello'
>>> re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }')
'<name>james</name>'
>>> re.sub('({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})', '<\\g<key>>\\g<value></\\g<key>>', '{ "name": "james" }')
'<name>james</name>'
>>> re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', r'<\2>\3</\2>', '{ "name": "james" }')
... '<name>james</name>'
SyntaxError: multiple statements found while compiling a single statement
