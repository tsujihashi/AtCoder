# https://atcoder.jp/contests/abc177/tasks/abc177_c

N = int(input())
A = list(map(int, input().split()))
ans = 0
sum = sum(A)
for i in range(1, N):
    sum -= A[i]
    ans += A[i]*sum
ans = ans % (1000000000+7)
print(ans)