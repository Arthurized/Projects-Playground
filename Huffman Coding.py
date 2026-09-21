def huffman():
    # freq[i] is the frequency of character i
    # left[i] and right[i] store the children of node i

    total = 2 * n - 1 # number of nodes in a final tree
    left, right, freq = [-1] * total, [-1] * total, [0] * total
    for i in range(n):
        freq[i] = int(char[i][1])

    for i in range(n, total):
        x = -1 # two smallest nodes
        y = -1
        for j in range(i):
            if j not in left[n:i] and j not in right[n:i]:
                if x == -1 or freq[j] < freq[x]:
                    y = x
                    x = j
                elif y == -1 or freq[j] < freq[y]:
                    y = j
        freq[i] = freq[x] + freq[y]
        left[i] = x
        right[i] = y

    print("Huffman code:")

    for i in range(n):
        node = i
        code = ""
        while node != total - 1:
            parent = -1
            for j in range(n, total):
                if left[j] == node or right[j] == node:
                    parent = j
                    break
            if left[parent] == node:
                code = "0" + code
            else:
                code = "1" + code
            node = parent
        print(char[i][0], code)


"""Data input:"""

n = int(input())  # number of characters
char = []
for i in range(n):
    char.append(input().split())  # character, frequency

huffman()
