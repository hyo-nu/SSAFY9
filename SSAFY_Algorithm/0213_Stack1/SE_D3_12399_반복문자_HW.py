# 스택1_반복문자_지우기

Test = int(input())

def push(item):
    global top
    top += 1
    S[top] = item

def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

for T in range(Test):
    word = input()
    top = -1
    S = [0] * len(word)

    for i in word:
        if top == -1 :
            push(i)
        else:
            if S[top] != i :
                push(i)
            elif S[top] == i :
                pop()
    print(f'#{T + 1}', end=' ')
    print(top+1)

