# 쇠막대기 자르기
def push(item):
    global top
    top +=1
    S[top] = item

Test = int(input())

for T in range(Test):
    barcket = input()
    S = [0] * len(barcket)
    stick = cut_stick = 0
    top =-1

    for i in barcket:
        if i =='(' : push(i) ; stick += 1 # 스택하고 막대기 추가
        elif i == ')': # 컷팅 여부판단
            if S[top] == '(': # 컷팅하는 경우
                cut_stick += stick - 1 # 막대기 컷팅해서 담아두기
                stick -= 1             # 레이저의'('도 추가됐으니 stick - 1
                push(i)

            elif S[top] == ')': # 컷팅이 아니라 하나의 막대기가 끝나는 부분
                stick -= 1      # 레이저의'('도 추가됐으니 stick - 1
                cut_stick += 1  # 막대기 하나가 끝났으니 1개만 추가
                push(i)

    print(f'#{T+1}', cut_stick)