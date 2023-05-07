import sys;sys.stdin=open('input.txt')

def perm(r,Sum):
    global Min
    if r == N :
        if Min > Sum:
            Min = Sum
        return
    for c in range(N):
        if Min < Sum: return
        if not vi[c]:
            vi[c] = 1
            perm(r+1,Sum +G[r][c])
            vi[c] = 0

Test = int(input())

for TC in range(Test):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    vi = [0] * N
    Min = (N**2)*99
    perm(0,0)

    print(f'#{TC+1}',Min)