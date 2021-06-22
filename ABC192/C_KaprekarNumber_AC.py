# https://atcoder.jp/contests/abc192/tasks/abc192_c

N, K = list(map(int, input().split()))

for i in range(K):
    N_list = list(map(int, list(str(N))))
    # print(N_list)
    g1 = int(''.join(list(map(str, sorted(N_list)))))
    g2 = int(''.join(list(map(str, sorted(N_list, reverse=True)))))
    f = g2 - g1
    N = f
ans = N
print(ans)