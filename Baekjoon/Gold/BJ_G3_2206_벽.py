# 0 : 이동가능
# 1 : 이동불가
import sys;sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

def BFS():
    vi = [[0] * M for _ in range(N)]
    vi[0][0] = 1
    while Q:
        r,c  = Q.popleft()
        for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
            nr,nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and wall[nr][nc] == '0' and  vi[nr][nc] == 0:
                vi[nr][nc] = vi[r][c] + 1
                Q.append((nr,nc))

    if vi[N-1][M-1]:
        return vi[N-1][M-1]
    else : return 0xffffffff


N, M = map(int,input().split())
wall = [list(input()) for _ in range(N)]
Q = deque()
INF = 0xffffffff
Min = INF
change = 0

for r in range(N):
    for c in range(M):
        Q.append((0, 0))
        if r == 0 and c == 0:
            Min = min(Min,BFS())
        else:
            if wall[r][c] == '1':
                wall[r][c] = '0'
                change = 1
                Min = min(Min,BFS())
            if change :
                wall[r][c] = '1'
                change = 0

if Min == INF:print (-1)
else : print(Min)