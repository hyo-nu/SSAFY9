import sys;sys.stdin=open('input.txt')

from collections import deque

def BFS():

    while Q:
        now = Q.popleft()
        for d in (1,-1, 2, -10):
            if d == 2 : next = now * d
            else : next = now + d
            if 0 < next <= 1000000 and not visited[next]:
                visited[next] = visited[now] + 1
                Q.append(next)
            if next == M:
                return


Test = int(input())

for TC in range(Test):
    N, M = map(int,input().split())
    Q = deque()
    Q.append(N)
    visited = [0] * 1000001
    visited[N] = 1
    BFS()
    print(f'#{TC+1}',visited[M]-1)