import sys;sys.stdin = open('input.txt')
# N,K = map(int,input().split())
# DP = [[0,[]] for _ in range(K+1)]
# WV_lst =[]
#
# for i in range(N):
#     W,V = map(int,input().split())
#     WV_lst.append((W, V))
#     if W <= K and DP[W][0] < V:
#         DP[W][0] = V
#         if DP[W][1]:
#             DP[W][1] = [i]
#         else:
#             DP[W][1].append(i)
# print(WV_lst)
# for j in range(len(DP)):
#     for idx, WV in enumerate(WV_lst):
#         w, v = WV[0], WV[1]
#         if DP[j][0] != 0 and j + w <= K and idx not in DP[j][1]:
#             if DP[j+w][0] < DP[j][0] + v:
#                 DP[j+w][0] = DP[j][0] + v
#                 DP[j+w][1] = DP[j][1]+[idx]
#                 print(f'idx : {idx} =>',DP)
# print(max(DP,key = lambda x : x[0])[0])
# print(DP)
# =========================

N, K = map(int, input().split())
weights = [list(map(int, input().split())) for i in range(N)]
dp = [0] * (K + 1)
print(weights)
for W, V in weights:
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)
        print(f'W:{W} , i:{i}=>',dp)

print(dp[-1])









