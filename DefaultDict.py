#Given two groups of words A and B, print the 1-based positions of each word from Group B in Group A. If a word from Group B does not appear in Group A, print `-1`.

from collections import defaultdict
n, m = map(int, input().split())

d = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    d[word].append(str(i))

for _ in range(m):
    word = input()
    if word in d:
        print(" ".join(d[word]))
    else:
        print(-1)