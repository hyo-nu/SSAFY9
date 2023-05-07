# 계산기3
icp = {'+':1, '-':1, '*':2, '/':2, '(':3, ')':0}
isp = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}

Test = 10

for T in range(Test):
    N = int(input())
    calcul = input()
    S = []
    postfix = ''

    for token in calcul:
        if token in icp:
            if token ==')':
                while S[-1] !='(':
                    postfix += S.pop()
                S.pop()
            else:
                while S and icp[token] < isp[S[-1]]:
                    postfix += S.pop()
                S.append(token)
        else : postfix += token
    while S:
        postfix += S.pop()

    for token in postfix:
        if token in icp:
            b = S.pop()
            a = S.pop()
            if token == '+' : S.append(a+b)
            elif token == '-': S.append(a - b)
            elif token == '*': S.append(a * b)
            elif token == '/': S.append(a // b)
        else:
            S.append(int(token))
    print(f'#{T + 1}',end = ' ')
    print(S[0])


