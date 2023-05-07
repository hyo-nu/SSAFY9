# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def is_position_safe(N, M, position):

    position_lst = list(position) # tuple -> list
    
    # M 방향으로 한칸 이동
    if M == 0: # 위로 한칸
        position_lst[0] -= 1 
    elif M == 1: # 아래로 한칸
        position_lst[0] += 1
    elif M == 2: # 왼쪽으로 한칸
        position_lst[1] -= 1
    elif M == 3: # 오른쪽으로 한칸s
        position_lst[1] += 1
    
    # 범위내에 있는지 판별
    if position_lst[0] >= N or position_lst[1] >= N: 
        return False
    elif position_lst[0] < 0 or position_lst[1] < 0: 
        return False
    else:
        return True   

if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
