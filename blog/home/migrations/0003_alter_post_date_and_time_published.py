# Generated by Django 5.0 on 2023-12-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_and_time_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date and time published'),
        ),
    ]
