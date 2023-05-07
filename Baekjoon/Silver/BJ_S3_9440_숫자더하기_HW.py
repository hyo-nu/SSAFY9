import sys;sys.stdin=open('input.txt')
while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0 : break

    nums = sorted(lst[1:])
    zero = nums.count(0)
    for i in range(2):
        if nums[i] == 0:
            nums[i], nums[i + zero] = nums[i + zero], nums[i]

    left = []
    right = []

    for i in range(lst[0]):
        if i % 2 == 0 : left.append(nums[i])
        else: right.append(nums[i])
    print(int(''.join(map(str,left))) + int(''.join(map(str,right))))