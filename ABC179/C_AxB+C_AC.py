# https://atcoder.jp/contests/abc179/tasks/abc179_c

N = int(input())

ans = 0
for i in range(1, N):
    num = int((N-1)/i)
    ans += int(num)
print(ans)