import sys
input = sys.stdin.readline
# 2 <= N <= 100,000
# 1 <= K <= N
N, K = map(int,input().split())
temp = list(map(int,input().split()))


Sum = sum([temp[i] for i in range(K)])
Max = Sum
for i in range(N-K): # 0 1 2 3 4 5 6 7
    Sum = Sum - temp[i] + temp[i+K]
    if Max < Sum : Max = Sum
print(Max)