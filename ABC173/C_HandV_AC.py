# https://atcoder.jp/contests/abc173/tasks/abc173_c



H, W, K = list(map(int, input().split()))
c = [list(input()) for _ in range(H)]
#print(c)

ans = 0
for i in range(2**H):
    for j in range(2**W):
        h_bin = format(i, '0{}b'.format(H))
        w_bin = format(j, '0{}b'.format(W))
        count = 0
        for y in range(H):
            for x in range(W):
                if c[y][x] == '#' and h_bin[y] != '1' and w_bin[x] != '1':
                     count += 1
        if count == K:
            ans += 1

print(ans)