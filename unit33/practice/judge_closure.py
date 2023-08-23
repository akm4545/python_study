def countdown(n):
    count = n + 1
    def minus_count():
        nonlocal count
        count = count - 1
        return count
    return minus_count

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')
