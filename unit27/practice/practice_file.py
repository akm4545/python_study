with open('words.txt', 'r') as file:
    count = 0
    for line in file:
        if len(line.strip('\n')) <= 10:
            count += 1
    print(count)
