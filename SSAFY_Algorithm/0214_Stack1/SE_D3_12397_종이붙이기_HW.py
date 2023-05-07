def paper(N):
    if N == 0:
        return 1
    elif N % 2 != 0:
        return 2 * paper(N - 1) - 1
    elif N % 2 == 0:
        return 2 * paper(N - 1) + 1

Test = int(input())

for T in range(Test):
    N = int(input())
    N = N//10
    print(f'#{T+1}',end = ' ')
    print(paper(N))

