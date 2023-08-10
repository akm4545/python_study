Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

    
38
21
53
62
19
for i in [38, 21, 53, 62, 19]:
    print(i)

    
38
21
53
62
19
>>> a = [38, 21, 53, 62, 19]
>>> for index, value in enumerate(a):
...     print(index, value)
... 
...     
0 38
1 21
2 53
3 62
4 19
>>> for index, value in enumerate(a):
...     print(index + i, value)
... 
...     
19 38
20 21
21 53
22 62
23 19
>>> for index, value in enumerate(a, start = 1):
...     print(index, value)
... 
...     
1 38
2 21
3 53
4 62
5 19
>>> for i in range(len(a)):
...     print(a[i])
... 
...     
38
21
53
62
19
