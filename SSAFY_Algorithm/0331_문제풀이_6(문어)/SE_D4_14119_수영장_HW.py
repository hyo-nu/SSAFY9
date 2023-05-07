def dfs(n,sm):
    global ans
    if ans <= sm:
        return

    if n>12:
        ans = min(ans,sm)
        return
    dfs(n + 1, sm + day*lst[n])
    dfs(n + 1, sm + mon)
    dfs(n + 1, sm + mon3)
    dfs(n + 1, sm + year)


Test= int(input())
for TC in range(Test):
    day,mon,mon3,year = map(int,input().split())
    lst = [0] + list(map(int,input().split()))

    ans = 365*3000
    dfs(1,0)
    print(f'#{TC+1}', ans)

#============================================

Test= int(input())
for TC in range(Test):
    day,mon,mon3,year = map(int,input().split())
    lst = [0] + list(map(int,input().split()))
    s = [0]*13

    for i in range(1,13):
        s[i] = s[i-1] + day * lst[i]
        s[i] = min(s[i], s[i-1] + mon)
        if i >= 3:
            s[i] = min(s[i], s[i - 3] + mon3)
        if i >= 12:
            s[i] = min(s[i], s[i - 12] + year)

    ans = s[12]
    print(f'#{TC+1}', ans)
