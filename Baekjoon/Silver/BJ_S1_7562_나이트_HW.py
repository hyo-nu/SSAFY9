import sys;sys.stdin = open('input.txt')


def BFS():
    dr = [-2, -1, 1, 2, 2, 1, -1, -2]  # 우상대2, 우하대2, 좌하대2, 좌상대2
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

