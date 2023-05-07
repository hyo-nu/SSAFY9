# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def over_24(people):
       
    over_24_cnt = 0 # 24세 초과 지원자수
       
    for pp in people:
        if pp.get('age') > 24:
            over_24_cnt += 1
            
    return over_24_cnt
            
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4