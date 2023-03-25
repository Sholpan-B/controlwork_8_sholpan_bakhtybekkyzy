from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'text', 'rate')
        labels = {
            'author': 'Автор отзыва',
            'text': 'Текст отзыва',
            'rate': 'Оценка'
        }

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if rate < 5:
            raise ValidationError('Оценка должна быть от 1 до 5')
        return rate
