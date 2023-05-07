import sys;sys.stdin = open('input.txt')
from collections import deque

Test = int(input())

for TC in range(Test):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    D = [[9999999999999999] * N for _ in range(N)]
    D[0][0] = 0
    Q = deque()
    Q.append((0,0))
    dr = (1,0,-1,0)
    dc = (0,1,0,-1)

    while Q:
        r,c = Q.popleft()
        for d in range(4): #우하좌상
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if G[nr][nc]-G[r][c] <= 0 : high = 0
                else: high = G[nr][nc] - G[r][c]
                if D[nr][nc] > D[r][c] + 1 + high:
                    D[nr][nc] = D[r][c] + 1 + high
                    Q.append((nr,nc))

    for lst in D:
        print(lst)
    print(f'#{TC+1}',D[N-1][N-1])


