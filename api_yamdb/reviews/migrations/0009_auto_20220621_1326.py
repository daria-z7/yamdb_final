# Generated by Django 2.2.16 on 2022-06-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20220407_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True, verbose_name='Имя пользователя'),
        ),
    ]
