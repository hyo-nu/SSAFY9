from collections import deque

def BFS():
    dr = [0, 1, 0,-1] #우하좌상
    dc = [1, 0,-1, 0]
    result = 0
    for x in range(N):
        for y in range(M):
            if G[x][y] == 1:
                Q.append((x, y))
                result += 1
                while Q:
                    r,c = Q.popleft()
                    G[r][c] = 0
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < N and 0<= nc < M and G[nr][nc] == 1:
                            Q.append((nr, nc))
    return result
Test = int(input())

for TC in range(Test):
    M, N, K = map(int,input().split())
    G = [[0] * (M) for _ in range(N)]
    Q = deque()
    result = 0
    for _ in range(K):
        y,x = map(int,input().split())
        G[x][y] = 1

    print(BFS())