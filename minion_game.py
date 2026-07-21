#Que.Both players are given the same string,S. Both players have to make substrings using the letters of the string S. Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.The game ends when both players have made all possible substrings.

def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)