import sys ; sys.stdin=open("input.txt")


N, K = map(int,input().split())
lst = sorted([int(input()) for _ in range(N)], reverse=True)

coin = cnt =0
while K:
    if K < lst[coin]:
        coin += 1
    else:
        cnt += K // lst[coin]
        K = K % lst[coin]
print(cnt)