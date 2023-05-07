def start_end():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2: nr, nc = r, c  # 출발위치(now)
            if maze[r][c] == 3: er, ec = r, c  # 도착위치(end)
    return nr, nc, er, ec

def direction(dr, dc):
    if 0 <= dr < N and 0 <= dc < N:
        return True
    else:
        return False

def BFS(mr,mc):
    if direction(mr, mc):
        if maze[mr][mc] == 0 or maze[mr][mc] == 3:
            visited[mr][mc] = visited[now[0]][now[1]] + 1
            Q.append([mr, mc])

Test = int(input())

for TC in range(Test):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    Q = []
    visited = [[0] * N for _ in range(N)]

    nr, nc, er, ec = start_end()
    visited[nr][nc] = 1
    Q.append([nr,nc])

    while Q:
        now = Q.pop(0) # 현재 위치
        maze[now[0]][now[1]] = 1
        # 경로 탐색 함수로
        BFS(now[0], now[1]-1) # 좌
        BFS(now[0]-1, now[1]) # 상
        BFS(now[0], now[1]+1) # 우
        BFS(now[0]+1, now[1]) # 하

    arrive = visited[er][ec]
    if arrive != 0: print(f'#{TC+1}',arrive-2)
    else:print(f'#{TC+1}',arrive)
