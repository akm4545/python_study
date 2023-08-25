def type_check(a, b):
    def real_decorator(func):
        def wrapper(x, y):
            if isinstance(x, a) and isinstance(y, b):
                return func(x, y)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(10, 20))
print(add('hello', 'world'))
