# Generated by Django 3.1.3 on 2020-12-05 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
    ]
