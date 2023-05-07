# 1  2  3  4
# 동 서  남 북
import sys ; sys.stdin = open('input.txt')

def right(lst):
    for i in range(3):
        if lst[i] == max(lst):
            if i == 2 : idx = 0
            else : idx = i + 1
            return idx

def left(lst):
    for i in range(3):
        if lst[i] == max(lst):
            if i == 0 : idx = 2
            else : idx = i - 1
            return idx

K = int(input())
row = []
col = []
dire_lst = [0] * 5
for _ in range(6):
    dire,dist = map(int,input().split())
    dire_lst[dire] += 1
    if dire >= 3 : row.append(dist)
    else : col.append(dist)

if dire_lst[4] == 2 and dire_lst[1] == 2:
    rdx, cdx = right(row), left(col)
elif dire_lst[4] == 2 and dire_lst[1] == 1:
    rdx, cdx = left(row), right(col)
elif dire_lst[4] == 1 and dire_lst[1] == 2:
    rdx, cdx = left(row), right(col)
elif dire_lst[4] == 1 and dire_lst[1] == 1:
    rdx, cdx = right(row), left(col)

remove = row[rdx] * col[cdx]
total = (max(row) * max(col)) - remove
print(total*K)

