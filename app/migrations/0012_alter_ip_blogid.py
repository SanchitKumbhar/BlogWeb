# Generated by Django 3.2.9 on 2024-06-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_ip_blogid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='blogid',
            field=models.CharField(max_length=128),
        ),
    ]
