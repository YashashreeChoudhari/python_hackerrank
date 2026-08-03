#Que. Given T test cases, each containing two values a and b, perform integer division a // b. If a ZeroDivisionError or ValueError occurs, print Error Code: followed by the exception message.


t = int(input())

for _ in range(t):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
