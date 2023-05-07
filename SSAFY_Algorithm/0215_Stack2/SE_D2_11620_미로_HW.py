# 미로탈출

def start_end(maze, N):
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2: nr, nc = r, c  # 출발위치(now)
            if maze[r][c] == 3: er, ec = r, c  # 도착위치(end)
    return nr, nc, er, ec


def movable(nr, nc):
    if 0 <= nr < N and 0 <= nc < N:
        return maze[nr][nc] == 0 or maze[nr][nc] == 3
    else:
        return False


def DFS(nr, nc, er, ec):
    while nr != er or nc != ec:
        maze[nr][nc] = '.'

        if movable(nr - 1, nc): S.append((nr, nc)); nr -= 1  # 상
        elif movable(nr, nc - 1): S.append((nr, nc)); nc -=1  # 좌
        elif movable(nr + 1, nc): S.append((nr, nc)); nr +=1  # 하
        elif movable(nr, nc + 1): S.append((nr, nc)); nc +=1  # 우
        elif S : nr,nc = S.pop()
        elif not S : return 0
    return 1

Test = int(input())

for TC in range(1, Test + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    S = []
    nr, nc, er, ec = start_end(maze, N)
    print(f'#{TC}',end = ' ')
    print(DFS(nr, nc, er, ec ))