import sys ; sys.stdin = open('input.txt')
from collections import deque

def Multi_BFS(Q):
    dr = [0, 1, 0, -1] #우하좌상
    dc = [1, 0, -1, 0]
    Max = 0
    cnt = 0
    while Q:
        r,c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0<= nc < M and mato[nr][nc] == -1:
                mato[nr][nc] = mato[r][c] + 1
                Q.append((nr,nc))
                if Max < mato[nr][nc]:
                    Max = mato[nr][nc]
    for lst in mato:
        cnt += lst.count(-1)
    if cnt != 0 : return -1
    else : return Max


# 2 <= M,N <= 1000
# M : 가로(열) , N : 세로(행)
M, N = map(int,input().split())
mato = [[-1]*M for _ in range(N)]

# 토마토 받아오기
Q = deque()
cnt = 0
for r in range(N):  # N 세로
    to = list(map(int,input().split()))
    for c in range(len(to)): # M 가로
        if to[c] == 1 : mato[r][c] = 0 ; Q.append((r,c))
        elif to[c] == -1 : mato[r][c] = -2
        elif to[c] == 0 : cnt += 1

if cnt == 0 : print(0) # 덜익은 토마토 없는경우
else : print(Multi_BFS(Q))
# 익토   1 : 0
# 덜익토 0 : -1
# 빈칸  -1 : -2

