from collections import deque

def BFS():
    move = [-1,1,2]
    cnt = 0
    while Q:
        XB = Q.popleft()
        for d in range(3):
            if d != 2 : XA = XB + move[d]
            else : XA = XB * move[d]

            if 0 <= XA <= 100000 and visited[XA] == -1:
                Q.append(XA)
                visited[XA] = visited[XB] + 1
                if XA == K:
                    return

N, K = map(int,input().split())
Q = deque()
Q.append(N)
visited = [-1] * 100001
visited[N] = 0
BFS()
print(visited[K])