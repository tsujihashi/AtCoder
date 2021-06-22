N = int(input())
A = list(map(int, input().split()))


diff = [(min(A[i], A[N-1-i]), max(A[i], A[N-1-i])) for i in range(int(N/2)) if A[i] != A[N-1-i]]

# print(diff)

ans = 0
s1 = ''
s2 = ''
for d in diff:
    s1 += str(d[0])
    s2 += str(d[1])
for i in range(len(s1)):
    if s1[i] != s2[i]:
        ans += 1
        s2 = s2.replace(s2[i], s1[i])
print(ans)