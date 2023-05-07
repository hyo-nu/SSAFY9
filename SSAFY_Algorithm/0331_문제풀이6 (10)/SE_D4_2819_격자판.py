import sys;sys.stdin=open('input.txt')

def DFS(n,r,c,Sum):
    if n==7:
        sset.add(Sum)
        return
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    for d in range(4):
        if 0 <= r+dr[d] < 4 and 0 <= c+dc[d] < 4:
            DFS(n+1,r+dr[d],c+dc[d],Sum+G[r+dr[d]][c+dc[d]])

Test = int(input())

for TC in range(Test):
    G = [input().split() for _ in range(4)]
    sset = set()

    for r in range(4):
        for c in range(4):
            DFS(1,r,c,G[r][c])
    print(f'#{TC+1}',len(sset))