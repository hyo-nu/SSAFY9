import sys ; sys.stdin = open('input.txt')
from collections import deque

def BFS():
    dr = [0, 1, 0,-1]
    dc = [1, 0,-1, 0]
    while Q:
        r,c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0<= nc < M and maze[nr][nc] == -1:
                maze[nr][nc] = maze[r][c] + 1
                Q.append((nr,nc))

N,M = map(int,input().split())
maze = []
for _ in range(N):
    lst = list(input())
    for i in range(len(lst)):
        if lst[i] == '1' : lst[i] = -1
    maze.append(lst)

Q = deque()
Q.append((0,0))
maze[0][0] = 1
BFS()
print(maze[N-1][M-1])


