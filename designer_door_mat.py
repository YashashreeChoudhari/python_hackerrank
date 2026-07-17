#Que.Design a new door mat with the following specifications:
    # Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
    # The design should have 'WELCOME' written in the center.
    # The design pattern should only use |, . and - characters.

N, M = map(int, input().split())

for i in range(N // 2):
    pattern = ""
    for j in range(2 * i + 1):
        pattern += ".|."
    print(pattern.center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N // 2 - 1, -1, -1):
    pattern = ""
    for j in range(2 * i + 1):
        pattern += ".|."
    print(pattern.center(M, "-"))