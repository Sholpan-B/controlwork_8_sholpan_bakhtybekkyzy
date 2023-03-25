from decimal import Decimal

from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', )
        labels = {
            'name': 'Наименование',
            'description': 'Описание',
            'image': 'Фото',
            'category': 'Категория',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов!')
        return name


