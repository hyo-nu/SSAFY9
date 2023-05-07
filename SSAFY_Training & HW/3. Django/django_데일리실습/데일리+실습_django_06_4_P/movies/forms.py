from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            '제목' : forms.TextInput(attrs={'placeholder' : 'ex) 세 얼간이'}),
            '감독' : forms.TextInput(attrs={'placeholder' : 'ex) 라지쿠마르 히라니'}),
            '댓글' : forms.Textarea(attrs={'cols':40, 'rows':3,'placeholder' : 'ex) 나 얼간이 아니다!'}),
        }