# forth

Test = int(input())

sign = ['+', '-', '*', '/']
for TC in range(1, Test + 1):
    forth = input().split()
    S = []
    Error = 0
    for token in forth:
        if token in sign:
            if len(S) < 2 :
                Error += 1
                break
            else:
                b = int(S.pop())
                a = int(S.pop())
                if token == '+' : S.append(a + b)
                elif token == '-' : S.append(a - b)
                elif token == '*' : S.append(a * b)
                elif token == '/' : S.append(a // b)
        else:
            S.append(token)
    print(f'#{TC}', end=' ')
    if len(S) == 2 and Error == 0 : print(S[0])
    else : print('error')