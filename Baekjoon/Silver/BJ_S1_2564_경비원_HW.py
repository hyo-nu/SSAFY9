import sys;sys.stdin = open('input.txt')

def point(dire,dist):
    if dire == 1 : return [0, dist]
    elif dire == 2 : return [row, dist]
    elif dire == 3 : return [dist, 0]
    elif dire == 4 : return [dist, col]

def Min(lst):                           # 동근 : 상점
    if nr == 0 and lst[0] == row :      #   북 : 남
        result = row + (nc + lst[1])
        if result >= (row + col): result = ((row + col)*2) - result
    elif nr == row and lst[0] == 0 :    #   남 : 북
        result = row + (nc + lst[1])
        if result >= (row + col): result = ((row + col)*2) - result
    elif nc == 0 and lst[1] == col :    #   동 : 서
        result = col + (nr + lst[0])
        if result >= (row + col): result = ((row + col)*2) - result
    elif nc == col and lst[1] == 0 :    #   서 : 동
        result = col + (nr + lst[0])
        if result >= (row + col): result = ((row + col)*2) - result

    else:result = abs(lst[0]-nr) + abs(lst[1]-nc)
    tmp.append(result)
    return result

# N 가로 , M 세로
# col   , row
col,row = map(int,input().split())
shop = int(input())
G = [[0]*(col+1) for _ in range(row+1)]
shop_lst = []
tmp = []
# 상점 방향 1:북,2:남,3:서,4:동
# 북남 : 왼쪽에서의거리 , 동서 : 위쪽에서의거리
for i in range(shop):
    dire,dist = map(int,input().split())
    shop_lst.append(point(dire, dist))
    nr,nc = point(dire, dist)
    G[nr][nc] = 1

result = 0
r, c = map(int,input().split())
nr,nc = point(r,c)
G[nr][nc] = 1
for lst in shop_lst:
    result += Min(lst)

for lst in G:
    print(lst)
print(result)
print(tmp)