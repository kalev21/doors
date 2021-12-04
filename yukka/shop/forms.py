from .models import FeedBackModel
from django.forms import ModelForm, TextInput, Textarea


class FeedBackForm(ModelForm):      # Форма отзывов
    class Meta:
        model = FeedBackModel
        fields = ['author', 'text']
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'id': 'author-input'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Написать отзыв',
                'id': 'author-input'
            }),
        }
