# R : 가로, C : 세로
# 행     , 열
def where():
    dr = [0, 1, 0, -1]  # 우 하 좌 상
    dc = [1, 0, -1, 0]
    r = d = num = 0
    c = -1

    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == 0:
            num += 1
            G[nr][nc] = num
            if G[nr][nc] == K: break
            if G[nr][nc] == R * C:  [0]
            r, c = nr, nc
        else:
            d = (d + 1) % 4
    return [nr + 1, nc + 1]

R, C = map(int,input().split())
K = int(input())
G = [[0] * C for _ in range(R)]

print(*where())
