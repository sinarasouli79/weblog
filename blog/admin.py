from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'create', 'update', 'status']
    list_filter = ['publish', 'create', 'update', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']


admin.site.register(Article, ArticleAdmin)
