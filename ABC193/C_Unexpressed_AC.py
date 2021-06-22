# https://atcoder.jp/contests/abc193/tasks/abc193_c

N = int(input())

# a^bで表せない数
# 1,2,3,2^2,5,6,7,2^3,3^2,10,11,12,13,14,15,2^4,17,18,19,20,21,22,23,24,5^2,26,3^3,28,29,30,
# 31,2^5,33,34,35,6^2,37,38,39,40,41,42,43,44,45,46,47,48,7^2,50,51,52,53,54,55,56,57,58,59,60
# 61,62,63,2^6

N_sq = int(N**0.5)
nums = set()
flg1 = False
for a in range(2, N_sq + 1):
    n = a * a
    while n <= N:
        nums.add(n)
        n *= a

ans = N - len(nums)
# print(nums)
print(ans)
