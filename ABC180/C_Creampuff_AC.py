# https://atcoder.jp/contests/abc180/tasks/abc180_c

#nの約数を全て求める
def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

N = int(input())

divs = sorted(divisor(N))
for d in divs:
    print(d)

