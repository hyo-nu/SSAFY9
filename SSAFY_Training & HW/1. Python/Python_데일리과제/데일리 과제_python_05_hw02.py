# fn_d(91) 
# 출력 예시 
# 101

number = int(input())

def fn_d(n):
    result = n
    while n > 0:
        result = result + n % 10
        n = n // 10
    return result

def is_selfnumber(num):   
   
    count = 0
    for N in range(num):
        if fn_d(N) == num:
            count += 1 
    if count == 0:
        return num
    else:
        return 'No' 

self = is_selfnumber(number)
print(f'셀프넘버 : {self}')


