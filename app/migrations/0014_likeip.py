# Generated by Django 3.2.9 on 2024-06-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20240624_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='likeip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeip', models.CharField(max_length=128)),
                ('blogid', models.CharField(max_length=128)),
            ],
        ),
    ]
