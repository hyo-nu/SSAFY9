import sys ; sys.stdin = open('input.txt')

def start_point():
    for i in range(N):
        for j in range(M-1,-1,-1):
            if password[i][j] == '1' :
                return i,j

Test = int(input())

Dict = {'0001101' : 0,'0011001' : 1,'0010011' : 2,\
        '0111101' : 3,'0100011' : 4,'0110001' : 5,\
        '0101111' : 6,'0111011' : 7,'0110111' : 8, '0001011' : 9}
for T in range(Test):
    N,M = map(int,input().split())
    password = [input() for _ in range(N)]
    R,C = start_point()

    odd = 0
    even = 0
    for i in range(0,8):
        if i % 2 == 0 : even += Dict.get(password[R][C-7*(i+1)+1 : C-7*i+1])
        else : odd += Dict.get(password[R][C-7*(i+1)+1 : C-7*i+1])

    print(f'#{T+1}',end = ' ')
    if (odd * 3 + even) % 10 == 0 : print(odd + even)
    else : print(0)