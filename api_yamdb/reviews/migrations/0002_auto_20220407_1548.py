# Generated by Django 2.2.16 on 2022-04-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='username_email_unique'),
        ),
    ]