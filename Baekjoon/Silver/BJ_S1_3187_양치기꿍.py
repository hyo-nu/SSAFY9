import sys;sys.stdin=open('input.txt')

from collections import deque

def BFS():
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    sheep = wolf = 0

    while Q :
        r,c = Q.popleft()
        if G[r][c] == 'k' : sheep += 1
        elif G[r][c] == 'v' : wolf += 1
        G[r][c] = '#'

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != '#':
                if G[nr][nc] == 'k': sheep += 1
                elif G[nr][nc] == 'v': wolf += 1
                Q.append((nr,nc))
                G[nr][nc] = '#'

    if sheep > wolf:
        wolf -= wolf
    elif sheep <= wolf:
        sheep -= sheep

    return sheep,wolf

R,C = map(int,input().split())
G = [list(input()) for _ in range(R)]
Q = deque()
sheep = 0
wolf = 0
for r in range(R):
    for c in range(C):
        if G[r][c] != '#':
            Q.append((r,c))
            o,v = BFS()
            sheep , wolf = sheep + o, wolf + v

print(sheep, wolf)