number = int(input())

result = []
for c in range(1,number):
    if c % 2 == 0 or c % 7 == 0:
        result.append(c)
        
print(sum(result))