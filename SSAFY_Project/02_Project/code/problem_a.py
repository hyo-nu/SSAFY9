import requests
from pprint import pprint

def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=3e522bb11d9503474e85e9a710de1de4&language=en-US&page=1'
    response = requests.get(URL).json()
    
    # Popular.py 데이터 형태 { "page": 1, "results":[ {} , {} , {} ] }
    movies = response.get('results')
    cnt = 0
    for c in movies : cnt += 1        
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

