from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Article
# Create your views here.

class Home(LoginRequiredMixin, ListView):
    queryset = Article.objects.all()
    template_name = 'home.html'
