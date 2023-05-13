import requests
from pprint import pprint



def recommendation(title):
    
    try:
        URL1 = 'https://api.themoviedb.org/3/search/movie'
        parameter1 = {
        'api_key' : '3e522bb11d9503474e85e9a710de1de4',
        'language' : 'ko-KR',
        'query' : title,
        }
        # Popular.py 데이터 형태 { "page": 1, "results":[ {} , {} , {} ] }
        response1 = requests.get(URL1, params = parameter1).json()
        movie = response1.get('results')
        
        movie_id = movie[0].get('id')
        sug_movie_lst = []
        
        URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
        parameter2 = {
        'api_key':'3e522bb11d9503474e85e9a710de1de4',
        'language' : 'ko-KR'
        }
        response2 = requests.get(URL2, params = parameter2).json()        
        sug_movie = response2.get('results')
        
        for sm in sug_movie:
            sug_movie_lst.append(sm.get('title'))
                
        return sug_movie_lst
    except:
        return None     
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

