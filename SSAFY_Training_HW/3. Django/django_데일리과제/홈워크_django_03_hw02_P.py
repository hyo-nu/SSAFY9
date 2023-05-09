# 데일리 과제 3-2에서 작성한 모델 Article 모델을 참고하여 작성하시오.

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()


# python manage.py makemigrations
# python manage.py migrate

# 실습 편의를 위한 라이브러리
# pip install ipython : 파이썬으로 빌드 된 대화식 쉘
# pip install django-extensions : 장고의 기본 명령들의 기능을 확장해 주고
#                                 여러 부가 기능을 추가해주는 모듈 
#                                 INSTALLED_APPS에 추가해야함  

# python manage.py shell_plus : shell_plus는 모델을 적은 후 post.objects.all() 명령어를 불어와야하는 수고가 안듦

#
# 1. article = Article()
# 2. article.title = 'first'
# 3. article.content = 'django'
# 4. article.save()
