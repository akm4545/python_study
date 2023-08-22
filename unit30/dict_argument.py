Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

    
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동
personal_info(*x)
이름:  name
나이:  age
주소:  address
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

        
personal_info(name = '홍길동')
name: 홍길동
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
name: 홍길동
age: 30
address: 서울시 용산구 이촌동
x = {'name': '홍길동'}
personal_info(x)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    personal_info(x)
TypeError: personal_info() takes 0 positional arguments but 1 was given
personal_info(**x)
name: 홍길동
y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**y)
name: 홍길동
age: 30
address: 서울시 용산구 이촌동
>>> def personal_info(**kwargs):
...     if 'name' in kwargs:
...         perint('이름: ', kwargs['name'])
...     if 'age' in kwargs:
...         perint('나이: ', kwargs['age'])
...     if 'address' in kwargs:
...         perint('주소: ', kwargs['address'])
... 
...         
>>> def personal_info(name, **kwargs):
...     print(name)
...     print(kwargs)
... 
...     
>>> personal_info('홍길동')
홍길동
{}
>>> personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
홍길동
{'age': 30, 'address': '서울시 용산구 이촌동'}
>>> personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
홍길동
{'age': 30, 'address': '서울시 용산구 이촌동'}
>>> def custom_price(*args, **kwargs):
...     print(*args, **kwargs)
... 
...     
>>> custom_print(1, 2, 3, sep=':', end='')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    custom_print(1, 2, 3, sep=':', end='')
NameError: name 'custom_print' is not defined. Did you mean: 'custom_price'?
>>> def custom_print(*args, **kwargs):
...     print(*args, **kwargs)
... 
...     
>>> custom_print(1, 2, 3, sep=':', end='')
1:2:3
