# Generated by Django 5.0 on 2023-12-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='profile_picture',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]