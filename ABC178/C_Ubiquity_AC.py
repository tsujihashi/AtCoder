# https://atcoder.jp/contests/abc178/tasks/abc178_c

N = int(input())

all = 10**N
no_0_9 = 8**N
no_0 = 9**N
no_9 = 9**N
ans = (all - (no_9 + no_0 - no_0_9))%(1000000000+7)
print(ans)