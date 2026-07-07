#Que. Swap the case of the string given(lower to upper,vise versa)
def swap_case(s):
    string=""
    for i in s:
        if i.islower():
            string=string+i.upper()
        else:
            string=string+i.lower()  
    return string
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)