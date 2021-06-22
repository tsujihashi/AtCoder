# https://atcoder.jp/contests/abc191/tasks/abc191_c

H, W = list(map(int, input().split()))

S = []
for i in range(H):
    S.append(input())
# for i in range(H):
    # print(S[i])
vertexes = set()
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            judge_items = [
                [S[i-1][j] + S[i][j-1] + S[i-1][j-1], -0.5, -0.5],
                [S[i-1][j] + S[i][j+1] + S[i-1][j+1], -0.5, 0.5],
                [S[i+1][j] + S[i][j-1] + S[i+1][j-1], 0.5, -0.5],
                [S[i+1][j] + S[i][j+1] + S[i+1][j+1], 0.5, 0.5]
            ]
            vertex_patterns = ['##.', '...', '#.#', '.##', '..#']
            for item in judge_items:
                if item[0] in vertex_patterns:
                    vertexes.add(str(i+item[1]) + ',' + str(j+item[2]))

# print(vertexes)
ans = len(vertexes)
print(ans)