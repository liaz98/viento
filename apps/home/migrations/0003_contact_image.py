# Generated by Django 3.1.3 on 2020-12-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_contact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='contact/images', verbose_name='Company image'),
        ),
    ]
