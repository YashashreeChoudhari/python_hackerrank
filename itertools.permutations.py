#Que.You are given a string .
#Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

from itertools import permutations

s, k = input().split()

for p in permutations(sorted(s), int(k)):
    print(''.join(p))