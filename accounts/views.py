from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Article
# Create your views here.

# use listview for representing


@login_required
def home(request):
    articles = Article.objects.all()
    context = {
        'object_list': articles
    }
    return render(request, 'home.html', context)
