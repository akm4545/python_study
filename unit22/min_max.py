Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [38, 21, 53, 62, 19]
>>> smallest = a[0]
>>> for i in a:
...     if i < smallest:
...         smallest = i
... 
...         
>>> smallest
19
>>> 
>>> a = [38, 21, 53, 62, 19]
>>> largest = a[0]
>>> for i in a:
...     if i > largest:
...         largest = i
... 
...         
>>> largest
62
>>> 
>>> a = [38, 21, 53, 62, 19]
>>> a.sort()
>>> a[0]
19
>>> a.sort(reverse = True)
>>> a[0]
62
>>> min(a)
19
>>> max(a)
62
