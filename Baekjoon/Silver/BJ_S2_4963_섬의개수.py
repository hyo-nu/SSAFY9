import sys;sys.stdin=open('input.txt')
from collections import deque

def BFS(cnt):
    dr = [-1,0,1,1,1,0,-1,-1]
    dc = [1,1,1,0,-1,-1,-1,0]

    while Q:
        r,c = Q.popleft()
        G[r][c] = cnt
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < h and 0 <= nc < w and G[nr][nc] == 1:
                Q.append((nr,nc))
                G[nr][nc] = cnt


while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0 : break
    G = [list(map(int,input().split())) for _ in range(h)]
    Q = deque()

    cnt = 1
    for r in range(h):
        for c in range(w):
            if G[r][c] == 1:
                cnt += 1
                Q.append((r,c))
                BFS(cnt)
    print(cnt-1)
