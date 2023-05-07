
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25
num_list = [4, 4, 7, 8, 10, 4]

def sum_of_repeat_number(lst):
    num_dict = {}
    for l in lst:
        if l not in num_dict : num_dict[l] = 1
        else : num_dict[l] += 1
    
    num_lst = set(lst)
    result = 0
    for nl in num_lst:
        if num_dict[nl] == 1:
            result += nl  
    
    return result

print(sum_of_repeat_number(num_list))

    

