from collections import deque
def BFS():
    move = [-1,1,2]

    while Q:
        XB = Q.popleft()
        for d in range(3):
            if d == 2:
                XA = XB * move[d]
                if 0 <= XA <= 100000 and distance[XA] == -1:
                    Q.append(XA)
                    distance[XA] = distance[XB]
                if XA == K : return
            else :
                XA = XB + move[d]
                if 0 <= XA <= 100000 and distance[XA] == -1:
                    Q.append(XA)
                    distance[XA] = distance[XB] + 1
                if XA == K : return


N, K = map(int,input().split())
Q = deque()
Q.append(N)
distance = [-1] * 100
distance[N] = 0
BFS()
print(list(range(1,40)))
print(distance)