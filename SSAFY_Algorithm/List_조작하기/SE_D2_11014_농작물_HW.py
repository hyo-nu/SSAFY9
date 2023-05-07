# 농작물 수확하기
import sys ; sys.stdin = open('input.txt')

Test = int(input())

for T in range(Test):
    N = int(input())
    farm = [list(map(int,input().split()))for _ in range(N)]
    L = W = [i for i in range(0,N-1)]

    result = []
    for w in W:
        for l in L:
            jun1 = jae2 = min3 = 0
            for r in range(0,w+1):
                for c in range(0,l+1):
                    jun1 += farm[r][c]
            for r in range(w+1,N):
                for c in range(0,l+1):
                    jae2 += farm[r][c]
            for r in range(N):
                for c in range(l+1,N):
                    min3 += farm[r][c]
            result.append(max(jun1,jae2,min3) - min(jun1,jae2,min3))

    result.sort()
    print(f'#{T+1}',result[0])