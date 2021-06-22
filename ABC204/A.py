x, y = [int(v) for v in input().split(' ')]

res = 3 - x - y

if x==y:
    res = x
else:
    res = 3 - x - y

print(str(res))https://atcoder.jp/contests/abc204/tasks/abc204_a