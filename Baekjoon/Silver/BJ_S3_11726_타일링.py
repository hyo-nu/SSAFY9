N = int(input())
zero = one = 1
for i in range(2,N+1):
    three = one + zero
    zero = one
    one = three

print(one % 10007)