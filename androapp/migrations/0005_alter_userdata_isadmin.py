# Generated by Django 4.1 on 2022-08-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('androapp', '0004_appsinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='isadmin',
            field=models.BooleanField(default=False),
        ),
    ]