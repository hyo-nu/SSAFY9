# (x, y)
# (1, 1) : 출발
# (13,13) : 도착

Test = 10

def BFS(mr,mc):
    if maze[mr][mc] == 0 or maze[mr][mc] == 3:
        visited[mr][mc] = visited[now[0]][now[1]] + 1
        Q.append([mr,mc])

for TC in range(Test):
    N = 16 # N x N 미로
    T = int(input())
    maze = [list(map(int,input()))for _ in range(N)]
    Q = []
    visited = [[0] * N for _ in range(N)]

    nr, nc, er, ec = 1, 1, 13, 13
    visited[nr][nc] = 1
    Q.append([nr,nc])

    while Q:
        now = Q.pop(0)
        maze[now[0]][now[1]] = 1
        BFS(now[0], now[1] + 1) # 우
        BFS(now[0] + 1, now[1]) # 하
        BFS(now[0], now[1] - 1) # 좌
        BFS(now[0] - 1, now[1]) # 상

    arrive = visited[er][ec]
    if arrive == 0 : print(f'#{T}',0)
    else : print(f'#{T}',1)