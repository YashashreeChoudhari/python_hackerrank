#Que.Given a string s and an integer k (where len(s) is a multiple of k):
# Split s into equal substrings of length k.
# For each substring, remove duplicate characters while keeping only their first occurrence and preserving the original order.
# Print each processed substring on a new line.

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        seen = set()
        result = ""

        for char in substring:
            if char not in seen:
                seen.add(char)
                result += char

        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)