import json
from pprint import pprint

def max_revenue(movies):
    list_max = [] # 수익 담는list
    movies_jlst = [] # json_open 요소들 list
    
    for m_num in range(len(movies)):
        movie_id = movies[m_num].get('id')
        movies_open = json.load(open(f'data/movies/{movie_id}.json', encoding='utf-8'))
        list_max.append(movies_open.get('revenue')) # 수익을 담았고
        movies_jlst.append(movies_open) # 자체를 담았어요
    
    list_max.sort() # 정렬해서 마지막이 최댓값
    print(movies_jlst)

    for mj_num in range(len(movies_jlst)): 
        if movies_jlst[mj_num].get('revenue') == list_max[len(movies_jlst)-1]:
            return movies_jlst[mj_num].get('title')
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

