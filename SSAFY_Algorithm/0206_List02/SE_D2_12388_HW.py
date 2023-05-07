
# 두번쨰
Test = int(input())

A = [i for i in range(1,13)]

for T in range(Test):
    N,K = map(int,input().split())
    A_leng = len(A)
    count = 0
    for i in range(1<<A_leng):
        Sum = 0
        cnt = 0
        for j in range(A_leng):
            if i & (1<<j):
                Sum += A[j]
                cnt += 1
        if N == cnt and K == Sum:
            count +=1
    if count != 0 :print(f'#{T+1}',1)
    else:print(f'#{T+1}',0)

# 첫번째
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