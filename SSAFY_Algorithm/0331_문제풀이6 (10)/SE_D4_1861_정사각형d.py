import sys;sys.stdin=open('input.txt')

def DFS(r,c,room,start):
    global Max,Small
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N  and G[nr][nc] == G[r][c]+1:
            DFS(nr,nc,room+1,start)
            break
    if Max < room:
        Max = room
        Small = start
    elif Max == room:
        if Small > start:
            Small = start
    return


Test = int(input())

for TC in range(Test):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    Max = 0
    for r in range(N):
        for c in range(N):
            DFS(r,c,1,G[r][c])

    print(f'#{TC+1}',Small, Max)

