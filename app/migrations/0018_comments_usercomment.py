# Generated by Django 3.2.9 on 2024-06-25 08:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0017_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='usercomment',
            field=models.ManyToManyField(related_name='usercomment', to=settings.AUTH_USER_MODEL),
        ),
    ]
