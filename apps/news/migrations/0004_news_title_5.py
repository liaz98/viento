# Generated by Django 3.1.3 on 2020-12-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_title_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title_5',
            field=models.CharField(blank=True, max_length=50, verbose_name='Title 5'),
        ),
    ]
