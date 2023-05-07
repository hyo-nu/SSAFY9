# 두번째 풀이
# 카운팅 정렬 풀이
Test = int(input())

for T in range(Test):
    N = int(input())
    card = list(input())

    card_cnt = [0] * 10

    for i in card:
        card_cnt[int(i)] += 1
    Max = 0

    for j in range(len(card_cnt)):
        if Max <= card_cnt[j]:
            Max = card_cnt[j]
            card_number = j

    print(f'#{T + 1}', card_number, Max)

# 첫 풀이
Test = int(input())

for T in range(Test):
    card_N = int(input())  #
    a = int(input())

    a_lst = [0] * 96

    for i in range(card_N):
        a_lst[a % 10] += 1
        a = a // 10

    max = 0
    for i in range(96):
        if max <= a_lst[i]:
            max = a_lst[i]
            result = i
    print(f'#{T + 1} {result} {max}')