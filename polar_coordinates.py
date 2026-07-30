#Que. You are given a complex . Your task is to convert it to polar coordinates using cmath

import cmath

n = complex(input())

print(abs(n))
print(cmath.phase(n))