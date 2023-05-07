# 두번째
Test = int(input())
# Test = 10
N_lst = [2,3,5,7,11]
for T in range(Test):
    N = int(input())
    cnt = [0]* len(N_lst)

    for i in range(len(N_lst)):
        while N % N_lst[i] == 0:
            cnt[i] += 1
            N = N // N_lst[i]

    print(f'#{T+1}',*cnt)