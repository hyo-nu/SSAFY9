Test = int(input())

for T in range(Test):
    N = int(input())
    nums_lst = list(map(int,input().split()))

    for i in range(0,N-1):
        min_idx = i
        for j in range(i+1,N):
            if nums_lst[min_idx] > nums_lst[j]:
                min_idx = j
        nums_lst[i],nums_lst[min_idx] = nums_lst[min_idx], nums_lst[i]
    print(f'#{T+1}', *nums_lst)

