import sys ; sys.stdin = open('input.txt')
paper = int(input())
G = [[0] * 102 for _ in range(102)]

for _ in range(paper):
    X,Y = map(int,input().split())
    for r in range(1,11):
        for c in range(1,11):
            G[X+r][Y+c] = 1

dr = [-1, 1, 0, 0] # 상하 좌우
dc = [ 0, 0,-1, 1]
Sum = 0

for r in range(102):
    for c in range(102):
        if G[r][c] == 1:
            for d in range(4): # 상하
                nr = r + dr[d]
                nc = c + dc[d]
                if G[nr][nc] == 0:
                    Sum += 1
print(Sum)