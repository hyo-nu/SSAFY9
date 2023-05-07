Test = int(input())

for T in range(Test):
    N,K = map(int,input().split())
    count = 0
    N_lst = []
    for a in range(1,13):
        N_lst.append(a)

    for i in range(1<<12):
        sum = 0
        ns = 0
        for j in range(12):
            if i & (1<<j):
                sum += N_lst[j-1]
                ns += 1
        if sum == K and ns == N:
            count += 1
    print(f'#{T+1} {count}')

