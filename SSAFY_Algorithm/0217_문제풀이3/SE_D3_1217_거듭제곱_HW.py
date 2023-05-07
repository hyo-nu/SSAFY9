# 거듭제곱
def square(N,M):
    if M == 0 :
        return 1
    else:
        return N * square(N,M-1)

Test = 10

for T in range(Test):
    TC = int(input())
    N,M = map(int,input().split())

    print(f'#{TC}', square(N,M))