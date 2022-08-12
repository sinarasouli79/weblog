from django.urls import path
from .views import article_list
app_name = 'blog'
urlpatterns = [
    path('', article_list, name='article_list'),
]