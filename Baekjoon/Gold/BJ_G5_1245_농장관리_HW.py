from collections import deque

def DFS():
    Q = deque()
    for r in range(N):
        for c in range(M):
            Q.append((r,c))
            while

N,M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]

