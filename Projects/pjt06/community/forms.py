from django import forms
from django.forms.widgets import TextInput
from .models import Review
 
class ReviewForm(forms.ModelForm):
    movie_title = forms.CharField(
        label = '영화 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'my-moive_title',
                'placeholder': 'Enter the movie_title',
                'maxlength': '100',

            }   
        ),
    )

    title = forms.CharField(
        label = '리뷰 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'my-title',
                'placeholder': 'Enter the review title',
                'maxlength': '100',

            }   
        ),
    )

    content = forms.CharField(
        label = '리뷰 내용',
        widget = forms.Textarea(
            attrs = {
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 150,
            }
        ),
        error_messages={
            'required': '내용이 필요합니다'
        },
    )

    rank = forms.IntegerField(
        label = '점수',
        widget = forms.NumberInput(
            attrs = {
                'max_value': '5',
                'min_value': '1',
            } 
        ),
    )

    class Meta:
        model = Review
        fields = '__all__'