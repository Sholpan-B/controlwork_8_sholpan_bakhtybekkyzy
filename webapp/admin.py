from django.contrib import admin

from webapp.models import Product, Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'image')
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    fields = ('id', 'name', 'category', 'description', 'image')
    readonly_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'text', 'rate')
    list_filter = ('author', 'product')
    search_fields = ('author', 'product')
    fields = ('id', 'author', 'product', 'text', 'rate')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)

