import sys;sys.stdin = open('input.txt')
from itertools import product

ch = int(input())
button_er = int(input())
if not button_er : print(min(len(str(ch)),abs(ch-100)))
elif button_er == 10 : print(abs(ch-100))
else:
    er_lst = list(map(int,input().split()))
    co_lst = [str(i) for i in range(10) if i not in er_lst]

    # 채널 한칸 씩 이동할 때
    count1 = abs(ch-100)

    # 숫자 버튼과 채널 함께 이동
    ch_len = len(str(ch))
    Case = []
    Case.append(list(product(co_lst,repeat=ch_len+1)))
    Case.append(list(product(co_lst,repeat=ch_len)))
    if ch_len > 1:Case.append(list(product(co_lst,repeat=ch_len-1)))

    mn = 10000000001
    for lst in Case:
        for case in lst:
            case = ''.join(case)
            if mn > abs(ch - int(case)) + len(str(int(case))):
                mn = abs(ch - int(case)) + len(str(int(case)))
    print(min(count1, mn))