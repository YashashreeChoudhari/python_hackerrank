result = []

for k in range(int(input())):
    name = input()
    score = float(input())
    result.append([name, score])

lowest = result[0][1]
second = None

for i in result:
    if i[1] < lowest:
        lowest = i[1]

for i in result:
    if i[1] != lowest:
        if second is None or i[1] < second:
            second = i[1]

names = []
for i in result:
    if i[1] == second:
        names.append(i[0])

names.sort()
for name in names:
    print(name)