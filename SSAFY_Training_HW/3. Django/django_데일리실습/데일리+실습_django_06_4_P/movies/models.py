from django.db import models

# Create your models here.
class Movie(models.Model):
    제목 = models.CharField(max_length=50)
    감독 = models.CharField(max_length=30)
    댓글 = models.TextField()
