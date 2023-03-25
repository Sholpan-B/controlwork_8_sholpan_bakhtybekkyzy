from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms.reviews import ReviewForm
from webapp.models import Review, Product


class ReviewsView(ListView):
    template_name = 'reviews/reviews.html'
    model = Review
    context_object_name = 'reviews'
    paginate_by = 3
    paginate_orphans = 0


class ReviewDetail(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review


class ProductAddReviewView(CreateView):
    template_name = 'reviews/add_review.html'
    model = Product
    form_class = ReviewForm
    extra_context = ()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = self.get_object()
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            return redirect('product_detail', product.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ReviewUpdateView(UpdateView):
    template_name = 'reviews/review_edit.html'
    form_class = ReviewForm
    model = Review
    context_object_name = ''

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ReviewDeleteView(DeleteView):
    template_name = 'reviews/review_confirm_delete.html'
    model = Review
    success_url = reverse_lazy('index')

