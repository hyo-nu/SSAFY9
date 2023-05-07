# import sys ; sys.stdin = open('input.txt')
# from collections import deque
# import copy
#
# def BFS(arr):
#     dr = [0, 1, 0,-1] # 우하좌상
#     dc = [1, 0,-1, 0]
#     area = 0
#     for r in range(N):
#         for c in range(N):
#             if arr[r][c] != 0:
#                 Q.append((r,c))
#                 area += 1
#                 while Q:
#                     r,c = Q.popleft()
#                     for d in range(4):
#                         nr, nc = r + dr[d], c + dc[d]
#                         if 0 <= nr < N and 0 <= nc < N and arr[r][c] == arr[nr][nc] :
#                             Q.append((nr, nc))
#                             arr[r][c] = 0
#     return area
#
# N = int(input())
# RGB = [list(input()) for _ in range(N)]
# RGB_N = copy.deepcopy(RGB)
#
# for i in range(N):
#     for j in range(N):
#         if RGB_N[i][j] == 'G': RGB_N[i][j] = 'R'
#
# Q = deque()
# print(BFS(RGB),end = ' ')
# print(BFS(RGB_N))


import sys ; sys.stdin = open('input.txt')
from collections import deque

def BFS():
    global visited
    dr = [0, 1, 0,-1] # 우하좌상
    dc = [1, 0,-1, 0]
    Q = deque()
    visited = [[0] * N for _ in range(N)]
    area = 0
    num = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                num += 1
                visited[x][y] = num
                Q.append((x,y))
                area += 1
                while Q :
                    r,c = Q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N and RGB[nr][nc] == RGB[r][c]:
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = num
                                Q.append((nr,nc))
    return area
def BFS2():
    global visited
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    Q = deque()
    visited = [[0] * N for _ in range(N)]
    area = 0
    num = 0
    for x in range(N):
        for y in range(N):
            if RGB[x][y] == 'G' : RGB[x][y] = 'R'
            if visited[x][y] == 0:
                num += 1
                visited[x][y] = num
                Q.append((x, y))
                area += 1
                while Q:
                    r, c = Q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            if RGB[nr][nc] == 'G': RGB[nr][nc] = 'R'
                            if RGB[nr][nc] == RGB[r][c]:
                                if visited[nr][nc] == 0:
                                    visited[nr][nc] = num
                                    Q.append((nr, nc))
    return area
N = int(input())
RGB = [list(input()) for _ in range(N)]
print(BFS(),end = ' ')
print(BFS2())






