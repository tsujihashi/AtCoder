A, B, C = list(map(int, input().split()))

# Cが奇数→A<0 偶数→A>0

# > の条件：abs(A)>abs(b)&&
ans = ''
if C%2 == 0:
    if abs(A) > abs(B):
        ans = '>'
    elif abs(A) == abs(B):
        ans = '='
    else:
        ans = '<'
else:
    if A >= 0 and B >= 0:
        if A > B:
            ans = '>'
        elif A == B:
            ans = '='
        else:
            ans = '<'
    elif A >= 0 and B < 0:
        ans = '>'
    elif A < 0 and B >= 0:
        ans = '<'
    else:
        if A > B:
            ans = '>'
        elif A == B:
            ans = '='
        else:
            ans = '<'
print(ans)

https://atcoder.jp/contests/abc205/tasks/abc205_c