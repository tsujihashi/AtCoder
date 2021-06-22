# https://atcoder.jp/contests/abc194/tasks/abc194_c

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

counts = Counter(A)
counts = sorted(counts.items(), key=lambda x: x[0])
# print(counts)

ans = 0
for k1, v1 in counts:
    for k2, v2 in counts:
        if k2 > k1:
            ans += v1*v2*(k2 - k1)**2

print(ans)

