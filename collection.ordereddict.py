#Que. You need to group the same item names together and add their prices.
# Print each item with its total price in the order it first appeared.

from collections import OrderedDict

n = int(input())
d = OrderedDict()

for i in range(n):
    data = input().split()
    price = int(data[-1])
    name = " ".join(data[:-1])

    if name in d:
        d[name] += price
    else:
        d[name] = price

for name in d:
    print(name, d[name])