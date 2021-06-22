import itertools

seq = ('a', 'b', 'c', 'd', 'e')

#階乗
ptr = list(itertools.permutations(seq)) #組み合わせ列挙 5!

'''実行結果
[('a', 'b', 'c', 'd', 'e'),
 ('a', 'b', 'c', 'e', 'd'),
 ('a', 'b', 'd', 'c', 'e'),
 ('a', 'b', 'd', 'e', 'c'),
           中略
 ('e', 'd', 'c', 'a', 'b'),
 ('e', 'd', 'c', 'b', 'a')]
 '''

ptr_num = len(list(itertools.permutations(seq))) #組み合わせ数

'''実行結果
    120
'''

#順列
ptr = list(itertools.permutations(seq, 3)) #順列列挙 5P3

'''実行結果
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'b'),
       中略
 ('e', 'd', 'a'),
 ('e', 'd', 'b'),
 ('e', 'd', 'c')]
'''

ptr_num = len(list(itertools.permutations(seq, 3))) #順列数

'''実行結果
    60
'''

#組み合わせ
ptr = list(itertools.combinations(seq,3)) # 組み合わせ列挙 5C3

'''実行結果
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'd'),
 ('a', 'c', 'e'),
 ('a', 'd', 'e'),
 ('b', 'c', 'd'),
 ('b', 'c', 'e'),
 ('b', 'd', 'e'),
 ('c', 'd', 'e')]
 '''

#数え上げ
from collections import Counter
arr = [1,1,4,6,1,1,35,1,5,1,3]
d = Counter() #インスタンスを生成
d.update(arr)
print(d[1]) #d[数えたい値]

'''実行結果
6
'''