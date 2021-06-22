# https://atcoder.jp/contests/abc206/tasks/abc206_b

N = int(input())
m=0
ans=0
while m<N:
    ans += 1
    m+=ans
print(ans)