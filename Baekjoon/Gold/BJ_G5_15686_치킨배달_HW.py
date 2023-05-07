from collections import deque
from itertools import combinations
def BFS(lst,EP):
    dr = [0, 1, 0,-1]#우하좌상
    dc = [1, 0,-1, 0]
    vi = [[-1]*N for _ in range(N)]
    Q = deque()
    for r,c in lst:
        Q.append((r,c))
        vi[r][c] = 0

    while Q:
        r,c = Q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and vi[nr][nc] == -1:
                vi[nr][nc] = vi[r][c] + 1
                Q.append((nr,nc))
    result = 0
    for r,c in EP:
        result += vi[r][c]
    return result

N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
EP = []
tmp = []
for r in range(N):
    for c in range(N):
        if G[r][c] == 1:
            EP.append((r,c))
        if G[r][c] == 2:
            tmp.append((r,c))
Min = []
SP = combinations(tmp,M)
for lst in SP:
    Min.append(BFS(lst,EP))
Min.sort()
print(Min[0])
