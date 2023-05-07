from collections import deque
import sys;

sys.stdin = open('input.txt')

N = int(input())  # 1 <= N <= 20
dr, dc = [0, -1, 0, 1], [1, 0, -1, 0]  # 우상좌하
Map = [[0] * 101 for _ in range(101)]
# 방향 : 반시계 + 1
# x = c, y = r
for _ in range(N):
    # 0<=x,y<=100 , 0<=d<=3, 0<=g<=10
    X, Y, D, G = map(int, input().split())
    d_lst = [D]
    Map[Y][X] = 1

    for g in range(G):  # 0,1,2
        for i in range(2 ** g - 1, -1, -1):
            d_lst.append((d_lst[i] + 1) % 4)

    for d in d_lst:
        Y, X = Y + dr[d], X + dc[d]
        Map[Y][X] = 1

Dr = [0, 1, 1]  # 우대하
Dc = [1, 1, 0]
result = 0
for r in range(101):
    for c in range(101):
        if Map[r][c] == 1:
            for d in range(3):
                nr, nc = r + Dr[d], c + Dc[d]
                if 0 <= nr < 101 and 0 <= nc < 101:
                    if Map[nr][nc] != 1: break
                else:
                    break
            else:
                result += 1
print(result)

from collections import deque

Q = deque()
Q.popleft()
