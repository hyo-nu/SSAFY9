from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    GENRE_CHOICES = [
        ('comedy','코미디'),
        ('horror','공포'),
        ('romance','로맨스')
        ]
    genre = forms.ChoiceField(choices= GENRE_CHOICES)
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs= {
                'min' : 0,
                'max' : 5,
                'step' : 0.5,
            }
        )
    )

    release_date = forms.DateField(widget=forms.DateInput(
        attrs={
        'type' : 'date',
        }      
    )
    )

    class Meta:
        model = Movie
        fields = "__all__"