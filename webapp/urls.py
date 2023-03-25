from django.urls import path
from webapp.views.products import IndexView, IndexRedirectView, ProductDetail, ProductAddView, ProductUpdateView, \
    ProductDeleteView
# from webapp.views.reviews import ProductAddReviewView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("product/", IndexRedirectView.as_view(), name='product_index_redirect'),
    path("product/add", ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/confirm_delete/<int:pk>/', ProductDeleteView.as_view(), name='confirm_delete'),
    # path('products/<int:pk>/reviews/add/', ProductAddReviewView.as_view(), name='review_add'),
 ]
