# 두번
Test = int(input())
for T in range(Test):
    N = int(input())
    lst = []
    for i in range(N):
        alpa, num = input().split()
        lst.extend(*[alpa * int(num)])

    jump = 0
    for i in lst:
        print(i, end='')
        jump += 1
        if jump % 10 == 0: print();

# 처음
Test = int(input())

for T in range(Test):
    N = int(input())
    words = ''
    for i in range(N):
        word, num = input().split()
        words += word * int(num)

    jump = 0
    print(f'#{T + 1}')
    for j in words:
        jump += 1
        print(j, end='')
        if jump % 10 == 0: print()
    print()