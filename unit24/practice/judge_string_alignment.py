prices = map(int, input().split(';'))

prices = list(prices)
prices.sort(reverse=True)

for price in prices:
    print('%9s' % format(price, ','))
