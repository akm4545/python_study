Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'I am %s.' % 'james'
'I am james.'
name = 'maria'
'I am %s.' % name
'I am maria.'
'I am %d years old.' % 20
'I am 20 years old.'
'%f' % 2.3
'2.300000'
'%.2f' % 2.3
'2.30'
'%.3f' % 2.3
'2.300'
'%10s' % 'python'
'    python'
'%10d' % 150
'       150'
'%10d' % 15000
'     15000'
'%10.2f' % 2.3
'      2.30'
'%10.2f' % 2000.3
'   2000.30'
'%-10s' % 'python'
'python    '
'Today is %d %s.' % (3, 'April')
'Today is 3 April.'
'Today is %d%s.' % (3, 'April')
'Today is 3April.'
'Hello, {0}'.format('world!')
'Hello, world!'
'Hello, {0}'.format(100)
'Hello, 100'
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'Hello, Python 3.6 Script'
'{0} {0} {1} {1}'.format('Python', 'Script')
'Python Python Script Script'
'Hello, {} {} {}'.format('Python', 'Script', 3.6)
'Hello, Python Script 3.6'
'Hello, {language} {version}'.format(language='Python', version=3.6)
'Hello, Python 3.6'
language = 'Python'
version = 3.6
f'Hello, {language} {version}'
'Hello, Python 3.6'
'{{ {0} }}'.format('Python')
'{ Python }'
'{0:<10}'.format('python')
'python    '
>>> '{0:>10}'.format('python')
'    python'
>>> '{:>10}'.format('python')
'    python'
>>> '%03d' % 1
'001'
>>> '{0:03d}'.format(35)
'035'
>>> '%08.2f' % 3.6
'00003.60'
>>> '{0:08.2f}'.format(150.37)
'00150.37'
>>> '{0:0<10}'.format(15)
'1500000000'
>>> '{0:0>10}'.format(15)
'0000000015'
>>> '{0:0>10.2f}'.format(15)
'0000015.00'
>>> '{0: >10}'.format(15)'
SyntaxError: incomplete input
>>> '{0: >10}'.format(15)
KeyboardInterrupt
>>> '{0: >10}'.format(15)
'        15'
>>> '{0:>10}'.format(15)
'        15'
>>> '{0:x>10}'.format(15)
'xxxxxxxx15'
>>> format(1493500, ',')
'1,493,500'
>>> '%20s' % format(1493500, ',')
'           1,493,500'
>>> '{0:,}'.format(1493500)
'1,493,500'
>>> '{0:>20,}'.format(1493500)
'           1,493,500'
>>> '{0:0>20,}'.format(1493500)
'000000000001,493,500'
