from math import log

highest = 0
line_num = 1
with open('p099_base_exp.txt', 'r') as f:
    lines = f.readlines()
    for n, l in enumerate(lines, start=1):
        x, y = l.split(',')
        if int(y)*log(int(x)) > highest:
            line_num = n
            highest = int(y)*log(int(x))

print(line_num)
