#Que. Given an array and two disjoint sets **A** (liked) and **B** (disliked), calculate your final happiness by adding **+1** for each array element in **A** and **−1** for each element in **B**, then print the total.

n, m = map(int, input().split())

arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)