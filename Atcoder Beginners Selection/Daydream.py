#文字列を反転し、後ろから探索してみる

def execute(S):
    while "dreameraser" in S:
        S = S.replace("dreameraser", "")
    while "dreamerase" in S:
        S = S.replace("dreamerase", "")
    while "eraser" in S:
        S = S.replace("dreamerase", "")
    while "dreamerase" in S:
        S = S.replace("dreamerase", "")
    while "dreamerase" in S:
        S = S.replace("dreamerase", "")
    S = S.replace("dreamer", "")\
        .replace("eraser", "")\
        .replace("dream", "")\
        .replace("erase", "")
    #print(S)
    res = ''
    if S == '':
        res = 'YES'
    else:
        res = 'NO'
    print(res)
    return res

if __name__ == '__main__':
    S = input()
    execute(S)