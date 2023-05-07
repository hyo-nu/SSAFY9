import sys;sys.stdin = open("input.txt")
from collections import deque

def BFS():
    Q = deque()
    for r in range(N):
        for c in range(M):
            if Map[r][c]==0:Q.append((r,c));break
        if Q : break
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    Map[Q[0]][Q[1]] = '*'
    while Q:
        R,C = Q.popleft()
        for d in range(4):
            nr = R + dr[d]
            nc = C + dc[d]
            if 0 <= nr < N and 0 <= nc < M and Map[nr][nc]==0:
                Map[nr][nr] = '*'
                Q.append((nr,nc))


N,M = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
time = 0
cnt_lst = []
while 1 in Map:
    BFS()
    time +=1
    cnt = 0
    for r in range(N):
        for c in range(M):
            if Map[r][c] == 1:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if Map[nr][nr] == '*':
                        Map[r][c] = 0
                        cnt += 1
                        break
    cnt_lst.append(cnt)
print(time)
print(cnt_lst[time-2])
