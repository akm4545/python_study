files = input().split()

print(list(map(lambda file: '{0:03d}.{1}'.format(int(file.split('.')[0]), file.split('.')[1]), files)))
