from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from blog.models import Article

from .forms import ProfileForm
from .mixins import (AuthorAccessMixin, AuthorsAccessMixin, FormFieldsMixin,
                     FormValidMixin, SuperUserAccessMixin)
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


class LoginView(views.LoginView):

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy('account:home')

        else:
            return reverse_lazy('account:profile')


class PasswordChangeView(views.PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
    template_name='registration/account_password_change_form.html'

class PasswordResetView(views.PasswordResetView):

    email_template_name = "registration/password_reset_email1.html"
    success_url = reverse_lazy("account:password_reset_done")
    template_name = "registration/password_reset_form1.html"


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "registration/password_reset_done1.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name="registration/password_reset_confirm1.html"
    success_url= reverse_lazy('account:password_reset_complete')


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name='registration/account_password_change_done.html'


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "registration/password_reset_complete1.html"

    