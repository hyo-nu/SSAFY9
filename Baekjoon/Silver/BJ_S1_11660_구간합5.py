import sys;sys.stdin=open('input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())
G = [[0]*(N + 1)]+[[0] + list(map(int,input().split())) for _ in range(N)]
point = [list(map(int,input().split())) for _ in range(M)]

for i in range(1,N+1):
    for j in range(1,N+1):
        G[i][j] += G[i][j-1]+G[i-1][j]-G[i-1][j-1]

for x1,y1,x2,y2 in point:
    result = G[x2][y2] - G[x1-1][y2] - G[x2][y1-1] + G[x1-1][y1-1]
    print(result)
