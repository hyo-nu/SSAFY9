Test = int(input())

for TC in range(Test):
    N = int(input())
    X = round(N**(1/3))

    while X**3 < N:
        X +=1

    print(f'#{TC + 1}', end=' ')
    if X ** 3 == N:print(X)
    else:print(-1)


