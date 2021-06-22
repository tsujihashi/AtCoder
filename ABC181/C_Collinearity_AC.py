# https://atcoder.jp/contests/abc181/tasks/abc181_c
from collections import Counter
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 'No'
lines = []
for i in range(N - 1):
    for j in range(i + 1, N):
        # 2点ごとに直線の傾きと切片を求める
        a = (XY[j][1]-XY[i][1])/(XY[j][0]-XY[i][0]) if XY[j][0]-XY[i][0] != 0 else 10**10
        b = XY[i][1] - a * XY[i][0] if XY[j][0]-XY[i][0] != 0 else XY[i][0]

        lines.append((a, b))

counter = Counter(lines)
# print(counter)
for k, v in counter.items():
    if v >= 2:
        ans = 'Yes'
        break
print(ans)