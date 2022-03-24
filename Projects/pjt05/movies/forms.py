from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs = {
                'maxlength': 100,
                'placeholder': '제목을 입력해주세요',
            }
        ),
    )
    overview = forms.CharField(
        label = '줄거리',
        widget = forms.Textarea(
            attrs = {
                'placeholder': '줄거리를 입력해주세요',
                'rows': 15,
                'cols': 150,
            }
        ),
    )
    director = forms.CharField(
        label = '감독',
        widget = forms.TextInput(
            attrs = {
                'maxlength': 30,
                'placeholder': '감독을 입력해주세요',
            }
        ),
    )
    actor = forms.CharField(
        label = '배우',
        widget = forms.TextInput(
            attrs = {
                'maxlength': 100,
                'placeholder': '주연배우들을 입력해주세요',
            }
        ),
    )


    class Meta:
        model = Movie
        fields = '__all__'