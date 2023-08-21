Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {i for i in 'apple'}
>>> a
{'e', 'p', 'l', 'a'}
>>> a = {i for i in 'pineapple' if i not in 'apl'}
>>> a
{'e', 'n', 'i'}
