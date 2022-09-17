from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from blog.models import Article
from .mixins import (FormFieldsMixin, FormValidMixin,
                     UpdateAccessMixin, SuperUserAccessMixin)
from django.urls import reverse_lazy
# Create your views here.


class Home(LoginRequiredMixin, ListView):
    template_name = 'home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class CreateArticle(LoginRequiredMixin, FormFieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = 'create_article.html'


class UpdateArticle(UpdateAccessMixin, FormFieldsMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = 'create_article.html'


class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'article_confirm_delete.html'
