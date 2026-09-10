def encode(array):
    """Encodes the list of words into a string"""
    ans = ''
    for i in array:
        ans += str(len(i)) + '@' + i
    return ans


def decode(string):
    """Decodes an encoded string into the initial list of words..."""
    res, j = [], 0
    while j < len(string):
        i = j
        while string[j] != '@':
            j += 1
        k = int(string[i:j])
        res.append(string[j + 1: j + 1 + k])
        j = j + 1 + k
    return res


a = ['Write', 'your', 'list', 'here', ',', 'please', '...']
print(f'Your word list: {a}.', encode.__doc__, encode(a), decode.__doc__, decode(encode(a)),
      f'Verifying correctness: {decode(encode(a)) == a}!', sep='\n\n')
