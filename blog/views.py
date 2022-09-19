from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from account.models import User
from django.views.generic import DetailView
from account.mixins import AuthorAccessMixin
# Create your views here.


def article_list(request):
    queryset = Article.objects.filter(status='P')
    categories = Category.objects.all()
    context = {'queryset': queryset, 'categories': categories}
    return render(request, 'index.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def post(request, slug):
    obj = get_object_or_404(Article, slug=slug, status='P')
    context = {'object': obj}
    return render(request, 'post.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def author_article_list(request, username):
    # author = User.objects.get(username=username)
    author = get_object_or_404(User, username=username)
    articles = author.articles.filter(status='P')
    context = {'author': author,
               'articles': articles}
    return render(request, 'author-article-list.html', context)


class ArticlePreview(AuthorAccessMixin, DetailView):
    template_name = 'post.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)
