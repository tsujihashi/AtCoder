# https://atcoder.jp/contests/abc189/tasks/abc189_c

import numpy as np

N = int(input())
A = [*map(int, input().split())]

ans = 0
for l in range(N):
    x = A[l]
    for r in range(l, N):
        x = min(x, A[r])
        ans = max(ans, x*(r-l+1))
print(ans)
