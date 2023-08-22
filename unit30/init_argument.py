Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def personal_info(name, age, address='비공개'):
...     print('이름: ', name)
...     print('나이: ', age)
...     print('주소: ', address)
... 
...     
>>> personal_info('홍길동', 30)
이름:  홍길동
나이:  30
주소:  비공개
>>> personal_info('홍길동', 30, '서울시 용산구 이촌동')
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동
>>> def personal_info(name, address='비공개', age):
...     
SyntaxError: non-default argument follows default argument
