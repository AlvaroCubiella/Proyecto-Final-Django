# Generated by Django 4.1.2 on 2022-11-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_portal', '0004_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='articles'),
        ),
    ]
