# 남자 : 받은 수의 배수이면 스위치 변경
def man(number):
    for i in range(S_num):
        if (i + 1) % number == 0:
            if switch[i] == 0: switch[i] = 1
            elif switch[i] == 1: switch[i] = 0


# 여자 : 받은 수 중심으로 좌우 대칭이면서 가장 많은 스위치 포함하는 구간 변경
# 여자 : 대칭 없으면 자신만
def women(number):
    idx = number - 1
    cnt = 1
    if 2 <= number <= S_num:
        while 0 <= idx - cnt and idx + cnt <= S_num - 1 and \
                switch[idx - cnt] == switch[idx + cnt]:
            if switch[idx - cnt] == 0:
                switch[idx - cnt] = switch[idx + cnt] = 1
            elif switch[idx - cnt] == 1:
                switch[idx - cnt] = switch[idx + cnt] = 0
            cnt += 1

    if switch[idx] == 0:switch[idx] = 1
    elif switch[idx] == 1:switch[idx] = 0

S_num = int(input())
switch = list(map(int, input().split()))
N = int(input())

for _ in range(N):
    gender, number = map(int, input().split())

    if gender == 1: man(number)  # 남자면
    elif gender == 2: women(number)  # 여자면

for i in range(S_num):
    print(switch[i],end = ' ')
    if (i+1) % 20 == 0:
        print()