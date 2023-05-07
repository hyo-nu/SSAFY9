def dfs(n,tst,ci,cj):
    if n==7:
        sset.add(tst)
        return

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if 0 <= ni < 4 and 0 <=nj < 4:
            dfs(n+1, tst+arr[ni][nj], ni, nj)

Test = int(input())

for TC in range(Test):
    # 문자열보다 정수로 받고 처리하면 빠르다.
    arr = [input().split() for _ in range(4)]
    sset = set()

    for i in range(4):
        for j in range(4):
            dfs(1,arr[i][j],i,j)

    ans = len(sset)
    print(f'#{TC+1}',ans)
