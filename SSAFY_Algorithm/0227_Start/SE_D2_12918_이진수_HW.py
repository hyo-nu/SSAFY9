# HEX = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
# Test = int(input())
#
# for T in range(Test):
#     N , hex = input().split()
#
#     print(f'#{T + 1}', end=' ')
#     for i in range(int(N)):
#         if hex[i] in HEX :print('%04d' % int(bin(HEX.get(hex[i]))[2:]),end = '')
#         else :print('%04d' % int((bin(int(hex[i]))[2:])),end = '')
#     print()

#==========================================
Test = int(input())

for TC in range(Test):
    N, Hex = input().split()
    Bin = bin(int(Hex,16))[2:]
    print(str(0)*(int(N)*4 - len(Bin))+Bin)