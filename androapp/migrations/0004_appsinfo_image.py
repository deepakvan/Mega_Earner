# Generated by Django 4.1 on 2022-08-10 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('androapp', '0003_appsinfo_total_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsinfo',
            name='image',
            field=models.ImageField(default='', upload_to='appphoto/'),
            preserve_default=False,
        ),
    ]
