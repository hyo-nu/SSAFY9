# 스택제로

Test = int(input())

def push(item):
    global top
    top += 1
    S[top] = item

def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

for T in range(Test):
    N = int(input())
    nums = list(map(int,input().split()))
    S = [0] * N
    top = -1

    for i in range(len(nums)):
        if nums[i] != 0 : push(nums[i])
        elif nums[i] == 0 : pop()

    Sum = 0
    for i in range(top+1):
        Sum += S[i]
    print(f'#{T+1}',Sum)



