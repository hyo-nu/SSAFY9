
# 두번
Test = int(input())
# Test = 10
def binary(P,page):

    start = 1
    end = P
    cnt = 0
    while 1:
        middle = (start+end)//2
        if middle == page : return cnt
        elif middle > page : end = middle ; cnt += 1
        elif middle < page : start = middle ; cnt += 1

for T in range(Test):

    P,A,B = map(int,input().split())

    if binary(P,A) < binary(P,B) : print(f'#{T+1}','A')
    elif binary(P,A) > binary(P,B) : print(f'#{T+1}','B')
    else : print(f'#{T+1}','O')
# 처음
Test = int(input())

for T in range(Test):
    P,A,B = map(int,input().split())
    player = [A,B]

    for key in range(len(player)):
        count = 0
        start = 1
        end = P
        while start <= end:
            middle = (start + end) // 2
            if middle == player[key] : count += 1 ; break
            elif middle > player[key] : end = middle ; count += 1
            elif middle < player[key] : start = middle ; count += 1

        player[key] = count

    if player[0] > player[1] : print(f'#{T + 1} B')
    elif player[0] < player[1]: print(f'#{T + 1} A')
    elif player[0] == player[1]: print(f'#{T + 1} 0')