from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from blog.models import Article


class FormFieldsMixin:

    def dispatch(self, request, *args, **kwargs):
        self.fields = ['title', 'slug', 'category',
                       'description', 'is_special', 'thumbnail', 'publish', 'status']
        if request.user.is_superuser:
            self.fields.append('author')
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:
    def form_valid(self, form):
        if not self.request.user.is_superuser:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if self.obj.status not in ['D', 'I']:
                self.obj.status = 'D'
       
        form.save()

        return super().form_valid(form)


class AuthorAccessMixin:

    def dispatch(self, request, pk, *args, **kwargs):
        article_update = get_object_or_404(Article, pk=pk)
        if request.user == article_update.author and article_update.status in ['D', 'B']\
                or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('مجاز به نمایش نیست')


class AuthorsAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:profile')


class SuperUserAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()
