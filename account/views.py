from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from blog.models import Article

from .forms import ProfileForm
from .mixins import (AuthorAccessMixin, FormFieldsMixin, FormValidMixin,
                     SuperUserAccessMixin, AuthorsAccessMixin)
from .models import User

# Create your views here.


class Home(LoginRequiredMixin, AuthorsAccessMixin, ListView):
    template_name = 'home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class CreateArticle(LoginRequiredMixin, AuthorsAccessMixin, FormFieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = 'create_article.html'


class UpdateArticle(AuthorAccessMixin, FormFieldsMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = 'create_article.html'


class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'article_confirm_delete.html'


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/profile.html'

    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class LoginView(BaseLoginView):

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy('account:home')

        else:
            return reverse_lazy('account:profile')
