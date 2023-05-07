def DFS(n, sm, cnt):
    global ans

    if n == N:
        if sm == K and cnt == N:
            ans += 1
        return

    DFS(n+1,sm + lst[n],cnt+1)
    DFS(n+1,sm,cnt)

Test = int(input())

for TC in range(Test):
    N,K = map(int, input().split())
    lst = [n for n in range(1,13)]
    Num = 12

    ans = 0
    DFS(0, 0, 0)
    print(f'#{TC+1}',ans)
