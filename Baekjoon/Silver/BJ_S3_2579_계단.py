
# input = sys.stdin.readline
#
# def back(n, Sum, cnt):
#     global Max
#     if cnt >= 3 : return
#     if n > N : return
#     if n == N:
#         Max = max(Max,Sum)
#         return
#     if DP[n] > Sum:return
#     DP[n] = Sum
#     back(n+1,Sum + lst[n+1],cnt + 1)
#     back(n+2,Sum + lst[n+2],1)
#
# N = int(input())
# lst = [0] + [int(input()) for _ in range(N)] + [0]
# DP = [0] * (N+1)
# Max = 0
# back(0,0,0)
# print(Max)

#=======================================
import sys;sys.stdin=open('input.txt')

N = int(input())
stair = [0] + [int(input()) for _ in range(N)]
DP = [0] * (N + 1)
DP[1] = stair[1]
cnt = 1

for i in range(2, N + 1):
    if max(DP[i-1] + stair[i], DP[i-2] + stair[i]) - stair[i] == DP[i-1] : cnt += 1
    else: cnt = 1

    if cnt == 3:
        DP[i] = DP[i-2] + stair[i]
        cnt = 1
    else:
        DP[i] = max(DP[i-1] + stair[i],DP[i-2] + stair[i])

    print(DP)
print(DP[-1])











