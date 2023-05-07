# 두번째
Test = int(input())
# Test = 10

for T in range(Test):
    TC = int(input())
    scores = list(map(int, input().split()))
    score_lst = [0] * 101

    for i in scores:
        score_lst[i] += 1

    Max = 0
    for j in range(100, -1, -1):
        if Max < score_lst[j]:
            Max = score_lst[j]
            Maxidx = j

    print(f'#{T + 1}', Maxidx)
# 첫번째
Test = int(input())

for c in range(0, Test):
    number = int(input())
    grades = list(map(int, input().split()))
    freq = [0] * 101
    mode = 0
    for grade in grades:
        freq[grade] += 1

    for grade in range(101):
        if freq[grade] >= mode:
            mode = freq[grade]
            result = grade

    print(f"#{c + 1} {result}")