json!!!
 1. json : (javaScript Object Notation)은 키-값 쌍으로 이루어진 데이터 오브젝트를
          전달하기 위해 인간이 읽을 수 있는 텍스트를 사용하는 개방형 표준 포멧

 2. open('data/movie.json', encoding='utf-8') : 파일을 여는 함수

 3. json.load(movie_json) : json파일을 읽어 dict형태로 저장합니다.   

 4. json.load(open(f'data/movies/{movie_id}.json', encoding='utf-8')) 
   여러개의 파일을 open하고 load할 시에 f-string을 사용해서 반복문을 통해
   한번에 표현하는 아이디어를 얻을 수 있었습니다.
 
 5. 딕셔너리 값 get() : 딕셔너리를 잘 활용할 수 있게 되었다.
    result = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    } 
 