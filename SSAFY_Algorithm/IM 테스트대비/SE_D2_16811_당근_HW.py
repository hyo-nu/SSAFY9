# 대 중 소
#
Test = int(input())

for TC in range(Test):
    N = int(input())
    ca = sorted(list((map(int,input().split()))))

    minV = 1000
    for i in range(N-2):
        for j in range(i+1,N-1):
            if ca[i] != ca[i+1] and ca[j] != ca[j+1]:
                A = i + 1
                B = j + 1
                C = N - 1 -j


