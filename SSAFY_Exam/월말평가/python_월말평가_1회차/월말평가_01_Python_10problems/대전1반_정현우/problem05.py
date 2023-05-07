# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def calc_lunch_cost(lunch_cost):
    
    All_cost_lst = list(lunch_cost.values()) # 비용 list
    sum_cost = 0 # 지불 비용의 총합
    
    for acl in All_cost_lst:
        sum_cost += acl 
        
    return sum_cost

if __name__ == '__main__':
    lunch_cost = {
        '이싸피' : 12000,
        '김싸피' : 30000,
        '박싸피' : 10000,
        '최싸피' : 15000,
        '조싸피' : 18000, 
    }

    print(calc_lunch_cost(lunch_cost))  # 85000