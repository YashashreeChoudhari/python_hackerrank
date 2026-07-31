#Que.Write a Python program to find the average of all distinct elements in an array using a set.
#The result should be rounded to 3 decimal places.


def average(arr):
    arr = set(arr)
    return sum(arr) / len(arr)
        
         
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)