def file_read():
    with open('words.txt') as file:
        for i in file:
            yield i.strip('\n')


for i in file_read():
    print(i)
