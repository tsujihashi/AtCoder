'''
Pythonは低速なのでTLEになる。PyPIで提出することでAC(250ms<(1500ms))

https://qiita.com/u2dayo/items/edd462bf0d8b2f2df55f#c%E5%95%8F%E9%A1%8Cmandarin-orange
'''

N = int(input())
A = [*map(int, input().split())]

ans = 0
for l in range(N):
    m = 10 ** 6  # 適当な10 ** 5より大きい数で初期化します
    for r in range(l, N):
        d = r - l + 1  # 区間の幅
        m = min(m, A[r])  # 区間の最小を更新
        score = m * d  # 食べたみかん
        ans = max(ans, score)

print(ans)

# https://atcoder.jp/contests/abc189/tasks/abc189_c