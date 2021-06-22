# https://atcoder.jp/contests/abc190/tasks/abc190_c

N, M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(2**K):
    ball_dishes = set()
    bin_i = format(i, '0{0}b'.format(K))
    for j in range(K):
        if bin_i[j] == '0':
            ball_dishes.add(CD[j][0])
        else:
            ball_dishes.add(CD[j][1])
    # print(ball_dishes)
    count = 0
    for cond in AB:
        if cond[0] in ball_dishes and cond[1] in ball_dishes:
            count += 1
    if count > ans:
        ans = count
print(ans)

# ※itertoolsが便利(https://docs.python.org/ja/3/library/itertools.html)
# product('ABCD', repeat=2): AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2): AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2): AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2): AA AB AC AD BB BC BD CC CD DD
