from collections import defaultdict

prior_lists = defaultdict(list)
with open('p079_keylog.txt') as file:
    for l in file:
        if l[0] not in prior_lists:
            prior_lists[l[0]] = []
        prior_lists[l[1]].append(l[0])
        prior_lists[l[2]].append(l[1])

s = ''
while len(prior_lists) > 0:
    for key, val in prior_lists.items():
        if len(val) == 0:
            s += key
            prior_lists.pop(key)
            for k, v in prior_lists.items():
                prior_lists[k] = list(filter(lambda x: x!=key, v))
            break
