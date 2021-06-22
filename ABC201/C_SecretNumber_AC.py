# https://atcoder.jp/contests/abc201/tasks/abc201_c

S = input()
_S = S
ans = 0
for i in range(10000):
    num = str(i).zfill(4)
    no_x = True
    for j in range(4):
        if S[int(num[j])] == 'x':
            no_x = False
        S = S[:int(num[j])] + '-' + S[(int(num[j])+1):]
    no_o = ('o' not in S)
    if no_x and no_o:
        ans += 1
    S = _S
print(ans)




#S[num[j]]がxではない
#S except S[num[j]]がoではない


