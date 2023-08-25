Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request
>>> response = urilib.request.urlopen('http://www.google.co.kr')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    response = urilib.request.urlopen('http://www.google.co.kr')
NameError: name 'urilib' is not defined. Did you mean: 'urllib'?
>>> response = urllib.request.urlopen('http://www.google.co.kr')
>>> response.status
200
>>> import urllib.request as r
>>> response = r.urlopen('http://www.google.co.kr')
>>> response.status
200
>>> from urllib.request import Request, urlopen
>>> req = Request('http://www.google.co.kr')
>>> response = urlopen(req)
>>> response.status
200
>>> from urllib.request import *
>>> req = Request('http://www.google.co.kr')
>>> response = urlopen(req)
respo
>>> nse.status
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    nse.status
NameError: name 'nse' is not defined
>>> response.status
200
>>> from urllib.request import Request as r, urlopen as u
>>> req = r('http://www.google.co.kr')
>>> response = u(req)
>>> response.status
200
