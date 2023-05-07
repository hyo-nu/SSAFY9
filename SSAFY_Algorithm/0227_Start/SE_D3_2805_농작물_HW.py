import sys ; sys.stdin = open('input.txt')
Test = int(input())

for T in range(Test):
    N = int(input())
    S = R = -1  # S = size , R = ref
    M = N // 2  # M = middle
    Sum = 0

    for _ in range(N):
        farm = input()
        if R < M : S += 1 ; R += 1
        else : S -= 1 ; R += 1
        for c in range(M - S, M + S + 1):
            Sum += int(farm[c])
    print(f'#{T+1}',Sum)