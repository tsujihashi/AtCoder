import random

def execute(N, Y):
    for x in range(0, N + 1):
        flg = False
        for y in range(0, N - x + 1):
            z = N - x - y
            total = 10000*x + 5000*y + 1000*z
            if total == Y:
                print('{0} {1} {2}'.format(x, y, z))
                flg = True
                break
        if flg:
            break

    if flg == False:
        print('-1 -1 -1')

if __name__ == '__main__':
    N, Y = [int(v) for v in input().split(' ')]
    #N = int(sN)
    #Y = int(sY)

    # 5y+9z=10N-Y/1000
    execute(N, Y)

