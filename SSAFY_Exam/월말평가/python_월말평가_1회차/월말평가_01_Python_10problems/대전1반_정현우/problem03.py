# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def is_good_rate(movie):
      
    if movie.get("user_rating") >= 8: # movie 딕셔너리의 "유저 평점" 값 비교
        return True
    else :
        return False

if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(is_good_rate(movie))  # True