import requests
from pprint import pprint


def credits(title):
    try : 
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
        
        URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        parameter2 = {
        'api_key' : '3e522bb11d9503474e85e9a710de1de4',
        'language' : 'en-US',
        }
        response2 = requests.get(URL2, params = parameter2).json()
        cast_lst = response2.get('cast')
        crew_lst = response2.get('crew')

        credits_dict = {}
    
        for c in cast_lst:
            if c.get('cast_id') < 10:
                if 'cast' in credits_dict: 
                    credits_dict['cast'] = credits_dict['cast'] + [c.get('name')]
                else:
                    credits_dict['cast'] = [c.get('name')]
               
        for d in crew_lst:  
            if d.get("department") == "Directing":
                if 'directing' in credits_dict:
                    credits_dict['directing'] = credits_dict['directing'] + [d.get('name')] 
                else:
                    credits_dict['directing'] = [d.get('name')]
        
        return credits_dict
    except:
        return None
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None



# https://api.themoviedb.org/3/movie/496243/credits?api_key=3e522bb11d9503474e85e9a710de1de4&language=en-US

# https://api.themoviedb.org/3/search/movie?api_key=3e522bb11d9503474e85e9a710de1de4&language=en-US&query=%EA%B8%B0%EC%83%9D%EC%B6%A9&page=1&include_adult=false