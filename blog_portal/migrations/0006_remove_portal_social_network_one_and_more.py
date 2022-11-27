# Generated by Django 4.1.2 on 2022-11-27 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_portal', '0005_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portal',
            name='social_network_one',
        ),
        migrations.RemoveField(
            model_name='portal',
            name='social_network_two',
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]