# Generated by Django 3.1.3 on 2020-12-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201205_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='name')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='phone')),
                ('subject', models.CharField(blank=True, max_length=60, verbose_name='subject')),
                ('message', models.TextField(blank=True, verbose_name='message')),
            ],
        ),
    ]
