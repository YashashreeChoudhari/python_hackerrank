#Que. You are given a string and width. Your task is to wrap the string into a paragraph of width.
def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width):
        result += string[i:i+max_width] + "\n"
    return result.rstrip()


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)