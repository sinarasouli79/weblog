from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def article_list(request):
    queryset = Article.objects.filter(status='P')
    context = {'queryset': queryset}
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


