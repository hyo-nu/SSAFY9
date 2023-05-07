import time
start = time.time()

def DFS(n,sum):
    if n == N:
        ans.append(sum)
        return

    ans.sort()
    if sum > ans[0]:
        return

    for i in range(0, N): #3
        if v[i] == 0:
            v[i] = 1
            DFS(n + 1, sum + arr[i][n])
            v[i] = 0

Test = int(input())

for T in range(Test):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans, v = [9999], [0] * N

    DFS(0,0)
    print(f'#{T+1}',ans[0])

print(time.time()-start)