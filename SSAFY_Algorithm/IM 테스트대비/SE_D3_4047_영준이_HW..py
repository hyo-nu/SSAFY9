import sys;sys.stdin = open('input.txt')

def card_check():
    for lst in card:
        if len(lst) == len(list(set(lst))):
            result.append(13 - len(lst))
        else :
            return 'ERROR'

Test = int(input())

for T in range(Test):
    S = list(input())
    dict = {'S': 0, 'D' : 1, 'H' : 2, 'C': 3}
    card = [[] for _ in range(4)]
    result = []
    for c in range(len(S)//3):
        card[dict.get(S[3*c])].append(S[3*c+1] + S[3*c+2])

    ans = card_check()
    print(f'#{T+1}',end = ' ')
    if ans == None:
        print(*result)
    else:
        print(ans)


