paragraph = input().split()

count = 0

for word in paragraph:
    if word.strip(',.') == 'the':
        count += 1
    

print(count)
