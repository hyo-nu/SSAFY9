import json

def dec_movies(movies):
    list_month = [] # 12월 개봉영화 list
    movies_jlst = [] # json_open 요소들 list
    
    for m_num in range(len(movies)):
        movie_id = movies[m_num].get('id')
        movies_open = json.load(open(f'data/movies/{movie_id}.json', encoding='utf-8'))
        movies_jlst.append(movies_open)
    
    for mj_num in range(len(movies_jlst)): 
        if movies_jlst[mj_num].get('release_date')[5:7] == '12':
            list_month.append(movies_jlst[mj_num].get('title'))
    return list_month

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
