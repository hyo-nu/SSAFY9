N, M = map(int, input().split())
nums = list(map(int, input().split()))

lst = []
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # print([i,j,k]) 
            lst.append([i, j, k])

max_lst = []
for l in lst:
    sum = 0
    for o in l: sum += nums[o]
    if sum <= M: max_lst.append(sum)

max_lst.sort()
print(max_lst[-1])

#===================================================
N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            if ans < lst[i] + lst[j] + lst[k] <= M:
                ans = lst[i] + lst[j] + lst[k]
print(ans)