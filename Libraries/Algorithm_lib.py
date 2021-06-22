#多次元配列のソート
A = [[1, 2], [3, 1], [2, 5]]
B = sorted(A, key=lambda x: x[0]) # 0番目の要素でソート
C = sorted(A, key=lambda x: x[1]) # 1番目の要素でソート

'''実行結果
B = [[1, 2], [2, 5], [3, 1]]
C = [[3, 1], [1, 2], [2, 5]]
'''

'''---------------------------------------------------------------------'''

#二分探索
import bisect
A = []
x = 0
#ソートされたリストAにソートを崩さずに値xを挿入するとき、xの入るべきインデックスを返す。
bisect.bisect(A,x)

#リストAに値xを入れ、xが複数になるとき、一番左の値xのインデックスを返す
bisect.bisect_left(A,x)

#リストAに値xを入れ、xが複数になるとき、一番右の値xのインデックスを返す
bisect.bisect_right(A,x)

'''---------------------------------------------------------------------'''

#Union-Find-木
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)


'''---------------------------------------------------------------------'''

#クラスカル法にはunion-find木が必要

#クラスカル法
# V: 頂点集合(リスト) E: 辺集合[始点, 終点, 重み](リスト)
V=[]
E=[]
class kruskal():
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.E.sort(key=lambda x: x[2]) #辺の重みでソート

    def weight(self): #最小全域木の重み和を求める
        UF = UnionFind(len(V)) #頂点数でUnion Find Treeを初期化
        res = 0
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res += e[2]

        return res

    def edge(self):
        UF = UnionFind(len(self.V)) #頂点数でUnion Find Treeを初期化
        res_E = []
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_E.append(e)

        return res_E

    def node(self):
        UF = UnionFind(len(V)) #頂点数でUnion Find Treeを初期化
        res_V = []
        for i in range(len(E)):
            e = E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_V.append(e[0])
                res_V.append(e[1])

        return list(set(res_V))


'''---------------------------------------------------------------------'''

#ワ―シャルフロイド法
#d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
def warshall_floyd(d, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d #d[i][j]に頂点i, j間の最短距離を格納