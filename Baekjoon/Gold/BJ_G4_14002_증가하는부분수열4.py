import sys;sys.stdin=open('input.txt')
from collections import deque

N = int(input())
N_lst = [0] + list(map(int,input().split()))
DP = [0] * (N + 1)

for i in range(1,N+1):
    mx = 0
    for j in range(0,i):
        if N_lst[i] > N_lst[j]:
            mx = max(mx, DP[j])
    DP[i] = mx + 1

mx = max(DP)
start = DP.index(mx)
top_idx = DP.index(mx)
route = deque()
route.append(N_lst[top_idx])
for i in range(start-1,0,-1):
    if mx-1 == DP[i] and N_lst[top_idx] > N_lst[i]:
        mx -= 1
        top_idx = i
        route.appendleft(N_lst[i])

print(max(DP))
print(*route)
'''
100 50 10 20 30 40 30 70 60 80

# 10 20 30 40 60 80
'''


# N = int(input())
# N_lst = [0] + list(map(int,input().split()))
# route = []
# DP = [0] * 1001
# for i in range(1,N+1):
#     DP[N_lst[i]] = max(DP[:N_lst[i]]) + 1
# mx = max(DP)
# N_lst.sort(reverse=True)
# for n in N_lst:
#     if DP[n] == mx:
#         route.append(n)
#         mx -= 1
#     if mx == 0:break
# route.sort()
# print(max(DP))
# print(*route)
