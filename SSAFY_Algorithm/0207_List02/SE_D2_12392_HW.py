# 두번쨰
Test = int(input())
# Test = 10

for T in range(Test):
    N = int(input())
    nums = list(map(int,input().split()))


    for i in range(N-1):
        maxidx = i
        minidx = i
        for j in range(i+1,N):
            if i % 2 == 0:
                if nums[maxidx] < nums[j] : maxidx = j
            else :
                if nums[minidx] > nums[j] : minidx = j
        if i % 2  == 0 : nums[i],nums[maxidx] = nums[maxidx],nums[i]
        else : nums[i],nums[minidx] = nums[minidx],nums[i]

    print(f'#{T+1}',*nums)

# 처음
Test = int(input())

for T in range(Test):
    N = int(input())
    N_lst = list(map(int,input().split()))
    # [10,9,8,7,6,5,4,3,2,1]
    N_lst.sort(reverse=True)

    for i in range(0,N-1): #0 1 2 3 4 5 6 7 8 9
        max_idx = i
        min_idx = i
        if i % 2 == 0:  # 큰 수 출력할 때
            for j in range(i+1,N):
                if N_lst[max_idx] < N_lst[j]:
                    max_idx = j
            N_lst[i], N_lst[max_idx] = N_lst[max_idx], N_lst[i]

        else :  # 작은 수 출력할 때
            for k in range(i+1, N):
                if N_lst[min_idx] > N_lst[k]:
                    min_idx = k
            N_lst[i], N_lst[min_idx] = N_lst[min_idx], N_lst[i]

    print(f'#{T+1}', *N_lst[:10])