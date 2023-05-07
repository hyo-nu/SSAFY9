# S = 1
# N = 0
# 시계 : 1
# 반시계 : -1
from collections import deque
import sys;sys.stdin=open('input.txt')

gear_lst = [deque(['.'] * 8)] + [deque(list(input())) for _ in range(4)]
cycle = [list(map(int,input().split())) for _ in range(int(input()))]
Q = deque()

for gear, dire in cycle:
    Q.append((gear,dire))
    vi = [0] * 5
    while Q:
        G,D = Q.popleft()
        vi[G] = 1
        if 1 <= G <= 4:
            # 왼쪽 톱니
            if 1 <= G-1 and not vi[G-1] and gear_lst[G-1][2] != gear_lst[G][6]:
                vi[G-1] = 1
                Q.append((G-1,D*(-1)))
            # 오른쪽 톱니
            if G+1 <= 4 and not vi[G+1] and gear_lst[G][2] != gear_lst[G+1][6]:
                vi[G+1] = 1
                Q.append((G+1,D*(-1)))
            gear_lst[G].rotate(D)

score, result = 1, 0
for lst in gear_lst[1:]:
    if lst[0] == '1' : result += score
    score *= 2
print(result)