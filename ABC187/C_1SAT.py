# https://atcoder.jp/contests/abc187/tasks/abc187_c

N = int(input())
S = [input() for _ in range(N)]

g1 = set()
g2 = set()

for i in range(N):
    if S[i][0] == '!':
        g2.add(S[i][1:])
    else:
        g1.add(S[i])

g3 = g1 & g2

# print(g3)

if len(g3) > 0:
    print(g3.pop())
else:
    print('satisfiable')