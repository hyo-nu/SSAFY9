# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.

def dec_to_bin(number):
   
    binary_lst = []
    
    while number > 0:
        if number % 2 == 0:
            binary_lst.append('0')
        
        elif number % 2 == 1:
            binary_lst.append('1')
        number = number // 2 # number의 몫이 다음 number
        
    result = ''.join(binary_lst[::-1]) # 결과 list를 반대로 출력    
    return result
            
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010





