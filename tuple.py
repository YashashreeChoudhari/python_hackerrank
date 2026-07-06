#Que. Create a tuple with the given integer inputs and print the hash value of the tuple.
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int,input().split())

    t=tuple(integer_list)
    print(hash(t))