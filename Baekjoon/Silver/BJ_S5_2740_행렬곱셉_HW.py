N, MM = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

M, K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(M)]

result = []
for a in A:
    for k in range(K): # 0 1 2
        sum = 0
        for m in range(M): # 0 1
            sum += a[m]*B[m][k]
        result.append(sum)

for i in range(len(result)):
    print(result[i],end = ' ')
    if (i+1) % K == 0:print()
