from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ActorDetailSerializer(ActorSerializer):
    class ActorMovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movies = ActorMovieTitleSerializer(read_only=True, many = True)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(MovieSerializer):
    class MovieReviewSetSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title','content')

    class MovieActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)


    actors=  MovieActorSerializer(read_only=True, many = True)
    review_set = MovieReviewSetSerializer(read_only=True, many = True)
    review_count = serializers.IntegerField(source = 'review_set.count', read_only=True)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__' 
        read_only_fields = ('movie',)


class ReviewDetailSerializer(ReviewSerializer):   #위에서 만든 ReviewSerializer를 상속받은 새로운 클래스 생성
    class ReviewSetSerializer(serializers.ModelSerializer): # 내가 추가하고 요소만 담은 싶은 클래스 생성 
        class Meta:
            model = Movie          # moedels.py의 Movie에서
            fields = ('title',)    # title만 빼옴
    movie = ReviewSetSerializer(read_only=True,)  # moedels.py의 riview 내에 movie에 추가 # Movie는 단일데이터이기 때문에 many=True 쓰지 않기 


    

        

