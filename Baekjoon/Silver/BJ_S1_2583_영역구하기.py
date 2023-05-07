# M : R
# N : C
import sys;sys.stdin=open('input.txt')
from collections import deque

def BFS():
    wide = 1
    while Q:
        r,c = Q.popleft()
        for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == 0:
                wide += 1
                Q.append((nr,nc))
                G[nr][nc] = 1
    return wide

C,R,K = map(int,input().split())
G = [[0]*C for _ in range(R)]

for _ in range(K):
   sr,sc,er,ec = map(int,input().split())
   for r in range(sr,er):
       for c in range(sc,ec):
            G[r][c] = 1
Q = deque()
wide_lst =[]
area = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == 0:
            area += 1
            G[r][c] = 1
            Q.append((r,c))
            wide_lst.append(BFS())

print(area)
print(*sorted(wide_lst))
