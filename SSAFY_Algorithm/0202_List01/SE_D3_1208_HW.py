# 두번째 
# Test = int(input())
Test = 10

for T in range(Test):
    dump_num = int(input())
    box = list(map(int, input().split()))

    for i in range(dump_num):
        Maxidx = 0
        Minidx = 0
        for j in range(100):
            if box[Maxidx] < box[j]: Maxidx = j
            if box[Minidx] > box[j]: Minidx = j
        box[Maxidx] -= 1
        box[Minidx] += 1

    Max = 0
    Min = 100
    for j in range(100):
        if Max < box[j]: Max = box[j]
        if Min > box[j]: Min = box[j]

    print(f'#{T + 1}', Max - Min)

# 첫번쨰
Test = 10

for T in range(Test):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        max = 0
        min = 100

        # dump 한번의 과정, 계속 바뀌는 최고높이, 최저높이를 판별
        for j in range(100):
            if max < box[j]: max = box[j]; max_bump = j
            if min > box[j]: min = box[j]; min_bump = j
        if max == min:
            print(f'#{T + 1} {1}')
            break
        # 최고, 최저 높이에서 -1
        box[max_bump] -= 1
        box[min_bump] += 1

    max = 0
    min = 100
    # dump 종료 후 최저 높이 판별
    for k in range(100):
        if max < box[k]: max = box[k]
        if min > box[k]: min = box[k]

    print(f'#{T + 1} {max - min}')