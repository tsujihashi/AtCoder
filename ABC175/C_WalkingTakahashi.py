# https://atcoder.jp/contests/abc175/tasks/abc175_c

X, K, D = list(map(int, input().split()))

ans = 0
a = abs(X) // D
if K % 2 == 0:
    if a % 2 == 0:
        ans = abs(max(abs(X) % D, abs(X) - K * D))
    else:
        ans = abs(max(abs(X) % D - D, abs(X) - K * D))
else:
    if a % 2 == 0:
        ans = abs(max(abs(X) % D - D, abs(X) - K * D))
    else:
        ans = abs(max(abs(X) % D, abs(X) - K * D))

print(ans)