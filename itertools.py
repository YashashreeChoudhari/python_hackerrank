#This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

if __name__ == '__main__':
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    from itertools import product
    C = list(product(A, B))
    C.sort()
    for x in C:
        print(x, end = ' ')
    print("\n")