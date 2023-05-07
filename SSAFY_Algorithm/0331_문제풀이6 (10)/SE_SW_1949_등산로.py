import sys;sys.stdin=open('input.txt')
from collections import deque

def BFS():
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    cut = 0
    while Q:
        r,c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] < G[r][c]:
                Q.append((nr,nc))
            elif 0 <= nr < N and 0 <= nc < N and G[nr][nc] >= G[r][c] and cut == 0:
                cut = 1
                G[nr][nc]


Test = int(input())

for TC in range(Test):
    N, K = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(N)]
    Max = max([max(lst) for lst in G])

    Q = deque()
    for r in range(N):
        for c in range(N):
            if G[r][c] == Max:
                Q.append((r,c))
                BFS()
