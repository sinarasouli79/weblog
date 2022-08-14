from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = [
        ('P', 'منتشرشده'),
        ('D', 'بایگانی'),
    ]
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    create = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    update = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله‌ها'

    def __str__(self):
        return self.title
