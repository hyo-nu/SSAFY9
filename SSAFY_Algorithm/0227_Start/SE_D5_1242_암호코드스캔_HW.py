import sys ; sys.stdin = open('input.txt')
from collections import deque

# 암호의 길이가 늘어나는경우
# def long_code():

# 각 암호부분 찾기
def start_point():
    for i in range(N):
        for j in range(M):
            if password[i][j] != '0':
                if password[i] not in Q_SP:
                    Q_SP.append(password[i])
                    break

# 16진수를 2진수로 변경
def change_HEX():
    global Bin
    HEX = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    Bin = ''
    while Q_SP:
        code = Q_SP.popleft()
        for co in code:
            if co in HEX:
                Bin += '%04d' % int(bin(HEX.get(co))[2:])
            elif co not in HEX:
                Bin += '%04d' % int(bin(int(co))[2:])
        Bin = Bin.rstrip('0')
        Bin_lst.append(Bin)

# Bin_lst에 여러개 들어오는 경구
# Bin_lst 요소가 n의 배수가 넘는경우
# 암호판독
def reading():
    Dict = {'0001101': 0, '0011001': 1, '0010011': 2,\
            '0111101': 3, '0100011': 4, '0110001': 5,\
            '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    while Bin_lst:
        odd = even = 0 # 홀수 짝수
        code = Bin_lst.pop()
        start = len(code)-56
        for i in range(0,8): # 34  41
            if i % 2 == 0 : odd += Dict.get(code[start + (i*7) : start + (i*7) + 7]) ;
            else : even += Dict.get(code[start + (i*7) : start + (i*7) + 7])

    if (odd * 3 + even) % 10 == 0: return(odd + even)
    else : return 0

Test = int(input())

for T in range(Test):
    # 1 <= N <= 2000, 1 <= M < 500
    N,M = map(int,input().split())
    password = [input() for _ in range(N)]
    Bin_lst = []
    Q_SP = deque()
    start_point()
    change_HEX()
    print(f'#{T+1}',reading())





