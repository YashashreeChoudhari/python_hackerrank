#Que.Shop has x number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money  earned.

n=int(input())
shoes=list(map(int, input().split()))

customers=int(input())
total=0

for i in range(customers):
    size, price = map(int, input().split())

    if size in shoes:
        total += price
        shoes.remove(size)

print(total)