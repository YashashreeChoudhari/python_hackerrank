#You are given an integer. Your task is to print an alphabet rangoli of size N in specified pattern.
def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * n - 3

    rows = []

    for i in range(n):
        row = []

        for j in range(n - 1, i, -1):
            row.append(alpha[j])

        for j in range(i, n):
            row.append(alpha[j])

        rows.append("-".join(row).center(width, "-"))

    print("\n".join(rows[::-1] + rows[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)