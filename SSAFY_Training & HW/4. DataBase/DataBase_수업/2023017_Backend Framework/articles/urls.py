from django.urls import path
from . import views

urlpatterns = [
    # /api/v1/articles/ => 전체 게시글 조회(GET). 게시글 생성(POST)
    path('articles/',views.article_list),
    
    # /api/v1/article/1/ => r게시글 상세 조회(GET), 수정(PUT) ,삭제(DELETE)
    path('articles/<int:article_pk>/', views.article_detail),

    # 댓글 전체 조회, 생성
    path('comments/',views.comments_list),

    # 댓글 생성'
    path('articles/<int:article_pk>/comments/',views.comments_create),

]   
