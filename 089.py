def roman_diff(s):
    sub_dict = {
        'DCCCC': 'CM',
        'CCCC': 'CD',
        'LXXXX': 'XC',
        'XXXX': 'XL',
        'VIIII': 'IX',
        'IIII': 'IV',
    }
    original = len(s)
    for key, val in sub_dict.items():
        s = s.replace(key, val)
    return original - len(s)

total_diff = 0
with open('p089_roman.txt') as file:
    for l in file:
        total_diff += roman_diff(l)
