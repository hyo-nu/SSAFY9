# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def average(scores):
 
    sum = 0
    for s in scores:
        sum += s # 모든 scores의 합
    
    avg = sum/len(scores) # scores 합의 평균 
    return avg

if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5