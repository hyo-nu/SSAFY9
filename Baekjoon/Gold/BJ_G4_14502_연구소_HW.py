from itertools import combinations
from collections import deque
import sys ; sys.stdin = open('input.txt')

def BFS(road,wa,SP,Max):
    vi = [[1]*M for _ in range(N)]
    Q = deque()
    area = 0
    for r,c in road : vi[r][c] = 0 ; area += 1 # vi배열에 road 표시, 0갯수 파악
    for r,c in wa : vi[r][c] = 1 ; area -= 1  # 새로운 벽 생설
    for r,c in SP: Q.append((r,c)) # start point Q에 enQ

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    while Q:
        R,C = Q.popleft()
        for d in range(4):
            nr, nc = R + dr[d], C + dc[d]
            if 0 <= nr < N and 0 <= nc < M and vi[nr][nc] == 0:
                vi[nr][nc] = 2
                Q.append((nr,nc))
                area -= 1
            if Max > area : break
    if Max < area : Max = area
    return Max


N,M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
road = []  # 0인 지점, 움직일 수 있는 길
SP = [] # 2인 지점, 바이러스 위치
for r in range(N):
    for c in range(M):
        if G[r][c] == 0 : road.append((r,c)) # 빈칸 좌표 모음
        elif G[r][c] == 2 : SP.append((r,c)) # 바이러스 좌표 모음

wall = combinations(road,3) # 1로 바꿀 0인지점의 조합
Max = 0
for wa in wall:
    Max = BFS(road,wa,SP,Max)
print(Max)


# 2 <= 2의수 < 10
# 0 : 빈칸
# 1 : 벽
# 2 : 바이러스