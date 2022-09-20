from django.contrib import admin
from .models import Article, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'slug', 'status']
    list_filter = ['status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'jpublish', 'jcreate',
                    'jupdate', 'status', 'get_category', 'author', 'is_special']
    list_filter = ['publish', 'create', 'update', 'status', 'is_special']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']



    # return 'categories'
admin.site.register(Article, ArticleAdmin)
