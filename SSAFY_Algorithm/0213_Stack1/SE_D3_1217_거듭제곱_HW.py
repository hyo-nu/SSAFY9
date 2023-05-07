# 거듭제곱

Test = 10
def square(N,M):
    if M == 0:
        return 1
    else:
        return N*square(N,M-1)

for T in range(Test):
    TC = int(input())
    N,M = map(int,input().split())

    print(f'#{T+1}',square(N,M))




