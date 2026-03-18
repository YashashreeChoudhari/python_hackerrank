#Q. List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list=[]

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            newlist=[i,j,k]
            if i+j+k!=n:
                list.append(newlist)
print(list)

#Q.Find runner up
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sortedinglist = sorted(list(set(arr)))
print(sortedinglist[-2])