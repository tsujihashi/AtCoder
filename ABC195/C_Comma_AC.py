# https://atcoder.jp/contests/abc195/tasks/abc195_c

N = int(input())

# 1,000~999,999(10^6-1):1 10^6-10^3個 4~6桁
# 1,000,000~999,999,999(10^9-1):2　10^9-10^6個　7~9桁
# Σ(10^(3(k+1))-10^(3k)) k=1~

ans = 0
lev_counts = [0, 0, 0, 0, 0, 1]
for i in range(5):
    lev_counts[i] = 10**(3*(i+1)) - 10**(3*i)
# print(lev_counts)
lev = int((len(str(N))-1)/3)
for l in range(lev):
    ans += l * lev_counts[l]
ans += lev * (N - 10**(3*(lev)) + 1)

print(ans)