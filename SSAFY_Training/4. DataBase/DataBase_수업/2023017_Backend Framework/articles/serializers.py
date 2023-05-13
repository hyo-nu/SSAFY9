from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class SimpleCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)
    comment_set = SimpleCommentSerializer(read_only=True,many=True)


    comment_count = serializers.IntegerField(source='comment_set.count',read_only=True)
    # source='comment_set.count' : comment_set 의 갯수

    comment_set = CommentSerializer(read_only = True, many=True)
    # read_only = True : 읽어 올 때만 작동한다.
    class Meta:
        model = Article
        fields = '__all__'

