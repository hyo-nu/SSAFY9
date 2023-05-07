# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify (identify):
       
    identify = list(identify.replace('-',''))
    
    for i in range(len(identify)):
        if i >= 6:
            identify[i] = '*'
            
    return ''.join(identify)   

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))