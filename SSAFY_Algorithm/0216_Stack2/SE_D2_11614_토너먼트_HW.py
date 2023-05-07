# 스택2_토너먼트카드게임_확인용

# 1 : 가위
# 2 : 바위
# 3 : 보
def RSP(p1, p2):
    VS = p1 - p2
    if VS == -2 or VS == 1 : return p1
    elif VS == -1 or VS == 2: return p2
    else : return False


def find_winner(i, j):
    if i == j:
        return rsp[i], i + 1
    else:
        mid = (i + j) // 2
        p1,num1 = find_winner(i, mid)
        p2,num2 = find_winner(mid + 1, j)

        if RSP(p1, p2) == p1 : winner = p1 ; win_num = num1
        elif RSP(p1, p2) == p2: winner = p2 ; win_num = num2
        elif RSP(p1, p2) == False:
            if num1 < num2 : winner = p1 ; win_num = num1
            else : winner = p2 ; win_num = num2
        return winner , win_num

Test = int(input())

for TC in range(Test):
    N = int(input())  # 1 ~ N
    rsp = list(map(int, input().split()))
    win_rsp,win_num = find_winner(0,N-1)
    print(f'#{TC+1}',end = ' ')
    print(win_num)

