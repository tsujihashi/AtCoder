# https://atcoder.jp/contests/abc198/tasks/abc198_c

import math

R, X, Y = list(map(int, input().split()))

d = math.sqrt(X**2 + Y**2)
print(d)
ans = 0
if d == R:
    ans = 1
elif d < 2*R:
    ans = 2
else:
    ans = math.ceil(d / R)
print(ans)