from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView

from webapp.forms.products import ProductForm
from webapp.models import Product


class GroupPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'Moderators']).exists()


class IndexView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3
    paginate_orphans = 0


class ProductDetail(DetailView):
    template_name = 'products/product_detail.html'
    model = Product


class ProductAddView(GroupPermissionMixin, LoginRequiredMixin, CreateView):
    template_name = 'products/product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(GroupPermissionMixin, LoginRequiredMixin, UpdateView):
    template_name = 'products/product_edit.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(GroupPermissionMixin, LoginRequiredMixin, DeleteView):
    template_name = 'products/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')


class IndexRedirectView(RedirectView):
    pattern_name = 'index'
