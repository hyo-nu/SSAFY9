from collections import deque

def BFS():
    move = [-1,1,2]

    while Q:
        XB = Q.popleft()
        for d in range(3):
            if d != 2 : XA = XB + move[d]
            else : XA = XB * move[d]

            if 0 <= XA <= 100000 and visited[XA] == 0:
                Q.append(XA)
                visited[XA] = visited[XB] + 1
                if XA == K:
                    return

N, K = map(int,input().split())
Q = deque()
Q.append(N)
visited = [0] * 100001
visited[N] = 1
BFS()
print(visited[K]-1)