# https://atcoder.jp/contests/abc182/tasks/abc182_c
from collections import Counter
N_str = input()
N = int(N_str)
k = len(N_str)
modes = Counter([int(N_str[i]) % 3 for i in range(k)])
# print(modes)
ans = 0
if N%3 == 0:
    pass
elif N%3 == 1:
    if 1 in modes.keys() and k > 1:
        ans = 1
    elif 2 in modes.keys() and modes[2] >= 2 and k > 2:
        ans = 2
    else:
        ans = -1
elif N%3 == 2:
    if 2 in modes.keys() and k > 1:
        ans = 1
    elif 1 in modes.keys() and modes[1] >= 2 and k > 2:
        ans = 2
    else:
        ans = -1
print(ans)
