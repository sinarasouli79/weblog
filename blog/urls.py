from django.urls import path
from .views import article_list, about, post, contact, author_article_list
app_name = 'blog'
urlpatterns = [
    path('', article_list, name='article_list'),
    path('<slug:username>/', author_article_list, name='author_article_list'),
    path('about/', about, name='about'),
    path('post/<slug:slug>/', post, name='post'),
    path('contact/', contact, name='contact'),
]
