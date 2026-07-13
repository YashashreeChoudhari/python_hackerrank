#Que.The user enters a string and a substring. You have to print the number of times that the substring occurs.

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i : i + len(sub_string)] == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Slide a window equal to the length of sub_string across string.
# At each index, compare the sliced part (string[i:i+len(sub_string)])
# with sub_string. If they match, increment the count.
# This checks every position, including overlapping matches.