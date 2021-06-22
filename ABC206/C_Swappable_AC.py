from collections import Counter
import itertools

N = int(input())

A = list(map(int, input().split()))

# 組み合わせ
ans = int(N*(N-1)/2)
counter = Counter(A)
for k, v in counter.items():
    if v > 1:
        ans -= int(v*(v-1)/2)
print(ans)