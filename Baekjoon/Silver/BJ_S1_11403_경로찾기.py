import sys;sys.stdin=open('input.txt')

def DFS(r,c):


N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
route = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        DFS(r,c)

