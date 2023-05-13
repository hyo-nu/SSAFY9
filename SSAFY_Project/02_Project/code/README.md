1. TMDB에서 데이터 가져오기 (request사용)
-> URL = '.....'
-> parameter = {
      'api_key' : '.....', # api 갑 가져오기
      'language' : 'ko-KR', # 언어 선택
}
response = requests.get(URL1, params = parameter).json()
- 여기까지가 기본적으로 넣어줘야하는 내용들

2. problem_a
- Get popular
- 영화 정보에 관한 내용이 list로 넘어오기 때문에 len으로 갯수를 세어 정답을 도출

3. problem_b
- Get popular
- list의 요소를 하나하나 꺼내어 8을 넘어가는 데이터만 다른 list에 담아서 출력

4. problem_c
- Get popular, sorted
- 중요!!!!! -> key = lambda x : x.get('vote_average'), reverse = True)

5. problem_d
- Search Movies : query에 정보를 넣어서 해당 정보와 부합한 데이터를 가져온다.
- Get Recommendations : 해당 movie_id에 대한 추천 영화 목록을 불러온다.

6. problem_d
- Search Movies, Get Credits = 찾은 영화에 대한 다른 정보(출연진,연출진)를 불러온다.