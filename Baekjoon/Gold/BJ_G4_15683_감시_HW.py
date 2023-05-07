import sys;sys.stdin=open('input.txt')

def back(n,lst):
    if n >= cnt:
        break

    for d in range(4):


def blind_spot():
    global cnt
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    CCTV = [[], [0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]  # 1,2,3,4,5
    vi = [[0] * N for _ in range(M)]
    cnt = 0
    for TV, spot in TV_dict.items():
        for R,C in spot:
            vi[R][C] = TV
            if TV != 6 : cnt += 1
    back(0,[])

N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
TV_dict = {}

for r in range(N):
    for c in range(M):
        if G[r][c] != 0:
            if G[r][c] not in TV_dict : TV_dict[G[r][c]] = [[r,c]]
            else : TV_dict[G[r][c]] += [[r,c]]

print(blind_spot())