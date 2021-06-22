N, K = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]
AB.sort()

res = K

for i in range(N):
    if AB[i][0] <= res:
        res += AB[i][1]
    else:
        break

print(res)
https://atcoder.jp/contests/abc203/tasks/abc203_c