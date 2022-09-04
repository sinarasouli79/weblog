from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس')
    status = models.BooleanField(
        default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = [
        ('P', 'منتشرشده'),
        ('D', 'بایگانی'),
    ]
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس')
    category = models.ManyToManyField(Category, verbose_name='دسته‌بندی')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    publish = models.DateTimeField(
        default=timezone.now, verbose_name='زمان انتشار')
    create = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    update = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ بروزرسانی')
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده', related_name='articles')
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله‌ها'

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = 'تاریخ انتشار'

    def jcreate(self):
        return jalali_converter(self.create)
    jcreate.short_description = 'تاریخ ساخت'

    def jupdate(self):
        return jalali_converter(self.update)
    jupdate.short_description = 'تاریخ بروزرسانی'

    def get_category(self):
        return '، '.join([category.title for category in self.category.all()])

    get_category.short_description = 'دسته‌بندی'

