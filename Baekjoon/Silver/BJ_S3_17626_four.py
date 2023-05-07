num = int(input())
count = 0
while num:
    number = num ** (1/2)
    num -= int(number) ** 2
    count += 1
print(count)