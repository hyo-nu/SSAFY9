 # 16

def sum_of_digit_while(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def sum_of_digit_not_while(num):
    num_lst = map(int,list(str(num)))
    sum_num = sum(num_lst)
    return sum_num

print(sum_of_digit_while(516818415))
print(sum_of_digit_not_while(516818415))

