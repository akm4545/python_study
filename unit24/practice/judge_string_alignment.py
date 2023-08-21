prices = map(int, input.split(';'))

prices = list(map)
prices.sort(reverse=True)

for price in prices:
    '%9s' % format(price, ',')
