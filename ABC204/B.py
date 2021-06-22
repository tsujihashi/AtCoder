N = int(input())

A = [int(v) for v in input().split(' ')]

res = 0
for i in range(N):
    if A[i] > 10:
        res += (A[i] - 10)

print(str(res))https://atcoder.jp/contests/abc204/tasks/abc204_b