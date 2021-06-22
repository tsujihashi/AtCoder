#C
import random as r
c = ['o', 'x', '?']
for i in range(100):
    S = ''.join([r.choice(c) for j in range(10)])