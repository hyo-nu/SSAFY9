Test = int(input())

for T in range(Test):
    N = int(input())
    money = list(map(int,input().split()))
    Max = 0
    revenue = 0

    for i in range(len(money)-1,-1,-1):
        if Max < money[i] : Max = money[i]
        else:
            revenue = revenue + Max - money[i]
    print(f'#{T+1}', revenue)
