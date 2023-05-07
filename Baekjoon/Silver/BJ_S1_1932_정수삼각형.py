import sys;sys.stdin=open('input.txt')

N = int(input())
tri = [list(map(int,input().split())) for _ in range(N)]
DP = [[0] * i for i in range(1,N+1)]
DP[0][0] = tri[0][0]

for n in range(1,N):
    for i in range(len(tri[n])):
        if i == 0:
            DP[n][i] += DP[n-1][0] + tri[n][i]
        elif i == len(tri[n])-1:
            DP[n][i] += DP[n-1][i-1] + tri[n][i]
        else :
            DP[n][i] += max(DP[n-1][i-1] + tri[n][i],DP[n-1][i] + tri[n][i])
print(max(DP[N-1]))