# import sys ; sys.stdin = open('input.txt')
# from collections import deque
#
# def Multi_BFS(Q):
#     dr = [0, 1, 0,-1, N,-N] #우,하,좌,상,위,아래
#     dc = [1, 0,-1, 0, 0, 0]
#     Max = 0
#     cnt = 0
#     while Q:
#         r,c = Q.popleft()
#         for d in range(6):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if d <= 3:
#                 tmpr = (r % N) + dr[d]
#                 if 0 <= tmpr < N and 0 <= nc < M and mato[nr][nc] == -1:
#                     mato[nr][nc] = mato[r][c] + 1
#                     Q.append((nr, nc))
#                     if Max < mato[nr][nc]:
#                         Max = mato[nr][nc]
#             elif d > 3:
#                 if 0 <= nr < N * H and 0 <= nc < M and mato[nr][nc] == -1:
#                     mato[nr][nc] = mato[r][c] + 1
#                     Q.append((nr, nc))
#                     if Max < mato[nr][nc]:
#                         Max = mato[nr][nc]
#     for lst in mato:
#         cnt += lst.count(-1)
#     if cnt != 0 : return -1
#     else : return Max
#
# M,N,H = map(int,input().split())
# mato = [[-1]*M for _ in range(N * H)]
#
# # 토마토 받아오기
# Q = deque()
# cnt = 0
#
# for r in range(N * H):  # N 세로
#     to = list(map(int,input().split()))
#     for c in range(M): # M 가로
#         if to[c] == 1 : mato[r][c] = 0 ; Q.append((r,c))
#         elif to[c] == -1 : mato[r][c] = -2
#         elif to[c] == 0 : cnt += 1
#
# if cnt == 0 : print(0) # 덜익은 토마토 없는경우
# else : print(Multi_BFS(Q))

# 익토   1 : 0
# 덜익토 0 : -1
# 빈칸  -1 : -2

import sys ; sys.stdin = open('input.txt')
from collections import deque

def Multi_BFS(Q,unripe):
    dr = [-1, 1, 0, 0, 0, 0] # 상,하
    dc = [ 0, 0,-1, 1, 0, 0] # 좌,우
    dh = [ 0, 0, 0, 0, 1,-1] # 위,아래
    day = 0
    if not unripe : return 0  # 덜익토가 없는 상태, 즉! 다 익음
    while Q:
        r,c,h = Q.popleft()
        for d in range(6):
            nr, nc, nh = r + dr[d], c + dc[d],h + dh[d]
            if 0 <= nr < N and 0<= nc < M and 0<= nh < H and box[nh][nr][nc] == -1:
                box[nh][nr][nc] = box[h][r][c] + 1
                Q.append((nr,nc,nh))
                if day < box[nh][nr][nc]:
                    day = box[nh][nr][nc]
    #덜익토 있는 경우 판단
    Sum = 0
    for arr in box:
        for lst in arr:
            Sum += lst.count(-1)
    if Sum : return -1
    else : return day

# M : 가로 , N : 세로
M, N, H = map(int,input().split())

Q = deque()
unripe = 0
box = []

for h in range(H):
    tomato = []
    for r in range(N):
        lst = list(map(int,input().split()))
        for c in range(M):
            if lst[c] == 1 : lst[c] = 0 ; Q.append((r,c,h)) # 익토 0
            elif lst[c] == 0 : lst[c] = -1 ; unripe += 1 # 덜익토 -1
            elif lst[c] == -1 : lst[c] = -2 # 빈칸 -2
        tomato.append(lst)
    box.append(tomato) # 012 , 345

print(Multi_BFS(Q,unripe))
1 5 13 14 3 4
