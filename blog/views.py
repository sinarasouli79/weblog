from django.shortcuts import render
from.models import Article

# Create your views here.
def article_list(request):
    queryset = Article.objects.all()
    context = {'queryset' : queryset}
    return render(request, 'base.html', context)