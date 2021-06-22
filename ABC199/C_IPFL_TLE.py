# https://atcoder.jp/contests/abc199/tasks/abc199_c
import time
N = int(input())
S = input()
Q = int(input())
TAB = [list(map(int, input().split())) for i in range(Q)]
#print(TAB)

Sl = list(S)
#print(Sl)
flg = False
for i in range(Q):
    if TAB[i][0] == 1:
        if not flg:
            A = TAB[i][1]
            B = TAB[i][2]
        else:
            c = 1
            A = TAB[i][1]
            B = TAB[i][2]
            if A < N+1:
                A += N
            else:
                A -= N
            if B < N+1:
                B += N
            else:
                B -= N

        '''tmp_a = Sl[A-1]
        tmp_b = Sl[B-1]
        Sl[A-1] = tmp_b
        Sl[B-1] = tmp_a
        S = ''.join(Sl)'''
        A, B = min(A, B), max(A, B)
        S = ''.join(S[:A-1]).join(S[B-1]).join(S[A:B-1]).join(S[A-1]).join(S[B:])
    else:
        flg = not flg

if flg:
    S = S[N:] + S[:N]
print(S)