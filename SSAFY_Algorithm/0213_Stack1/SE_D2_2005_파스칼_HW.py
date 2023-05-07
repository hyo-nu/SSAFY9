# 파스칼의 삼각형
# 현우스
Test = int(input())

for T in range(Test):
    N = int(input()) # 5

    copy_tri = []
    print(f'#{T+1}')
    for i in range(-1,N-1) : # -1 0 1 2 3
        tri = [1, 1]
        if i <= 0:
            copy_tri.append(1)
            print(*copy_tri)
        else:
            for j in range(i):
                tri.insert(j+1,copy_tri[j]+copy_tri[j+1])
            copy_tri = tri
            print(*tri)

# 동훈스
Test = int(input())

for T in range(Test):
    N = int(input())
    ans = [[1] * i for i in range(1,N+1)]

    for i in range(1,N-1):
        for j in range(len(ans[i])-1):
            ans[i+1][j+1] = ans[i][j]+ans[i][j+1]

    for i in ans:
        print(*i)