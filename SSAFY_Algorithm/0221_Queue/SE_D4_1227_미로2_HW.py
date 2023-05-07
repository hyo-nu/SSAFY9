import sys;sys.stdin = open('input.txt')


def direction(mr, mc):
    if maze[mr][mc] == '3' or maze[mr][mc] == '0':
        Q.append([mr,mc])

def BFS():
    while Q:
        now = Q.pop(0)
        if maze[now[0]][now[1]] == '3' : return 1
        maze[now[0]][now[1]] = '.'
        direction(now[0], now[1] + 1) # 우
        direction(now[0] + 1, now[1]) # 하
        direction(now[0], now[1] - 1) # 좌
        direction(now[0] - 1, now[1]) # 상
    return 0

Test = 10

for T in range(Test):
    TC = int(input())
    N = 100
    maze = [list(input()) for _ in range(N)]
    Q = []
    Q.append([1, 1])
    print(f'#{TC}',BFS())