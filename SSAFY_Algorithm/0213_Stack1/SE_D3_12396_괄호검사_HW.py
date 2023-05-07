# 스택1_괄호검사

def push(item):
    global top
    top += 1
    S[top] = item

def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

Test = int(input())

for T in range(Test):
    String = input()
    S = [0] * len(String)

    top = -1
    bracket_o = ['{', '(']
    bracket_c = ['}', ')']
    Good = 0

    for i in String:
        if i in bracket_o:
            push(i)
        elif i == '}':
            if S[top] == '{' : pop()
            else : break
        elif i == ')':
            if S[top] == '(' : pop()
            else : break
    else:
        Good +=1

    print(f'#{T + 1}',end =' ')
    if top >= 0 or Good == 0 : print(0)
    elif Good == 1 : print(1)
