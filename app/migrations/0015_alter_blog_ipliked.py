# Generated by Django 3.2.9 on 2024-06-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_likeip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='ipliked',
            field=models.ManyToManyField(to='app.likeip'),
        ),
    ]
