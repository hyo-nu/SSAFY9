import json
from pprint import pprint


def movie_info(movies, genres):
    final_result = []
    for ms_num in range(len(movies)):
        list_result = []
        
        for m_num in range(len(movies[ms_num].get('genre_ids'))):
            for g_num in range(len(genres)):            
                if genres[g_num].get('id') == movies[ms_num].get('genre_ids')[m_num]:
                    list_result.append(genres[g_num].get('name'))
                
        result = {
            'id' : movies[ms_num].get('id'),
            'title' : movies[ms_num].get('title'),
            'poster_path' : movies[ms_num].get('poster_path'),
            'vote_average' : movies[ms_num].get('vote_average'),
            'overview' : movies[ms_num].get('overview'),
            'genre_names' : list_result
        }
        final_result.append(result)    
    return final_result
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
