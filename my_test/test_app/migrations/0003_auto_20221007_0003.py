# Generated by Django 2.2 on 2022-10-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20221006_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habr',
            name='title',
            field=models.TextField(verbose_name='Заголовок статьи'),
        ),
    ]