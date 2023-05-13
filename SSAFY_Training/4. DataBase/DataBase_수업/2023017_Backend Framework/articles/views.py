from django.shortcuts import render, get_object_or_404,get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleSerializer,CommentSerializer
from .models import Article,Comment

# 데코레이터가 필요함
@api_view(['GET','POST',])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        # articles = Article.objects.all()이거랑 위에랑 같음 
        # get_list_or_404 데이터를 전부 다 가져온다.

        serializer = ArticleSerializer(articles, many = True)
        # artcies 인스턴스안에 저장되어있는 모든 데이터를 시리얼라이즈에 넘겨줌, 
        # many = true는 articles인스턴스의 데이터가 여러개 라는 것을 알려줌
    
        return Response(serializer.data)
        # response의 인스턴스를 반환해줌
    elif request.method == 'POST':
        # request.data
        serializer = ArticleSerializer(data = request.data)
        # 첫번째 인자가 인스턴스??
        # 두번째 인자부터 데이터 라는데
        # 두번째 인자라서 'request.data' 이렇게만 주면 안되고, data = request.data 이렇게 줘야한다는데

        if serializer.is_valid(raise_exception=True): # 유효성 통과하면
            serializer.save() # db에 넣어줘
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
            # Respose클래스의 두 번째 인자가 status임
            # status = 201 적어도 되지만 가독성을 위해서 모듈을 사용한다.
            # status=status.HTTP_201_CREATED모듈로 쓰면 이렇게 쓴다.
            # 201 크리에이터는 생성에요청에 대한 응답으로 주로사용
        
        # return Response(serializer.errors)
        # 유효성을 통과못하면 errors에 오류내용을 적어줌  
        # errors이거 안해줘도 raise_exceptions=True를 is_valud()괄호안에 넣어주면 오류를 알아서 처리해준다.


    # 반환할 때 rest에서 제공하는 Response가 필요함
    # Status : 정해진 응답코드를 사용할 수 있는 모듈


@api_view(['GET','PUT','DELETE',])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':        
        serializer = ArticleSerializer(instance = article)
        # ArticleSerializer의 첫번쨰 인자가 instance라서 article 이렇게만 써두됨
        return Response(serializer.data)
        
    # 수정    
    elif request.method == 'PUT':
        # 수정할 데이터는 requset.data, 기존 레코드는 article 인스턴스
        serializer = ArticleSerializer(article,request.data, partial=True)
        # partial=True 일부 데이터만 수정이 가능

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        article.delete()
        msg = {'delete' : f'{article_pk}번 게시글 삭제'}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)
        #status=status.HTTP_204_NO_CONTENT : 데이터가 삭제되고 없다는 뜻의 status임

@api_view(['GET','POST'])
def comments_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment.objects.order_by('-pk'))
        serializer =  CommentSerializer(comments,many=True)
        return Response(serializer.data)


# 여기 이해 실패       
@api_view(['POST'])
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    serializer =  CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        # save(article_id=1) 강제로 갖다 박는거는 좋지 않음
        return Response(serializer.data)