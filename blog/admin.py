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
                    'jupdate', 'status', 'get_category', 'user']
    list_filter = ['publish', 'create', 'update', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']


    def get_category(self, obj):
        return '، '.join([category.title for category in obj.category.all()])

    get_category.short_description = 'دسته‌بندی'


    # return 'categories'
admin.site.register(Article, ArticleAdmin)
