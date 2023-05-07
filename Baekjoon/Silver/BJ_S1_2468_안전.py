import sys;sys.stdin=open('input.txt')
from collections import deque

def BFS():
    while Q:
        r,c = Q.popleft()
        vi[r][c] = 1
        for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not vi[nr][nc] and G[nr][nc] > rain:
                vi[nr][nc] = 1
                Q.append((nr,nc))

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
Max = max([max(lst) for lst in G])
Q = deque()
best_safe = 0
for rain in range(Max-1,-1,-1):
    safe = 0
    vi = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if G[r][c] > rain and not vi[r][c]:
                Q.append((r,c))
                BFS()
                safe += 1
    best_safe = max(best_safe,safe)
print(best_safe)
