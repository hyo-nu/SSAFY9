# Test = int(input())
#
# for T in range(Test):
#     N = float(input())
#
#     Bin = []
#     while N:
#         Bin.append(int((N * 2)//1))
#         N = (N * 2) % 1
#
#     print(f'#{T + 1}', end = ' ')
#     if len(Bin) >= 13 : print('overflow')
#     else : print(''.join(list(map(str,Bin))))
#
#=====================================
Test = int(input())

for TC in range(Test):
    N = float(input())
    Bin = []
    while N:
        Bin.append(int(N*2)//1)
        N = (N * 2) % 1
    print(Bin)


