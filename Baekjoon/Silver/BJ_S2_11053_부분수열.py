import sys;sys.stdin=open('input.txt')

N = int(input())
N_lst = [0] + list(map(int,input().split()))
DP = [0] * (N + 1)

for i in range(1,N+1):
    mx = 0
    for j in range(0,i):
        if N_lst[i] > N_lst[j]:
            mx = max(mx, DP[j])
    DP[i] = mx + N_lst[i]
print(max(DP))

