# import sys ; sys.stdin = open('input.txt')
from collections import deque
from collections import deque

def BFS():
    move = [-1,1,2]
    stop = -2
    cnt = 1
    while Q:
        XB = Q.popleft()
        if visited[XB] == visited[K] - 1:
            if XB == K-1 or XB == K + 1 or XB == K/2:
                cnt += 1
        for d in range(3):
            if d != 2 : XA = XB + move[d]
            else : XA = XB * move[d]
            if 0 <= XA <= 100000:
                if stop:
                    if visited[XA] == -1 or visited[XA] == visited[XB] + 1:
                        Q.append(XA)
                        visited[XA] = visited[XB] + 1
                        if XA == K:
                            stop = 0
                else : break
    return cnt

N, K = map(int,input().split())
Q = deque()
Q.append(N)
visited = [-1] * 100001
visited[N] = 0
cnt = BFS()
print(visited[K])
print(cnt)
