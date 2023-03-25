from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from webapp.managers import ReviewManager
from webapp.models import Product


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review_author',
        verbose_name='Автор отзыва'
    )
    product = models.ForeignKey(
        to='webapp.Product',
        on_delete=models.CASCADE,
        related_name='review_product',
        verbose_name='Товар'
    )
    text = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name='Текст отзыва'
    )
    rate = models.IntegerField(
        verbose_name='Oценка',
        null=False,
        blank=False,
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    ),
    reviewed_product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, null=True)

    objects = ReviewManager()

    def __str__(self):
        return f"{self.author} - {self.text} - {self.rate}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = "Отзывы"
