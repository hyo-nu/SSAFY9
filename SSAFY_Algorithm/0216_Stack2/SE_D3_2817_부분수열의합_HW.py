# 부분수열의 합
def DFS(n,sum):
    global cnt
    if n == N:
        if sum == K:
            cnt += 1
        return
    DFS(n+1,sum + A[n])
    DFS(n+1,sum)

Test = int(input())

for T in range(Test):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))  # 개수가 N 1<=A<=100
    cnt = 0
    DFS(0,0)
    print(f'#{T+1}', cnt)