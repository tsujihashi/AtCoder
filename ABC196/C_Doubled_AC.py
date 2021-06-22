N_str = input()
N = int(N_str)

ans = 0
if N >= 10:
    i = 1
    while True:
        x_str = str(i) + str(i)
        x = int(x_str)
        if x <= N:
            ans += 1
            i += 1
        else:
            break

print(ans)
https://atcoder.jp/contests/abc196/tasks/abc196_c