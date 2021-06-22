# https://atcoder.jp/contests/abc188/tasks/abc188_c

N = int(input())
A = [*map(int, input().split())]

rates = [(i, A[i]) for i in range(2**N)]

ans = 0
while len(rates) > 2:
    for i in range(int(len(rates)/2)):
        if rates[i][1] < rates[i+1][1]:
            del rates[i]
        else:
            del rates[i+1]

# print(rates)
ans = 0
r_min = 10**9
for i, r in rates:
    if r < r_min:
        r_min = r
        ans = i + 1

print(ans)