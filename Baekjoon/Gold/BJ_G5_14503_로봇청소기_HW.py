import sys;sys.stdin = open('input.txt')
# 현재칸 청소
# 4칸중 청소 안된 빈칸 없으면 ->
# d 상우하좌
# d 0 1 2 3
N,M = map(int,input().split())
r,c,D = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]#상우하좌
dc = [ 0, 1, 0,-1]

clean = 0
while True:
    if G[r][c] == 0:
        clean += 1
        G[r][c] = 2

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if G[nr][nc] == 0:
            D = (D + 3) % 4
            mr, mc = r + dr[D] ,c + dc[D]
            if G[mr][mc] == 0 : r,c = mr,mc
            break
    else:
        back = (D + 2) % 4
        br, bc = r + dr[back], c + dc[back]
        if G[br][bc] != 1 : r,c = br,bc
        else: break
print(clean)