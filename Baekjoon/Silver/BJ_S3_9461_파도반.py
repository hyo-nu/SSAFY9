import sys;sys.stdin=open('input.txt')

Test = int(input())

lst = [1,1,1,2,2]
for TC in range(Test):
    N = int(input())
    lst = lst + [0] * N

    for i in range(N):
        if i <= 4 : continue
        else: lst[i] = lst[i-1] + lst[i-5]

    print(lst[N-1])

