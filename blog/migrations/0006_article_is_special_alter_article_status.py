# Generated by Django 4.1 on 2022-09-20 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_article_user_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='مقاله ویژه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('P', 'منتشرشده'), ('D', 'پیش\u200cنویس'), ('I', 'در حال برسی'), ('B', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
