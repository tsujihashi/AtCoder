# https://atcoder.jp/contests/abc206/tasks/abc206_a

N = int(input())
if int(N * 1.08) < 206:
    print('Yay!')
elif int(N * 1.08) == 206:
    print('so-so')
else:
    print(':(')