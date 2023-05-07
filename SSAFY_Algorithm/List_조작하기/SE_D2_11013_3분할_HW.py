import sys ; sys.stdin = open('input.txt')

Test = int(input())

for T in range(Test):
    N = int(input())
    A = list(map(int,input().split()))

    Min = []
    for i in range(N):
        for j in range(i+1,N):
            Sum = [sum(A[0:i+1]),sum(A[i+1:j+1]),sum(A[j+1:])]
            Sum.sort()
            Min.append(Sum[2]-Sum[0])
    Min.sort()
    print(f'#{T+1}',Min[0])

