import sys;sys.stdin=open('input.txt')
from collections import deque

def BFS(cnt):
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    build = 1
    while Q:
        r,c = Q.popleft()
        G[r][c] = cnt
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == '1':
                build += 1
                G[nr][nc] = cnt
                Q.append((nr,nc))

    build_cnt.append(build)

N = int(input())
G = [list(input()) for _ in range(N)]

Q = deque()
build_cnt = []
cnt = 0
for r in range(N):
    for c in range(N):
        if G[r][c] == '1':
            Q.append((r,c))
            cnt += 1
            BFS(cnt)
print(cnt)
for i in sorted(build_cnt):
    print(i)
