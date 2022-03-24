from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    rank = forms.IntegerField(
        widget= forms.NumberInput(
            attrs = {
                'max_value': '10',
                'min_value': '1',
            }
        ),
    )
    content = forms.CharField(
        widget = forms.Textarea(
            attrs = {
            'rows': 5,
            'cols': 50,

            }
        ),
    )
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField()
    
    class Meta:
        model = Comment
        exclude = ['review', 'user']
