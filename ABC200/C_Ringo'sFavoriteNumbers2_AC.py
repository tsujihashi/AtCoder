# https://atcoder.jp/contests/abc200/tasks/abc200_c

from collections import Counter
from scipy.special import comb

N = int(input())
A = list(map(int, input().split()))

mod = [i % 200 for i in A]
counts = Counter(mod)

ans = 0
for c in counts.values():
    ans += comb(c, 2, exact=True)
print(ans)
