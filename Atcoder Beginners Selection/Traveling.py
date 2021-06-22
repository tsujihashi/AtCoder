N = int(input())

t = []
x = []
y = []
for i in range(N):
    ti, xi, yi = [int(v) for v in input().split(' ')]
    t.append(ti)
    x.append(xi)
    y.append(yi)

for i in range(1, N+1):
    if i > 1:
        for j in range(t[i-1], t[i] + 1):
            pass
    #print('{0} {1} {2}'.format(ti, xi, yi))
