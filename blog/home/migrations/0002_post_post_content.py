# Generated by Django 4.2.7 on 2023-11-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=models.TextField(default='', verbose_name='Post Content'),
            preserve_default=False,
        ),
    ]
