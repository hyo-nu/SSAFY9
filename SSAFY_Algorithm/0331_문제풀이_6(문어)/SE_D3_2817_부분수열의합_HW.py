def dfs(n,sm):
    global ans
    if n==N:
        if sm==K:
            ans += 1
        return
    dfs(n+1,sm+lst[n])
    dfs(n+1,sm)

Test = int(input())

for TC in range(Test):
    N, K = map(int, input().split())
    lst = list(map(int,input().split()))

    ans = 0
    dfs(0,0)
    print(f'#{TC+1}',ans)