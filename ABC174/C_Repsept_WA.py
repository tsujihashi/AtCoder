# https://atcoder.jp/contests/abc174/tasks/abc174_c

K = int(input())

a = [int('7'*(i+1)) % K for i in range(K)]
ans = -1
for i in range(K):
    if a[i] == 0:
        ans = i+1

print(ans)