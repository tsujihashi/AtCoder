# https://atcoder.jp/contests/abc202/tasks/abc202_c

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

#print('{0}\n{1}\n{2}'.format(A,B,C))

ans = 0

A.sort()

counts = [0]*N

for j in range(N):
    idx = C[j]-1
    val = B[idx]
    counts[val-1] += 1
for i in range(N):
    ans += counts[A[i]-1]

print(ans)