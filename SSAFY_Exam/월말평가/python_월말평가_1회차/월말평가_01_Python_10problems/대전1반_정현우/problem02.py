# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지

def min_max(scores):

    scores.sort() # scores 오름차순 정렬
    min_max_lst = (scores[0],scores[-1]) # 1번째, 마지막째 값을 tuple로 묶음
    
    return min_max_lst

if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
