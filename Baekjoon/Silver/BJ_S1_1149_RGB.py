# import sys;sys.stdin = open('input.txt')
# input = sys.stdin.readline
#
# def back(n,sm,color):
#     global Min
#     if Min <= sm : return
#     if n == N:
#         Min = min(Min,sm)
#         return
#     for i in range(3):
#         if color != i:
#             back(n + 1,sm + RGB[n][i],i)
#
# N = int(input())
# RGB = [list(map(int,input().split())) for _ in range(N)]
# Min = 0xfffffffffffff
# back(0,0,-1)
# print(Min)
#=======================================================
import sys;sys.stdin = open('input.txt')

N = int(input())
RGB = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*3 for _ in range(N)]
DP[0] = RGB[0]

for n in range(1,N):
    for i in range(3):
        if i == 0:
            DP[n][0] = min(DP[n-1][1]+RGB[n][0],DP[n-1][2]+RGB[n][0])
        elif i == 1:
            DP[n][1] = min(DP[n-1][0]+RGB[n][1],DP[n-1][2]+RGB[n][1])
        elif i == 2:
            DP[n][2] = min(DP[n-1][0]+RGB[n][2],DP[n-1][1]+RGB[n][2])
print(min(DP[N-1]))