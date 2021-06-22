# https://atcoder.jp/contests/abc176/tasks/abc176_c

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    if A[i-1] > A[i]:
        base = A[i-1] - A[i]
        A[i] += base
        ans += base
print(ans)