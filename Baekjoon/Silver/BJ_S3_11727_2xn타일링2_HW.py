N = int(input())
result = 1

for i in range(1,N+1):
    if i % 2 != 0 : result = 2 * result - 1
    else : result = 2 * result + 1

print(result % 10007)
