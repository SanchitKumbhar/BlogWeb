# Generated by Django 3.2.9 on 2024-06-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blog_delete_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipadd', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.ManyToManyField(to='app.ip'),
        ),
    ]
