# 계산기1

icp = {'+':1, '-':1, '*':2, '/':2, '(':3, ')':0}
isp = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}
Test = 10

for TC in range(1,Test+1):
    N = int(input())
    infix = input()

    postfix = ''
    S = []
    for token in infix:
        if token in icp :
            if token == ')':
                while S[-1] != '(':
                    postfix += S.pop()
                S.pop()
            else:
                while S and icp[token] <= isp[S[-1]]:
                    postfix += S.pop()
                S.append(token)

        elif token not in icp:
            postfix += token
    while S:
        postfix += S.pop()

    for token in postfix:
        if token in icp:
            b = S.pop()
            a = S.pop()
            if token == '+' : S.append(a + b)
            elif token == '-': S.append(a - b)
            elif token == '*': S.append(a * b)
            else : S.append(a//b)
        else:
            S.append(int(token))
    print(f'#{TC}',end = ' ')
    print(S[0])