# 계산기2
Test = 10
icp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 3, ')' : 0}
isp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0, ')' : 0}

# (6+5*(2-8)/2)
for TC in range(Test):
    N = int(input())
    calcu = input()
    S = []
    postfix = ''

    for token in calcu:
        if token in icp:
            if token == ')' :
                while S[-1] != '(' : postfix += S.pop()
                S.pop()
            else :
                if S and icp[token] <= isp[S[-1]] :
                    postfix += S.pop()
                S.append(token)
        else : postfix += token
    while S:
        postfix += S.pop()

    for token in postfix:
        if token in icp:
            b = S.pop()
            a = S.pop()
            if token == '+' : S.append(a + b)
            elif token == '-' : S.append(a - b)
            elif token == '*' : S.append(a * b)
            elif token == '/' : S.append(a / b)
        else:
            S.append(int(token))
    print(f'#{TC+1}', end = ' ')
    print(S[0])