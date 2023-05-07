from django.urls import path
from . import views

urlpatterns = [
    path('articles/',views.article_list),

    # RESTfull API => GET, PUT, DELETE 
    path('articles/<int:article_pk>/',views.article_detail),
]
