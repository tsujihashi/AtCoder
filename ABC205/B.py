N = int(input())
A = list(map(int, input().split()))

ans = 'Yes'

for i in range(N):
    if (i+1) not in A:
        ans = 'No'
        break

print(ans)https://atcoder.jp/contests/abc205/tasks/abc205_b