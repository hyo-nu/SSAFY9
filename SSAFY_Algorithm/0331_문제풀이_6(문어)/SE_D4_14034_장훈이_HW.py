def dfs(n, sm):
    global ans
    # 최소값 구할 때 항상 겅공하는 가지치기
    # if ans <=sm-B:
    #     return

    if ans == 0:
        return

    if n == N:
        if sm >= B:
            ans = min(ans, sm - B)
        return
    dfs(n + 1, sm + lst[n])
    dfs(n + 1, sm)


Test = int(input())
for TC in range(Test):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N * 10000
    dfs(0, 0)