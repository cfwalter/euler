from random import choice, randint

num_squares = 40

def community_chest(n):
    cards = [n for i in range(16)]
    cards[0] = 0  # go
    cards[1] = 10  # jail
    return choice(cards)

def chance(n):
    cards = [n for i in range(16)]
    cards[0] = 0  # Advance to GO
    cards[1] = 10  # Go to JAIL
    cards[2] = 11  # Go to C1
    cards[3] = 24  # Go to E3
    cards[4] = 39  # Go to H2
    cards[5] = 5  # Go to R1
    cards[6] = {7:15, 22:25, 36:5}[n]  # Go to next R (railway company)
    cards[7] = {7:15, 22:25, 36:5}[n]  # Go to next R
    cards[8] = {7:12, 22:18, 36:12}[n]  # Go to next U (utility company)
    cards[9] = n-3  # Go back 3 squares.
    return choice(cards)

squares = [(lambda n: n) for i in range(num_squares)]
squares[2]  = (lambda n: community_chest(n))
squares[17] = (lambda n: community_chest(n))
squares[33] = (lambda n: community_chest(n))
squares[7]  = (lambda n: chance(n))
squares[22] = (lambda n: chance(n))
squares[36] = (lambda n: chance(n))
squares[30] = (lambda n: 10)  # go to jail

heat_map = [0 for i in range(num_squares)]
speed_trap = 0
d_size = 4
p = 0
for n in range(1000000):
    d1 = randint(1, d_size)
    d2 = randint(1, d_size)
    if d1 == d2:
        speed_trap += 1
    else:
        speed_trap = 0
    if speed_trap == 3:
        p = 10  # speeding, go to jail
    else:
        p = (p+d1+d2) % num_squares
        p = squares[p](p)
    heat_map[p] += 1

print([i[0] for i in reversed(sorted(enumerate(heat_map), key=lambda x:x[1]))][:3])
