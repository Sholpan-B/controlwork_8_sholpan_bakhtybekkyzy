from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    LAPTOPS = 'LAPTOP', 'Ноутбуки'
    SMARTPHONES = 'SMARTPHONES', 'Смартфоны'
    FOR_KITCHEN = 'FOR_KITCHEN', 'Техника для кухни'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    category = models.CharField(
        choices=StatusChoice.choices,
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Категория'
    )
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/',
        verbose_name='Фото',
        default='images/no-image.jpg'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"
