from itertools import product

alpha = list(range(ord('a'), ord('z')+1))

with open('p059_cipher.txt') as file:
    text = [int(n) for n in file.readline().split(',')]
    for pw in product(alpha, repeat=3):
        decode = ''.join([chr(n ^ pw[i%3]) for i, n in enumerate(text)])
        if decode.find('An ') > -1:
            print(decode)
            print(sum(ord(c) for c in decode))
