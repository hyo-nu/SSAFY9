#비밀번호

def push(item):
    global top
    top += 1
    S[top] = item

def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

Test = 10
for T in range(Test):
    N,password = input().split()
    top = -1
    S = [0]*int(N)

    for i in password:

        if top == -1:
            push(i)
        else:
            if S[top] != i:
                push(i)
            elif S[top] == i:
                pop()
    print(f'#{T+1}',end = ' ')
    for i in range(top+1):
        print(S[i],end='')
    print()