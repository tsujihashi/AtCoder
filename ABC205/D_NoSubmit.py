# https://atcoder.jp/contests/abc205/tasks/abc205_d

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]

values = {}
'''for i in range(Q):
    count = K[i]
    _count = count
    if _count not in values.keys():
        for j in A:
            if A[j] <= _count:
                count -= 1
            else:
                break
        values[_count] = count
    print(count)
'''


for i in range(Q):

    Ki = K[i]
    ans = Ki
    if Ki in values.keys():
        ans = values[Ki]
    else:
        extra = 0
        for a in A:
            if a < Ki:
                extra += 1
    print(ans)
