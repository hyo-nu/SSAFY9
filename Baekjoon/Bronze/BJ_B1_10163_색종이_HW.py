import sys ; sys.stdin = open('input.txt')
N = int(input()) # N <= 10
num = 0
Map = [[0] * 1001 for _ in range(1001)]

cnt = [0] * (N+1)
rs = cs = re = ce = 0
for n in range(N):
    R,C,W,H = map(int,input().split())
    num += 1
    if re < R + W : re = R + W
    if ce < C + H : ce = C + H
    if rs > R : rs = R
    if cs > C : cs = C
    for r in range(R,R + W):
        Map[r][C:C+H] = [num] * H

for r in range(rs,re):
    for c in range(cs,ce):
        cnt[Map[r][c]] += 1

for i in range(1,len(cnt)):
    print(cnt[i])

