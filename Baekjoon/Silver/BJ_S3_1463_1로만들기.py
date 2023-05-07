# 백트래킹
def back(N,cnt):
    global Min
    if Min <= cnt : return
    if N == 1:
        Min = min(Min,cnt)
        return
    if N % 3 == 0 : back(N/3,cnt+1)
    if N % 2 == 0 : back(N/2,cnt+1)
    back(N-1,cnt+1)

N = int(input())
Min = 10 ** 6 + 1
back(N,0)
print(Min)

#=================================
# DP
N = int(input())
DP = [0] * (N + 1)

for i in range(2, N + 1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0 : DP[i] = min(DP[i], DP[i//2] + 1)
    if i % 3 == 0 : DP[i] = min(DP[i], DP[i//3] + 1)

print(DP[N])