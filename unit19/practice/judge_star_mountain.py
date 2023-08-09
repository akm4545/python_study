star = int(input())

for i in range(star):
    for j in range(star + i):
        if j < star - i - 1:
            print(' ', end='') 
        else:
            print('*', end='')
    print()
