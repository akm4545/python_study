def find(word):
    result = False
    while True:
        string = (yield result)
        result = word in string

f = find('Python')
next(f)

print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python script'))

f.close()
