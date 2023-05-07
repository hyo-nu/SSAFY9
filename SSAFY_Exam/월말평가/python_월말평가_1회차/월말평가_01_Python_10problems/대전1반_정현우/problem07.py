# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def calculator(*numbers):

    values = list(numbers) #tuple -> list
    
    # 0 반환
    if len(values) == 0:
        return 0

    # 원의 넓이
    elif len(values) == 1:
        circle = values[0]**2 * 3.14
        return circle

    # 삼,사각형 넓이
    elif len(values) == 2:
        # 삼각형
        if (values[0] + values[1]) % 2 != 0 :
            triangle = values[0] * values[1] / 2
            return triangle
        # 사각형
        else :
            rectangle = values[0] * values[1]
            return rectangle
    
    # (합,평균)반환    
    elif len(values) >= 3:
        sum = 0
        for value in values:
            sum += value
        values_tuple = (sum,sum / len(values))
        return values_tuple

if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0