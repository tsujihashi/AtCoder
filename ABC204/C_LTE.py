N, M = map(int, input().split())

A = [0]*M #出発地
B = [0]*M #目的地
next_city_counts = []
next_cities = [[] for i in range(N)]


for i in range(N):
    next_cities[i].append(i+1)

for i in range(M):
    A[i], B[i] = [int(v) for v in input().split(' ')]
    for j in range(N):
        for k in range(len(next_cities[B[i]-1])):
            if (A[i] in next_cities[j]) and (next_cities[B[i]-1][k] not in next_cities[j]):
                next_cities[j].append(next_cities[B[i]-1][k])
            #print(next_cities)

res = 0
for i in range(N):
    res += len(next_cities[i])


print(res)
https://atcoder.jp/contests/abc204/tasks/abc204_c