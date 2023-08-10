a, b = map(int, input().split())

list = [2 ** i for i in range(a, b + 1)]
list.pop(1)
list.pop(-2)

print(list)
