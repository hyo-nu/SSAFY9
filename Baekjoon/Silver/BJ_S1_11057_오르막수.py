# N = int(input())
# DP = [[0]*10 for _ in range(N + 1)]
# DP[1] = [1] * 10
#
# for i in range(2, N + 1):
#     for j in range(10):
#         DP[i][j] = sum(DP[i-1][j:])
#
# print(sum(DP[N]) % 10007)

#======================================
N = int(input())
DP = [1] * 10

for i in range(1,N):
    for j in range(10):
        DP[j] = sum(DP[j:])

print(sum(DP))