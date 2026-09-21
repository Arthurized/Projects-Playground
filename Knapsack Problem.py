def backpack():
    """Given a set of items, each with a weight and a value,
     determine which items to include in the collection so that
      the total weight is less than or equal to a given limit
       and the total value is as large as possible."""
    a = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(w + 1):
            if char[i][0] > j:
                a[i][j] = a[i - 1][j]
            else:
                a[i][j] = max(a[i - 1][j], a[i - 1][j - char[i][0]] + char[i][1])

    print(f'The greatest possible value is {a[n][w]}')


def infinite_backpack():
    """Allow item repetition."""
    a = [0] * (w + 1)
    for i in range(1, n + 1):
        for j in range(char[i][0], w + 1):
            a[j] = max(a[j], a[j - char[i][0]] + char[i][1])
    print(f'The greatest possible value is {a[w]}')


"""Data input:"""

n = int(input())  # number of items
char = [0]
for i in range(n):
    char.append(list(map(int, input().split())))  # first item's mass, then the value
w = int(input())  # mass limit

backpack(), infinite_backpack()
