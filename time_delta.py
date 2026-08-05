#Que. Given two timestamps (including their time zones), compute and print the absolute difference between them in **seconds** for each test case.


from datetime import datetime

t = int(input())

format = "%a %d %b %Y %H:%M:%S %z"

for _ in range(t):
    t1 = datetime.strptime(input(), format)
    t2 = datetime.strptime(input(), format)
    print(int(abs((t1 - t2).total_seconds())))