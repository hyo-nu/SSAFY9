Test = 10

for TC in range(Test):
    N,nums = input().split()
    S = []
    top = -1
    for i in nums:
        if top == -1: S.append(i) ; top += 1
        elif S[top] == i : S.pop() ; top -= 1
        else : S.append(i) ; top += 1
    print(f'#{TC+1}',''.join(S))